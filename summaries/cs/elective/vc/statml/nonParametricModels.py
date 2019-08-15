from os import environ
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from genData import *


xmin = -35
xmax = 55
x = np.arange(xmin, xmax, 0.1)


data = models_read()



# Histogram.
def doHistogram(binSizes):
    binsS = [np.arange(xmin, xmax, binSize) for binSize in binSizes]

    fig, ax = plt.subplots()
    models_plot(x, ax)
    for i, bins in enumerate(binsS):
        ax.hist(data, bins,
                    alpha = 0.5,
                    edgecolor = 'black',
                    density = True,
                    label = ('Bin Size = %.2f' % binSizes[i]))
    ax.legend()
    fig.savefig('tmp-nonParametricModels-histogram.pdf')



# TODO: Not working.
# KDE: Parzen window.
def kde_parzen_H(u, h):
    if (abs(u) <= h / 2).all():
        return np.ones(len(u))
    return np.zeros(len(u))

def kde_parzen_p(x, X, h):
    sum = 0
    for xi in X:
        sum += kde_parzen_H(x - xi, h)
    return sum / (len(X) * h)

def doKdeParzen(h):
    y = [kde_parzen_p(x, data, hi) for hi in h]

    fig, ax = plt.subplots()
    models_plot(x, ax)
    for i, yi in enumerate(y):
        ax.plot(x, yi, label = ('$ h = %.2f $' % h[i]))
    ax.legend()
    fig.savefig('tmp-nonParametricModels-kde-parzen.pdf')



# KDE: Gaussian kernel.
def kde_gaussian_H(u, h):
    return np.exp(-(u ** 2) / (2 * h ** 2)) / np.sqrt(2 * np.pi * h ** 2)

def kde_gaussian_p(x, X, h):
    sum = 0
    for xi in X:
        sum += kde_gaussian_H(x - xi, h)
    return sum / len(X)

def doKdeGaussian(h):
    y = [kde_gaussian_p(x, data, hi) for hi in h]

    fig, ax = plt.subplots()
    models_plot(x, ax)
    for i, yi in enumerate(y):
        ax.plot(x, yi, label = ('$ h = %.2f $' % h[i]))
    ax.legend()
    fig.savefig('tmp-nonParametricModels-kde-gaussian.pdf')



# KNN.
def knn_getNeighbors(x, X, K):
    d = list(X - x)
    d.sort(key = abs)
    d = d[:K]
    return np.array(d) + x

def knn_getMaxDistance(x, neighbors):
    d = np.abs(neighbors - x)
    return d.max()

def knn(x, X, K):
    neighbors = knn_getNeighbors(x, X, K)
    distance = knn_getMaxDistance(x, neighbors)
    return K / (len(X) * distance)

def doKnn(K):
    y = []
    for Ki in K:
        yi = []
        for xi in x:
            yi.append(knn(xi, data, Ki))
        y.append(yi)

    fig, ax = plt.subplots()
    models_plot(x, ax)
    for i, yi in enumerate(y):
        ax.plot(x, yi, label = ('$ K = %d $') % K[i])
    ax.legend()
    fig.savefig('tmp-nonParametricModels-knn.pdf')





doHistogram((0.5, 3, 20))
doKdeParzen((1, 5, 10))
doKdeGaussian((1, 5, 10))
doKnn((10, 75, 1000))

if environ.get('SHOW') != None:
    plt.show()
