from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import SelectFromModel
import pickle, sys  
def Run_Forrest_Run():
    root = './test_and_train_sets'
    test_data = pd.read_csv(root + '/out_TEST.tsv', sep='\t', header=None)
    train_data = pd.read_csv(root + '/out_TRAIN.tsv', sep='\t', header=None)
    y_test = test_data[0]
    x_test = test_data.loc[:, test_data.columns != 0]
    y_train = train_data[0]
    x_train = train_data.loc[:, test_data.columns != 0]
    for n in range(1,12):
        feat_clf = SelectFromModel(RandomForestClassifier(n_estimators=20))
        clf = RandomForestClassifier(n_estimators=20)
        clf.fit(x_train, y_train)
        feat_clf.fit(x_train, y_train)
        features_selected = x_train.columns[(feat_clf.get_support())]
        print(len(features_selected))
        print(features_selected)
        print(clf.estimators_[0])
        prediction_of_y = clf.predict(x_test)
        acc = accuracy_score(y_true=y_test, y_pred=prediction_of_y)
        print(n ," Precision: " + str(acc))
        
    
    #save_clf(clf)
    


def save_clf(model):
    with open("model.pickle", 'wb') as f:
        pickle.dump(model, f, protocol=pickle.HIGHEST_PROTOCOL)


if "t" in sys.argv:
    Run_Forrest_Run()
    print("forest COMPLETED")
    exit()