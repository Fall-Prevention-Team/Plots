from urllib.error import HTTPError
import pandas as pd
import numpy as np
import urllib

class SisFallCollector:
    root = 'https://raw.githubusercontent.com/Fall-Prevention-Team/sisfallData/main/'

    young_people = {
        'amount':23,
        'ext':'SA'
    }
    old_people = {
        'amount':15,
        'ext':'SE'
    }
    rec_no_fall = {
        'amount':19,
        'iters':5,
        'last_single':4,
        'char':'D'
        }
    rec_fall = {
        'amount':15,
        'iters':5,
        'char':'F'
        }

    @classmethod
    def get_datasets_by_person_id_iter(cls, pid, age_group='SA'):
        person_full_id = ''
        if cls.young_people['ext'] == age_group or cls.old_people['ext'] == age_group:
            person_full_id += age_group
        else:
            raise ValueError('Age groups are SA and SE.')

        if len(str(pid)) == 1:
            person_full_id += '0'
        person_full_id += str(pid)

        # should assert if person exists i dataset

        for rec_num in range(1, cls.rec_no_fall['amount']+1):
            url_id_first = person_full_id+'/'+cls.rec_no_fall['char']
            if len(str(rec_num)) == 1:
                url_id_first += '0'
            url_id_first += str(rec_num)
            
            if rec_num < cls.rec_no_fall['last_single'] + 1:
                iter_range = 2
            else:
                iter_range = cls.rec_no_fall['iters'] +1

            for it in range(1, iter_range):
                try:
                    url_id_iter = '_'+person_full_id+'_R0'+str(it)+'.txt'
                    final_url = cls.root + url_id_first + url_id_iter
                    res = pd.read_csv(final_url, header=None)
                    yield res, url_id_first + url_id_iter
                except urllib.error.HTTPError as e:
                    print(e)
                    continue
                    

        for rec_num in range(1, cls.rec_fall['amount']+1):
            url_id_first = person_full_id+'/'+cls.rec_fall['char']
            if len(str(rec_num)) == 1:
                url_id_first += '0'
            url_id_first += str(rec_num)

            for it in range(1, cls.rec_fall['iters'] +1):
                
                url_id_iter = '_'+person_full_id+'_R0'+str(it)+'.txt'
                final_url = cls.root + url_id_first + url_id_iter
                res = pd.read_csv(final_url, header=None)
                yield res, url_id_first + url_id_iter


if __name__ == '__main__':
    for i in SisFallCollector().get_datasets_by_person_id_iter(1):
        print(i)

