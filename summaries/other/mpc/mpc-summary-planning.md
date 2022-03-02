# MPC Summary Planning

## Slides

Done/Structured/Total: 0/369/369+?; 0%/?%/100%

* [x] Chapter  1: Introduction (24)
* [x] Chapter  2: System Theory Basics (37)
* [x] Chapter  3: Linear Quadratic Regulator (36)
* [x] Chapter  4: Constrained Optimization (28)
* [x] Chapter  5: Nominal MPC, Part 1 (38)
* [x] Chapter  6: Nominal MPC, Part 2 (33)
* [x] Chapter  7: Robust MPC (33)
* [x] Chapter  8: Stochastic MPC (23)
* [x] Chapter  9: Machine Learning in MPC (20)
* [x] Chapter 10: Gaussian Processes (52)
* [x] Chapter 11: Artificial Neural Networks (25)
* [x] Chapter 12: Summary (20)
* [ ] Chapter 13: Outlook (???)



## Structure

* Introduction {1.1, 1.3, 1.4, 1.5, 1.11, 1.20, 1.23, 12.2, 12.3}
    - What is Model Predictive Control? {1.6, 1.7, 1.8, 1.9, 1.10}
    - What is Machine Learning? {1.7, 1.18, 1.19}
    - Examples {1.12, 1.13, 1.14, 1.15, 1.16}
* Preliminaries {N/A}
    - System Theory {2.1, 2.3, 2.36}
        + Types of Dynamical Systems {2.4, 2.15}
            * Time-Continous {2.5, 2.6, 2.8, 2.9}
                - Linearization {2.7}
            * Time-Discrete {2.12, 2.13, 2.14}
                - Discretization {2.10, 2.11}
        + Stability {2.16, 2.17, 2.29, 12.4}
            * State-Feedback Controllers {2.18}
            * Lyapunov Stability {2.19}
            * Asymptotic Stability {2.20}
            * Lyapunov Functions {2.21, 2.22, 2.23, 2.24, 2.25, 2.26, 2.27, 2.28, 12.5}
        + Detectability, Observability, Controllability, and Stabilizability {2.30, 2.31, 2.32, 3.3, 3.4}
        + Outlook {2.33, 2.34, 2.35}
    - Linear Quadratic Regulator {3.1, 3.2, 3.5, 3.6, 3.7, 3.8, 3.10, 3.11, 3.13, 3.35, 12.6, 12.7}
        + Cost Functions {3.14, 3.15, 3.16, 3.17}
        + LQR Formulation {3.18, 3.19, 3.20}
        + Batch Optimization {3.21, 3.22, 3.23, 3.24}
        + Dynamic Programming {3.25}
            * Optimal Cost-to-Go {3.26}
            * Recursive Solution {3.27, 3.28, 3.29}
            * Infinite Horizon {3.30, 3.31}
        + Stability {3.32, 3.33, 12.8}
        + Outlook {3.36}
    - Constrained Optimization {4.1, 4.2, 4.3, 4.4, 4.28, 12.9}
        + Nomenclature {4.5, 4.6, 4.7, 4.8}
        + Global and Local Optimality {4.9}
        + Convexity {N/A}
            * Convex Sets {4.10, 4.11, 4.12, 4.13}
            * Convex Functions {4.14, 4.15}
            * (Sub-) Level Sets {4.16}
            * Convex Optimization Problems and Optimality {4.18, 4.19}
        + Quadratic Programming {4.20, 4.21}
        + Optimality Conditions for Constraints Optimization Problems {4.22}
            * Lagrangian {4.23, 4.24}
            * Generalized Lagrangian and KKT-Conditions {4.25, 4.26}
        + Numerical Solver {6.23, 6.24, 6.25, 6.30}
            * Penalty Functions {6.26, 6.27, 6.28, 6.29}
            * Soft Constraints {6.31, 6.32}
