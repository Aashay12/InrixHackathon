import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import sklearn.tree as tree

import pickle

df_ranks = pd.read_csv('./dataWithRanks.csv', index_col=0)

# df_rank_only = df_ranks.drop(['Latitude', 'Longitude'], axis=1)

X = df_ranks.drop('ranks', axis=1)
Y = df_ranks.ranks

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.3, random_state=0)

# print(X_train)
cl = RandomForestClassifier(random_state=0)
cl.fit(X_train, Y_train)

# lr = LogisticRegression()
# lr.fit(X_train, Y_train)

# dt = tree.DecisionTreeClassifier(max_depth=3)
# dt.fit(X_train, Y_train)


filename = 'finalized_model_with_LatLong.sav'
pickle.dump(cl, open(filename, 'wb'))
