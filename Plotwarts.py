import numpy
import pandas as pd

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