* Nominal Model Predictive Control {5.1, 5.2, 5.3, 5.4, 5.5, 5.38, 12.10}
    - Receding Horizon {5.6, 5.7, 5.8, 5.9, 5.10, 5.11}
    - Nominal MPC {5.12, 5.13}
    - Linear MPC {5.14, 5.15}
    - Recursive Feasibility and Stability {5.16, 5.17, 5.18, 5.19, 5.20, 5.21, 12.11}
        + \dots using a Terminal Equality {5.22}
            * Achieving Recursive Feasibility {5.23, 5.24}
            * Achieving Stability {5.25, 5.26, 5.27}
        + \dots using a Terminal Set {5.28, 5.29}
            * Invariant Sets {5.30, 5.31}
            * Stability of MPC {5.32, 5.37, 6.10}
            * Showing Recursive Feasibility {5.33, 5.34}
            * Showing Stability {5.35, 5.36, 6.8, 6.9}
    - Solving MPC Problem {6.11, 6.12, 6.33, 12.12}
        + Reformulation Linear MPC as a QP {6.13, 6.22}
            * \dots with Substitution {6.14, 6.15, 6.16, 6.17}
            * \dots without Substitution {6.18, 6.19, 6.20, 6.21}
* Robust Model Predictive Control {7.1, 7.3, 7.20, 7.32, 12.13, 12.14}
    - Inherent Robustness of Nominal MPC {7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 7.10, 7.11}
    - Uncertain Models {7.12, 7.13, 7.14}
        + System Evolution {7.15, 7.16}
    - Cost Functions for Uncertain Systems {7.17, 7.18}
    - Minimax MPC {7.19}
    - Set Subtraction and Addition {7.21, 7.22, 7.23}
    - Robust Open-Loop MPC {7.24, 7.25, 7.26}
    - Tube MPC {7.27, 7.28, 7.29, 7.30, 7.31}
* Stochastic Model Predictive Control {8.1, 8.8, 8.13, 8.22, 12.13, 12.15}
    - Stochastic Uncertainty {8.9, 8.10, 8.11}
    - Uncertain System Evolution {8.12}
    - Chance Constraints {8.14, 8.15, 8.16, 8.17}
    - Stochastic Tube MPC {8.18, 8.19}
    - Outlook {8.20, 8.21}
* Machine Learning in Model Predictive Control {9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9, 9.10, 9.12, 12.16, 12.17}
    - Machine Learning for MPC {9.11, 9.13, 10.8}
        + Modeling Dynamical Systems with ML {9.14}
            * Implications {9.15, 9.16, 9.19}
                - Safe Sets {9.17}
                - Robust Learning Supported Tube MPC {9.18}
        + Modeling External Signals {10.3, 10.4}
        + Modeling Constraints {10.5}
        + Modeling Cost Functions {10.6}
        + Learning Control Input: Replacing MPC {10.7}
    - Gaussian Processes {10.1, 10.9, 10.35, 12.18}
        + Setup and Definition {10.10, 10.17, 10.18, 10.19}
        + GP Regression {10.20}
            * Prior Distribution {10.21, 10.26}
                - Mean Function {10.22, 10.37, 10.38, 10.39}
                - Covariance Function {10.23, 10.24, 10.25, 10.40, 10.49, 10.50}
            * Posterior Distribution {10.27, 10.28}
            * Noise Observations {10.51, 10.52}
        + Hyper-Parameter Learning {10.29}
            * Influence of the Hyper-Parameters {10.41, 10.42, 10.43, 10.44, 10.45, 10.46, 10.47}
            * Automatic Relevance Determination {10.48}
        + Dynamic Process Models {10.32, 10.33}
        + Benefits and Drawbacks {10.30, 10.31}
    - (Artificial) Neural Networks {11.1, 11.3, 11.25, 12.19}
        + Setup {11.4, 11.6, 11.7, 11.8}
        + Signal Direction {11.9, 11.10, 11.11}
        + Connections Between Nodes {11.12}
        + Activation Functions {11.13}
        + Training {11.14, 11.15, 11.16, 11.17}
            * Optimization Algorithm {11.18}
            * Challenges {11.19, 11.20}
        + Neural Networks in MPOC {11.24}
        + Benefits and Drawbacks {11.23}
    - Remarks on Nomenclature {11.21}
* Outlook {13.1, 13.6, 13.10}
    - Libraries for Machine Learning {13.3, 13.4, 13.5}
    - Reinforcement Learning vs. MPC {13.7, 13.8, 13.9}
