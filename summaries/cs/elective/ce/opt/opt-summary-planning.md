# Opt Zusammenfassung Planung

## Foliensätze

Done/Sorted/Total: 0/320/?; 0%/?%/100%

* [x] Kapitel 1: Einführung (27)
* [x] Kapitel 2: Nichtlineare Optimierung ohne Beschränkungen (gradientenbasiert) (55)
* [x] Kapitel 3: Gradientenfreie Optimierung (66)
* [x] Kapitel 4: Nichtlineare Optimierung mit Beschränkungen (79)
* [x] Kapitel 5: Berechnung von Ableitungen (43)
* [x] Kapitel 6: Minimierung von Abweichungen (50)


## Themen

* Einführung {1.5}
    - Beispiele {1.6, 1.7, 1.8, 1.10, 1.11}
    - Fragestellungen {1.12}
    - Allgemeine Formulierung eines Optimierungsproblems {1.13, 1.14}
    - Statische vs. Dynamische Optimierung {1.15, 1.16, 1.17, 1.18}
    - Klassifizierung von Optimierungsverfahren {1.23}
    - Typische Struktur {1.24}
* Gradientenbasierte Optimierung ohne Beschränkungen {2.2}
    - Charakterisierung der Lösung {2.2}
        + Eindimensionale Optimierung {2.3, 2.4, 2.5}
        + Mehrdimensionale Optimierung {2.6, 2.10}
            * placeholder
                - Beispiel {2.7, 2.8, 2.9}
    - Numerische Gradientenbasierte Verfahren {2.11}
        + Ausgangssituation {2.13}
            * Struktur gradientenbasierter Verfahren {2.14}
            * Abstiegsrichtung {2.15}
            * Algorithmische Struktur {2.16}
        + Methode des steilsten Abstiegs (Steepest Descent) {2.17}
        + Methode der konjugierten Gradienten (Conjugate Gradient) {2.18, 2.19, 2.20}
        + Newton-Verfahren {2.21, 2.22, 2.23}
            * Verfügbarkeit der zweiten Ableitungen {2.24}
        + Quasi-Newton-Verfahren {2.25, 2.26, 2.27}
            * BFGS-Aktualisierung {2.28}
        + Vergleich der Verfahren {2.29, 2.30, 2.31, 2.32, 2.33, 2.34, 2.35, 2.36, 2.37, 2.38}
    - Schrittweitenbestimmung, Liniensuche {2.39, 2.40, 2.47}
        + Charakterisierung der Lösung {2.41}
        + Übersicht und Anforderungen {2.42, 2.43}
        + Näherungsweise Liniensuche {2.44, 2.45, 2.46}
    - Vertrauensbereichsverfahren (Trust Region Methods) {2.48, 2.49, 2.50}
    - Konvergenzraten {2.51, 2.52, 2.53, 2.54}
        + Gradientenbasierte Verfahren {2.55}
* Gradientenfreie Optimierung ohne Beschränkungen {3.1, 3.2}
    - Einleitung
        + Historische Entwicklung {3.3}
        + Problemstellung {3.4}
        + Simulationsbasierte Optimierung {3.5, 3.6, 3.7, 3.8}
        + Black-Box Optimierung {3.9}
    - Metaheuristiken {3.10}
        + Evolutionäre Algorithmen (EA) {3.11}
        + Genetische Algorithmen (GA) {3.12}
            * placeholder
                - Beispiel {3.13, 3.14}
        + Weitere Metaheursitiken {3.15}
    - Deterministische Sampling Verfahren (Mustersuchverfahren) {3.16, 3.17}
        + Nelder-Mead Simplexverfahren {3.18, 3.26, 3.27}
            * Iterationsphase {3.19, 3.20}
            * Algorithmus {3.21, 3.22, 3.23}
        + Multidirektionales Suchverfahren (MDS) {3.28}
        + Asynchronous Parallel Pattern Search (APPS) {3.29, 3.30, 3.31}
            * placeholder
                - Beispiel {3.32, 3.33, 3.34}
        + Implizites Filtern {3.35, 3.36, 3.37, 3.38}
    - Optimierung mit Ersatzfunktionen {3.39, 3.40, 3.41}
        + Approximationsmethoden {3.42}
            * Response Surface Methoden (RSM) {3.43}
            * Radial Basis FUnctions (RBF) {3.44}
            * Design and Analysis of Computer Experiments (DACE) {3.45}
        + Auswahl der Stützstellen/Datenbasis/Anfangswerte {3.46}
            * Design of Experiments (DoE) {3.47}
        + Minimierung der Ersatzfunktion {3.48}
            * Optimierung am Ersatzproblem {3.49}
                - Strawman {3.48}
                - Shoemaker {3.48}
                - DACE-basierte, sequentielle Update-Strategien {3.50}
        + Diskussion {3.54}
    - Vergleich der Verfahren {3.55}
        + Design eines Magnetlagers {3.56, 3.57, 3.58, 3.59, 3.60, 3.61}
        + Laufoptimierung eines Humanoidroboters {3.62, 3.63}
    - Diskussion {3.65, 3.66}
