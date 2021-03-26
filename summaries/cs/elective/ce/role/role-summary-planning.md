# RoLe Summary Planung

## Slides

Done/Structured/Total: 668/1160/1160; 58%/100%/100%

* [x] Chapter  1 : Introduction (47); Core
* [X] Chapter  2 : Robotics in a Nutshell (112); Core
* [X] Chapter  3a: Optimal Control; Discrete State-Action (43); Core
* [X] Chapter  3b: Optimal Control; Continuous State-Action (60); Core
* [x] Chapter  4a: Approximate Optimal Control; Differential Dynamic Programming (31); Wider
* [x] Chapter  4b: Approximate Optimal Control; Approximate Dynamic Programming (29); Wider
* [–] Chapter  5a: Machine Learning; Probabilistic Graphical Models (67); Advanced (**Dropped**)
* [x] Chapter  5b: Machine Learning; Foundations (140); Core
* [x] Chapter  5c: Machine Learning; Neural Networks (96); Wider
* [x] Chapter  6 : State Estimation (64); Advanced
* [X] Chapter  7 : Model Learning (66); Wider
* [X] Chapter  8 : Policy Models, Movement Primitives (65); Core
* [X] Chapter  9 : Model-Based Reinforcement Learning (59); Wider
* [X] Chapter 10 : Policy Gradient Methods (59); Core
* [X] Chapter 11 : Value Function Methods (42); Core
* [X] Chapter 12 : Probabilistic Policy Search (66); Core
* [X] Chapter 13 : Imitation Learning, Behavioral Cloning and Inverse RL (96); Core
* [x] Chapter 14 : Bayesian Reinforcement Learning (54); Advanced
* [x] Chapter 15 : Outlook (31); Core


## Structure

* Introduction {1.1, 1.2, 1.7}
    - History {1.8, 1.9, 1.10, 1.11, 1.12, 1.13, 1.14, 1.15, 1.16, 1.17, 1.18, 1.19, 1.20}
        + Deep Learning {1.21, 1.22, 1.23}
        + How Long Does Learning Take? {1.24, 1.25}
        + Inductive Biases {1.26, 1.27, 1.28}
* Statistics, Linear Algebra and Calculus Refresher {5b.4}
    - Basics {5b.5, 5b.6, 5b.7, 5b.8}
        + Entropy {5b.9}
        + Gaussian Distribution and Properties {5b.17, 5b.18, 5b.19}
    - Kullback-Leibler Divergence {10.36, 10.37, 10.38}
        + Fisher Information Matrix {10.39, 10.40}
    - Monte-Carlo Integration and Gradient Estimation {5b.10}
        + Gradient Estimation {5b.11, 5b.12, 5b.13}
    - Linear Algebra and Calculus {5b.15}
        + Moore-Penrose Pseudo-Inverse {5b.16}
* Robotics {2.1, 2.2, 2.5}
    - Modeling Robots {2.6, 2.7, 2.10, 2.11, 2.12, 2.13}
        + Kinematics {2.15, 2.16, 2.17}
            * Rotations and Euler Angles {2.18, 2.19, 2.20, 2.21, 2.22}
            * Homogeneous Transformations {2.23, 2.24, 2.25}
            * Denavit-Hartenberg Convention {2.26, 2.27}
        + Inverse Kinematics {2.90, 2.92, 2.94, 2.95}
        + Differential Forward Kinematics (Velocities) {2.28, 2.30, 2.31, 2.33}
            * Singularities {2.32}
        + Differential Inverse Kinematics {2.96, 2.97}
        + Dynamics {2.35, 2.36, 2.37, 2.38}
            * Computing the Forces {2.39}
                - Newton-Euler Method {2.40}
                - Lagrangian Methods {2.41, 2.42, 2.43}
                - Comparison of Newton-Euler and Lagrangian {2.44}
            * General Forms {2.45, 2.47, 2.48, 2.49}
    - Representing Trajectories {2.50, 2.51, 2.52, 2.53}
        + Splines {N/A}
            * Cubic Splines {2.54, 2.55, 2.56}
            * Quintic Splines {2.57, 2.58}
        + Alternatives {2.59}
    - Control in Joint Space {2.60, 2.62, 2.63, 2.64}
        + Linear Feedback Control {2.65, 2.66, 2.67, 2.68, 2.69, 2.70}
            * P-Controller {2.71}
            * PD-Controller {2.74, 2.80}
                - With Gravity Compensation {2.76, 2.77}
            * PID-Controller {2.79}
        + Model-Based Control {2.81, 2.82, 2.83}
        + Feedforward Control {2.84, 2.85, 2.86}
    - Control in Task Space {2.87, 2.88, 2.89}
        + Differential Inverse Kinematics {2.97}
        + Jacobian Transpose {2.98, 2.99}
        + Jacobian Pseudo-Inverse {2.100, 2.101}
        + Task-Prioritization with Null-Space Movements {2.102}
        + More Advanced Solutions {2.103}
        + Singularities and Damped Pseudo-Inverse {2.104, 2.105}
    - Wrap-Up {2.107}
