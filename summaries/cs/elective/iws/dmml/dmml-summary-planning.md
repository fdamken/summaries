# DMML Zusammenfassung :: Planung

## Folien

Fertig/Strukturiert/Gesamt: 213/544/544; 39%/100%/100%

* [X] Kapitel 1: Einleitung (104)
* [X] Kapitel 2: kNN, Überanpassung, Kreuzvalidierung und Datenanalyse-Zyklus (63)
* [X] Kapitel 3: Modellselektion und Evaluierung (45)
* [x] Kapitel 4: Baumbasierte Verfahren (45)
* [x] Kapitel 5: Ensemble Methoden (52)
* [x] Kapitel 6: Probabilistische Graphische Modelle, Stützvektormethode und Clustering (94)
* [x] Kapitel 7: Deep Learning; Faltende Neuronale Netzwerke (70)
* [x] Kapitel 8: Deep Learning; Trainieren von faltenden Neuronalen Netzwerken (41)
* [x] Kapitel 9: Apriori und Page Rank (30)


## Struktur

* Einleitung {1.1, 1.2, 1.3, 1.4}
    - Was ist Künstliche Intelligenz? {1.5, 1.6, 1.7, 1.8, 1.9, 1.10, 1.11, 1.12, 1.13, 1.14, 1.15, 1.16}
    - Was ist ein Algorithmus {1.17, 1.18, 1.19}
    - Maschinelles Lernen {1.20, 1.21, 1.22}
    - Geschichte {1.23, 1.24, 1.25, 1.26, 1.46, 1.47, 1.48, 1.49, 1.50, 1.51, 1.52, 1.53}
        + Das Perzeptron {1.27, 1.44, 1.45}
            * Aufbau {1.28, 1.29, 1.30, 1.31, 1.32, 1.33, 1.34, 1.35, 1.36}
            * Lernalgorithmus {1.37, 1.38, 1.39, 1.40, 1.41, 1.42}
            * Mehrschichtige Netzwerke {1.43}
    - KI Heute {1.54, 1.55, 1.56, 1.57, 1.58, 1.59, 1.60, 1.61, 1.62, 1.63, 1.64, 1.65, 1.79}
    - Was ist Maschinelles Lernen? {1.80, 1.81, 1.82, 1.83, 1.84, 1.85, 1.92}
        + Kurzgefasst {1.86, 1.87, 1.88, 1.89}
        + Arten des Maschinellen Lernens {1.90, 1.91}
    - Ausblick {1.93, 1.94, 1.95}
* Grundlagen {N/A}
    - CRISP: Verlaufsmodell der Wissensentdeckung {2.25, 2.26}
    - Klassifikation und Regression {2.31, 2.32, 2.33, 2.34}
    - Statistik {N/A}
        + Erwartungswert, 2.24, 3.12, 3.13 {2.49, 2.50, 2.51, 2.52}
        + Bias {2.53, 2.54}
        + Normalverteilung {3.6}
        + Bayes-Statistik {3.14}
        + Bedingte Wahrscheinlichkeiten {4.11}
        + Konfidenzintervalle {4.26}
* k-Nächste Nachbarn (kNN) {2.2, 2.3, 2.7, 2.8, 2.9}
    - Globale und Lokale Modelle {2.2}
    - Beispiel {2.4, 2.5}
    - Ähnlichkeitsmaße {2.6, 2.10, 2.11}
    - Auswahlfunktion {2.12}
    - Überanpassung {2.13, 2.14}
    - Asymptotische Ergebnisse und Fluch der hohen Dimension {2.15, 2.16, 2.17}
* Lineare Modelle und Funktionsapproximation {2.63, 3.2, 3.3, 3.4, 3.24}
    - Lineare Modelle {2.28, 2.30, 2.37, 2.38, 2.39, 2.47}
        + Modell-Anpassung {2.42, 2.43, 2.44, 2.45, 2.46}
    - Fehler {2.48, 2.55, 2.56}
        + Bias und Varianz {2.57, 2.58, 2.59, 2.60}
    - Gütekriterien {N/A}
        + Maximum Likelihood {3.5}
            * Maximum Likelihood für Lineare Modelle {3.7, 3.8}
        + Kreuzentropie {3.9}
    - Fluch der hohen Dimension {2.61}
    - Logistische Regression {3.36, 3.37}
* Modellselektion und Evaluierung {2.18, 2.19, 2.20, 3.1, 3.2, 3.10, 3.11}
    - Aufteilung in Test- und Trainingsmenge {2.21, 2.22, 2.23}
        + Kreuzvalidierung {2.24, 3.12, 3.13}
    - Bayes'sche Modellselektion {3.15}
        + Approximation der A-Posteriori Wahrscheinlichkeit {3.16}
        + Bayes Information Criterion (BIC) {3.17, 3.18}
        + Minimum Description Length (MDL) {3.19, 3.20, 3.21, 3.22}
        + Zusammenhang zwischen BIC und MDL {3.23}
    - Evaluierungsmaße {3.25, 3.26, 3.27, 3.28}
        + ROC-Analyse und -Kurve {3.38, 3.39, 3.40, 3.41, 3.42}
        + Präzision und Recall {3.43, 3.44}
        + F-Measure, Breakeven Point {3.45}
    - Zusammenfassung von Experimentellen Ergebnissen {3.29, 3.30}
        + Vorzeichen-Test {3.31, 3.32, 3.33, 3.34}
