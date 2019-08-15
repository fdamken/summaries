# SML Summary :: Planning

## Slides

Done/Structured/To-Do: 693/823/823; 84%/100%/100%

- [x] Chapter 1: Organization (Slides: 62)
- [X] Chapter 2: Linear Algebra (Slides: 37)
- [X] Chapter 3: Statistics Refresher (Slides: 64)
- [X] Chapter 4: Optimization Refresher (Slides: 64)
- [X] Chapter 5: Bayesian Decision Theory (Slides: 36)
- [X] Chapter 6: Probability Density Estimation (Slides: 87)
- [X] Chapter 6A: Expectation Maximization (Slides: 9)
- [X] Chapter 7: Clustering and Evaluation (Slides: 38)
- [X] Chapter 8: Regression (Slides: 55)
- [X] Chapter 9: Classification (Slides: 61)
- [X] Chapter 10: Linear Dimensionality Reduction and Statistical Learning Theory (Slides: 71)
- [X] Chapter 11: Neural Networks (Slides: 109)
- [x] Chapter 12: Support Vector Machines (Slides: 59)
- [x] Chapter 13: Kernel Regression and Gaussian Processes (Slides: 71)



## Topics (Not in TeX)

* Placeholder



## Self-Test Questions

* Chapter 1: Organization
    - What are some of Machine Learning applications?
    - When can we benefit from using Machine Learning methods?
    - What are the different types of learning?
    - What is the difference between classification and regression? Can you give some examples of both tasks (and identify the domain and codomain)?
    - What are the challenges when solving a Machine Learning problem?
    - What is generalization? What is overfitting?
* Chapter 2: Linear Algebra Refresher
    - Remember vectors and what you can do with them.
    - Remember matrices and what you can do with them.
    - What is a projection? How do you use it?
    - How to compute the inverse of a matrix?
    - What are Eigenvalues and Eigenvectors?
    - What is a change of basis? What is a linear transformation? Are they the same?
* Chapter 3: Statistics Refresher
    - What is a random variable?
    - What is a distribution?
    - What is a Binomial distribution?
    - How does a Poisson distribution relate to Binomial distributions?
    - What is a Gaussian distribution?
    - What is an expectation?
    - What is a joint distribution?
    - What is a conditional distribution?
    - What is a distribution with a lot of information?
    - How to measure the difference between distributions?
* Chapter 4: Optimization Refresher
    - Why is optimization important for machine learning?
    - What do well-formulated learning problems look like?
    - What is a convex set and what is a convex function?
    - How do I find the maximum of a vector-valued function?
    - How to deal with constrained optimization problems?
    - How to solve such problems numerically?
* Chapter 5: Bayesian Decision Theory
    - How can we device on classifying a query based on simple and general loss functions?
    - What does "Bayes Optimal" mean?
    - How to deal with two or more classes?
    - How to deal with high dimensional feature vectors?
    - How to incorporate prior knowledge on the class distribution?
    - What are the equations for misclassification rate and risk?
* Chapter 6: Probability Density Estimation
    - Where do we get the probability of data from?
    - What are parametric methods and how to obtain their parameters?
    - How many parameters have non-parametric methods?
    - What are mixture models?
    - Should gradient methods be used for training mixture models?
    - How does the EM algorithm work?
    - What is the biggest problem of mixture models?
* Chapter 7: Clustering and Evaluation
    - How can we find meaningful clusters in the data?
    - How does density estimation with mixture models relate to clustering?
    - What is the bias-variance trade-off?
    - What is a BLUE estimator?
    - Are maximum likelihood estimators always unbiased?
    - What is leave on out cross-validation? What do we need it for?
* Chapter 8: Regression
    - What is regression (in general) and linear regression (in particular)?
    - What is the cost function of regression and how can I interpret it?
    - What is overfitting?
    - How can I derive a Maximum-Likelihood Estimator for Regression?
    - Why are Bayesian methods important?
    - What is MAP and how is it different to full Bayesian regression?
* Chapter 9: Classification
    - How do we get from Bayesian optimal decisions to discriminant functions?
    - How to derive a discriminant function from a probability distribution?
    - How to deal with more than two classes?
    - What does "linearly separable" mean?
    - What is Fisher discriminant analysis? How does it relate to regression?
    - Is Fisher's linear discriminant Bayes optimal?
    - What are perceptrons? How can we train them?
    - What is logistic regression? How can be derive the parameter update rule?
* Chapter 10: Linear Dimensionality Reduction and Statistical Learning Theory
    - What does dimensionality reduction mean?
    - What is PCA? What are the three things that it does?
    - What are the roles of Eigenvectors and Eigenvalues in PCA?
    - Can you describe applications of PCA?
    - What does risk in statistical learning theory mean?
    - How is the true risk different from the empirical risk?
    - What is the learning power of a function approximator?
    - What is expressed by a VC-Dimension?
    - Is the VC-Dimension always correlated with the number of parameters?
* Chapter 11: Neural Networks
    - How does logistic regression relate to neural networks?
    - How do neural networks relate to the brain?
    - What kind of functions can single layer neural networks learn?
    - Why do two layers help? How many layers do you need to represent arbitrary functions?
    - Why were neural networks abandoned in the 1970s, and later in the 1990s? Why did neural networks re-awaken in the 2010s?
    - What output layer and loss function to use given the task (regression, classification)?
    - Why use a ReLU activation instead of a sigmoid?
    - Derive the equations for forward and backwardpropagation for a simple network.
    - What is mini-batch gradient descent? Wha use it instead of SGD or full gradient descent?
    - Why neural networks can overfit and what are the options to prevent it?
* Chapter 12: Support Vector Machines
    - How did learning theory motivate support vector machines?
    - What does maximum margin separation mean?
    - Why did the SVM-craze drown the Neural-Networks-craze?
    - What is a Kernel?
    - How can I build Kernels from Kernels?
    - What functions does the Radial Basis Function Kernel contain?
    - How does support vector regression work?
* Chapter 13: Kernel Regression and Gaussian Processes
    - Why kernel methods for regression?
    - How do you get from radial basis functions to kernels?
    - What is the role of the two pseudo-inverses in kernel regression?
    - Why are kernel regression methods very computationally expensive?
    - Why is kernel regression the dual to linear regression?
    - What is the major advantage of GPs over Kernel Ridge Regression?
    - Why are GPs a Bayesian approach?
    - What principle allowed deriving GPs from a Bayesian regression point of view?
    - How to get the hyperparameters in a Bayesian setup?
