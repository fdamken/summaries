# DLAM Summary :: Planning

## Slides

Done/Structured/Total: 210/1350/1350; 9%/100%/100%

* [X] Chapter  1 : Introduction (45)
* [X] Chapter  2 : Optimization (81)
* [X] Chapter  3 : Backpropagation (84)
* [x] Chapter  4 : Training Neural Networks 1 (102)
* [x] Chapter  5 : Training Neural Networks 2 (48)
* [x] Chapter  6 : Convolutional Neural Networks 1 (170)
* [x] Chapter  7 : Convolutional Neural Networks 2 (118)
* [x] Chapter  8 : Recurrent NNs, LSTMs, and Applications (98)
* [x] Chapter  9a: Generative Adversarial Networks (50)
* [x] Chapter  9b: Generative Models (133)
* [x] Chapter 10a: Deep Probabilistic Models (69)
* [x] Chapter 10b: Tractable Probabilistic Models (209)
* [x] Chapter 11 : Text Processing with Deep NNs (84)
* [x] Chapter 12 : Attention Models (46)
* [x] Chapter 13 : Transformers (13)

### Tentative Topics

* Intro, Computer Vision History, Classification, kNN
* Linear Classification, Feature Selection, Optimization, Stochastic Gradient, Backpropagation
* Training DNNs: Activation Functions, Initialization, Gradient Flow, Batch Normalization, Parameter Updates, Ensembles, Dropout
* Convolutional Neural Networks
* Recurrent Networks, LSTMs
* Deep NLP
* Variational Autoencoder
* Deep Probabilistic Models
* Interpreting DNNs
* DNNs for Games
* Deep Reinforcement Learning


## Structure

* Introduction {1.1, 1.5, 1.6, 1.7, 1.8, 1.12, 1.15, 1.21, 1.22, 1.23, 1.24, 1.25, 1.26, 1.32, 1.33, 1.44}
    - Milestones {1.16, 1.17, 1.18, 1.19, 1.20}
    - History {1.34, 1.35, 1.36}
    - The (Surprising?) Success of Deep Neural Networks {1.37, 1.38, 1.39, 1.40, 1.41, 1.42, 1.43}
    - Inspiration {4.8, 4.9, 4.10, 4.11, 4.12, 4.13, 4.14, 4.15, 4.16, 4.17, 4.18, 4.19, 4.20, 4.21, 4.22}
    - The Automatic Statistician and AutoML {10a.58, 10a.59, 10a.60, 10a.61, 10a.62, 10a.63, 10a.64, 10a.65, 10a.66, 10a.67, 10a.68}
* Basics {N/A}
    - Linear Classifier {2.4, 2.5, 2.6, 2.7}
    - Random Variables, Distributions, and Bayes Rule {10a.8, 10a.9, 10a.10, 10a.11, 10a.12}
    - Bias and Variance, Loss Functions, and Weight Regularization {2.8, 2.9, 2.10, 2.11}
* Optimization {2.1, 2.12, 2.13, 2.14, 2.81}
    - Gradient Descent {2.17, 2.33, 2.34}
        + Evaluating the Gradient {2.25, 2.26, 2.27, 2.28, 2.29, 2.30, 2.32, 3.4}
        + Mini-Batch and Stochastic Gradient Descent {2.35, 2.36, 2.37, 2.38, 2.39, 2.40, 2.41, 4.2, 5.40}
    - Newton's Method and L-BFGS {2.42, 2.43, 2.44, 2.45, 2.46, 2.47, 2.48, 2.49, 2.50}
    - Convergence {2.51, 2.52, 2.53, 2.54}
    - Momentum {2.56, 2.57, 2.58, 2.59, 2.60}
        + Nesterov Momentum {2.61, 2.62, 2.63, 2.64, 2.65, 2.66, 2.67}
        + AdaGrad {2.68, 2.69, 2.70}
        + RMSProp {2.71, 2.72, 2.73, 2.74}
        + Adam {2.75, 2.76, 2.77, 2.78}
    - Learning Rate {2.79, 2.80}
