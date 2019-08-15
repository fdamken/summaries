# FMSe Zusammenfassung :: Planung

## Foliensätze

* [x] Kapitel 1: Introduction
* [x] Kapitel 2: Introduction to PROMELA
* [x] Kapitel 3: Verification with SPIN
* [x] Kapitel 4: Modeling Concurrency
* [x] Kapitel 5: Modeling Distributed Systems
* [x] Kapitel 6: Specifying with Linear Temporal Logic
* [x] Kapitel 7: Model Checking with Temporal Logic
* [x] Kapitel 8: Deduction in First-Order Logic (FOL)
* [x] Kapitel 9: JML: The Java Modeling Language
* [x] Kapitel 10: Java Modeling Language (JML) 2
* [x] Kapitel 11: Dynamic Logic Part 1
* [x] Kapitel 12: Dynamic Logic Calculus
* [x] Kapitel 13: Method Calls and Contracts
* [x] Kapitel 14: Programs with Loops



## Themen

* Introduction {1.10, 1.11, 1.12, 9.2, 9.3, 9.4}
    - Normal Testing {1.13, 1.14}
    - Formal Methods {1.15, 1.16, 1.17, 1.18, 1.19, 1.20, 1.21, 1.23, 1.24}
    - Abstraction and Expressiveness {1.25, 1.26, 1.27}
    - Automatic Proof Search {1.28}
    - Model Checking {1.29, 1.30, 1.31}
    - Deductive Verification {1.32, 1.33, 1.34}
    - Tool Support {1.35}
* PROMELA {2.1, 2.4, 2.5, 2.37, 3.2}
    - Syntax/Semantics {2.6}
        + Data Types {N/A}
            * Arithmetic {2.7}
            * Booleans {2.8}
            * Enumerations {2.9}
            * Arrays {2.16}
            * Records {2.17}
        + Control Statements {2.10}
            * Guarded Statements {2.12}
            * Selection (\texttt{if}) {2.11, 2.13}
            * Repetition (\texttt{do}) {2.14}
            * For-Loops {2.15}
            * Jumps {2.18}
        + Inlining Code {2.19}
    - Non-Determinism {2.20}
        + Value Generation {2.21, 2.22, 2.23, 2.24}
    - Concurrency {2.25, 2.27, 4.1, 4.2, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 4.10}
        + Starting Processes {4.11, 4.12, 4.13, 4.16}
            * Parameters {4.15}
        + Joining Processes {4.14}
        + Local and Global Data {4.17, 4.18, 4.19}
            * Synchronisation {4.26}
        + Execution and Computations {2.26, 2.28}
            * Interleaving {2.29, 2.30, 4.20}
        + Atomicity {2.31, 2.32, 2.34, 4.22}
            * Deterministic Sequences {4.23}
            * Atomic Sequences {4.24}
            * Backdraws {4.44}
        + Executability {4.27, 4.28}
            * Blocking {4.29}
        + The Critical Section Problem {4.30, 4.31}
            * Mutual Exclusion {4.32 4.33, 4.34, 4.35, 4.36, 4.37, 4.38, 4.39, 4.40}
            * Variations {4.43}
        + Deadlocks {4.41, 4.42}
    - Distributed Systems {5.1, 5.2, 5.3}
        + Channels {5.4, 5.5}
            * Sending/Receiving {5.7, 5.30, 5.31}
                - Pattern Matching {5.32, 5.34}
                - Random receive {5.35}
                - Prefix Syntax {5.36}
            * Checking State {5.29}
            * Scope {5.8}
            * Rendezvous {5.5}
                - Executability {5.12}
                - Synchronous Rendezvous {5.16, 5.17}
                - Limitations {5.25}
            * Buffered {5.27, 5.27}
                - Executability {5.28}
                - Verification {5.37}
        + Client-Server Model {5.9, 5.10}
            * Replies {5.18, 5.19, 5.20, 5.21}
        + Sending Channels {5.22, 5.23}
        + Sending Process IDs {5.24}
            * Interleaving {5.14}
* Linear Temporal Logic (LTL) {6.1, 6.2, 6.3}
    - Propositional Logic {6.4}
        + Syntax {6.5}
            * Concrete Syntax {6.6}
        + Semantics {6.8, 6.9, 6.10}
            * Notations {6.12}
        + Expressiveness {6.15, 6.16, 6.17}
    - Motivation {6.17}
    - Kripke Structure {6.18}
    - Transition Systems {6.19, 6.20}
    - Syntax {6.21}
    - Semantics {6.22, 6.23, 6.24}
        + Validity {6.27}
        + Transition Systems {6.30, 6.31}
    - Safety and Liveness Properties {6.25}
        + Safety Properties {7.13}
        + Liveness Properties {7.14}
    - Formal \(\omega\)-Languages {6.33}
        + Büchi Automaton {6.34, 6.35}
            * LTL \(\leftrightarrow\) Büchi Automaton {6.40, 6.41}
        + \(\omega\)-Regular Expressions {6.36}
    - Decidability {6.37}