* Machine Learning Foundations {5b.1, 5b.2, 5b.21, 5b.22, 5b.23, 5b.24, 5b.25, 5b.26}
    - The Six Machine Learning Choices {5b.27, 5b.28, 5b.62}
        + Problem Class {5b.30, 5b.31, 5b.32, 5b.33, 5b.34, 5b.35}
        + Problem Assumptions {5b.36}
        + Evaluation {5b.37, 5b.38, 5b.39, 5b.40, 5b.41}
        + Model Type {5b.42}
        + Model Class Selection {5b.43, 5b.44, 5b.45}
        + Algorithm Realization {5b.46}
        + Example {5b.47, 5b.48, 5b.49, 5b.50, 5b.51, 5b.52, 5b.53, 5b.54, 5b.55, 5b.56, 5b.57, 5b.58, 5b.59, 5b.60, 5b.61}
    - Evaluation {5b.63, 5b.65}
        + Occams Razor {5b.66}
        + Bias and Variance {5b.67, 5b.68, 5b.69}
        + Model Selection {5b.70, 5b.71, 5b.72, 5b.73}
    - Frequentis vs. Bayesian Assumptions {5b.74, 5b.75}
        + Maximum Likelihood Estimation {5b.76, 5b.77, 5b.78, 5b.79}
        + Bayesian Thinking and Maximum A-Posteriori {5b.80, 5b.81, 5b.82}
            * Ridge Regression (Tikhonov Regularized Regression) {5b.83, 5b.84}
            * Predictions {5b.85, 5b.86, 5b.87}
        + Bayesian Regression {5b.88, 5b.89, 5b.90, 5b.91, 5b.92}
    - Hand-Crafted Feature Construction {5b.93, 5b.94}
        + Discrete Inputs {5b.95, 5b.96}
        + Continuous Inputs {5b.97}
            * One-Hot {5b.98}
            * Radial Basis Functions (RBFs) {5b.99, 5b.100, 5b.101}
    - Automatic (Linear) Feature Construction {5b.102, 5b.103, 5b.104, 5b.105, 5b.106, 5b.107}
        + Respective Field Weighted Regression (RFWR) {5b.108, 5b.109, 5b.110}
        + Automatic Adaption of RFWR {5b.111, 5b.112, 5b.113}
    - Non-Parametric Approaches {5b.114, 5b.115, 5b.116, 5b.117}
        + Weighted Linear Regression {5b.118, 5b.119, 5b.120, 5b.121, 5b.122}
        + Locally Weighted Bayesian Linear Regression {5b.123}
        + Kernel Methods {5b.124, 5b.125, 5b.128}
            * Kernel Ridge Regression {5b.126, 5b.127}
        + Bayesian Kernel Regression: Gaussian Processes (GPs) {5b.129, 5b.130, 5b.131, 5b.136}
            * GP-Posterior {5b.132, 5b.133, 5b.134, 5b.135}
    - Neural Networks {5c.1, 5c.2, 5c.4, 5c.5, 5c.6, 5c.7, 5c.7, 5c.8, 5c.9}
        + Biology and Neuron Abstraction {5c.10, 5c.11, 5c.12, 5c.13}
        + Components of a Neural Network {N/A}
            * Single- and Multi-Layer Networks {5c.14, 5c.15, 5c.16, 5c.17, 5c.18, 5c.19}
            * Topologies {5c.20, 5c.21}
            * Activation Functions {5c.22, 5c.23, 5c.24, 5c.25}
            * Output Neurons {5c.26}
            * Loss Functions {5c.27}
        + Forward- and Backpropagation {5c.28, 5c.29, 5c.30}
            * Forwardpropagation {5c.31, 5c.32}
            * Backpropagation {5c.33, 5c.34, 5c.35, 5c.37}
                - Skip Connections {5c.36}
            * Finite Differences {5c.38, 5c.39}
            * Automatic Differentiation {5c.40}
        + Efficient Gradient Descent {5c.42, 5c.43, 5c.44, 5c.47}
            * Stochastic Gradient Descent {5c.45, 11.19, 11.20}
            * Mini-Batch Gradient Descent {5c.46}
        + Choosing the Learning Rate {5c.48, 5c.49, 5c.50, 5c.51}
            * Plateaus and Valleys {5c.52}
            * Adaptive Learning Rates {N/A}
                - Momentum {5c.53}
                - Adadelta {5c.54}
                - Adam {5c.55}
        + Choosing the Descent Direction {N/A}
            * Hessian Approaches {5c.56}
            * Conjugate Gradient {5c.57}
            * Levenberg-Marquardt {5c.58}
        + Initialization of the Parameters {5c.59, 5c.60}
        + Overfitting {5c.61, 5c.62, 5c.63, 5c.64, 5c.65, 5c.66}
            * Weight Decay {5c.67}
            * Early Stopping {5c.68}
            * Input Noise Augmentation {6.69}
            * Dtopout {5c.70}
            * Batch Normalization {5c.71}
        + Theoretical Analysis {5c.72, 5c.73, 5c.75, 5c.76, 5c.77}
            * Universal Function Approximation Theorem {5c.74}
        + Network Architectures {5c.78, 5c.79, 5c.80}
            * Convolutional Neural Networks (CNNs) {5c.81, 5c.82, 5c.83, 5c.84, 5c.85, 5c.86}
            * Recurrent Neural Networks (RNNs) {5c.78}
        + Neural Networks in Robotics {5c.88, 5c.89}
            * Value Functions {5c.90, 5c.91}
            * Policies {5c.92, 5c.93}
    - Wrap-Up {5b.138, 5c.95}
