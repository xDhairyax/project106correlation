import numpy as np 
import csv

def getdataSource(datapath):
    marks=[]
    daysPresent=[]
    with open(datapath)as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for i in csv_reader:
            marks.append(float(i["Marks"]))
            daysPresent.append(float(i["Days Present"]))

    return {"x":marks,"y":daysPresent}
    
def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between Marks and Number of Days Present is:",correlation[0,1])

def setup():
    datapath="data.csv"
    dataSource=getdataSource(datapath)
    findCorrelation(dataSource)

setup()

    