from os import environ
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math
import scipy.stats as stats
from genData import *
from cvxopt import matrix, solvers


xmin = -2.5
xmax = 8.5
ymin = -1
ymax = 8


data = np.array(modelsSeparable_read())
dataX = data[:, :-1]
dataY = data[:, -1].reshape(-1, 1)
dataNotSeparable = np.array(modelsNotSeparable_read())
dataNotSeparableX = dataNotSeparable[:, :-1]
dataNotSeparableY = dataNotSeparable[:, -1].reshape(-1, 1)



# Utility.
def separate(X, label1Name, label2Name, classify):
    classes = { }
    classes[label1Name] = []
    classes[label2Name] = []
    for x in X:
        labelPrediction = classify(x)
        if labelPrediction < 0:
            classes[label1Name].append(x)
        elif 0 < labelPrediction:
            classes[label2Name].append(x)
        else:
            print('Cannot classify %s as %s or %s (got %.2f)!' % (str(x), label1Name, label2Name, labelPrediction))
    return classes

def plotClasses(ax, classes, highlight = False):
    for key, value in classes.items():
        ax.scatter(*(np.array(value)[:, :2].T), label = 'Class %s' % key, s = (20 if highlight else 2), marker = ('x' if highlight else 'o'))

def plotData(ax):
    classes = separate(data, 'A', 'B', lambda x: x[2])
    plotClasses(ax, classes)

def plotNotSeparableData(ax):
    classes = separate(dataNotSeparable, 'A', 'B', lambda x: x[2])
    plotClasses(ax, classes)


# Truth.
def doTruth():
    fig, ax = plt.subplots()
    plotData(ax)
    ax.legend()
    ax.set_title('Original Data')
    fig.savefig('tmp-svm-separable.pdf')


# Linear SVM.
def doLinearSVM(X, labels):
    support_vector_threshold = 1e-5

    # Cost function.
    left = labels @ labels.T
    right = np.empty(left.shape)
    for i, xi in enumerate(X):
        for j, xj in enumerate(X):
            right[i, j] = np.inner(xi, xj)
    P = matrix(np.multiply(left, right))
    q = matrix(-np.ones((left.shape[0], 1)))
    # Inequality constraints.
    G = matrix(np.vstack((-np.identity(len(labels)))))
    h = matrix(np.vstack((np.zeros(len(labels)).reshape(-1, 1))))
    # Equality constraints.
    A = matrix(labels.reshape(1, -1))
    b = matrix(0.0)

    # Solve the optimization problem.
    solvers.options['show_progress'] = False
    sol = solvers.qp(P, q, G, h, A, b)
    alphas = np.array(sol['x'])

    # Retrieve the support vectors and construct the disriminator.
    S = (alphas > support_vector_threshold).flatten()
    support_vectors = X[S]
    support_alphas = alphas[S]
    support_labels = labels[S]
    w = (np.multiply(support_labels, support_alphas).T @ support_vectors).T
    b = np.sum(support_labels - support_vectors @ w) / len(support_vectors)

    def discriminator(x):
        return w.T @ x + b


    fig, ax = plt.subplots()
    x = np.arange(xmin, xmax, 0.1)
    y = np.arange(ymin, ymax, 0.1)
    xMesh, yMesh = np.meshgrid(x, y)

    margin = support_vectors[1:3]
    delta = margin[0] - margin[1]
    marginM = delta[1] / delta[0]
    marginB = margin[0][1] - marginM * margin[0][0]
    ax.plot(x, marginM * x + marginB, '--', color = 'lightblue')
    marginB = support_vectors[0][1] - marginM * support_vectors[0][0]
    ax.plot(x, marginM * x + marginB, '--', color = 'lightblue')

    classes = separate(X, 'A (Pred.)', 'B (Pred.)', discriminator)
    plotClasses(ax, classes, True)
    plotData(ax)
    ax.scatter(*(np.array(support_vectors).T), label = 'Support Vectors', facecolors = 'none', edgecolors = 'black', s = 20)
    pos = np.empty(xMesh.shape + (2,))
    pos[:, :, 0] = xMesh
    pos[:, :, 1] = yMesh
    z = np.array([[float(discriminator(datum)) for datum in po] for po in pos])
    ax.contour(xMesh, yMesh, z, levels = [0])
    ax.set_title('Linear Support Vector Machine')
    ax.legend()
    fig.savefig('tmp-svm-linear.pdf')





doTruth()
doLinearSVM(dataX, dataY)

if environ.get('SHOW') != None:
    plt.show()
