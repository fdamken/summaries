# FMSe Summary :: Planning

## Slides

Done/Structured/Total (Slides): 0/559/559; 0%/100%/100%

* [x] Chapter  1: Introduction (Slides: 41)
* [x] Chapter  2: Introduction to PROMELA (Slides: 45)
* [x] Chapter  3: Verification with SPIN (Slides: 35)
* [x] Chapter  4: Modeling Concurrency (Slides: 51)
* [x] Chapter  5: Modeling Distributed Systems (Slides: 38)
* [x] Chapter  6: Specification with Linear Temporal Logic (Slides: 58)
* [x] Chapter  7: Model Checking with Temporal Logic (Slides: 30)
* [x] Chapter  8: Deduction in First-Order Logic (Slides: 52)
* [x] Chapter  9: Java Modeling Language (Slides: 41)
* [x] Chapter 10: Java Modeling Language (Slides: 36)
* [x] Chapter 11: Dynamic Logic (Slides: 32)
* [x] Chapter 12: Dynamic Logic Calculus (Slides: 38)
* [x] Chapter 13: Method Calls and Contracts (Slides: 23)
* [x] Chapter 14: Programs with Loops (Slides: 39)


## Subjects

* Introduction {N/A}
    - Motivation {1.10}
    - Traditional Reliability Measures {1.11, 1.12}
    - Classical Testing {1.13, 1.14}
    - Formal Methods {1.15, 1.16, 1.17, 1.19, 1.20}
        + Specification {1.18}
        + Difficulties {1.21, 1.22, 1.23, 1.24}
        + Abstraction and Expressiveness {1.25, 1.26, 1.27}
        + Automatic Proof Search {1.28}
    - Model Checking {1.29, 1.30, 1.31}
    - Deductive Verification {1.32, 1.33, 1.34}
    - Tool Support {1.35}
* PROMELA {2.3, 2.4, 2.5, 2.6}
    - Data Types {N/A}
        + Arithmetic {2.7}
        + Booleans {2.8}
        + Enumerations {2.9}
        + Arrays {2.16}
        + Record {2.17}
    - Control Statements {2.10}
        + Selection {2.11, 2.12, 2.13}
        + Repetition {2.14, 2.15}
        + Jumps {2.18}
    - Inlining Code {2.19}
    - Nondeterminism {2.20}
        + Value Generation {2.21, 2.22, 2.23}
    - Concurrent Systems {2.24, 2.25, 2.26, 2.27, 4.2, 4.5, 4.6, 4.8, 4.9, 4.10}
        + Starting Processes {4.11, 4.12, 4.13, 4.16}
            * Parameters {4.15}
        + Joining Processes {4.14}
        + Local and Global Data {4.17, 4.18, 4.19}
            * Synchronizing Global Data {4.26}
        + Computations {2.28}
            * Interleaving {2.29, 2.30, 4.20}
        + Atomicity {2.31, 2.32, 2.34, 4.22, 4.44}
            * Deterministic Sequences {4.23}
            * Atomic Sequences {4.24}
        + Executability {4.27, 4.28}
            * Blocking {4.29}
        + Critical Section Problem {4.30, 4.31, 4.32}
            * Mutual Exclusion {4.33, 3.34, 4.35, 4.36, 4.37}
            * Verifying ME {4.38, 4.39, 4.40}
            * Variations {4.43}
        + Deadlocks {4.41, 4.42}
    - Distributed Systems {5.2, 5.3}
        + Channels {5.4, 5.5, 5.6}
            * Sending/Receiving {5.7, 5.12, 5.30}
                - Pattern Matching {5.31, 5.32, 5.33, 5.34}
                - Random Receive {5.35}
                - Prefix Syntax {5.36}
            * Scope {5.8}
            * Rendezvous {5.14, 5.16, 5.17, 5.25}
            * Buffered {5.26, 5.27, 5.28, 5.29, 5.37}
        + Client-Server Model {5.9, 5.10, 5.18, 5.19}
            * Reply Channels {5.20, 5.21}
        + Sending Channels via Channels {5.22, 5.23}
        + Sending Process IDs {5.24}
