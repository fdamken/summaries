import numpy as np
import os
import scipy.stats as stats
import matplotlib.mlab as mlab
import random


def writeToFile(file, iterable):
    if os.path.exists(file):
        os.remove(file)
    with open(file, 'w+') as fd:
        for dat in iterable:
            fd.write(dat + '\n')



np.random.seed(11111997)

samples = 10000
samples2d = 1000
samplesSeparable = 250
samplesNotSeparable = 500
samplesRegression = 20

params = ((5, 10), (30, 5))
weights = (0.5, 0.5)

def models_read():
    data = []
    with open('tmp-models.txt', 'r') as fd:
        for line in fd.readlines():
            data.append(float(line))
    return np.array(data)

def models_gen():
    mixture_idx = np.random.choice(2, size = samples, replace = True, p = weights)
    data = np.fromiter((stats.norm.rvs(*(params[i])) for i in mixture_idx), np.float64)
    writeToFile('tmp-models.txt', [str(x) for x in data])

def models_plot(x, plt, plotComponents = False):
    a = stats.norm.pdf(x, params[0][0], params[0][1]) * 0.5
    b = stats.norm.pdf(x, params[1][0], params[1][1]) * 0.5
    plt.plot(x, a[:] + b[:], color = 'red', label = 'Real Mixture')
    if plotComponents:
        plt.plot(x, a, color = 'green', label = 'Real Gaussian A (Scaled)')
        plt.plot(x, b, color = 'blue', label = 'Real Gaussian B (Scaled)')



params2d_mu = ((-4, 2), (5, 6), (4, -4))
params2d_sigma = ((1, 2), (2, 1), (2, 2))
params2d_cov = (0.7, 0.5, 1)
weights2d = (0.25, 0.25, 0.5)
params2d = []
for i in range(len(weights2d)):
    params2d.append((params2d_mu[i], ((params2d_sigma[i][0], params2d_cov[i]), (params2d_cov[i], params2d_sigma[i][1]))))

def models2d_read():
    data = []
    with open('tmp-models2d.txt') as fd:
        for line in fd.readlines():
            line = line.split(' ')
            data.append((float(line[0]), float(line[1])))
    return np.array(data)

def models2d_gen():
    mixture_idx = np.random.choice(3, size = samples2d, replace = True, p = weights2d)
    data = []
    for id in mixture_idx:
        data.append(stats.multivariate_normal.rvs(*(params2d[id])))
    writeToFile('tmp-models2d.txt', [str(x) + ' ' + str(y) for x, y in data])

def models2d_plot(x, y, plt, plotSamples = False):
    X, Y = np.meshgrid(x, y)
    z1 = mlab.bivariate_normal(X, Y, params2d_sigma[0][0], params2d_sigma[0][1], params2d_mu[0][0], params2d_mu[0][1], params2d_cov[0]) * weights2d[0]
    z2 = mlab.bivariate_normal(X, Y, params2d_sigma[1][0], params2d_sigma[1][1], params2d_mu[1][0], params2d_mu[1][1], params2d_cov[1]) * weights2d[1]
    z3 = mlab.bivariate_normal(X, Y, params2d_sigma[2][0], params2d_sigma[2][1], params2d_mu[2][0], params2d_mu[2][1], params2d_cov[2]) * weights2d[2]
    zN = z1 + z2 + z3
    zMin = min(z1.min(), z2.min(), z3.min(), zN.min())
    zMax = max(z1.max(), z2.max(), z3.max(), zN.max())
    levels = np.arange(zMin, zMax, 0.002)
    plt.contour(X, Y, zN, levels = levels)
    if plotSamples:
        (x, y) = models2d_read().T
        plt.scatter(x, y, s = 2)



paramsSeparable_labels = [-1, 1]
paramsSeparable_mu = [(1, 1), (5, 6)]
paramsSeparable_cov = [((1, 0), (0, 1)), ((1, 0), (0, 1))]

def modelsSeparable_read():
    data = []
    with open('tmp-modelsSeparable.txt') as fd:
        for line in fd.readlines():
            line = line.split(' ')
            data.append((float(line[0]), float(line[1]), float(line[2])))
    return np.array(data)

def modelsSeparable_gen():
    data = []
    for label, mu, cov in zip(paramsSeparable_labels, paramsSeparable_mu, paramsSeparable_cov):
        generated = list(np.array(np.random.multivariate_normal(mu, cov, int(samplesSeparable / len(paramsSeparable_mu)))))
        appended = []
        for point in generated:
            point = list(point)
            point.append(label)
            appended.append(point)
        data += appended
    writeToFile('tmp-modelsSeparable.txt', [str(x) + ' ' + str(y) + ' ' + str(label) for x, y, label in data])



paramsNotSeparable_labels = [-1, 1]
paramsNotSeparable_mu = (3, 3)
paramsNotSeparable_mu_a = np.array(paramsNotSeparable_mu)
paramsNotSeparable_cov = ((2, 0), (0, 2))
paramsNotSeparable_circle = 1.25

def modelsNotSeparable_read():
    data = []
    with open('tmp-modelsNotSeparable.txt') as fd:
        for line in fd.readlines():
            line = line.split(' ')
            data.append((float(line[0]), float(line[1]), float(line[2])))
    return np.array(data)

def modelsNotSeparable_gen():
    samples = np.array(np.random.multivariate_normal(paramsNotSeparable_mu, paramsNotSeparable_cov, samplesNotSeparable))
    data = []
    for sample in samples:
        point = list(sample)
        distance = sample - paramsNotSeparable_mu_a
        point.append(paramsNotSeparable_labels[0 if np.linalg.norm(distance) <= paramsNotSeparable_circle ** 2 else 1])
        data.append(point)
    writeToFile('tmp-modelsNotSeparable.txt', [str(x) + ' ' + str(y) + ' ' + str(label) for x, y, label in data])



paramsRegression_xmin = -4
paramsRegression_xmax = 7
paramsRegression_noise = 1

def modelsRegression_f(x):
    return 100 * ((1 / (1 + np.exp(-x))) ** 2) * np.sin(x)

def modelsRegression_fNoisy(x):
    f = modelsRegression_f(x)
    noise = np.random.normal(scale = paramsRegression_noise, size = len(x))
    return f + noise

def modelsRegression_read():
    data = list(np.loadtxt('tmp-modelsRegression.txt'))
    random.shuffle(data)
    return np.array(data).T

def modelsRegression_gen():
    X = np.random.uniform(low = paramsRegression_xmin, high = paramsRegression_xmax, size = samplesRegression)
    Y = modelsRegression_fNoisy(X)
    writeToFile('tmp-modelsRegression.txt', [str(x) + ' ' + str(y) for x, y in zip(X, Y)])

def modelsRegression_plot(X, plt, plotSamples = False, limit = None):
    Y = modelsRegression_f(X)
    plt.plot(X, Y, label = r'$ \sigma(x) \, \sin(x) $')
    if plotSamples:
        data = modelsRegression_read()
        if limit != None:
            data = data[:, :limit]
        plt.scatter(*(data), s = 15, color = 'green', label = 'Samples')





if __name__ == '__main__':
    models_gen()
    models2d_gen()
    modelsSeparable_gen()
    modelsNotSeparable_gen()
    modelsRegression_gen()