* Backpropagation {3.1, 3.2, 3.4, 3.5, 3.61, 4.3, 4.4}
    - Differentiating a Computational Graph {3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13, 3.14, 3.15, 3.16, 3.17, 3.18, 3.19, 3.20, 3.21, 3.22, 3.23, 3.24, 3.25, 3.26, 3.27, 3.28, 3.29, 3.30, 3.31, 3.32, 3.33, 3.34, 3.35, 3.36, 3.37, 3.38, 3.39, 3.40, 3.41}
    - Patterns in the Backward Flow {3.42, 3.43}
    - Forward and Backward Differentiation {3.47, 3.48, 3.49, 4.5, 4.6, 4.7}
    - Vectorized Operations {3.55, 3.56, 3.57, 3.58, 3.59}
    - Neural Networks {3.62, 3.63, 3.64, 3.65, 3.66, 3.67, 3.83, 3.84}
        + Brain Analogies {3.72, 3.73, 3.74, 3.75, 3.76}
        + Activation Functions {3.77, 4.30, 4.31, 4.32, 4.46}
            * Sigmoid {4.33, 4.34, 4.35}
            * Tanh {4.36}
            * Rectified Linear Unit (ReLU) {4.37, 4.38, 4.39, 4.40, 4.41}
            * Leaky and Parametric ReLU {4.42, 4.43}
            * Exponential Linear Unit (ELU) {4.44}
            * Maxout {4.45}
        + Regularization {3.81, 3.82}
* Training Neural Networks {4.1, 4.29, 4.101, 4.102, 5.1, 5.2, 5.3, 5.48}
    - History {4.24, 4.25, 4.26, 4.27, 4.28}
    - Data Pre-Processing {4.47, 4.48, 4.49, 4.50}
    - Weight Initialization {4.51, 4.52, 4.53, 4.54, 4.63}
        + Activation Statistics {4.55, 4.56, 4.57, 4.58, 4.59, 4.60, 4.61, 4.62}
        + Batch Normalization {4.64, 4.65, 4.66, 4.67, 4.68, 4.69}
    - Babysitting the Learning Process {4.70, 4.71, 4.72, 4.73, 4.74, 4.75, 4.76, 4.77, 4.78, 4.79, 4.80, 4.81, 4.82, 4.82}
    - Hyperparameter Optimization {4.84, 4.85, 4.86, 4.87, 4.88, 4.89, 4.90, 4.91, 4.92, 4.93, 4.94, 4.95, 4.96, 4.97, 4.98, 4.99, 4.100}
    - Ensemble Learning {5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 5.10, 5.11, 5.12, 5.13, 5.14, 5.15, 5.16, 5.17}
    - Dropout Regularization {5.18, 5.19, 5.20, 5.21, 5.22, 5.23, 5.30}
        + At Test Time {5.24, 5.25, 5.26, 5.27, 5.28, 5.29}
        + Inverted Dropout {5.31}
    - Gradient Clipping {5.32, 5.33, 5.34, 5.35, 5.36, 5.39}
        + Extreme Gradient Clipping {5.37}
        + One-Bit Gradient {5.38}
    - Gradient Noise {5.41, 5.42, 5.43, 5.44, 5.45, 5.46, 5.47}
* Convolutional Neural Networks {6.1, 6.2, 6.3, 6.64, 6.65, 6.66, 6.67, 6.68, 6.170}
    - Biology {N/A}
        + Retinal Receptive Fields {6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 6.10, 6.11, 6.12, 6.13, 6.14}
        + Cortical Receptive Fields {6.15, 6.16, 6.17, 6.18, 6.19, 6.20, 6.21, 6.22, 6.23, 6.24, 6.25, 6.26, 6.27, 6.28}
    - Convolutions {6.29, 6.30, 6.31, 6.32, 6.33, 6.34, 6.35, 6.36, 6.37, 6.38}
        + Examples {6.39, 6.40, 6.41, 6.42, 6.43, 6.44, 6.45, 6.46, 6.47, 6.48, 6.49, 6.50, 6.51, 6.52, 6.53, 6.54, 6.55, 6.56, 6.57, 6.58, 6.59, 6.60, 6.61, 6.62, 6.63}
    - Convolutional Layers {6.66, 6.67, 6.68, 6.69, 6.70, 6.71, 6.72, 6.73, 6.74, 6.75, 6.76, 6.77, 6.78, 6.79, 6.80, 6.81, 6.82, 6.83, 6.84, 6.85, 6.86, 6.120, 6.121}
        + Activation Volume {6.87, 6.88, 6.89, 6.90, 6.91, 6.92, 6.93, 6.94, 6.95, 6.96, 6.115, 6.122}
        + Zero-Padding and Stride {6.100, 6.101, 6.102, 6.103, 6.104, 6.105, 6.106, 6.107, 6.108, 6.109, 6.110, 6.111, 6.112, 6.113, 6.114}
        + Neuron View {6.123, 6.124, 6.125, 6.126}
    - Pooling {6.127, 6.128, 6.129, 6.130, 6.131}
    - Examples {N/A}
        + placeholder
            * placeholder
                - LeNet-5 {6.133, 6.134, 7.11}
                - AlexNet {6.136, 6.137, 6.138, 6.139, 6.140, 6.141, 6.142, 6.143, 7.12, 7.13}
    - Transfer Learning {6.144, 6.145, 6.146, 6.147, 6.148, 6.149, 6.150, 6.151}
        + Examples {N/A}
            * placeholder
                - VGGNet {6.152, 6.153, 6.154, 6.155}
                - GoogLeNet {6.156, 6.157}
                - ResNet {6.158, 6.159, 6.160, 6.161, 6.162, 6.163, 6.164, 6.165, 6.166, 6.167, 7.26, 7.27, 7.28, 7.32, 7.34}
                - AlphaGo {6.168, 6.169}
