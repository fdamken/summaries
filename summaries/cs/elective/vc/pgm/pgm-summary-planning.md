# PGM Summary Planning

## Slides

Done/Structured/Total: 0/711/711; 0%/100%/100%

* [x] Chapter  1: Introduction (79)
* [x] Chapter  2: Bayesian Networks 1 (59)
* [x] Chapter  3: Bayesian Networks 2 (57)
* [x] Chapter  4: Inference (100)
* [x] Chapter  5: Learning 1 (50)
* [x] Chapter  6: Learning 2 (91)
* [x] Chapter  7: Dynamic Bayesian Networks (85)
* [x] Chapter  8: Approximate Inference (88)
* [x] Chapter  9: Tractable Probabilistic Models (59)
* [x] Chapter 10: Deep Generative Models (43)



## Structure

- Introduction {1.1, 1.2, 1.28, 1.29, 1.30, 1.38}
    - Examples {1.3, ..., 1.27}
    - Fundamental Questions {1.36, 1.37}
- Foundations {N/A}
    - Probability Theory {1.40}
        - (Conditional) Independence {1.57, 1.58, 1.59, 1.60}
            - Monty Hall Problem {1.61, 1.62, 1.63, 1.64, 1.65, 1.66, 1.67}
        - Inference {1.70, 1.71, 1.72}
            - Information Theory {1.73, 1.74, 1.75}
        - Potentials {4.19, 4.20, 4.21, 4.22, 4.23}
    - Machine Learning {N/A}
        - (Document) Classification {2.11, 2.12, 2.13, 2.14, 2.15, 2.16}
- Bayesian Networks {1.79, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.31, 2.32}
    - The Naive Bayes Model {2.8, 2.9}
        - Classification {2.20, 2.21, 2.22, 2.27}
        - Maximum Likelihood Parameter Estimation {2.23, 2.24, 2.25, 2.26}
        - Application {2.28, 2.29}
    - Definition and Independence Assumptions {2.36, 2.37, 2.38, 2.39, 2.40, 2.46, 2.58}
        - Local Markov Assumption {2.41, 2.42, 2.45}
        - "Explaining Away" / Berkson's Paradox {2.43, 2.44}
        - Representation Theorem {2.47, 2.48, 2.49, 2.50, 2.51, 2.52, 2.53, 2.54}
        - Building a Bayesian Network {2.55, 2.56, 2.57}
    - Encoded Independencies {2.59, 3.2, 3.3, 3.28, 3.29}
        - Dependency Structures {3.4}
        - d-Separation {N/A}
            - (Active) Trails {3.5, 3.6}
            - Independencies {3.9}
            - Soundness {3.15, 3.16}
            - Completeness {3.18, 3.20}
        - Faithful Distributions {3.17}
        - Context-Specific Independence (CSI) {3.21, 3.22, 3.23, 3.27}
            - Tree CPD {3.24}
            - Determinism {3.25, 3.26}
        - The Bayes' Ball Algorithm {3.19}
- Inference {3.30, 3.31, 3.32, 3.33}
    - Chain Models {3.34, 3.35, 3.36, 3.37}
    - Variable Elimination {3.38, 3.39, 3.40, 3.41, 3.42, 3.43, 3.44, 3.45, 3.46, 3.54, 3.57}
        - Evidence {3.47, 3.48, 3.49, 3.50, 3.51, 3.52, 3.53}
        - Complexity {3.55, 3.56}
        - VE for Potentials {4.24, 4.25}
    - Abductive Inference {4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.12, 4.17, 4.58}
        - Consistency {4.8}
        - Finding Most Probable Explanations (MPEs) {4.9, 4.10, 4.11}
    - Complexity of Conditional Queries {4.13, 4.14, 4.15, 4.16, 4.17}
    - Moralizing {4.26, 4.27, 4.28, 4.29, 4.30, 4.31, 4.32}
    - Variable Elimination in Moral Graphs {4.18, 4.33, 4.34, 4.35, 4.59}
        - Perfect Elimination Sequences {4.36, 4.37, 4.38, 4.39, 4.40, 4.41, 4.42}
        - Complexity {4.43, 4.44, 4.45}
        - Induced Graph {4.46, 4.47, 4.48}
        - Induced Treewidth {4.49}
        - Elimination on Trees {4.50, 4.51, 4.52}
            - Polytrees {4.53}
        - General Networks {4.54, 4.55, 4.56, 4.57}
