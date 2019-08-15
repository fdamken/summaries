from os import environ
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


# Rosenbrock.
def rosenbrock(theta):
    return theta[0] ** 4 - 2 * theta[0] ** 2 * theta[1] + 0.01 * theta[0] ** 2 - 0.02 * theta[0] + theta[1] ** 2 + 0.01

def rosenbrock_gradient(theta):
    return np.array((4 * 0.02 * theta[0] - 4 * theta[0] * theta[1] + 4 * theta[0] ** 3 - 0.02,
                     2 * theta[1] - 2 * theta[0] ** 2))

def rosenbrock_hessian_inv(theta):
    return np.matrix(((0.25,           0.5 * theta[0]),
                      (0.5 * theta[0], 1.5 * (theta[0] ** 2 - 1/3 * theta[1] + 1/600)))) / (theta[0] ** 2 - theta[1] + 0.005)


# Quadratic.
def quadratic(theta):
    return theta[0] ** 2 + theta[0] * theta[1] - 15 * theta[0] + theta[1] ** 2 - 15 * theta[1] + 75

def quadratic_gradient(theta):
    return np.array((2 * theta[0] + theta[1] - 15,
                     theta[0] + 2 * theta[1] - 15))

def quadratic_hessian_inv(theta):
    return np.matrix(((2, -1),
                      (-1, 2))) / 3


# Steepest descent.
def steepestDescent(gradient, init, alpha, iterations):
    thetas = [np.array(init)]
    for i in range(0, iterations):
        theta = thetas[-1]
        thetas.append(theta - alpha * gradient(theta))
    return thetas


# Newtons method.
def newtonsMethod(gradient, hessian_inv, init, alpha, iterations):
    thetas = [np.array(init)]
    for i in range(0, iterations):
        theta = thetas[-1]
        thetas.append(theta - alpha * np.asarray(hessian_inv(theta) @ gradient(theta))[0])
    return thetas


# Quasi-Newton method.
def bfgs(gradient, init, initH, alpha, iterations):
    thetas = [np.array(init)]
    hessian = np.matrix(initH)
    I = np.identity(hessian.shape[0])
    for i in range(0, iterations):
        theta = thetas[-1]
        theta_next = theta - alpha * np.asarray(hessian @ gradient(theta))[0]
        thetas.append(theta_next)
        y = gradient(theta_next) - gradient(theta)
        s = alpha * (theta_next - theta)
        ys = np.inner(s, y)
        a = np.outer(s, y) / ys
        b = np.outer(y, s) / ys
        c = np.outer(s, s) / ys
        hessian = (I - a) @ hessian @ (I - b) + c
    return thetas


# Conjugate gradients.
def cg(gradient, init, alpha, iterations):
    thetas = [np.array(init), np.array(init)]
    delta = 0
    for i in range(0, iterations):
        theta = thetas[-1]
        theta_prev = thetas[-2]
        delta_next = gradient(theta) + (np.inner(gradient(theta), gradient(theta))
                                      / np.inner(gradient(theta_prev), gradient(theta_prev))) * delta
        thetas.append(theta - alpha * delta_next)
        delta = delta_next
    return thetas





delta = 0.1
init_rosenbrock = (-2, 2)
init_quadratic = (-9, 14)

# Steepest descent.
def doSteepestDescent():
    alpha = 0.1
    iterations = 10000

    # Rosenbrock.
    thetas = steepestDescent(rosenbrock_gradient, init_rosenbrock, alpha, iterations)
    x = np.arange(-2.5, 2.5, delta)
    y = np.arange(-2, 4, delta)
    X, Y = np.meshgrid(x, y)
    z = rosenbrock((X, Y))

    fig, ax = plt.subplots()
    c = ax.contourf(x, y, z)
    ax.plot([x[0] for x in thetas], [x[1] for x in thetas], '-o', color = 'red')
    fig.colorbar(c)
    ax.set_title('$ \\alpha = %.2f, n = %d $' % (alpha, iterations))
    fig.savefig('tmp-steepestDescent-rosenbrock.pdf')
    fig.canvas.set_window_title('Steepest Descent (Rosenbrock)')


    # Quadratic.
    thetas = steepestDescent(quadratic_gradient, init_quadratic, alpha, iterations)
    x = np.arange(-10, 15, delta)
    y = np.arange(-5, 15, delta)
    X, Y = np.meshgrid(x, y)
    z = quadratic((X, Y))

    fig, ax = plt.subplots()
    c = ax.contourf(x, y, z)
    ax.plot([x[0] for x in thetas], [x[1] for x in thetas], '-o', color = 'red')
    fig.colorbar(c)
    ax.set_title('$ \\alpha = %.2f, n = %d $' % (alpha, iterations))
    fig.savefig('tmp-steepestDescent-quadratic.pdf')
    fig.canvas.set_window_title('Steepest Descent (Quadratic)')



