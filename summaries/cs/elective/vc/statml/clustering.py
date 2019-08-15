from os import environ
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math
import scipy.stats as stats
from genData import *


alphabet = ('A', 'B', 'C', 'D', 'E', 'F')


xmin = -8
xmax = 11
ymin = -10
ymax = 11
x = np.arange(xmin, xmax, 0.1)
y = np.arange(ymin, ymax, 0.1)
X, Y = np.meshgrid(x, y)


data = models2d_read()



# MoG.
def doMoG():
    fig, ax = plt.subplots()
    models2d_plot(x, y, ax, True)
    fig.savefig('tmp-clustering-example.pdf')



# Mean shift clustering.
def msc_kernel_grad(u):
    return (-u * np.exp(-(u ** 2) / 2)) / np.sqrt(2 * np.pi)

def meanShift(X, g, h, alpha, iterations):
    pastX = [np.copy(X)]
    for k in range(iterations):
        for j in range(len(X)):
            x = X[j]
            dif = (x - X).T
            gi = g((np.multiply(dif[0], dif[1]) / h) ** 2)
            gi = np.repeat(gi.reshape(-1, 1), X.shape[1], axis = 1)
            m = np.sum(np.multiply(X, gi)) / np.sum(gi) - x
            X[j] = X[j] + alpha * m
        pastX.append(np.copy(X))
    return pastX

def belongsToCluster(s, cluster, epsilon):
    return (np.linalg.norm(s - cluster, 2) <= epsilon).any()

def extractClusters(X, shifted, epsilon):
    clusters = []
    clusterValues = []
    for i, s in enumerate(shifted):
        x = X[i]
        inserted = False
        for j, cluster in enumerate(clusters):
            if belongsToCluster(s, cluster, epsilon):
                cluster.append(s)
                clusterValues[j].append(x)
                inserted = True
                break
        if not inserted:
            clusters.append([s])
            clusterValues.append([x])
    return (clusters, clusterValues)

def doMeanShiftClustering(X, g, h, epsilon, alpha, iterations):
    shifted = np.copy(X)
    pastX = meanShift(shifted, g, h, alpha, iterations)
    print('Mean shifting finished. Extracting clusters.')
    clusters, clusterValues = extractClusters(X, shifted, epsilon)

    fig, ax = plt.subplots()
    models2d_plot(x, y, ax)
    for i, clusterValue in enumerate(clusterValues):
        ax.scatter(*(np.array(clusterValue).T), label = ('Cluster %d' % (i + 1)))
    ax.legend()
    ax.set_title('$ h = %.2f, \\varepsilon = %.2f, \\alpha = %.2f, n = %d $' % (h, epsilon, alpha, iterations))
    fig.savefig('tmp-clustering-meanShift.pdf')
    for pastx in pastX:
        ax.scatter(*(np.array(pastx).T), s = 1, color = 'red')
    fig.savefig('tmp-clustering-meanShift-way.pdf')





doMoG()
doMeanShiftClustering(data, msc_kernel_grad, 0.5, 0.1, 0.2, 50)

if environ.get('SHOW') != None:
    plt.show()