* Computer Vision Tasks {7.36, 7.37, 7.38, 7.118}
    - Classification + Localization {7.39, 7.40, 7.63}
        + Localization as Regression {7.41, 7.42, 7.43, 7.44, 7.45, 7.46, 7.47}
            * Localizing Multiple Objects {7.48}
            * Human Pose Estimation {7.49}
        + Sliding Window {7.50, 7.51, 7.52, 7.53, 7.54, 7.55, 7.56, 7.57, 7.58, 7.59, 7.60, 7.61, 7.62}
    - Object Detection {7.65, 7.87, 7.88, 7.117}
        + Detection as Regression {7.66, 7.67, 7.68}
        + Detection as Classification {7.69, 7.70, 7.71, 7.72, 7.73, 7.76}
            * Deformable Parts Model (DPM) {7.74, 7.75}
            * Region Proposals {7.77, 7.78, 7.79, 7.80}
        + R-CNN {7.81, 7.82, 7.83, 7.84, 7.85, 7.86, 7.89, 7.90, 7.91, 7.92, 7.93}
        + Fast R-CNN {7.94, 7.95, 7.96, 7.98, 7.98, 7.99, 7.100, .101, 7.102, 7.103, 7.104, 7.105, 7.106}
        + Faster R-CNN {7.107, 7.108, 7.109, 7.110, 7.111, 7.112, 7.113}
        + YOLO: You Only Look Once {7.114, 7.115}
* Recurrent Neural Networks {8.1, 8.4, 8.5, 8.23, 8.24, 8.25, 8.26, 8.27, 8.28, 8.29, 8.98}
    - Unrolling and Backprop-Through-Time {8.6, 8.7, 8.8, 8.9, 8.10, 8.11, 8.12, 8.13, 8.14, 8.15, 8.16, 8.17, 8.18, 8.19, 8.20, 8.21, 8.22}
    - Vanilla RNN {8.30, 8.31, 8.32, 8.33, 8.34}
        + Example: Character-Level Language Model {8.35, 8.36, 8.37, 8.38, 8.47, 8.48, 8.52, 8.53, 8.54, 8.55, 8.56, 8.57, 8.58, 8.59, 8.60, 8.61}
            * Interpretable Cells {8.62, 8.63, 8.64, 8.65, 8.66, 8.67}
        + Image Captioning {8.68, 8.69, 8.70, 8.71, 8.72, 8.73, 8.74, 8.75, 8.76, 8.77, 8.78, 8.79, 8.80, 8.81, 8.82, 8.83}
    - Long Short-Term Memory (LSTM) {8.84, 8.85, 8.86, 8.87, 8.88, 8.89, 8.90, 8.91, 8.92, 8.93}
        + Gradient Flow Dynamics {8.94, 8.95, 8.96}
        + Variants and Friends {8.97}
