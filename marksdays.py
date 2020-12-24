import csv
import numpy as np

def getDataSource(datapath):
    Student_Marks = []
    Days_Present = []
    with open(datapath) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader :
            Student_Marks.append(float(row["Marks scored by Students"]))
            Days_Present.append(float(row["No. of Days Present"]))

    return{"x":Student_Marks,"y":Days_Present}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation between Students Marks and No. of Days Present :- \n--->",correlation[0,1])

def setup():
    data_path = "Student Marks vs Days Present.csv" 

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()

