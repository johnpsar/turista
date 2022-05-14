import pandas as pd
import random


from .collaborative_filtering import calcultateResults


def results(location):

    if location == "Athens":
        df = pd.read_csv(
            "../frontend/src/assets/points_of_interest/athens/athens.csv")
    elif location == "Rome":
        df = pd.read_csv(
            "../frontend/src/assets/points_of_interest/rome/rome.csv")
    else:
        df = pd.read_csv(
            "../frontend/src/assets/points_of_interest/paris/paris.csv")

    li = df.values.tolist()

    places = calcultateResults()

    beachNo = places.count("beach")
    outNo = places.count("out")
    museumNo = places.count("museums")
    religionNo = places.count("religion")
    natureNo = places.count("nature")

    museum = []
    out = []
    beach = []
    nature = []
    religion = []

    for i in range(28):
        if li[i][3] == "museum":
            museum.append(li[i])
        elif li[i][3] == "out":
            out.append(li[i])
        elif li[i][3] == "beach":
            beach.append(li[i])
        elif li[i][3] == "nature":
            nature.append(li[i])
        else:
            religion.append(li[i])

    beachFinal = random.sample(beach, beachNo)
    outFinal = random.sample(out, outNo)
    museumFinal = random.sample(museum, museumNo)
    religionFinal = random.sample(religion, religionNo)
    natureFinal = random.sample(nature, natureNo)

    allFinal = beachFinal + outFinal + museumFinal + religionFinal + natureFinal

    random.shuffle(allFinal)

    print("Final Places: ", allFinal)
    return allFinal
