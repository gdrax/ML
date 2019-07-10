# bin/python2.7

import graphlab as gl
# print gl.get_dependencies()
# Load the data
import pandas as pd

CUP = "../DATA/training_set.csv"
import numpy as np


def getTrainData(data_path, DimX, DimY, sep):
    startX, endX = DimX.split(':')
    startY, endY = DimY.split(':')
    data = pd.read_csv(data_path, header=None, sep=sep)
    print(data.shape)
    X = np.array(data.iloc[:, int(startX):int(endX)])
    Y = np.array(data.iloc[:, int(startY):int(endY)])

    return X, Y


data = gl.SFrame.read_csv('training_set.csv', header=True)

# Label 'p' is edible
# data['label'] = data['label'] == 'p'
# print data
# print "ciao"

# Make a train-test split
# train_data, test_data = getTrainData(CUP, '1:11', '11:13', ',')
train_data, test_data = data.random_split(0.8)
# train_data = test_data = data
# train_data= gl.SFrame(train_data, test_data)
# test_data = gl.SFrame(train_data,test_data)
# Create a model.
model = gl.random_forest_regression.create(train_data,
                                           max_iterations=1000,
                                           max_depth=9, target='target1',
                                           features=['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10'], metric='mse')

# model2 = gl.random_forest_regression.create(train_data,
#                                             max_iterations=1000,
#                                             max_depth=9, target='target2',
#                                             features=['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10'])

# Save predictions to an SArray
test_data = test_data.remove_column('target2')
predictions = model.predict(test_data)

# Evaluate the model and save the results into a dictionary
results = model.evaluate(test_data)

# model.show(view="Tree", tree_id=0)
# model.show(view="Tree", tree_id=1)
