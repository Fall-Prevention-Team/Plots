import matplotlib.pyplot as plt
import pandas as pd
from link_builder import SisFallCollector


def GetList(Req=1, max_count=15):
    list_of_urls = []
    for i, n in SisFallCollector.get_datasets_by_person_id_iter(Req):
        watch = makedata(i)
        url = getURL(n, watch)
        list_of_urls.append(url)

    return list_of_urls


def makedata(data):
    Traning_set = []
    watch = []
    Traning_set = data.values.tolist()
    for i in Traning_set:
        watch.append([i[0], i[1], i[2]])
    
    return watch



def getURL(n,watch):
    y1 = []
    y2 = []
    y3 = []
    for j in watch:
    
        y1.append(j[0])
        y2.append(j[1])
        y3.append(j[2])

    plt.subplot(3,1,1)
    plt.plot(y1)

    plt.subplot(3,1,2)
    plt.plot(y2)

    plt.subplot(3,1,3)
    plt.plot(y3)
    
    path = "./static/images/dataset" + str(n) + ".png"
    plt.savefig(path)
    plt.cla()
    plt.clf()
    return path