* Linear Temporal Logic (LTL) {N/A}
    - Propositional Logic {N/A}
        + Syntax {6.5, 6.6, 6.7, 6.8}
        + Semantics {6.9, 6.10, 6.11}
        + Semantic Notions {6.12, 6.13, 6.14}
        + Expressiveness {6.15, 6.16, 6.17}
    - Kripke Structure and Transition Systems {6.18, 6.19}
    - Syntax {6.21}
    - Semantics {6.22, 6.23, 6.24}
        + Validity {6.27, 6.28, 6.29}
        + Transition Systems {6.30, 6.31}
    - Safety and Liveness Properties {6.25, 6.26, 7.13}
    - Formal Languages {6.33}
        + Büchi Automaton {6.34, 6.35}
            * \(\omega\)-Regular Expressions {6.36, 6.38}
            * LTL \(\leftrightarrow\) Büchi Automaton {6.40, 6.41, 6.42, 6.43}
    - Decidability, Closure Properties {6.37}
* SPIN {3.2}
    - Model Checking {2.3, 3.4, 3.6, 3.7, 3.8, 6.45, 6.46, 6.47, 7.2}
    - Workflow {3.9, 3.10, 3.11, 3.18, 3.19, 3.20, 3.26}
        + Guided Simulation {3.21, 3.22}
        + Temporal Properties {7.15, 7.20, 7.23, 7.25, 7.26}
    - Preliminaries {7.4}
        + Acceptance Cycles {7.5}
        + Fairness {7.6, 7.24, 7.27}
    - Correctness Properties {3.12, 3.13, 7.3}
        + Assertions {3.14, 3.15, 3.16, 3.17}
        + Valid End States {3.30, 3.31, 3.32, 3.33}
        + Temporal Properties {7.7, 7.8, 7.9, 7.19}
            * Boolean Temporal Logic {7.10, 7.11, 7.12}
            * Safety Properties {7.14, 7.15}
                - Never Claims {7.16, 7.17, 7.18}
            * Liveness Properties {7.21, 7.22, 7.23, 7.25, 7.29}
            * Label Checking {7.28, 7.29}
* First-Order Logic (FOL) {8.2, 8.3}
    - Syntax {N/A}
        + Signature {8.4, 8.5, 8.6, 8.7}
        + Terms {8.8, 8.9, 8.10}
        + Atomic Formulas {8.11, 8.12, 8.13}
        + General Formulas {8.14, 8.15, 8.16}
    - Semantics {8.18, 8.19, 8.20, 8.21, 8.22, 8.23, 8.24}
        + Variable Assignments {8.25}
        + Semantic Evaluation {N/A}
            * Terms {8.26, 8.27, 8.28}
            * Formulas {8.29, 8.30, 8.31}
        + Semantic Notions {8.32}
        + Impracticality and Reasoning by Syntactic Transformation {8.33, 8.34}
    - Sequent Calculus {8.35, 8.36}
        + Rules
                - Propositional Calculus Rules {8.38}
                - First-Order Calculus Rules {8.42, 8.43, 8.44, 8.45, 8.47, 8.49, 8.50}
        + Proofing {8.39, 8.49}
            * Examples {N/A}
                - Propositional {8.40}
                - First-Order {8.46}
                - First-Order with Equality {8.48}
        + Soundness and Completeness {8.37, 8.41}