- Markov Random Fields {4.60, 4.61, 4.62, 4.63, 4.64, 4.99}
    - Bayesian Networks as MRFs {4.65, 4.66, 4.67, 4.68, 4.69, 4.70}
    - Triangulated Graphs {4.71, 4.72, 4.73, 4.74, 4.75}
    - Join Trees {4.76, 4.77, 4.78, 4.79, 4.80, 4.81, 4.82, 4.83, 4.84, 4.85, 4.86}
    - Junction Trees {4.87, 4.88, 4.89, 4.90}
        - Collecting Evidence {4.91, 4.92, 4.93, 4.94, 4.95, 4.96}
        - Distributing Evidence {4.97}
    - Non-Triangulated Graphs {4.98}
- Learning {5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.22, 5.28, 5.38, 6.58}
    - Complete and Incomplete Data Sets {5.9, 5.10, 5.11, 5.12}
        - Hidden Variables {5.12, 5.13, 5.14, 5.15, 5.16, 5.17, 5.18, 5.19, 5.20, 5.21}
    - Parameter Estimation {5.23, 5.55, 6.3}
        - Known Structure, Complete Data {5.29}
            - Maximum Likelihood {5.24, 5.25, 5.26, 5.27, 5.30}
            - Decomposability of the Likelihood {5.31, 5.32}
            - Likelihood for (Conditional) Bi- and Multinomials {5.33, 5.34, 5.35, 5.36, 5.37}
        - Known Structure, Incomplete Data (Expectation-Maximization) {5.39, 5.44, 5.48, 5.49, 5.53, 6.1}
            - EM Idea {5.40, 5.41, 5.42, 5.45}
            - Complete-Data Likelihood {5.43}
            - EM for (Conditional) Multinomials {5.46, 5.47}
            - Monotonicity {5.50}
        - Gradient Ascent {5.54}
        - Bayesian Parameter Estimation {6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 6.10}
            - Laplace Estimation {6.11, 6.12, 6.13, 6.16, 6.17}
            - Bayesian Prediction {6.18, 6.19, 6.24}
            - Conjugate Priors {6.20, 6.21, 6.25}
                - Binomial Prior {6.22, 6.23}
                - Dirichlet Prior {6.26, 6.27, 6.28, 6.29, 6.30}
            - Bayesian Networks and Bayesian Prediction {6.31, 6.32}
        - Summary {6.33, 6.34, 6.35}
    - Structure Learning / Model Selection {6.36, 6.37, 6.38, 6.39, 6.40, 6.57}
        - Minimal I-Maps {6.41, 6.42, 6.43}
        - Perfect Maps (P-Maps) {6.44, 6.45}
        - I-Equivalence {6.46, 6.47}
            - Skeleton and Immoralities {6.48, 6.49, 6.50, 6.51}
        - Obtaining a P-Map {6.52}
            - Identifying the Skeleton {6.53, 6.54}
            - Identifying Immoralities {6.55}
            - From Immoralities to Structures {6.56}
        - Accurate Structures {6.59}
        - Learning {6.60, 6.61}
            - Constrained-Based {6.62, 6.63}
            - Score-Based {6.64}
                - Likelihood Score {6.65}
                - Bayesian Score and Bayesian Information Criterion {6.66, 6.67, 6.68, 6.69, 6.70}
        - Structure Search as Optimization {6.71}
            - Learning Trees (Complete Data) {6.72, 6.73}
            - Heuristic (Local) Search {6.74, 6.75, 6.76, 6.77, 6.78, 6.79, 6.80, 6.81, 6.82, 6.83}
        - Structural EM {6.84, 6.85, 6.86, 6.87, 6.88}
        - Summary {6.89}
