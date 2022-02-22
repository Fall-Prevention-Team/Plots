# Visualize training history
from cgitb import html
from msilib import sequence
import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox
import numpy
import pandas as pd
import base64
from io import BytesIO

url_training = 'https://raw.githubusercontent.com/Fall-Prevention-Team/KerasFallPredicter/main/results/inception/TSC_itr_1/Meat/history.csv'
# Below, not the real validation dataset, to be continued...
url_test = 'https://raw.githubusercontent.com/Fall-Prevention-Team/KerasFallPredicter/main/results/inception/TSC_itr_2/Meat/history.csv'
DataFrame_training = pd.read_csv(url_training)
DataFrame_test = pd.read_csv(url_test)

def makeGr():
    fig_path = "./static/images/graph.png"

    accuricy_training_acc = DataFrame_training.iloc[:,1]
    accuricy_test_acc = DataFrame_test.iloc[:,1]
    plt.subplot(1,2,1)
    plt.plot(accuricy_training_acc)
    plt.plot(accuricy_test_acc)
    plt.xlim(0,75)
    plt.ylabel('accuricy')
    plt.xlabel('epoch')
    accuricy_training_loss = DataFrame_training.iloc[:,0]
    accuricy_test_loss = DataFrame_test.iloc[:,0]
    plt.subplot(1,2,2)
    plt.plot(accuricy_training_loss)
    plt.plot(accuricy_test_loss)
    plt.xlim(0,75)
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.savefig(fig_path, bbox_inches='tight')
    return fig_path
    #plt.show()
