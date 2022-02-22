# Visualize training history
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

    plt.subplot(2,1,1)
    plt.plot(acc_train)
    plt.plot(acc_test)
    plt.xlim(0, 1500)
    plt.ylabel('accuracy')
    plt.xlabel('epochs')

    plt.subplot(2,1,2)
    plt.plot(loss_train)
    plt.plot(loss_test)
    plt.xlim(0, 1500)
    plt.ylabel('loss')
    plt.xlabel('epochs')

    plt.savefig(hp.get_final_img_url())
    #plt.show()
    return hp.get_final_img_url()



