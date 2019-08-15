from os import environ
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math
import scipy.stats as stats
from sklearn.decomposition import PCA
from matplotlib.lines import Line2D


plants = ('Setosa', 'Versicolor', 'Virginica')

data = np.loadtxt('datasets/iris.txt', delimiter = ',')
X = data[:, :-1]
Y = data[:, -1].astype('int32')


mean = np.mean(X, axis = 0)
std = np.std(X, axis = 0)
Xnorm = (X - mean) / std
covNorm = np.cov(Xnorm.T, rowvar = True)

eigenvalues, eigenvectors = np.linalg.eig(covNorm)
eigenvalues, eigenvectors = zip(*sorted(zip(eigenvalues, eigenvectors), reverse = True))
eigenvectors = np.array(eigenvectors)
variance = np.cumsum(eigenvalues) / np.sum(np.var(Xnorm, axis = 0))

fig, ax = plt.subplots()
x = range(1, len(variance) + 1)
ax.plot(x, variance, '-o')
ax.set_xticks(x)
ax.set_title('Explained Variance')
ax.set_xlabel('No. of Components')
ax.set_ylabel('Explained Variance (Proportion)')
fig.savefig('tmp-pca-variance.pdf')

# Get the first 2 eigenvectors.
B = eigenvectors[:, :2]

a = B.T @ Xnorm.T

colors = np.array(('blue', 'green', 'black'))
fig, ax = plt.subplots()
ax.scatter(*a, c = colors[Y], s = 10)
ax.set_xlabel('Principal Component 1')
ax.set_ylabel('Principal Component 2')
ax.set_title('Principal Component Analysis (Iris Dataset)')
ax.legend(handles = [Line2D([0], [0], marker = 'o', color = 'w', label = plants[label], markerfacecolor = colors[label]) for label in set(Y)])
fig.savefig('tmp-pca-iris.pdf')





if environ.get('SHOW') != None:
    plt.show()