* Optimal Control {N/A}
    - Discrete State-Action Space {3a.1, 3a.2}
        + Foundations {N/A}
            * Dynamic Programing and Principle of Optimality {3a.6, 3a.7}
            * Markov Decision Process and Policies {3a.9, 3a.10}
        + Finite-Horizon Optimal Control {3a.12, 3a.13}
            * Value and State-Action Value Functions {3a.14, 3a.15, 3a.17}
            * Value Iteration {3a.18, 3a.19}
            * Consequences of a Finite Time Horizon {3a.21}
        + Infinite-Horizon Optimal Control {3a.22, 3a.23, 3a.24, 3a.25}
            * Value and State-Action Value Functions {3a.30, 3a.31, 3a.32, 3a.33}
            * Value Iteration {3a.26}
            * Policy Iteration {3a.29, 3a.34, 3a.36, 3a.37}
    - Continuous State-Action Space {3b.1, 3b.2}
        + Modeling the System {3b.5, 3b.7, 3b.8, 3b.9, 3b.10, 3b.11}
        + Linear Quadratic Regulator (LQR) {3b.12, 3b.13, 3b.14, 3b.15}
            * Recap of Value Iteration {3b.17, 3b.18}
            * Solving the Optimal Control Problem {3b.19, 3b.20, 3b.21, 3b.22, 3b.23, 3b.24, 3b.25, 3b.26, 2.27}
                - Computing the Expectation {3b.21}
                - Computing the Maximization {3b.23}
        + Approximating Nonlinear Systems {3b.32, 3b.33, 3b.34, 3b.35, 3b.36}
            * Local Solutions by Linearization {3b.37, 3b.38, 3b.39}
        + Optimal Control with Learned Models {3b.42, 3b.43, 3b.44, 3b.45, 3b.46, 3b.48, 3b.51}
            * State-Of-The-Art Approaches {3b.52, 3b.55}
    - Wrap-Up {3a.39, 3a.40, 3a.41, 3a.42, 3b.59}
* Approximate Optimal Control {N/A}
    - Differential Dynamic Programming (DDP) {4a.1, 4a.2, 4a.3, 4a.12}
        + Locally Nonlinear LQR {4a.13, 4a.14}
        + Differential Dynamic Programming {4a.15, 4a.16, 4a.17}
            * Implementation Details {4a.18, 4a.19, 4a.20}
        + Iterative LQR {4a.22, 4a.23, 4a.24}
        + Stochastic DDP {4a.25, 4a.26}
        + Guided Policy Search {4a.27, 4a.28}
    - Approximate Dynamic Programming {4b.1, 4b.2, 4b.6}
        + Function Approximation {4b.7, 4b.8, 4b.9, 4b.10, 4b.11, 4b.12}
        + Approximate Value Iteration {4b.13, 4b.14}
            * Theoretical Analysis and Bellman Operator {4b.15, 4b.16, 4b.17}
            * Approximation Error and Performance Loss {4b.18, 4b.19, 4b.20}
        + Approximate Policy Iteration {4b.21, 4b.23, 4b.24, 4b.25}
            * Approximation Error and Performance Loss {4b.26}
    - Wrap-Up {4a.30, 4b.28}