* Baumbasierte Verfahren {4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.45}
    - Information und Informationsgewinn {4.12}
        + Numerische Werte {4.15}
    - Top-Down Induction of Decision Trees (TDIDT): ID3 {4.21, 4.22}
    - Stutzen (Pruning) des Baumes {4.23, 4.24, 4.25}
        + Fehlerschätzung {4.27, 4.28, 4.29, 4.30, 4.31}
        + Anwendung zum Stutzen {4.32}
    - Andere Gütemaße {N/A}
        + Gini-Index {4.33, 4.34}
        + Regression {4.35}
    - Evaluierung {4.36, 4.37, 4.38}
        + Fehlergewichtung {4.39}
* Ensemble-Methoden {5.1, 5.2, 5.3, 5.4, 5.52}
    - Zufallswälder (Random Forests) {5.5, 5.6, 5.7, 5.8, 5.9, 5.10, 5.11, 5.12, 5.13, 5.14}
    - Bagging {5.22, 5.23}
    - Boosting {5.25, 5.26, 5.27, 5.28, 5.29, 5.35, 5.38, 5.39}
        + AdaBoost {5.30, 5.31, 5.32, 5.33, 5.34}
    - Vergleich {5.40}
    - Gradient Boosting {5.41, 5.42, 5.43, 5.44, 5.45, 5.46}
* Probabilistische Graphische Modelle und Stützvektormethode {6.1, 6.23, 6.34}
    - Naive Bayes Klassifikator {6.2, 6.13, 6.15, 6.16, 6.17, 6.18, 6.19, 6.20, 6.21, 6.22}
        + Beispiel {6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 6.10, 6.11, 6.14}
    - Bayes'sche Netzwerke {6.24, 6.25, 6.26, 6.27, 6.28}
    - Parameterschätzung bei Vollständigen Daten: Maximum Likelihood {6.29, 6.30}
    - Parameterschätzung bei Unvollständigen Daten: Expectation Maximization (EM) {6.31, 6.32, 6.33}
    - Diskriminative Ansätze {6.35, 6.36, 6.37, 6.40}
        + Stützvektormethode {6.42, 6.43, 6.44, 6.45, 6.51, 6.52, 6.62}
            * Optimalität der Hyperebene {6.53, 6.54, 6.55, 6.56}
            * Optimierungsproblem {6.57, 6.58, 6.59, 6.60, 6.61, 6.63}
        + Nicht linear trennbare Daten {6.64, 6.65, 6.69}
            * Transformation in ein lineares Problem {6.66, 6.67}
            * Kernel-Trick {6.68}
* Clustering {6.70, 6.71, 6.72, 6.81, 6.94}
    - Dendrogramme und Hierarchisches Clustering (Agglomerativ/Aufteilend) {6.73, 6.74, 6.75, 6.76, 6.77}
    - (Vorgetäuschte) Strukturen, Anzahl Cluster und Ausreißer {6.78, 6.79, 6.80}
    - Partitionierung und K-Means {6.83, 6.84, 6.89, 6.90, 6.91, 6.92, 6.93}
* Deep Learning und Faltende Neuronale Netzwerke {7.1, 7.5, 7.6, 7.7, 7.67, 7.68, 7.69, 8.41}
    - Modellierung eines Neurons {7.8, 7.12, 7.53}
    - Aufeinanderschichten von Einheiten {7.14}
    - Faltungsschichten {7.19, 7.20, 7.21, 7.22, 7.23, 7.24, 7.25, 7.26, 7.27, 7.49, 7.50}
        + Räumliche Auflösung, Stride und Zero-Padding {7.29, 7.30, 7.31, 7.32, 7.33, 7.34, 7.35, 7.36, 7.37, 7.38, 7.39, 7.40, 7.41, 7.42, 7.43, 7.44, 7.45, 7.46, 7.47, 7.48}
    - Räumliche Zusammenfassung {7.55, 7.56, 7.57}
    - Vollständig verbundene Schichten {7.59, 7.60, 7.61}
    - Training {8.7}
        + Stochastic Gradient Descent {7.12, 7.13, 7.15, 7.16, 7.17, 7.63, 8.9, 8.10, 8.21, 8.22}
        + Backpropagation {7.18, 8.11}
            * Sequential Brick {8.12}
            * Loss Bricks {8.13, 8.14}
            * Linear Brick {8.15}
            * Activation Function Bricks {8.16, 8.17}
                - Subgradienten {8.18}
                - Leaky ReLU {8.19}
    - Vermeidung von Überanpassung {8.23}
        + Dropout {8.24, 8.25, 8.26}
        + Datenaugmentierung {8.27}
    - Fine-Tuning und Transfer Learning {8.28, 8.29, 8.30}
    - Visualisierung {8.31, 8.32, 8.33, 8.34, 8.35, 8.36, 8.37, 8.38}
        + Täuschen von CNNs {8.39, 8.40}
    - Beispiele: LeNet-5, AlexNet, GoogLeNet {7.64, 7.65, 7.66, 8.2, 8.3, 8.4, 8.5, 8.6}
* Data Mining: Apriori und PageRank {9.1, 9.2, 9.3, 9.18}
    - Assoziationsregeln {9.4, 9.5, 9.8, 9.9, 9.10}
        + Binäre Datenbanken {9.6, 9.7}
    - Apriori Algorithmus {9.11, 9.14, 9.15, 9.16, 9.17, 9.19}
    - Regelbewertung {9.20, 9.21, 9.22, 9.23}
    - Web Mining {9.24, 9.25}
        + Ranking von Webseiten {9.26}
        + PageRank {9.27, 9.28, 9.29, 9.30}
