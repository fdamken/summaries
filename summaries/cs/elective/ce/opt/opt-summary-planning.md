# Opt Zusammenfassung Planung

## Foliensätze

Done/Sorted/Total: 320/541/541; 59%/100%/100%

* [X] Kapitel  1: Einführung (27)
* [X] Kapitel  2: Nichtlineare Optimierung ohne Beschränkungen (gradientenbasiert) (55)
* [X] Kapitel  3: Gradientenfreie Optimierung (66)
* [X] Kapitel  4: Nichtlineare Optimierung mit Beschränkungen (79)
* [X] Kapitel  5: Berechnung von Ableitungen (43)
* [X] Kapitel  6: Minimierung von Abweichungen (50)
* [x] Kapitel  7: Minimierung von Funktionalen (11)
* [x] Kapitel  8: Optimale Steuerung dynamischer Systeme (88)
* [x] Kapitel  9: Berechnung optimaler Trajektorien (49)
* [x] Kapitel 10: Optimale Rückkopplungssteuerung (33)
* [x] Kapitel 11: Weitere Themen (40)


## Themen (noch nicht in TeX)

* Minimierung von Funktionalen {7}
    - Einleitung {7.2, 7.3}
    - Charakteristika von Variationsproblemen {7.4}
    - Euler-Lagrangesche Differentialgleichung {7.5, 7.6, 7.9}
        + Beispiel {7.10}
        + Bemerkungen {7.11}
        + Herleitung {7.6, 7.7, 7.8, 7.9}
* Optimale steuerung dynamischer Systeme {8.1}
    - Einleitung
        + Zeitkontinuierliche Systeme {8.2, 8.3}
        + Allgemeine Problemstellung {8.4, 8.5}
    - Notwendige Bedingungen für ein Minimum des Basisproblems {8.6, 8.7, 8.8}
        + Notwendige Bedingungen erster Ordnung {8.20, 8.21, 8.22, 8.23, 8.27, 8.31}
        + Notwendige Bedingung zweiter Ordnung (Legendre-Clebsch Bedingung) {8.28, 8.31}
        + Beispiel {8.12}
        + Anwendung: Optimale Robotersteuerung {8.13}
            * Die Roboterdynamik {8.14, 8.15}
            * Optimale Steuerung {8.16, 8.17}
            * Gütekriterien {8.18}
            * Notwendige Bedingungen {8.24, 8.25, 8.26, 8.29, 8.30}
    - Bang-Bang und Singuläre Steuerung {8.32, 8.33, 8.34}
        + Singuläre Steuerung {8.35, 8.36}
            * Notwendige Bedingungen für singuläre Steuerung {8.37, 8.38}
        + Anwendung: Zeitminimale Robotersteuerung {8.39, 8.40, 8.41}
            * Eigenschaften {8.42}
        + Bemerkungen {8.43}
    - Die Wertefunktion {8.44, 8.45, 8.47, 8.51}
        + Hamilton-Jacobi-Bellman Gleichung {8.50}
            * Herleitung {8.46, 8.47, 8.48, 8.49, 8.50}
        + Bemerkungen {8.52}
    - Zustandsbeschränkungen {8.53, 8.54, 8.55}
        + Gemischte Ungleichungsbeschränkungen {8.56, 8.57}
            * Notwendige Bedingungen {8.58, 8.59, 8.60, 8.61}
        + Reine Zustandsungleichungsbeschränkungen {8.62, 8.63, 8.65}
            * Ordnung einer Zustandsbeschränkung {8.66}
            * Erweiterte Hamiltonfunktion {8.67, 8.68}
            * Maximumprinzip {8.69, 8.70, 8.71, 8.72}
            * Bemerkungen {8.73, 8.74}
        + Beispiele {8.75}
            * Optimale Robotersteuerung {8.76}
            * Energieminimierungsproblem {8.77, 8.78, 8.79, 8.80, 8.81, 8.82, 8.83, 8.84, 8.85, 8.86}
        + Zusammenfassung {8.87, 8.88}