* State Estimation {6.1, 6.2, 6.5, 6.6}
    - Kalman Filter as an Optimal Filter {6.8}
        + Observers {6.9, 6.10}
        + Optimal Observers {6.11, 6.12, 6.13, 6.14, 6.15, 6.16, 6.17, 6.18}
        + Geometric Perspective {6.19}
    - Kalman Filter as Bayesian Inference {6.20, 6.21, 6.22, 6.23, 6.24}
    - Partially Observed Optimal Control {6.27, 6.28, 6.29, 6.30}
    - Extended, Unscented and Particle Filter {6.32, 6.33}
        + Extended Kalman Filter (EKF) {6.34}
        + Cubature Kalman Filter (CKF) {6.35, 6.36, 6.37, 6.38}
        + Unscented Kalman Filter (UKF) {6.39}
        + Particle Filter / Sequential Monte Carlo (PF/SMC) {6.40, 6.41, 6.56}
            * Importance Sampling {6.42, 6.43}
            * Sequential Importance Sampling {6.48, 6.49, 6.50, 6.51, 6.52}
            * Sequential Importance Resampling {6.53, 6.54, 6.55}
        + Examples {N/A}
            * Approximate Message Passing {6.44, 6.45, 6.46, 6.47}
            * Pendulum {6.57, 6.58, 6.59, 6.60}
    - Wrap-Up {6.62, 6.63}
* Model Learning {7.1, 7.2}
    - Models in Robotics {7.4, 7.5, 7.6, 7.7, 7.8, 7.9}
    - Modling Assumptions: White, Black and Gray {7.10, 7.11}
        + White-Box Strategy {7.12}
        + Black-Box Strategy {7.13}
        + Gray-Box Strategy {7.14}
    - System Identification and Signal Processing {7.15, 7.16, 7.17}
        + Impulse Response {7.18, 7.19, 7.20, 7.21, 7.22, 7.23}
        + Step Response {7.24, 7.25}
        + Characterization of Dynamical Systems {7.26, 7.27}
        + Frequency Analysis {7.28, 7.29}
        + Ornstein-Uhlenbeck Process {7.30, 7.31}
        + Active Learning {7.32, 7.33, 7.34}
    - Learning Models {7.36, 7.37}
        + Linear Gaussian Dynamical Systems (LGDS) {7.38, 7.39, 7.40, 7.41, 7.42, 7.43, 7.44}
    - Case Studies {7.47}
        + Combining Rigid Body Dynamics and GPs {7.48, 7.49, 7.50}
        + Deep Lagrangian Networks {7.51, 7.52, 7.53, 7.54, 7.55}
        + The Differentiable Recusive Newton-Euler Algorithm {7.56, 7.57, 7.58, 5.59, 7.60, 7.61, 7.62, 7.63}
    - Wrap-Up {7.65}
* Policy Representations {8.1, 8.4}
    - Parametric Policies {8.3, 8.7, 8.8, 8.9}
    - Off-The-Shelf Policies {8.10, 8.16}
        + Linear Basis Functions {8.11, 8.12, 8.13}
        + Radial Basis Functions (RBFs) {8.14, 8.15}
    - Movement Primitives {8.17, 8.18, 8.20, 8.21, 8.22, 8.23, 8.24, 8.25}
        + Dynamic Movement Primitives (DMDs) {8.26, 8.27, 8.28}
            * Temporal Scaling {8.29, 8.30, 8.34}
            * Representation of the Forcing Function [8.31, 8.32]
            * Multiple Degrees of Freedom {8.33}
            * Imitation Learning {8.35}
        + Probabilistic Movement Primitives (ProMPs) {8.40, 8.41, 8.42, 8.43, 8.44, 8.45}
            * Conditioning {8.46}
            * Combination {8.47}
        + Time-Independent Stable Movement Primitives {8.51}
            * Nonlinear Stable Dynamical Systems {8.52, 8.53, 8.54}
        + Imitation Flows {8.55, 8.56, 8.57}
        + Libraries of Primitives {8.59, 8.60, 8.61}
    - Wrap-Up {8.64}
