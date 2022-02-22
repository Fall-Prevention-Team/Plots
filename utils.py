
def build_url_dict():
    root = 'https://raw.githubusercontent.com/Fall-Prevention-Team/Current_model_stats/main/stats/'
    urls = {
        'history':root+'history.csv',
        'best_model':root+'df_best_model.csv',
        'df_metrics':root+'df_metrics.csv',
        'test_duration':root+'test_duration.csv'
    }
    return urls