# Newtons method.
def doNewtonsMethod():
    alpha = 0.1
    iterations = 10000

    # Rosenbrock.
    thetas = newtonsMethod(rosenbrock_gradient, rosenbrock_hessian_inv, init_rosenbrock, alpha, iterations)
    x = np.arange(-2.5, 2.5, delta)
    y = np.arange(-2, 4, delta)
    X, Y = np.meshgrid(x, y)
    z = rosenbrock((X, Y))

    fig, ax = plt.subplots()
    c = ax.contourf(x, y, z)
    ax.plot([x[0] for x in thetas], [x[1] for x in thetas], '-o', color = 'red')
    fig.colorbar(c)
    ax.set_title('$ \\alpha = %.2f, n = %d $' % (alpha, iterations))
    fig.savefig('tmp-newtonsMethod-rosenbrock.pdf')
    fig.canvas.set_window_title('Newtons Method (Rosenbrock)')


    # Quadratic.
    alpha = 1
    iterations = 1
    thetas = newtonsMethod(quadratic_gradient, quadratic_hessian_inv, init_quadratic, alpha, iterations)
    x = np.arange(-10, 15, delta)
    y = np.arange(-5, 15, delta)
    X, Y = np.meshgrid(x, y)
    z = quadratic((X, Y))

    fig, ax = plt.subplots()
    c = ax.contourf(x, y, z)
    ax.plot([x[0] for x in thetas], [x[1] for x in thetas], '-o', color = 'red')
    fig.colorbar(c)
    ax.set_title('$ \\alpha = %.2f, n = %d $' % (alpha, iterations))
    fig.savefig('tmp-newtonsMethod-quadratic.pdf')
    fig.canvas.set_window_title('Newtons Method (Quadratic)')



# Quasi-Newton method.
def doBFGS():
    alpha = 0.25

    ## Rosenbrock.
    iterations = 100
    initH = ((1, 0), (0, 1))
    thetas = bfgs(rosenbrock_gradient, init_rosenbrock, initH, alpha, iterations)
    x = np.arange(-2.5, 2.5, delta)
    y = np.arange(-2, 4, delta)
    X, Y = np.meshgrid(x, y)
    z = rosenbrock((X, Y))

    fig, ax = plt.subplots()
    c = ax.contourf(x, y, z)
    ax.plot([x[0] for x in thetas], [x[1] for x in thetas], '-o', color = 'red')
    fig.colorbar(c)
    ax.set_title('$ \\alpha = %.2f, n = %d $' % (alpha, iterations))
    fig.savefig('tmp-bfgs-rosenbrock.pdf')
    fig.canvas.set_window_title('BFGS (Rosenbrock)')


    # Quadratic.
    iterations = 1000
    initH = ((1, 0), (1, 0))
    thetas = bfgs(quadratic_gradient, init_quadratic, initH, alpha, iterations)
    x = np.arange(-10, 15, delta)
    y = np.arange(-5, 20, delta)
    X, Y = np.meshgrid(x, y)
    z = quadratic((X, Y))

    fig, ax = plt.subplots()
    c = ax.contourf(x, y, z)
    ax.plot([x[0] for x in thetas], [x[1] for x in thetas], '-o', color = 'red')
    fig.colorbar(c)
    ax.set_title('$ \\alpha = %.2f, n = %d $' % (alpha, iterations))
    fig.savefig('tmp-bfgs-quadratic.pdf')
    fig.canvas.set_window_title('BFGS (Quadratic)')



# Conjugate gradients.
def doCG():
    alpha = 0.1
    iterations = 100

    # TODO: Not working.
    ## Rosenbrock.
    thetas = cg(rosenbrock_gradient, init_rosenbrock, alpha, iterations)
    x = np.arange(-2.5, 2.5, delta)
    y = np.arange(-2, 4, delta)
    X, Y = np.meshgrid(x, y)
    z = rosenbrock((X, Y))

    fig, ax = plt.subplots()
    c = ax.contourf(x, y, z)
    ax.plot([x[0] for x in thetas], [x[1] for x in thetas], '-o', color = 'red')
    fig.colorbar(c)
    ax.set_title('$ \\alpha = %.2f, n = %d $' % (alpha, iterations))
    fig.savefig('tmp-cg-rosenbrock.pdf')
    fig.canvas.set_window_title('CG (Rosenbrock)')


    # Quadratic.
    thetas = cg(quadratic_gradient, init_quadratic, alpha, iterations)
    x = np.arange(-10, 15, delta)
    y = np.arange(-5, 15, delta)
    X, Y = np.meshgrid(x, y)
    z = quadratic((X, Y))

    fig, ax = plt.subplots()
    c = ax.contourf(x, y, z)
    ax.plot([x[0] for x in thetas], [x[1] for x in thetas], '-o', color = 'red')
    fig.colorbar(c)
    ax.set_title('$ \\alpha = %.2f, n = %d $' % (alpha, iterations))
    fig.savefig('tmp-cg-quadratic.pdf')
    fig.canvas.set_window_title('CG (Quadratic)')





doSteepestDescent()
doNewtonsMethod()
doBFGS()
doCG()

if environ.get('SHOW') != None:
    plt.show()
