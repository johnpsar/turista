import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import layers
import matplotlib.pyplot as plt


class RecommenderNet(keras.Model):
    def __init__(self, num_users, num_places, embedding_size, **kwargs):
        super(RecommenderNet, self).__init__(**kwargs)
        self.num_users = num_users
        self.num_places = num_places
        self.embedding_size = embedding_size
        self.user_embedding = layers.Embedding(
            num_users,
            embedding_size,
            embeddings_initializer="he_normal",
            embeddings_regularizer=keras.regularizers.l2(1e-6),
        )
        self.user_bias = layers.Embedding(num_users, 1)
        self.place_embedding = layers.Embedding(
            num_places,
            embedding_size,
            embeddings_initializer="he_normal",
            embeddings_regularizer=keras.regularizers.l2(1e-6),
        )
        self.place_bias = layers.Embedding(num_places, 1)

    def call(self, inputs):
        user_vector = self.user_embedding(inputs[:, 0])
        user_bias = self.user_bias(inputs[:, 0])
        place_vector = self.place_embedding(inputs[:, 1])
        place_bias = self.place_bias(inputs[:, 1])
        dot_user_place = tf.tensordot(user_vector, place_vector, 2)
        # Add all the components (including bias)
        x = dot_user_place + user_bias + place_bias
        # The sigmoid activation forces the rating to between 0 and 1
        return tf.nn.sigmoid(x)


# TRAINING
def calcultateResults():
    ratingDf = pd.read_csv('places/cf/rating.csv')

    user_ids = ratingDf["userid"].unique().tolist()
    user2user_encoded = {x: i for i, x in enumerate(user_ids)}
    userencoded2user = {i: x for i, x in enumerate(user_ids)}
    place_ids = ratingDf["placeid"].unique().tolist()
    place2place_encoded = {x: i for i, x in enumerate(place_ids)}
    place_encoded2place = {i: x for i, x in enumerate(place_ids)}
    ratingDf["user"] = ratingDf["userid"].map(user2user_encoded)
    ratingDf["place"] = ratingDf["placeid"].map(place2place_encoded)

    num_users = len(user2user_encoded)
    num_places = len(place_encoded2place)
    ratingDf["rating"] = ratingDf["rating"].values.astype(np.float32)

    # min and max ratings will be used to normalize the ratings later
    min_rating = min(ratingDf["rating"])
    max_rating = max(ratingDf["rating"])

    print(
        "Number of users: {}, Number of Places: {}, Min rating: {}, Max rating: {}".format(
            num_users, num_places, min_rating, max_rating
        )
    )

    #df = ratingDf.sample(frac=1, random_state=42)
    df = ratingDf
    x = df[["user", "place"]].values
    # Normalize the targets between 0 and 1. Makes it easy to train.
    y = df["rating"].apply(lambda x: (x - min_rating) /
                           (max_rating - min_rating)).values
    # Assuming training on 90% of the data and validating on 10%.
    train_indices = int(0.8 * df.shape[0])
    x_train, x_val, y_train, y_val = (
        x[:train_indices],
        x[train_indices:],
        y[:train_indices],
        y[train_indices:],
    )

    EMBEDDING_SIZE = 50

    model = RecommenderNet(num_users, num_places, EMBEDDING_SIZE)
    model.compile(
        loss=tf.keras.losses.BinaryCrossentropy(), optimizer=keras.optimizers.Adam(lr=0.001)
    )

    history = model.fit(
        x=x_train,
        y=y_train,
        batch_size=64,
        epochs=25,
        verbose=1,
        validation_data=(x_val, y_val),
    )

    plt.plot(history.history["loss"])
    plt.plot(history.history["val_loss"])
    plt.title("model loss")
    plt.ylabel("loss")
    plt.xlabel("epoch")
    plt.legend(["train", "test"], loc="upper left")
    # plt.show()

    model.save("save.tf")

    # RECOMMENDATIONS
    place_df = pd.read_csv('places/cf/recommendations.csv')

    # Let us get a user and see the top recommendations.
    #user_id = df.userid.sample(1).iloc[0]
    user_id = df.userid.iloc[-1]

    places_selected_by_user = df[df.userid == user_id]

    places_not_selected = place_df[place_df["placeid"].isin(
        places_selected_by_user.placeid.values)]["placeid"]
    places_not_selected = list(
        set(places_not_selected).intersection(set(place2place_encoded.keys()))
    )

    places_not_selected = [
        [place2place_encoded.get(x)] for x in places_not_selected]
    user_encoder = user2user_encoded.get(user_id)

    user_place_array = np.hstack(
        ([[user_encoder]] * len(places_not_selected), places_not_selected)
    )

    ratings = model.predict(user_place_array).flatten()
    top_ratings_indices = ratings.argsort()[-15:][::-1]

    recommended_place_ids = [
        place_encoded2place.get(places_not_selected[x][0]) for x in top_ratings_indices
    ]

    # print("Showing recommendations for user: {}".format(user_id))
    # print("====" * 9)
    # print("Places with high ratings from user")
    # print("----" * 8)
    top_places_user = (
        places_selected_by_user.sort_values(by="rating", ascending=False)
        .head(5)
        .placeid.values
    )
    place_df_rows = place_df[place_df["placeid"].isin(top_places_user)]
    for row in place_df_rows.itertuples():
        print(row.title, ":", row.type)

    # print("----" * 8)
    # print("Top 10 place recommendations")
    # print("----" * 8)
    recommended_places = place_df[place_df["placeid"].isin(
        recommended_place_ids)]

    resultsList = []
    for row in recommended_places.itertuples():
        resultsList.append(row.type)

    print(resultsList)

    return resultsList
