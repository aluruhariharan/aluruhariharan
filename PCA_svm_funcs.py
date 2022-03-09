import numpy as np
import pandas as pd
from split import *
import matplotlib.pyplot as plt
import seaborn as sns

def standard_scaler(data):

	X = np.array(data)
	N = X.shape[0]
	#print("sum of series:",N,end='\n')
	U = np.mean(X,axis=0)
	#print("avg of input:",U)
	sig = np.square(X-U)
	sig1 = np.sum(sig,axis=0)
	sig = sig1/N
	sig  = np.sqrt(sig)
	#print("the sig value:",sig)
	Z = (X-U)/sig
	#print(Z)
	return Z

data = pd.read_csv('Iris.csv')
data = data.drop('Id',axis=1)
Y = data['Species']
data = data.drop('Species',axis=1)
print(data.head())
print(Y)

X_train , X_test = train_split(data)

Y = Y.sample(frac=1).reset_index(drop=True)
s = int(len(Y)/4)
s = int(len(Y)-s)
y_train = Y
y_test = Y.iloc[s:]

X_scaled=standard_scaler(X_train)

#print(X_scaled)
print(y_test)

feat = X_scaled.T

cov_mat = np.cov(feat)

#print(cov_mat)

eigen_values, eigen_vectors = np.linalg.eig(cov_mat)

print(eigen_values)
print(eigen_vectors)



projected_1 = X_scaled.dot(eigen_vectors.T[0])
projected_2 = X_scaled.dot(eigen_vectors.T[1])
res = pd.DataFrame(projected_1, columns=['PC1'])
res['PC2'] = projected_2
res['Y'] =  y_test
print(res.head(6))


plt.figure(figsize=(20, 10))
sns.scatterplot(res['PC1'], [0] * len(res), hue=res['Y'], s=200)

plt.show()