* Generative Models {9b.1, 9b.3, 9b.4, 9b.5, 9b.6, 9b.7, 9b.8, 9b.9, 9b.10, 9b.11, 9b.12, 9b.13, 9b.14, 9b.15, 9b.16, 9b.17, 9b.18, 9b.19, 9b.20, 9b.131, 9b.132, 9b.133, 9a.3, 9a.4, 9a.5, 9a.6, 9a.7, 9a.8}
    - Fully Visible Belief Network {9b.22, 9b.23, 9b.24, 9a.9}
    - WaveNet {9a.10}
    - Change of Variables {9a.11}
    - Boltzmann Machine {9a.13}
    - PixelRNN and PixelCNN {9b.21, 9b.25, 9b.26, 9b.27, 9b.28, 9b.29, 9b.30, 9b.31, 9b.32, 9b.33}
    - Variational Auto-Encoder (VAE) {9b.34, 9b.35, 9b.36, 9b.97, 9a.12}
        + Auto-Encoder {9b.37, 9b.38, 9b.39, 9b.40, 9b.41, 9b.42, 9b.43, 9b.44, 9b.45, 9b.46, 9b.47, 9b.48, 9b.49}
        + Model {9b.50, 9b.51, 9b.52, 9b.53, 9b.54, 9b.55, 9b.56, 9b.57, 9b.58, 9b.59, 9b.60, 9b.61}
        + Intractability {9b.62, 9b.63, 9b.64, 9b.65, 9b.66, 9b.67, 9b.68}
        + Encoder, Decoder, and Evidence Lower Bound (ELBO) {9b.69, 9b.70, 9b.71, 9b.72, 9b.73, 9b.74, 9b.75, 9b.76, 9b.77, 9b.78, 9b.79, 9b.80, 9b.81, 9b.82}
        + Training Procedure {9b.83, 9b.84, 9b.85, 9b.86, 9b.87, 9b.88, 9b.89, 9b.90}
        + Generating Data {9b.91, 9b.92, 9b.93, 9b.94, 9b.95, 9b.96}
    - Generative Adversarial Networks (GANs) {, 9b.114, 9b.115, 9b.130, 9a.1, 9a.2, 9a.14, 9a.15, 9a.16}
        + Two-Player Game {9b.104, 9b.105, 9b.106, 9b.107, 9b.108, 9b.109}
            * Optimization Problems {9b.110, 9b.111, 9b.112}
        + Convolutional Architectures {9b.118, 9b.119, 9b.120, 9b.121}
            * Interpretability {9b.122, 9b.123, 9b.124, 9b.125, 9b.126}
    - Generative Adversarial Networks (GANs) {9a.14, 9a.15, 9a.16, 9a.33, 9a.50, 9b.98, 9b.99, 9b.100, 9b.101, 9b.102, 9b.103, 9b.130}
        + Training Procedure {9a.17, 9a.23, 9a.34, 9b.104, 9b.105, 9b.113, 9b.114, 9b.115}
            * Minimax, Non-Saturating, and Maximum Likelihood Games {9a.18, 9a.19, 9a.20, 9a.21, 9b.106, 9b.107, 9b.108, 9b.109}
            * Discriminator Strategy {9a.22}
            * Mode Collapse {9a.29, 9b.110, 9b.111, 9b.112}
        + Convolutional Architectures {9b.118, 9b.119, 9b.120, 9b.121}
        + Vector Space Arithmetic {9a.28, 9b.122, 9b.123, 9b.124, 9b.125, 9b.126}
    - Optimization and Games {9a.37, 9a.38}
        + Nash Equilibrium {9a.39}
        + Well-Studies Cases {9a.40}
            * Continuous Minimax Game {9a.41}
            * Local Differential Nash Equilibria {9a.42}
            * Gradient Descent Convergence {9a.43, 9a.44}
        + Heuristics {9a.45, 9a.46}
        + Other Games in AI {9a.47}
