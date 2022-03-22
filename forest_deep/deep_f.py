from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.metrics import accuracy_score
    
def Run_Forrest_Run():
    root = './test_and_train_sets'
    test_data = pd.read_csv(root + '/out_TEST.tsv', sep='\t', header=None)
    train_data = pd.read_csv(root + '/out_TRAIN.tsv', sep='\t', header=None)
    y_test = test_data[0]
    x_test = test_data.loc[:, test_data.columns != 0]
    y_train = train_data[0]
    x_train = train_data.loc[:, test_data.columns != 0]
    print(y_test)
    print(x_test)
    clf = RandomForestClassifier(n_estimators=100)
    clf.fit(x_train, y_train)
    prediction_of_y = clf.predict(x_test)
    acc = accuracy_score(y_true=y_test, y_pred=prediction_of_y)
    print("Precision: " + str(acc))

for i in range(0,10):

    Run_Forrest_Run()