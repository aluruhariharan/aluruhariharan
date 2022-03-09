import numpy as np


def standard_scaler(data):

	X = np.array(data)
	N = X.shape[0]
	print("sum of series:",N,end='\n')
	U = np.average(X,axis=0)
	print("avg of input:",U)
	sig = np.square(X-U)
	sig1 = np.sum(sig,axis=0)
	sig = sig1/N
	sig  = np.sqrt(sig)
	print("the sig value:",sig)
	Z = (X-U)/sig
	print(Z)
	return Z

def normalized(data):
	X = np.array(data)
	U = np.average(X,axis=0)
	print(U)
	X_norm = (X-np.minimum(X[0],X[1]))/(np.minimum(X[0],X[1])-np.maximum(X[0],X[1]))
	return X_norm



data = [[0, 0],
 [1, 0],
 [0, 1],
 [1, 1]]

print(standard_scaler(data))
print(normalized(data))