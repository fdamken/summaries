# InfMan NLP Cheatsheet :: Planning

## Slides

* [x] Kapitel 11: Introduction
* [x] Kapitel 12: Natural Language Text
* [x] Kapitel 13: Linguistic Preprocessing
* [x] Kapitel 14, 15: Text Corpora, Lexical Resources and Knowledge Bases
* [x] Kapitel 16: Information Retrieval
* [x] Kapitel 17, 18: Information Extraction and Automatic Classification
* [x] Kapitel 19: Ausblick



## Themen

* Introduction {11, 11.4}
    - Language and Knowledge Processing {11.5, 11.6}
        + Implicit Information {11.7}
        + Recommender Systems {11.8}
        + Text- and Data-Mining {11.9}
        + Machine Learning (ML) {11.10}
        + Document Classification {11.11}
        + Machine Translation (MT) {11.13}
        + Speech Processing {11.16, 11.17}
        + Information Retrieval (IR) {11.18}
        + Information Extraction (IE) {11.19}
        + Question Answering {11.20}
        + Automatic Summorization {11.21}
        + Sentiment Analysis and Opinion-Mining {11.22}
        + Intelligent Computer-Assisted Language Learning (ICALL) {11.23}
    - Major Scientific Challenges {11.24}
        + Ambiguity {11.25}
        + Underspecification and Vagueness {11.26}
        + Complexity and Search Space {11.27}
        + Subjectivity {11.28}
        + Scientific Data {11.29}
        + System Evaluation {11.30}
* Natural Language Text {12.1, 12.3}
    - Scripts and Language {12.4}
    - Properties of Text {12.5}
        + Structure {12.6}
    - Examples of electronic Text Formats {12.7}
        + Text in relational Databases {12.8}
    - Character Encoding {12.9, 12.11, 12.13}
        + Encoding Issues in Software and Databases {12.22, 12.23}
            * Sorting {12.24, 12.25, 12.26}
            * Collation Framework {12.27}
        + Examples {-}
            * ASCII {12.10}
            * 8-Bit Encoding {12.12}
            * Unicode {12.14, 12.15, 12.16, 12.17}
            * UTF-32/UCS-4 {12.18}
            * UCS-2 {12.19}
            * UTF-16 {12.20}
            * UTF-8 {12.21}
* Linguistic Preprocessing {13}
    - Segmention {13.3, 13.4}
        + Tokenization {13.5, 13.6}
            * Amgiguity {13.7, 13.8, 13.9}
        + Segmention in other Languages {13.10}
        + Software {13.11}
    - Morphology {13.12, 13.13, 13.14, 13.15}
        + Definition {13.16}
        + Bases and Affixes {13.17}
            * Types of Affixes {13.18}
        + Classification of Morphemes {13.19}
            * Morphological Analysis {13.20}
        + Word Formation {13.21}
            * Decompounding {13.22}
        + Morphology in other Languages {13.23}
        + Morphological Normalization {13.24}
            * Stemming {13.25, 13.26}
                - Errors {13.27}
                - Ambiguity {13.28}
            * Lemmatization {13.29}
            * Stemming vs. Lemmatization {13.30}
            * Morphological Analysis {13.31}
        + Software {13.32}
    - Syntax {13.33, 13.34}
        + Part of Speech Tagging (POS Tagging) {13.35}
            * Parts of Speech {13.36, 13.39}
                - Tagsets {-}
                    + Penn-Treebank Tagset {13.37}
                    + Stuttgart-Tübingen Tagset {13.38}
                - Ambiguity {13.41}
            * Approaches to  POS Tagging {13.42}
            * Software {13.43}
        + Parsing {13.44}
            * Phrase Structure Grammars {13.45}
            * Constituent {13.45}
            * Phrase Types {13.46}
                - Head and Modifier {13.47}
            * Phare Parsing {13.48}
                - Parse Tree {13.49}
                - Alternative Notations {13.50}
            * Context-Free Grammars {13.51, 13.52}
            * Syntactical Ambiguity {15.54, 13.55, 13.56}
            * Dependency Grammar {13.57}
            * Software {13.59}
        + Semantic {13.60, 13.61}
            * Meaning {13.62}
            * Intension und Extension {13.63}
            * Ambiguity {-}
                - Lexical Ambiguity {13.64}
                - Syntactical Ambiguity {13.65}
                - Syntactical and Lexical Ambiguity {13.66, 13.67}
            * Word Sense Disambiguation {13.68}
