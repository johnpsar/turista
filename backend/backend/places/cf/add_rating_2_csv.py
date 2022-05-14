import pandas as pd
from csv import writer

from .findResults import results

userData = [4, 0, 1, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 3, 2]  # example, erxetai ap to frontend

# const images = [
#   Beach2,
#   Out1,
#   Beach1,
#   Out2,
#   Museum5,
#   Religion3,
#   Out3,
#   Nature3,
#   Religion1,
#   Museum3,
#   Museum1,
#   Beach3,
#   Museum5,
#   Religion2,
#   Nature1,
#   Museum2,
#   Out4,
#   Nature2
# ];


def addNewRating(userData4, location):
    ratingDf = pd.read_csv("places/cf/rating.csv")

    lenDf = ratingDf.shape[0]
    print("pipi")

    with open('places/cf/rating.csv', 'a', newline="") as f_object:

        writer_object = writer(f_object)

        for i in range(18):

            newRating = [str(ratingDf.iloc[-1]['userid']+1),
                         str(i+1), str(userData[i])]

            writer_object.writerow(newRating)

        f_object.close()

    allFinal = results(location)

    return allFinal
