from os import environ
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math
import scipy.stats as stats
from genData import *


epsilon = 1e-20
xmin = -2.5
xmax = 8.5
ymin = -1
ymax = 8


data = np.array(modelsSeparable_read())
dataNotSeparable = np.array(modelsNotSeparable_read())



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
    fig.savefig('tmp-classification-separable.pdf')


# Least squares classification.
def doLeastSquares(X, labels):
    learnX = np.vstack((X.T, np.ones((1, X.shape[0]))))
    labels = labels.reshape(-1, 1)

    w = np.linalg.solve(learnX @ learnX.T, learnX @ labels)

    def discriminator(x):
        x = x.reshape(-1, 1)
        b = np.vstack((x, np.ones((1, x.shape[1]))))
        return w.T @ b

    fig, ax = plt.subplots()
    classes = separate(X, 'A (Pred.)', 'B (Pred.)', discriminator)
    plotClasses(ax, classes, True)
    plotData(ax)
    x = np.arange(xmin, xmax, 0.1)
    y = np.arange(ymin, ymax, 0.1)
    xMesh, yMesh = np.meshgrid(x, y)
    pos = np.empty(xMesh.shape + (2,))
    pos[:, :, 0] = xMesh
    pos[:, :, 1] = yMesh
    z = np.array([[float(discriminator(datum)) for datum in po] for po in pos])
    ax.contour(xMesh, yMesh, z, levels = [0])
    ax.set_title('Least Squares')
    ax.legend()
    fig.savefig('tmp-classification-ls.pdf')


# Perceptron.
def doPerceptron(X, labels, w, b, iterations):
    w = np.array(w)

    for k in range(0, iterations):
        w_prev = w
        b_prev = b

        for x, y in zip(X, labels):
            yHat = np.sign(w.T @ x + b)
            if yHat != y:
                if y == -1:
                    w = w - x
                    b = b - 1
                elif y == 1:
                    w = w + x
                    b = b + 1
                else:
                    raise Exception('Invalid label %d!' % y)

        if np.linalg.norm(w - w_prev) <= epsilon and np.linalg.norm(b - b_prev) <= epsilon:
            print('Convergence after %d iterations!' % (k + 1))
            break

    fig, ax = plt.subplots()
    classes = separate(X, 'A (Pred.)', 'B (Pred.)', lambda x: w.T @ x + b)
    plotClasses(ax, classes, True)
    plotData(ax)
    x = np.arange(xmin, xmax, 0.1)
    y = np.arange(ymin, ymax, 0.1)
    xMesh, yMesh = np.meshgrid(x, y)
    pos = np.empty(xMesh.shape + (2,))
    pos[:, :, 0] = xMesh
    pos[:, :, 1] = yMesh
    z = np.array([[w.T @ datum + b for datum in po] for po in pos])
    ax.contour(xMesh, yMesh, z, levels = [0])
    ax.set_title('Perceptron')
    ax.legend()
    fig.savefig('tmp-classification-perceptron.pdf')





doTruth()
doLeastSquares(data[:, :-1], data[:, -1])
doPerceptron(data[:, :-1], data[:, -1].T, (1, 1), 0, 10)

if environ.get('SHOW') != None:
    plt.show()
