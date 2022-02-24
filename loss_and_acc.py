# Visualize training history
from cProfile import label
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy
import pandas as pd
from Plotwarts import HarryPlotManager



def makeGr():
    hp = HarryPlotManager()

    acc_train, acc_test = hp.get_dataset_dfs('history', 'accuracy', 'val_accuracy')
    loss_train, loss_test = hp.get_dataset_dfs('history', 'loss', 'val_loss') 
    k = 0
    x=[]
    for i in acc_test:
        x.append(k)
        k+=1

    ax1 = plt.subplot(2,1,1)
    ax1.plot(x, acc_train,c='r', label="training")
    ax1.plot(x, acc_test, label="validation")
    ax1.legend(loc="lower right")
    plt.xlim(-20, 75)
    plt.ylabel('accuracy')
    plt.xlabel('epochs')
    ax2 = plt.subplot(2,1,2)
    ax2.plot(x, loss_train, c='r', label="training")
    ax2.plot(x, loss_test,label="validation")
    ax2.legend(loc="upper right")
    plt.xlim(-20, 75)
    plt.ylabel('loss')
    plt.xlabel('epochs')
    plt.savefig(hp.get_final_img_url())
    #plt.show()
    return hp.get_final_img_url()