* Probabilistic Graphical Models {10b.6, 10b.7, 10b.8, 10b.9, 10b.10, 10b.11, 10b.12, 10b.13, 10b.14, 10b.15, 10b.16, 10b.17, 10b.18, 10b.19, 10a.1, 10a.2, 10a.3, 10a.6, 10a.13, 10a.14, 10a.22, 10a.23, 10a.24, 10a.69}
    - (Conditional) Independency {10a.15, 10a.16}
    - Tractability vs. Expressiveness {10b.60, 10b.61, 10b.62, 10b.63}
        + Inference and Queries {10a.19}
            * placeholder
                - Complete Evidence Queries (EVI) {10b.20, 10b.21, 10b.22}
                - Marginal Queries (MAR) {10b.31, 10b.32, 10b.33}
                - Conditional Queries (CON) {10b.34, 10b.35, 10b.36}
                - Maximum A-Posteriori (MAP) {10b.46, 10b.47, 10b.48, 10b.49}
                - Marginal MAP (MMAP) {10b.50, 10b.51, 10b.52, 10b.53}
                - Advanced Queries {10b.54, 10b.55, 10b.56, 10b.57, 10b.58}
        + Models {N/A}
            * Generative Adversarial Networks {10b.23,, 10b.24}
            * Variational Autoencoders {10b.25, 10b.26}
            * Probabilistic Graphical Models: Markov and Bayes Networks {10b.27, 10b.28, 10b.29, 10b.30, 10b.37, 10b.38, 10a.7, 10a.17, 10a.18, 10a.19, 10a.25}
                - Variable Elimination {10a.20, 10a.21}
            * Low-Tree-Width PGMs: Trees {10b.39, 10b.40, 10b.41}
            * Mixtures {10b.42, 10b.43, 10b.44, 10b.45}
            * Fully Factorized Models {10b.59}
    - Probabilistic Circuits {10b.64, 10b.65, 10b.66, 10b.67, 10b.68, 10b.69, 10b.70, 10b.71, 10b.72, 10b.73, 10b.74, 10b.75, 10b.76, 10b.77, 10b.78, 10b.79, 10b.80, 10b.81, 10b.82, 10b.104, 10b.126}
        + Ensuring Tractability {10b.83}
            * Decomposability and Smoothness {10b.84, 10b.85}
                - Tractable MAR/CON {10b.86, 10b.87, 10b.88, 10b.89}
            * Determinism {10b.90}
                - Tractable MAP {10b.91, 10b.92, 10b.93, 10b.94, 10b.95, 10b.96, 10b.97, 10b.98}
                - Approximate MAP {10b.99}
            * Structured Decomposability {10b.100, 10b.101, 10b.102, 10b.103}
        + Logical Circuits {10b.105, 10b.106, 10b.107, 10b.108}
            * Weighted Model Counting (WMC) {10b.109}
            * From Trees to Circuits {10b.110, 10b.111, 10b.112, 10b.113, 10b.114, 10b.115, 10b.116, 10b.117}
            * Low-Tree-Width PGMs {10b.118}
            * Arithmetic Circuits (ACs) {10b.119}
            * Sum-Product Networks (SPNs) {10b.120, 10a.26, 10a.27, 10a.28, 10a.29, 10a.30, 10a.31, 10a.32, 10a.33, 10a.53, 10a.54, 10a.55, 10a.56, 10a.57}
                - Semantics {10a.34}
                - Linear Inference {10a.35, 10a.36, 10a.37, 10a.38}
                - Image Completion {10a.40, 10a.41, 10a.42, 10a.43, 10a.44}
                - Variants {10a.45, 10a.46, 10a.47}
                - Symbolic Evaluation {10a.51, 10a.52}
            * Cutset Networks (CNets) {10b.121, 10b.122, 10b.123}
            * Probabilistic Sentential Decision Diagrams {10b.124}
        + Expressiveness {10b.127, 10b.128}
    - Building Circuits {10b.129, 10b.130, 10b.131, 10b.132, 10b.133, 10b.134, 10b.135, 10b.136, 10a.39}
        + Hard/Soft Parameter Updating: Gradient Descent and EM {10b.137, 10b.138}
        + (Bayesian) Parameter Learning {10b.139, 10b.140, 10b.141}
        + Structure Learning {10b.142}
            * LearnSPN {10b.143, 10b.144, 10b.145, 10b.146}
                - ID-SPN {10b.148}
                - Other Variants {10b.147, 10b.149}
            * Cut(e)set Network {10b.150}
            * PSDD Structure Learning {10b.151, 10b.152}
            * LearnPSDD {10b.153}
            * Learning Logistic Circuits {10b.154, 10b.155}
            * Bayesian Structure Learning {10b.156}
            * Automatic Bayesian Density Analysis (ABDA) {10b.157, 10b.158}
            * Bayesian SPNs {10b.159, 10b.160}
            * Randomized Structure Learning: RAT-SPNs {10b.161, 19b.162}
            * Extremely Randomized CNets: XCNets {10b.166, 10b.167}
            * Learning (Tree-)SPNs {10a.47, 10a.48, 10a.49, 10a.50}
        + Ensembles of Probabilistic Circuits {10b.163, 10b.164, 10b.165}
        + Online Learning {10b.168}
        + Knowledge Compilation {10b.169, 10b.170}
        + Hybridizing TPMs with Intractable Models {10b.171}
            * Sum-Product Graphical Model (SPGM) {10b.172}
            * Sum-Product Variational Auto-Encoder (SPVAE) {10b.173}
    - Applications {10b.174, 10b.175, 10b.176, 10b.177, 10b.181, 10b.188, 10b.191}
        + placeholder
            * placeholder
                - Computer Vision {10b.178, 10a.5}
                - Image Segmentation {10b.179}
                - Scene Understanding: Su-PAIR {10b.180}
                - Activity Recognition {10b.182}
                - Speec Reconstriction and Extension {10b.183, 10a.4}
                - Sequence Labeling {10b.184}
                - Robotics {10b.185}
                - SOP: Preference Learning {10b.186}
                - SOP: Routing {10b.187}
                - Probabilistic Programming {10b.189}
                - And more\dots {10b.190}
    - Takeaways and Open Challenges {10b.192, 10b.193, 10b.194, 10b.195}