* Java Modeling Language (JML) {9.2}
    - Running Examples {N/A}
        + \texttt{ATM} {9.8}
        + \texttt{LimitedIntegerSet} {10.2, 10.3}
    - Specification {9.3, 9.4, 9.5, 9.6, 9.7}
        + Informal Specification {9.9}
        + Specification as Contract {9.10, 9.11}
        + Formal Specification {9.12}
    - Introduction to JML {9.13, 9.14, 9.15}
        + JML as Java Comments {9.16, 9.17}
    - Specification Case {9.23}
        + Public {9.18}
        + Normal Behaviour {9.19, 10.23}
        + Exceptional Behaviour {10.22, 10.23, 10.24}
            * \texttt{signals} {10.25}
            * \texttt{signals_only}  {10.26}
        + Non-Termination {10.27}
    - Preconditions {9.20, 9.21}
    - Postconditions {9.22}
    - Assignable {9.25, 9.26, 9.27}
    - Modifiers {9.29}
        + \texttt{spec_public} {9.30}
        + \texttt{pure} {9.31, 9.32}
        + \texttt{nullable}, \texttt{non_null} {10.28, 10.29, 10.30, 10.31, 10.32}
    - JML Expressions {9.33, 9.34}
        + Access of Prestate {9.24}
        + Quantifier {9.35, 9.36, 9.37, 9.38, 9.39}
        + Result Values {10.4}
    - State Constraints {10.10, 10.11, 10.12, 10.13, 10.14, 10.15}
        + Class Invariants {10.16, 10.17, 10.18, 10.19, 10.20, 10.21}
    - Inheritance {10.33}
    - Loop Invariants {14.18, 14.19}
    - Loop Termination {14.20, 14.21, 14.22}
        + Example: GCD {14.23, 14.24, 14.25, 14.26, 14.27}
* Dynamic Logic (DL) {11.2, 11.4, 11.5, 11.6, 11.10, 11.11, 11.12, 12.2, 12.37, 13.21}
    - Type Hierarchy {11.7, 11.8, 11.9, 12.17}
    - Syntax {11.15}
        + Variables {11.13, 11.14, 11.17}
        + Terms {11.18}
        + Programs {11.19}
        + Modalities {11.20}
        + Formulas {11.23, 11.24}
    - Semantics {11.25}
        + Kripke Structure {11.26, 11.27, 11.28}
        + Semantic Evaluation {N/A}
            * Formulas {11.29, 11.30}
            * Programs {11.31}
        + Sequents {12.4}
    - KeY Input File {11.16, 11.21, 11.22, 12.24}
    - Modelling {N/A}
        + Heap {12.18, 12.19, 12.20}
            * Field Updates {12.21}
            * Field Access {12.22}
            * Pretty Printing {12.23}
        + Static Fields {12.30}
        + Abrupt Termination {12.25, 12.26, 12.27}
        + Aliasing {12.28, 12.29}
        + \texttt{this} and \texttt{self} {12.31}
        + Arrays {12.33}
        + Complex Expressions {12.34}
        + Method Calls {13.4, 13.6}
            * Object Initialization {12.32, 13.7}
    - Symbolic Execution {12.5, 12.6, 14.3}
        + Rules {12.7, 12.12, 12.21, 12.35, 13.5, 13.9, 13.11, 13.15, 13.16, 13.19, 14.4, 14.5, 14.7, 14.12, 14.15}
        + Updates {12.8, 12.9, 12.10}
            * Effects {12.11}
            * Assignment Rule {12.12}
            * Composition {12.13}
            * Parallel Updates {12.14, 12.15}
            * Quantifier {12.16}
            * Keeping the Context: Anonymising {13.12, 13.13, 13.14, 14.14}
        + Abrupt Termination {12.36}
        + Complex Expressions {12.35}
        + Method Calls {13.5}
            * Limitations of Inlining {13.8}
            * Method Contract Rule {13.9, 13.10, 13.11, 13.15, 13.16}
            * Proofing Correctness of Method Contracts {13.19}
        + Loop Invariants {14.4, 14.5, 14.8}
            * Deriving Loop Invariants {14.9, 14.10, 14.11, 14.29, 14.30}
            * Context Loss {14.12, 14.14, 14.15}
    - Understanding Unclosed Proofs {13.20}
        + Model Search {14.31, 14.32, 14.33, 14.34}