* Text Corpora, Lexical Resources and Knowledge Bases {14, (15)}
    - Text Corpora {14.3, 14.4, 14.5, 14.17}
        + Parameter {14.6}
        + Content of a Corpus {-}
            * Corpus Annotation {14.7}
                - Word-Based Annotations {14.8}
            * Frequencies {14.18, 14.19, 14.20, 14.21}
        + Corpus Creation {14.12}
            * Storing Annotations {14.13}
            * Relational Databases {14.14}
        + Corpus Query Languages {14.23}
        + Example Corpora {-}
            * Brown Corpus: POS Tagged Text {14.9}
            * Treebanks: Penn Treebank {14.10}
            * Learner Copurs ICLE {14.11}
            * XML Corpora: British National Corpus {14.15}
            * Getting Corpora {14.16}
    - Lexical Resources and Knowledge Bases {14.24, 14.25}
        + Lexical Resources \( \leftrightarrow \) Corpora {14.26}
        + Problematics {-}
            * Meaning {14.28}
            * Lexical Ambiguity vs. Synonymy {14.29}
        + Relation Types {14.33}
        + Wordnets {14.30, 14.31, 14.32}
        + Syntactic Resources, Semantic Resources {14.34}
* Information Retrieval {16}
    - Overview {16.3, 16.4}
        + Basic Concepts {16.5}
        + Classic Search Model {16.6}
        + IR Engine vs. DBMS {16.8}
        + Core Challenges in IR {16.9}
        + IR Activities {16.10}
            * Indexing {16.11}
    - Boolean Retrieval {16.12, 16.13}
        + Term-Document Matrix {16.14}
            * Boolean Search {16.15}
            * Scaling {16.16, 16.17}
            * Inverted Index {16.18, 16.19, 16.20}
    - Vector Space Model {16.21}
        + Boolean Search Issues {16.22}
        + Ranked Retrieval {16.23}
            * Time-Document Matrix Weights {-}
                - Binary {16.24}
                - Frequencies {16.25}
        + Set of Words, Bag of Words {16.26}
        + Vector Space Model (VSM) {16.27, 16.28}
        + Keyword-based Search {16.29}
        + Vector Similarity {16.30}
            * Euler Similarity {16.31}
            * Cosine Similarity {16.32, 16.33}
        + Vector Weights {-}
            * Binary {16.34}
            * Term Frequencies {16.35}
            * Normalized Term Frequencies {16.36}
            * Document Frequency {16.37}
            * Inverse Document Frequency {16.38}
            * TF.IDF {16.40}
        + VSM Retrieval {16.43, 16.44, 16.45, 16.46, 16.47}
    - Information Retrieval Evaluation {16.49, 16.50}
        + Precision and Recall {16.50, 16.51}
        + Error Types {16.52}
        + Error Types vs. Precision/Recall {16.53}
        + Confusion Matrix {16.54}
        + \( F _ 1 \) Score {16.55}
        + Cutoff and Precision at Rank {16.56}
* Information Extraction and Classification {17, (18)}
    - Information Extraction (IE) {17.3}
        + IE vs. IR {17.5, 17.6}
    - Entity Recognition {-}
        + Entity Types {17.7}
        + Challanges {17.8, 17.9}
        + Approaches {-}
            * List Lookup {17.10}
            * Rule-bases Methods {17.11, 17.12}
    - Supervised vs. Probabilistic Machine Learning {17.13, 17.14, 17.15}