* Natural Language Processing {11.1, 11.2, 11.82, 11.84}
    - Text Semantics {11.3, 11.4, 11.39}
        + Propositional Semantics {11.5, 11.6, 11.7, 11.8, 11.9, 11.10, 11.11, 11.12, 11.13, 11.14}
            * Vector Embeddings and Similarity {11.15, 11.16, 11.17}
            * Latent Semantic Analysis {11.18, 11.19, 11.20, 11.21, 11.22, 11.23}
        + Word2Vec {11.24, 11.25, 11.26, 11.27, 11.28, 11.29, 11.30}
            * Learned Relations {11.31, 11.32, 11.33, 11.34, 11.35, 11.36, 11.37, 11.38}
        + Skip-Thought Vectors {11.40, 11.41, 11.42, 11.43}
            * Sentence Similarity and Relatedness {11.44, 11.45, 11.46, 11.47}
        + Siamese Models {11.48, 11.49, 11.50, 11.51, 11.52}
            * Semantic Entailment {11.53, 11.54}
    - Translation Models {11.55}
        + Sequence-to-Sequence RNNs {11.56, 11.57}
            * Bleu Scores for Translation {11.58, 11.59, 11.60, 11.61, 11.62, 11.63, 11.64, 11.65, 11.66}
            * Sequence-to-Sequence Model Translation {11.67, 11.68, 11.69, 11.70}
        + State-of-the-Art Neural Machine Translation {11.71, 11.72}
            * Parsing {11.73, 11.74, 11.75}
            * Sequence-to-Sequence Parser {11.76, 11.77, 11.78, 11.79}
            * Neural Entity-Relation Extraction {11.80, 11.81, 11.82}
    - Attention Models {12.1, 12.3, 12.4, 12.5, 12.6, 13.2, 13.3, 13.4, 13.5}
        + Hard Attention for Recognition {12.7, 12.8, 12.9}
        + Soft Attention for Translation {12.10, 12.11, 12.12, 12.13, 12.14, 12.15, 12.16, 12.17, 12.18, 12.19, 12.20, 12.21, 12.22, 12.23}
        + Global and Local Attention Model {12.24, 12.25, 12.26}
        + Soft Attention for Captioning {12.27, 12.28, 12.29, 12.30, 12.31, 12.35}
            * Soft Attention for Video {12.32, 12.33, 12.34}
        + Attending to Arbitrary Regions {12.36, 12.37}
            * DRAW {12.38, 12.39}
            * Spatial Transformer Networks {12.40, 12.41, 12.42, 12.43, 12.44}
        + Takeaways {12.45, 12.46}
    - Transformer Networks {13.1, 13.6, 13.7, 13.8, 13.9, 13.10, 13.11}
        + GPT and GPT-2 {13.12}
        + BERT (Bidirectional Encoder Representation from Transformers) {13.13}