* Gradientenbasierte Optimierung mit Beschränkungen {4.1, 4.2, 4.3, 4.4, 4.5}
    - Charakterisierung der Lösung {4.6}
        + Motivation {4.7, 4.8}
        + Lagrange-Funktion {4.9}
        + Notwendige Optimalitätsbedingungen 1. Ordnung (Karush-Kuhn-Tucker, KKT) {4.10}
        + Notwendige Optimalitätsbedingungen 2. Ordnung {4.12}
        + Beispiel {4.11, 4.13}
    - Einfache Schranken {4.14, 4.15, 4.16, 4.17}
    - Straffunktionsverfahren {4.18, 4.19}
        + Äußere Straffunktionsverfahren {4.20, 4.21}
            * placeholder
                - Beispiel {4.22, 4.23}
        + Innere Straffunktionsverfahren {4.24, 4.25}
            * placeholder
                - Beispiel {4.26}
        + Exakte Straffunktionen {4.27}
            * placeholder
                - Beispiel 1 {4.28}
                - Beispiel 2 {4.29}
        + Erweiterte Lagrange-Funktion {4.30}
            * placeholder
                - Beispiel 1 {4.31, 4.32}
                - Beispiel 2 {4.33}
            * Eigenschaften {4.34, 4.35}
    - Elimination von Beschränkungen {4.36, 4.37, 4.41}
        + placeholder
            * placeholder
                - Beispiel 1 {4.38}
                - Beispiel 2 {4.39}
                - Beispiel 3 {4.40}
    - Verfahren der Sequentiellen Quadratischen Optimierung (SQP) {4.42}
        + Einleitung {4.43, 4.44}
        + Bestimmung der Suchrichtung {4.45, 4.46, 4.47}
            * Quadratisches Problem (QP) {4.48}
        + Bestimmung der Schrittweite {4.50}
        + Approximation der Lagrange-Multiplikatoren {4.52}
        + Terminierungskriterien {4.54, 4.55}
        + Approximation der Hesse-Matrix {4.58, 4.59}
            * Naiver Ansatz {4.60}
            * Reduzierte Hesse-Matrix {4.61, 4.63, 4.64, 4.65, 4.66, 4.67, 4.68}
                - Beispiel {4.62}
            * Approximation der reduzierten Hesse-Matrix {4.69}
        + SQP-Verfahren {4.52, 4.53, 4.57, 4.75}
        + Bemerkungen {4.49, 4.70, 4.75, 4.76, 4.77, 4.78, 4.79}
        + Beispiele {N/A}
            * Optimale Steuerung eines 6-gelenkigen Industrieroboters {4.71, 4.72}
            * PKW-Fahrt {4.73, 4.74}
* Berechnung von Ableitungen {5.1, 5.2, 5.3, 5.4}
    - Finite-Differenzen-Approximation (numerische Differentiation) {5.5}
        + Vorwärtsdifferenzen-Approximation {5.6, 5.13}
            * Fehler {5.8, 5.12}
                - Approximationsfehler {5.9}
                - Funktionsgenauigkeit {5.10}
                - Rundungsfehler {5.11}
            * Wahl der Schrittweite {5.14, 5.15, 5.16, 5.17}
        + Zentrale-Differenzen-Approximation {5.18, 5.19, 5.21, 5.22}
    - Numerische Differentiation von Simulationsmodellen {5.23, 5.24, 5.25}
        + Ableitung von ODE-Simulationsmodellen {5.27, 5.28}
        + Externe numerische Differentiation {N/A}
            * Naiver Ansatz {5.29, 5.30, 5.31}
            * Gekoppelte Vorwärtsdifferenzen-Approximation {5.32}
        + Interne numerische Differentiation {5.33, 5.34}
    - Symbolische Differentiation {5.35, 5.36}
    - Automatisches Differenzieren {5.37, 5.38, 5.39, 5.40}
        + placeholder
            * placeholder
                - Beispiel {5.41, 5.42, 5.43}
* Minimierung von Abweichungen {6.1, 6.2, 6.3}
    - Parameterschätzung bei ODE-Systemen {6.5, 6.7}
    - Gütekriterien zur Minimierung von Abweichungen {6.8, 6.9}
    - Lineare Ausgleichsrechnung {6.10, 6.11}
    - Optimalitätsbedingungen und Spezialverfahren {6.12, 6.13, 6.17}
        + Quasi-Newton {6.14}
        + Gauß-Newton Verfahren {6.15}
        + Levenberg-Marquardt Verfahren {6.16}
        + SQP-Verfahren {6.18}
    - Normalen-Gleichungen {6.22, 6.23}
        + placeholder
            * placeholder
                - Beispiel {6.24, 6.25, 6.26, 6.27, 6.28}
    - Interpretation von Berechnungsergebnissen {6.29}
        + Mögliche Ursachen für Schwierigkeiten {6.30, 6.31}
    - Die Varianz-Kovarianz-Matrix {6.32, 6.33, 6.34}
    - Optimale Experimentgestaltung {6.35, 6.36, 6.37}
    - Beispiele {6.39}
        + Parameterabhängige Gesamtfahrzeugdynamik {6.39, 6.40}
            * Simulierte Messwerte {6.41, 6.42, 6.43}
            * Echte Messwerte {6.44}
            * Vergleich der Verfahren {6.45}
        + Parameterschätzung für "BioBiped" {6.47, 6.48, 6.49}