* Model-Based Reinforcement Learning {9.1, 9.2, 9.5, 9.6}
    - Differentiation of Model-Based and Model-Free {9.7, 9.8}
        + Sample Efficiency {9.9, 9.10, 9.11}
    - Domain Knowledge in Reinforcement Learning {9.13, 9.14}
        + Performance Bias {9.15, 9.16, 9.17, 9.22, 9.25}
        + Local Optima and Sample-Based Methods {9.18, 9.21}
            * The Cross-Entropy Method (CEM) {9.19}
            * (Model Predictive) Path Integral Control (MPPI) {9.20}
        + Numerical Sensitivity {9.23}
            * Backprop-Through-Time {9.24}
        + Catastrophic Model Errors {9.26}
    - Optimism and Pessimism in Reinforcement Learning {9.27, 9.28, 9.29}
        + Aleatoric and Epistemic Uncertainty {9.30, 9.31}
        + Optimism Under Uncertainty {9.31, 9.32, 9.33, 9.34, 9.35, 9.39}
            * Neural Linear Models {9.36}
            * Variational Inference {9.37}
            * Ensembles {9.38}
    - Replanning {9.40, 9.41, 9.42}
    - Case Studies {9.43}
        + Probabilistic Learning for Control (PILCO) {9.44, 9.45, 9.46}
        + Guided Policy Search (GPS) {9.48, 9.49, 9.50, 9.51, 9.52}
        + Model Predictive Control (MPC) {9.54, 9.56}
    - Wrap-Up {9.58, 12.63}
* Value Function Methods {11.1, 11.2}
    - Recap of Dynamic Programming {11.4, 11.5, 11.6, 11.7}
    - Temporal Differences {11.8, 11.9, 11.10}
        + Policy Evaluation {11.11, 11.12, 11.13}
        + Policy Improvement {11.14, 11.15}
    - Value Function Approximation {11.16, 11.17, 11.18, 11.21, 11.22, 11.23}
    - Batch Reinforcement Learning Methods {11.25, 11.26}
        + Least-Squares Temporal Differences (LSTD) {11.27, 11.28, 11.29, 11.30}
        + Fitted Q-Iteration {11.31, 11.32, 11.33}
    - Case Study: Robot Soccer {11.34, 11.35, 11.36, 11.37, 11.38, 11.39}
    - Wrap-Up {11.41, 12.64}
* Policy Search {N/A}
    - Categorization of Policy Search {10.6, 10.7, 10.8}
        + Episode- vs. Step-Based Evaluation {10.9, 10.10, 10.11}
        + Epsiode-Based Policy Search {10.12, 10.13, 10.14}
        + Exploration vs. Exploitation {10.15, 10.16, 10.17, 10.18, 10.19}
    - Policy Gradient Methods {10.1, 10.2, 10.5}
        + Policy Gradients {10.20, 10.21}
            * Gradient Computation {N/A}
                - Finite Differences {10.22}
                - Likelihood Policy Gradients {10.23}
                - Baselines {10.24}
            * Step-Based Policy Gradient Methods {10.25, 10.26}
                - Likelihood Ratio Gradient {10.27, 10.28}
                - Using the Rewards to Come {10.29}
            * Choosing the Step Size, Metrics in Standard Gradients {10.30, 10.31, 10.32, 10.33}
        + Relative Entropy and Natural Gradient {10.34, 10.35, 10.41, 10.42, 10.43}
            * Computing the Natural Gradient {N/A}
                - Episode-Based {10.44}
                - Step-Based {10.45}
            * Compatible Function Approximation {10.46, 10.47, 10.48}
                - Connection to Value Function Approximation {10.49, 10.50, 10.51}
                - Episodic Natural Actor-Critic {10.52, 10.53, 10.54}
    - Probabilistic Policy Search {12.1, 12.2}
        + Success Matching Principle {12.5, 12.6, 12.7}
        + Weighted Maximum Likelihood {12.8, 12.9, 12.10, 12.11}
            * Difference to Policy Gradients {12.12}
            * Computing the Weights {12.13}
                - Notes on Expectation Maximization {12.14}
                - Notes on the Exponential Transformation {12.15}
            * Illustration and Results {12.16, 12.17, 12.19, 12.21}
        + Relative Entropy Policy Search (REPS) {12.22, 12.23}
            * Optimization Problem {12.24}
                - Solving {12.25, 12.26}
        + REPS for Contextual Policy Search {12.28, 12.29, 12.30}
            * Optimization Problem {12.31}
                - Solving {12.32, 12.33, 12.34, 12.35}
            * Contextual Policies with Weighted ML {12.36}
        + Learning Versatile Solutions {12.40, 12.41, 12.47}
            * Illustration {12.42, 12.43}
            * Hierarchy {12.44}
                - Naive Hierarichal Approach {12.45, 12.46}
                - Hierarichal REPS (HiREPS) {12.48, 12.49}
        + Sequencing Movement Primitives {12.54, 12.55, 12.56}
            * Sequential REPS {12.57, 12.65, 12.66}
    - Wrap-Up {10.55, 10.56, 10.58, 12.60}
