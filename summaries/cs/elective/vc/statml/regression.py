from os import environ
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math
import scipy.stats as stats
from genData import *


xmin = -4
xmax = 7
ymin = -300
ymax = 300
X = np.arange(xmin, xmax, 0.1).reshape(-1, 1)


data = modelsRegression_read()
dataX = data[0, :].reshape(-1, 1)
dataY = data[1, :].reshape(-1, 1)



def phi(x, d):
    result = []
    for i in range(0, d + 1):
        result.append(np.power(x, i).flatten())
    return np.array(result)


# Truth.
def doTruth():
    fig, ax = plt.subplots()
    modelsRegression_plot(X, ax, plotSamples = True)
    ax.set_xlim(xmin, xmax)
    ax.legend()
    ax.set_title('Regression: True Function')
    fig.savefig('tmp-regression-truth.pdf')


# Least squares regression.
def lsr_plot_one(dataX, dataY, d, ax):
    Phi = phi(dataX, d)
    w = np.linalg.solve(Phi @ Phi.T, Phi @ dataY)

    phis = phi(X, d)
    ys = w.T @ phis

    ax.plot(X, ys.T, label = 'LSR ($ d = %d $)' % d)

def doLeastSquaresRegression(dataX, dataY, D):
    fig, ax = plt.subplots()
    modelsRegression_plot(X, ax, plotSamples = True)
    for d in D:
        lsr_plot_one(dataX, dataY, d, ax)
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.legend()
    ax.set_title('Least Squares Regression')
    fig.savefig('tmp-regression-lsr.pdf')


# Maximum likelihood regression.
def doMaximumLikelihoodRegression(dataX, dataY, d):
    Phi = phi(dataX, d)
    w = np.linalg.solve(Phi @ Phi.T, Phi @ dataY)
    variance = np.sum(np.power(dataY - (w.T @ Phi).reshape(-1, 1), 2)) / dataY.shape[0]
    std = np.sqrt(variance)

    phis = phi(X, d)
    ys = w.T @ phis

    fig, ax = plt.subplots()
    modelsRegression_plot(X, ax, plotSamples = True)
    ax.plot(X, ys.T, '-k', label = 'MLR')
    ax.fill_between(X.flatten(), (ys - std).flatten(), (ys + std).flatten(), alpha = 0.5, label = 'MLE: Standard Deviation')
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.legend()
    ax.set_title('Maximum Likelihood Regression ($ d = %d $)' % d)
    fig.savefig('tmp-regression-mlr-%d.pdf' % d)


# Full bayesian regression.
def doFullBayesianRegression(n, dataX, dataY, d, alpha, beta):
    Phi = phi(dataX, d)
    I = np.identity(Phi.shape[0])
    meanMatrix = (alpha / beta) * I + Phi @ Phi.T
    varianceMatrix = alpha * I + beta * Phi @ Phi.T

    def mean(x):
        right = np.linalg.solve(meanMatrix, Phi) @ dataY
        return phi(x, d).T @ right

    def variance(x):
        right = np.linalg.solve(varianceMatrix, phi(x, d))
        return (phi(x, d).T @ right) / beta

    ys = []
    variances = []
    for x in X:
        ys.append(mean(x).flatten())
        variances.append(variance(x).flatten())
    ys = np.array(ys)
    std = np.sqrt(np.array(variances))

    fig, ax = plt.subplots()
    modelsRegression_plot(X, ax, plotSamples = True, limit = n)
    ax.plot(X, ys, '-k', label = 'Full FBR')
    ax.fill_between(X.flatten(), (ys - std).flatten(), (ys + std).flatten(), alpha = 0.5, label = 'FBR: Standard Deviation')
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.legend()
    ax.set_title('Full Bayesian Regression (%d samples, $ d = %d $)' % (n, d))
    fig.savefig('tmp-regression-fb-%d.pdf' % n)


# Kernel regression.
def doKernelRegression(dataX, dataY, ridge, kernel_name, kernel_parameter):
    def kernel(x, y):
        if kernel_name == 'Polynomial':
            return np.inner(x, y) ** kernel_parameter
        elif kernel_name == 'RBF':
            return np.exp(-(np.abs(x - y) ** 2) / (2 * kernel_parameter))
        else:
            raise Exception('Unknown kernel ' + str(kernel_name) + '!')

    # Gram matrix.
    K = np.zeros((dataX.shape[0], dataX.shape[0]))
    for i, xi in enumerate(dataX):
        for j, xj in enumerate(dataX):
            K[i, j] = kernel(xi, xj)

    theta = np.linalg.solve(K + ridge * np.identity(K.shape[0]), dataY)

    ys = []
    for x in X:
        ys.append(float(kernel(x, dataX).T @ theta))
    ys = np.array(ys)

    fig, ax = plt.subplots()
    modelsRegression_plot(X, ax, plotSamples = True)
    ax.plot(X, ys, label = 'KR')
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.legend()
    ax.set_title('Kernel Regression (%s, %d)' % (kernel_name, kernel_parameter * 100))
    fig.savefig('tmp-regression-kernel-%s-%d.pdf' % (kernel_name, kernel_parameter * 100))





doTruth()
doLeastSquaresRegression(dataX, dataY, (4, 7, 20))
doMaximumLikelihoodRegression(dataX, dataY, 4)
doMaximumLikelihoodRegression(dataX, dataY, 7)
doMaximumLikelihoodRegression(dataX, dataY, 20)
for n in (2, 8, dataY.shape[0]):
    doFullBayesianRegression(n, dataX[:n, :], dataY[:n, :], 10, 1 / 1, 0.01)
doKernelRegression(dataX, dataY, 0.01, 'RBF', 0.01)
doKernelRegression(dataX, dataY, 0.01, 'RBF', 1)

if environ.get('SHOW') != None:
    plt.show()
