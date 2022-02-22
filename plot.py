import matplotlib.pyplot as plt
import pandas as pd

first_watch_NOTFALL = []
second_watch_NOTFALL = [] 
third_watch_NOTFALL = []

first_watch_FALL = []
second_watch_FALL = [] 
third_watch_FALL = []

def GetListNF():

    with open('C:\DATA\SisFall_dataset\SA01\F05_SA01_R01.txt', 'r', encoding= "utf8") as f:
        return pd.read_csv(f)


def makedata(data):
    Traning_set = data.values.tolist()

    for i in Traning_set:
        first_watch_NOTFALL.append([i[0], i[1], i[2]])
        second_watch_NOTFALL.append([i[3], i[4], i[5]])
        third_watch_NOTFALL.append([i[6], i[7], i[8]])



makedata(GetListNF())
#print(first_watch_NOTFALL)
print(first_watch_NOTFALL[0][0])
y1 = []
y2 = []
y3 = []
x = []
k = 1
for j in second_watch_NOTFALL:
    
    y1.append(j[0])
    y2.append(j[1])
    y3.append(j[2])
    x.append(k)
    k+=1

def getURL():
    plt.subplot(3,1,1)
    plt.plot(x, y1)

    plt.subplot(3,1,2)
    plt.plot(x,y2)