* Berechnung optimaler Trajektorien {9.2}
    - Erste Berechnungsverfahren {9.2}
        + Dynamische Programmierung {9.3}
        + Gradientenverfahren {9.4}
    - Indirekte Verfahren {9.5, 9.6, 9.7}
    - Direkte Verfahren {9.8, 9.9, 9.10}
        + Direkte Kollokationsverfahren {9.11, 9.25}
            * Erste Diskretisierung {9.12, 9.13, 9.14}
                - Modellalgorithmus {9.15}
                - Bemerkungen {9.16}
            * Zweite Diskretisierung {9.17, 9.18}
                - Gauss- und Lobatto-Punkte {9.19, 9.20, 9.21}
                - Resultierendes NLP {9.21}
            * Diskretisierung von Ungleichungsbeschränkungen {9.22}
            * Konvergenzeigenschaften {9.30, 9.31, 9.32}
            * Validierung der berechneten Lösung {9.33}
            * Wahl der Gitterpunkte {9.36, 9.37}
                - Approximative, segmentweise Fehlerschätzung {9.38}
                - Segmentweise Fehlerschätzung bei zeitkontinuierlichen Nebenbedingungen {9.39}
                - Segmentweise Schätzung des Optimalitätsfehlers {9.40}
            * Vorgehensweise {9.41}
            * Bemerkungen {9.43}
            * Anwendung: Optimale Robotersteuerung {9.23, 9.24, 9.26, 9.27, 9.28}
            * Beispiel: Zeitminimale Robotersteuerung {9.34, 9.35}
        + Direkte Schießverfahren {9.44, 9.45, 9.46, 9.47}
    - Bemerkungen {9.48, 9.49}
* Optimale Rückkopplungssteuerung {10.1, 10.2, 10.3}
    - Feedforward Control {10.4, 10.5}
    - Sollwerttrajektorien-Folgeregelung {10.6, 10.7, 10.8, 10.9, 10.10}
    - Optimal Feedback Control {10.11, 10.12}
    - Linear-Quadratische Optimalsteuerung {10.13, 10.14}
        + Notwendige Bedingungen {10.15, 10.16, 10.17}
        + Zeitinvariante Dynamik {10.18, 10.19}
    - Benachbarte Extremalen {10.20, 10.21, 10.22}
        + Indirekte Verfahren {10.23, 10.24, 10.25, 10.26}
        + Direkte Verfahren {10.27}
        + Modellgestützte, prädiktive Regelung {10.28, 10.29}
    - Numerische Synthese der nichtlinearen Rückkopplungssteuerung {10.30, 10.31, 10.32, 10.33}
* Weitere Themen der Optimalen Steuerung {11.1}
    - Inverse Optimalsteuerung {11.2, 11.3}
    - Differentialspiele {11.4, 11.5}
        + Nichtkooperative Nullsummen-Differentialspiele {11.6, 11.7}
            * Beispiel {11.7}
        + Notwendige Bedingungen {11.8}
    - Lernverfahren und Optimierung {11.9}
        + Einleitung {11.10, 11.15, 11.17, 11.18}
        + Grundlagen {11.19, 11.20, 11.21, 11.22}
            * Formales Schema {11.23}
            * Gradien Descent {11.24}
            * (Tiefe) Neuronale Netze {11.25}
            * Grundlegende Fragen {11.26}
        + Bezüge zur (optimalen) Steuerung und Regelung {11.27, 11.28, 11.29, 11.30}
            * Bewertung der Aktionen {11.31}
            * Wertefunktion {11.32}
            * Erster Ansatz {11.33}
            * Lernen der Wertefunktion {11.34, 11.35}
            * Kombination aus Wertefunktion und optimaler Steuerung {11.36}
            * Bemerkungen {11.37}