* Imitation Learning: Behavioral Cloning and Inverse RL {13.1, 13.3, 13.4, 13.5, 13.8, 13.9, 13.10, 13.11, 13.12}
    - Distribution Matching {13.13}
        + Behavioral Cloning {13.14, 13.43}
            * Direct Behavioral Cloning {13.15, 13.16, 13.17, 13.18, 13.19, 13.20}
            * DAGGER: New Samples to Learn to Recover {13.21}
            * DART: Robustness in Imitation Learning {13.22}
        + Generative Adversarial Learning {13.23, 13.24, 13.25}
    - Inverse Reinforcement Learning {13.26, 13.27, 13.42, 13.44}
        + Basic Principle {13.46, 13.49, 13.55}
            * Feature-Based Reward Function {13.47, 13.48}
            * Constraint Generation {13.50, 13.51, 13.58}
            * Ill-Posed Problem {13.52, 13.54}
            * (Structured) Max. Margin Solution {13.53, 13.56}
            * Expert Suboptimality {13.57, 13.60}
        + Feature Matching by Max. Entropy {13.61}
            * Max. Entropy Approach to Inference {13.62}
            * Max. Entropy Approach to Inverse RL {13.63}
            * Maximum-Casual-Entropy Inverse RL {13.64, 13.65}
        + Reward-Parameterized Policies {13.66, 13.67}
    - Case Studies {13.68, 13.69}
        + Highway Driving {13.70}
        + Max. Margin {13.71, 13.72}
        + Parking Lot Navigation {13.73, 13.74, 13.75, 13.76, 13.77}
        + Human Path Planning {13.78, 13.79, 13.80, 13.81, 13.82, 13.83}
        + Goal Inference {13.84, 13.85}
        + Quadruped {13.86, 13.87, 13.88}
        + Extreme Helicopter Flight {13.89, 13.90, 13.91, 13.92}
    - Wrap-Up {13.45, 13.94}
* Bayesian Reinforcement Learning {14.1, 14.2, 14.15, 15.16, 14.17, 14.18}
    - Recap of Bayesian Methods {14.4, 14.5, 14.6, 14.7, 14.8, 14.9, 14.14}
        + Conjugate Prior {14.10, 14.11, 14.12, 14.13}
    - Bandits and Thompson Sampling {14.19, 14.20, 14.21}
        + Restaurant Selection {14.22, 14.23, 14.24, 14.25, 14.26, 14.27, 14.28, 14.29}
    - Model-Based Bayesian RL for Discrete MDPs {14.30, 14.31, 14.32, 14.33}
        + Belief {14.34, 14.35}
        + State Transition Model {14.36, 14.37}
        + Optimal Value Function for BAMPDs {14.38, 14.39}
        + Solving for the Optimal Value Function {14.40}
    - Continuous MDPs and Dual Control {14.41, 14.42, 14.43, 14.44}
        + One-Dimensional Linear Gaussian Dual Control {14.45, 14.46, 14.47, 14.48, 14.49, 14.50}
        + Practical Dual Control {14.51}
    - Wrap-Up {14.53}
* Outlook {15.1}
    - Recap {15.4, 15.5, 15.6, 15.7, 15.8, 15.9, 15.10, 15.11}
    - Open Research Question {15.13}
* Self-Test Questions {N/A}
    - Introduction {KI-Campus}
    - Robotics {2.108, KI-Campus}
    - Machine Learning Foundations {5b.139, 5c.96}
    - Optimal Control {3a.43, 3b.60}
    - Approximate Optimal Control {4a.31, 4b.29}
    - State Estimation {6.64}
    - Model Learning {7.66}
    - Policy Representations {8.65}
    - Model-Based Reinforcement Learning {9.59}
    - Value Function Methods {11.42}
    - Policy Search {10.59, 12.61}
    - Imitation Learning {N/A}
    - Bayesian Reinforcement Learning {14.54}