* SPIN {3.8, 3.28, 3.29}
    - Model Checking {2.3, 3.3, 3.4, 3.5, 3.6, 3.7, 6.45, 6.46, 6.47, 7.1, 7.2}
    - Workflow {3.9, 3.10, 3.11, 3.18, 3.19, 3.20, 3.26}
        + Guided Simulation {3.21, 3.22}
        + Temporal Properties {7.20, 7.23}
        + Fairness {7.25, 7.26}
    - Correctness Properties {3.12}
        + Static Correctness Properties {3.13, 7.3}
        + Assertion Statements {3.14, 3.15, 3.16, 3.17}
        + Valid End States {3.32, 3.33}
        + Temporal Properties {7.7, 7.8, 7.9, 7.10, 7.19}
            * Syntax {7.11, 7.14, 7.15}
                - Label Checking {7.28, 7.29}
            * Semantics {7.12}
            * Never Claim {7.15, 7.16, 7.17, 7.18}
    - Preliminaries {7.4}
        + Acceptance Cycles {7.5}
        + Fairness {7.6, 7.24, 7.27}
* Deduction in First-Order Logic (FOL) {8.1, 8.2, 8.3}
    - Syntax {N/A}
        + Signature {8.4, 8.5, 8.6, 8.7}
        + Terms {8.8, 8.9, 8.10}
        + Atomic Formulas {8.11, 8.12, 8.13}
        + General FOL-Formulars {8.14, 8.15, 8.16}
        + Concrete Syntax {8.16}
    - Semantics {8.18, 8.19}
        + Domains/Universes {8.20}
            * Signature Symbols vs. Domain Elements {8.24}
        + Variable Assignments {8.25}
        + States/Models {8.21, 8.22}
        + Reserved Signature Symbols {8.23}
        + Semantic Evaluation {N/A}
            * Terms {8.26, 8.27}
            * Formulas {8.29, 8.30}
        + Semantic Concepts {8.32}
        + Semantic Evaluation {8.33, 8.34, 8.35, 8.36, 8.37}
            * Rules {8.38, 8.50}
            * Proofs {8.39, 8.42, 8.43, 8.44, 8.45, 8.47, 8.48, 8.49}
            * Soundness and Completeness {8.41}
* Java Modeling Language (JML) {9.1, 9.5, 9.6, 9.9, 9.13, 9.14, 9.15}
    - Informal Specification {9.10, 9.11}
    - Formal Specification {9.12}
    - Syntax/Semantic {9.16, 9.17}
        + Modifiers {9.18, 9.29, 10.28, 10.29, 10.30, 10.32}
            * Pure {9.30, 9.31, 9.32}
        + Specification Cases {9.19, 9.23}
            * Normal Behavior {9.19}
            * Exceptional Behavior {10.22, 10.23, 10.24, 10.25, 10.26}
        + Preconditions {9.20, 9.21}
        + Postconditions {9.22}
        + Class Invariants {10.10, 10.16, 10.17, 10.18, 10.20}
            * Instance vs. Static Invariants {10.19}
        + Loop Invariants {14.17, 14.19, 14.22}
            * Finding Invariants {14.29, 14.30}
        + Expressions {9.33, 9.34}
            * Access of Prestate {9.24}
            * Quantifiers {9.35, 9.36, 9.37, 9.38, 9.39}
            * Result Values {10.4}
        + Assignable {9.25, 9.26, 9.27, 9.28}
        + Non-Termination {10.27}
        + Inheritance {10.33}
* Dynamic Logic (DL) {11.1, 11.2, 11.3}
    - Motivation {11.4, 11.5, 11.6, 11.10, 11.11}
    - Type Hierarchy {11.7, 11.8, 11.9, 12.17}
    - Syntax {11.12}
        + Signature {11.15}
            * Variables {11.13, 11.14, 11.17}
        + Terms {11.18}
        + Modalities {11.19, 11.20}
        + Formulas {11.23, 11.24}
        + KeY Input File {11.16, 11.22, 12.24}
    - States/Models {11.25}
    - Kripke Structure {11.26, 11.27, 11.28}
    - Semantic Evaluation {11.29, 12.4}
    - Symbolic Execution {11.31, 12.5, 12.6, 12.7}
        + Updates {12.8, 12.16}
            * Symbolic {12.9}
            * Explicit {12.10}
            * Compute Effects of Updates {12.11}
            * Assignment Rule {12.12}
            * Update Composition {12.13}
            * Parallel Updates {12.14, 12.15}
        + Abrupt Termination {12.25, 12.26}
            * Null Pointer Exceptions {12.27}
            * Exceptions and Jumps {12.36}
        + Complex Expressions {12.34, 12.35}
    - Modeling the Heap {12.18}
        + Fields {12.19, 12.20}
            * Updates {12.21}
            * Access {12.22}
            * Pretty Printing {12.23}
    - Modeling Static Fields {12.30}
    - Aliasing {12.28, 12.29}
    - \texttt{this}/\texttt{self} {12.31}
    - Arrays {12.33}
    - Method Calls {13.4, 13.6}
        + Inlining {13.5, 13.8}
        + Contract Rule {13.9, 13.10, 13.11, 13.15, 13.16}
        + Object Initialization {12.32, 13.7}
        + Keeping the Context {13.12}
            * Anonymising Heap Locations {13.13, 13.14}
    - Loop Invariants {14.4, 14.7, 14.8, 14.19}
        + Context Loss {14.12}
        + Keeping the Context {14.14, 14.15}
        + Termination {14.20, 14.21}
        + Decreasing Term / Variant {14.22}
    - Proving Method Contracts {13.19}
    - Understanding Unclosed Proofs {13.20}
        + Model Search {14.31, 14.32}
    - DL Calculus Overview {12.7, 12.12, 12.21, 12.35, 12.36, 13.5, 13.9, 13.11, 13.15, 13.16, 13.19, 14.3, 14.4, 14.7, 14.12, 14.15}
