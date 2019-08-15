from os import environ
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import scipy.stats as stats
from genData import *


alphabet = ('A', 'B', 'C', 'D', 'E', 'F')


xmin = -35
xmax = 55
x = np.arange(xmin, xmax, 0.1)


data = models_read()



# MoG.
def doMoG():
    fig, ax = plt.subplots()
    models_plot(x, ax, True)
    ax.legend()
    fig.savefig('tmp-mixtureModels-mog.pdf')



# EM.
def doEM(mu, sigma, prior, iterations):
    fig, ax = plt.subplots()
    models_plot(x, ax)

    dataExpanded = np.repeat(data.reshape(-1, 1), len(mu), axis = 1).T
    for i in range(iterations):
        # E-Step.
        tops = []
        for j, mui in enumerate(mu):
            sigmai = sigma[j]
            priori = prior[j]
            likelihood = stats.norm(mui, sigmai).pdf(data)
            tops.append(priori * likelihood)
        tops = np.array(tops)
        bottoms = sum(tops)
        np.set_printoptions(threshold=np.inf)
        alpha = np.divide(tops, np.repeat(bottoms.reshape(-1, 1), len(mu), axis = 1).T)

        # M-Step.
        Nj = sum(alpha.T)
        mu = sum(np.multiply(alpha.T, dataExpanded.T)) / Nj
        tmp = dataExpanded - np.repeat(mu.reshape(-1, 1), len(data), axis = 1)
        sigma = np.sqrt(sum(np.multiply(alpha.T, np.power(tmp, 2).T)) / Nj)
        prior = Nj / len(data)

        if i == 0 or i == iterations - 1:
            y = [stats.norm.pdf(x, muj, sigma[j]) * prior[j] for j, muj in enumerate(mu)]
            for j, yj in enumerate(y):
                ax.plot(x, yj, label = ('Est. Gaussian ' + alphabet[j] + ' (iter. ' + str(i + 1) + ')'))
    ax.set_title('$ n = %d $' % (iterations))
    ax.legend()
    fig.savefig('tmp-mixtureModels-em-gaussian.pdf')





doMoG()
doEM((1, 2), (1, 2), (0.25, 0.75), 50)

if environ.get('SHOW') != None:
    plt.show()
