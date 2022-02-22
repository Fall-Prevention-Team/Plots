# Visualize training history
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy
import pandas as pd
from utils import build_url_dict


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
    plt.savefig(fig_path)
    return fig_path
    #plt.show()


class HarryPlotter:
    def __init__(self):
        url_data_dict = utils.build_url_dict()
        fig_out_root = './static/images/'
        already_build_imgs = []
    
    def get_csv_by_dict_key(self, dict_key):
        return pd.read_csv(self.url_data_dict[dict_key])
    
    def is_build(self, plot_name):
        if plot_name in self.already_build_imgs:
            return True
        return False
    
    