- Dynamic Bayesian Networks {7.1, 7.2, 7.3, 7.48}
    - Hidden Markov Models {7.4, 7.14, 7.15, 7.16}
    - Inference {7.17}
        - Decoding {7.18, 7.19, 7.20, 7.21, 7.22, 7.36}
            - Forward Pass {7.23, 7.24, 7.25, 7.26, 7.27, 7.28, 7.29, 7.30, 7.31, 7.32}
            - Backward Pass {7.33, 7.34, 7.35}
        - Best State Sequence {7.37, 7.38, 7.39}
            - Viterbi Algorithm {7.40, 7.41, 7.42}
        - Parameter Estimation {7.43, 7.44, 7.45, 7.46, 7.47}
    - State Estimation (Kalman Filter) {7.49, 7.50, 7.51, 7.52}
        - Recursive Bayesian Updating {7.53, 7.54}
        - (Modeling) Actions {7.55, 7.56, 7.57, 7.58}
        - Bayes Filter {7.62, 7.63, 7.64, 7.65, 7.66}
        - Discrete-Time Kalman Filter {7.69, 7.70, 7.71}
            - Dynamics and Observations {7.72, 7.74}
            - Belief Update: Prediction {7.73}
            - Belief Update: Correction {7.75}
    - General Dynamic Bayesian Networks {7.77, 7.78, 7.79}
        - Exact Inference {7.80, 7.81}
        - Tractable, Approximate Inference {7.82}
            - Assumed Density Filtering {7.83, 7.84, 7.85}
- Approximate Inference {8.1, 8.2}
    - Message Passing {8.3, 8.4, 8.5, 8.6, 8.7, 8.8, 8.9, 8.10, 8.11}
        - Sum-Product Belief Propagation {8.12, 8.13, 8.14, 8.15, 8.16, 8.17, 8.18, 8.19, 8.20, 8.21}
        - (Acyclic) Belief Propagation as Dynamic Programming {8.22, 8.23, 8.24, 8.25, 8.26, 8.27, 8.28, 8.29, 8.30, 8.31, 8.32, 8.33, 8.34, 8.35, 8.36}
        - Loopy Belief Propagation {8.37, 8.38, 8.39, 8.40, 8.41}
    - Sampling {8.42, 8.43, 8.44, 8.45, 8.46, 8.47, 8.48}
        - Forward Sampling (Without Evidence) {8.49, 8.50, 8.51, 8.52}
        - Forward Sampling (With Evidence) {8.53, 8.54, 8.55, 8.56, 8.57}
        - Gibbs Sampling {8.58, 8.59, 8.60, 8.61, 8.62, 8.63, 8.64, 8.65, 8.66, 8.67, 8.68}
            - Burn-In {8.69}
            - Irreducibility, Aperiodicity, and Ergodicity {8.71, 8.72, 8.73}
            - Convergence {8.70, 8.74, 8.75}
            - Performance {8.77}
            - Speeding Convergence {8.77}
                - Skipping Samples {8.78}
                - Randomized Variable Order {8.79}
                - Blocking {8.80}
                - Rao-Blackwellization {8.81, 8.82}
                - Multiple Chains {8.83}
        - Likelihood Weighting {8.84, 8.85, 8.86, 8.87, 8.88}
- Tractable Probabilistic Models {9.1}
    - Deep Learning {9.2, 9.3, 9.4}
    - Probabilistic Circuits {9.5, 9.6, 9.7, 9.8, 9.9, 9.10}
    - Sum-Product Networks {9.11, 9.12, 9.58, 9.59}
        - Inference {9.13, 9.14, 9.15, 9.16}
        - Learning {9.16, 9.17}
            - Directly Learning SPNs {9.24, 9.25, 9.26, 9.27}
        - Inference on Devices {9.29}
- Deep Generative Models {10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8}
    - Likelihood-Based {10.9}
        - Autoregressive Generatie Models {10.10}
            - Learning and Inference {10.11}
            - Parametrization {10.12, 10.13, 10.14}
        - Variational Auto-Encoders {10.15, 10.16, 10.17}
            - Inference as Optimization {10.18, 10.19}
            - Variational Bayes {10.20, 10.21}
            - Learning and Inference {10.22}
            - Open Questions {10.24}
        - Normalizing Flows {10.25, 10.26, 10.27, 10.28, 10.29}
            - Learning and Inference {10.30}
    - Likelihood-Free {10.32}
        - Generative Adversarial Networks {10.33, 10.34, 10.35}
            - Inference {10.36}
    - Applications in Scientific Discovery {10.39, 10.40, 10.41, 10.42, 10.43}
