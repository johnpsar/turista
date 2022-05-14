from cmath import nan
import pandas as pd
import datetime as dt

def dataExtract (inputDate, inputCountry):
    precipDf = pd.read_csv('helper/PrecipitationDataProcessed.csv')
    windDf = pd.read_csv('helper/WindSpeedDataProcessed.csv')
    tempDf = pd.read_csv('helper/TemperatureDataProcessed.csv')

    if inputCountry == "Athens":
        precipColName = "precipGR (m)"
        windColName = "windGR (m/s)"
        tempColName = "tempGR (C)"
    elif inputCountry == "Paris":
        precipColName = "precipFR (m)"
        windColName = "windFR (m/s)"
        tempColName = "tempFR (C)"
    else: 
        precipColName = "precipIT (m)"
        windColName = "windIT (m/s)"
        tempColName = "tempIT (C)"


    # Precip
    rowPrep = precipDf.loc[precipDf['datePrecipDf'] == inputDate]
    precip = float(rowPrep[precipColName].values[0])
    precip = round(precip, 3)

    if precip > 0.01:
        isRain = True
    else:
        isRain = False

    isRainNext = isRain


    # Wind
    rowWind1 = windDf.loc[windDf['dateTempWindDf'] == inputDate]

    try:
        rowWind2 = rowWind1.loc[rowWind1['timeTempWindDf'] == '12:00']
        windSpeed = float(rowWind2[windColName].values[0])
    except IndexError:
        rowWind2 = rowWind1.loc[rowWind1['timeTempWindDf'] == '13:00']
        windSpeed = float(rowWind2[windColName].values[0])

    windSpeed = round(windSpeed, 3)

    try:
        rowWind3 = rowWind1.loc[rowWind1['timeTempWindDf'] == '15:00']
        windSpeedNext = float(rowWind3[windColName].values[0])
    except IndexError:
        rowWind3 = rowWind1.loc[rowWind1['timeTempWindDf'] == '16:00']
        windSpeedNext = float(rowWind3[windColName].values[0])

    windSpeedNext = round(windSpeedNext, 3)

    if windSpeed > 3:
        isWindy = True
    else:
        isWindy = False

    if windSpeedNext > 3:
        isWindyNext = True
    else:
        isWindyNext = False


    # Temp
    rowTemp1 = tempDf.loc[tempDf['dateTempWindDf'] == inputDate]

    try:
        rowTemp2 = rowTemp1.loc[rowTemp1['timeTempWindDf'] == '12:00']
        temp = float(rowTemp2[tempColName].values[0])
    except:
        rowTemp2 = rowTemp1.loc[rowTemp1['timeTempWindDf'] == '13:00']
        temp = float(rowTemp2[tempColName].values[0])

    temp = round(temp, 1)

    try:
        rowTemp3 = rowTemp1.loc[rowTemp1['timeTempWindDf'] == '15:00']
        tempNext = float(rowTemp3[tempColName].values[0])
    except IndexError:
        rowTemp3 = rowTemp1.loc[rowTemp1['timeTempWindDf'] == '16:00']
        tempNext = float(rowTemp3[tempColName].values[0])

    tempNext = round(tempNext, 1)

    return [isRain, isRainNext, isWindy, isWindyNext, temp, tempNext]

