import sklearn.preprocessing as sk_p
import pandas as pd
import numpy as np
import sys

data_path = sys.argv[1]

data = pd.read_csv(data_path, header='infer', engine='python')

# scale data
normalized_data = pd.DataFrame(sk_p.scale(data))

print(normalized_data)
print("STANDARD DEVIATION:")
print(np.std(normalized_data))
print("MEAN:")
print(np.mean(normalized_data))

remove_n = 102

drop_ind = np.random.choice(normalized_data.index, remove_n, replace=False)

print(type(drop_ind))

test_set = normalized_data.iloc[drop_ind, :]

filepath = "test_set.csv"
file = open(filepath, mode='w')
test_set.to_csv(file, sep=',', header=False, index=False)

training_set = normalized_data.drop(drop_ind)

filepath = "training_set.csv"
file = open(filepath, mode='w')
training_set.to_csv(file, sep=',', header=False, index=False)
