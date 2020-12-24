import csv
import numpy as np

def getDataSource(datapath):
    cups_of_cofee = []
    Hours_of_sleep = []
    with open(datapath) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader :
            cups_of_cofee.append(float(row["Cups of Coffee"]))
            Hours_of_sleep.append(float(row["Hours of sleep"]))

    return{"x":cups_of_cofee,"y":Hours_of_sleep}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation between cups of cofee and Hours of sleep :- \n--->",correlation[0,1])

def setup():
    data_path = "cups of coffee vs hours of sleep.csv" 

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()

