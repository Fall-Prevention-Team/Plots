from mimetypes import init
import numpy
import pandas as pd
import os
from link_builder import SisFallCollector
import matplotlib.pyplot as plt

class HarryPlotManager:
    
    # no functionality yet, just infrastructure
    already_build_imgs = []
    
    def __init__(self):
        self.url_data_dict = self.build_url_dict()
        self.fig_out_root = './static/images/'
        self.outpath = ''
    
    def get_dataset_dfs(self, csv_name='history', column_one='loss', column_two='val_loss'):
        csvf = self.get_csv_by_dict_key('history')
        self.outpath += f'{csv_name}{column_one}{column_two}'
        return csvf[column_one], csvf[column_two]
    
    def get_csv_by_dict_key(self, dict_key):
        return pd.read_csv(self.url_data_dict[dict_key])
    
    def is_build(self, plot_name):
        if plot_name in self.already_build_imgs:
            return True
        return False
    
    def get_final_img_url(self):
        self.already_build_imgs.append(self.outpath)
        return self.fig_out_root + self.outpath + '.png'
    
    @classmethod
    def reset_build_graphs(cls):
        cls.already_build_imgs = []
    

    
    def build_url_dict(self):
        root = 'https://raw.githubusercontent.com/Fall-Prevention-Team/Current_model_stats/main/stats/'
        urls = {
            'history':root+'history.csv',
            'best_model':root+'df_best_model.csv',
            'df_metrics':root+'df_metrics.csv',
            'test_duration':root+'test_duration.csv'
        }
        return urls

class RonPLotWheasley:

    def __init__(self):
        self.root_path_to_img = "./static/images/"
   
    def Make_placement_for_person_x(self, Req, age_tag):
        for i, folderpath in SisFallCollector.get_datasets_by_person_id_iter(Req, age_tag):
            foldername = folderpath.split('/')[0]
            if not os.path.exists(self.root_path_to_img + foldername):
                os.makedirs(self.root_path_to_img + foldername)

            return
            
     

    def getURL(self, folderpath, watch):
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
        plt.tight_layout()
        path = self.root_path_to_img + folderpath + ".png"
        plt.savefig(path)
        plt.cla()
        plt.clf()
        return path

    def Generate_plots_for_person_X(self, person_num, age_tag, maxcount=None):
        self.Make_placement_for_person_x(person_num, age_tag)
        list_of_urls = []
        if not maxcount:
            Mcount = 15
        else:
            Mcount = maxcount
        for data, folderpath in SisFallCollector.get_datasets_by_person_id_iter(person_num, age_tag):
           list_of_urls.append(self.getURL(folderpath, data.values.tolist()))
           print(len(list_of_urls), len(list_of_urls) > Mcount)
           if len(list_of_urls) >= Mcount:
               break
     
     
        return list_of_urls

