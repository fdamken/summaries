# CER Cheatsheet :: Planung

## Foliensätze

* [x] Kapitel 1: Einführung
* [x] Kapitel 2: Modellierung und Simulation mit nichtlinearen Gleichungsmodellen
* [x] Kapitel 3: Grundlagen zeitkontinuierlicher Modelle
* [x] Kapitel 4: Grundlagen der numerischen Simulation
* [x] Kapitel 5: Numerische Simulation zeitkontinuierliche Modelle
* [x] Kapitel 6: Teilschritte einer Simulationsstudie
* [x] Kapitel 7: Interpretation und Validierung
* [x] Kapitel 8: Identifikation von Modellen
* [x] Kapitel 9: Physikikalisch basierte Spiele
* [x] Kapitel 10: Simulation autonomer Roboter
* [ ] Kapitel 11: Beispiele aus der Forschung (Klausurrelevant?)
* [x] Kapitel 12: Klausurinformationen



## Themen

* Einführung {1}
    - Beispiele {1.11, 1.12, 1.13, 1.14, 1.15}
    - Was ist ein Roboter? {1.17, 1.18}
        + Funktionale Anforderungen {1.24, 1.25}
    - Was ist Robotik? {1.19, 1.20}
    - Typischer Aufbau eines Roboterarms/-beins {1.21, 2.9}
    - Begriffe {1.28}
        + Simulation {1.29, 1.30}
        + Modell {1.31, 1.32, 1.33}
    - Aufgaben einer Simulation {1.51}
- Mathematische Grundlagen und Notation {2.15}
    + Vektoren {2.16}
    + Matrizen {2.17, 2.18, 2.19, 2.20}
    + Koordinatensysteme {2.21}
    + Positionsvektor eines Punktes {2.22}
    + Räumliche Anordnung eines Objektes {2.23, 2.24}
    + Klassische Transformationsbeziehungen {2.25}
    + Homogene Transformationsbeziehungen {2.26}
    + Lösungsansätze für mathematische Modelle {1.61, 1.62}
    + Numerik { }
        * Lösung nichtlinearer Gleichungsmodelle {2.53}
            - Fixpunktiteration {2.55, 2.56, 2.57}
                + Iterationsvorschrift {2.55}
                + Konvergenzhilfe: Relaxationsmatrix {2.59}
                + Optimale Relaxationsmatrix {2.61}
            - Newton-Verfahren {2.62, 2.63, 2.64, 2.65}
                + Iterationsvorschrift {2.67, 2.69}
                + Newton <--> FPI {2.66}
                + Konvergenz {2.71, 2.72}
                + Praxis: Schrittweitensteuerung {2.73}
                + Praxis: Jacobi-Matrix {2.74, 2.75}
            - Vergleich Newton <--> FPI {2.76}
        * Weiter: Siehe Kapitel "Numerische Simulation" { }
        * Weiter: Siehe Kapitel "Numerische Simulation zeitkontinuierlicher Modelle" { }
    + Differentialgleichungen { }
        * Transformation auf System 1. Ordnung {3.13}
        * Autonomisierung nichtautonomer DGLS {3.14}
        * Lösbarkeit {3.17, 3.18}
            - Satz von Picard-Lindelöff {3.19}
        * Gleichgewichtslösungen {3.20, 3.21}
        * Linearisierung um die Ruhelage {3.42, 3.46, 3.47, 3.48}
        * Lösung von \( (\Delta x)' = A \cdot \Delta x' \) {3.50, 3.51, 3.52, 3.103, 3.104}
        * Stabilität {3.55, 3.56, 3.57, 3.58}
        * Steife DGL {3.107}
        * Unstetige rechte Seite {3.108}
* Modellung und Simulation mit nichtlinearen Gleichungsmodellen {2}
    - System und Modell: Notation {2.3, 2.4}
    - Explizite vs. Implizite Gleichungsmodelle {2.5}
    - Vorwärts-/Rückwärtsmodell {2.6}
    - Beispiel: Schiffsschaukel {2.7}
    - Aufbau von Roboterarmen/-beinen {2.10}
        + Koordinatensysteme {2.12, 2.13}
    - Explizite Gleichungsmodelle {2.8, 2.41}
    - Implizite Gleichungsmodelle {2.43, 2.44}
        + Jacobi-Matrix {2.46}
            * Beispiele {2.48, 2.49}
            * Numerische Approximation {2.50, 2.51, 2.52}
    - Vorwärtskinematikmodell {2.11, 2.28, 2.29, 2.34, 2.40}
        + DH-Konvention {2.30, 2.31, 2.32}
        + Homogene Transformation {2.33}
    - Inverses Kinematikmodell {2.36, 2.42, 2.81}
        + Beispiel: Analytische Lösung {2.37}
        + Numerische Lösung {2.77}
        + Besonderheiten {2.78, 2.79}
        + Berechnung {2.80}
* Zeitkontinuierliche Modelle {3}
    - Örtlich konzentrierter Systemzustand {3.3}
        + Beispiel: Linearer Schwinger {3.4, 3.5, 3.6}
    - Örtlich verteilter Systemzustand {3.7}
    - Beschreibung zeitkontinuierlicher Systeme {3.8}
        + System und Modell: Notation {3.9}
        + Beispiele {3.10}
        + Allgemeine Zustandsgleichung, Allgemeines Zustandsraummodell {3.11, 3.12, 3.102}
            * Zeitcharaktersitik {3.105, 3.106}
        + Lineare/Nichtlineare Systemdynamik {3.15}
        + Blockmodelle {3.16}
    - Gleichgewichtslösungen
        + Lineare/Nichtlineare Systemdynamik {3.23}
        + Beispiel: Linearer Schwinger {3.24}
        + Beispiel: Chemischer Reaktor {3.28, 3.29, 3.30, 3.31}
        + Beispiel: Inverses Pendel {3.32, 3.33, 3.34, 3.35}
        + Modellbildung eines Pendels {3.36, 3.37, 3.38, 3.39, 3.41}
        + Modellbildung eines invertierten Pendels {3.40}
    - Linearisierung um die Ruhelage {3.42, 3.43}
        + Beispiele {3.44, 3.45}
    - Stabilität {3.49}
        + Beispiel: Schwingung einer Masse an einer Feder {3.53, 3.54}
        + Beispiel: Wettrüsten {3.61, 3.62, 3.63, 3.64, 3.65, 3.66}
    - Regelung {3.68, 3.69, 3.70, 3.71}
        + Steuerung und Regelung {3.72, 3.73}
        + Regelung {3.74, 3.77, 3.75, 3.76}
    - Regelung Steuerung
        + Lineare Systemdynamik {3.79}
        + Untersuchung des Bewegungsverhaltens {3.80}
        + Erwartetes Bewegungsverhalten {3.81}
        + Berechnung des Bewegungsverhaltens {3.82, 3.83, 3.84, 3.85}
        + Gewünschtes Bewegungsverhalten {3.86, 3.87}
        + PD-Regelung {3.88, 3.89, 3.90, 3.91}
        + PID-Regelung (eines Servomotors) {3.93, 3.94}
        + PD-Kaskadenregelung {3.95}
* Numerische Simulation {4, 4.27}
    - Zahlendarstellung {4.32, …, 4.42}
    - Rundungsfehler {4.2, 4.5, 4.6}
        + Beispiel: Addition {4.3}
        + Beispiel: Multiplikation {4.4}
    - Fortpflanzung von Rundungsfehlern {4.10, 4.11}
        + Jacobi-Matrix {4.14, 4.15, 4.16}
        + Beispiel: Kosinus {4.12}
        + Beispiel: Ableitung {4.13}
    - Kondition {4.19, 4.20, 4.21, 4.27}
        + Beispiele {4.22}
    - Numerische Stabilität {4.23, 4.25}
        + Beispiele {4.24, 4.26}
* Numerische Simulation zeitkontinuierlicher Modelle {5}
    - Verschiedene Dynamikmodelltypen {5.5}
    - Numerische Integration {5.6, 5.7, 5.32}
        + Einschrittverfahren {5.13, 5.14}
            * Fehler {5.15, 5.16, 5.17}
        + Explizites Euler-Verfahren {5.9, 5.10, 5.11}
        + Implizites Euler-Verfahren {5.18, 5.19}
        + Heun-Verfahren {5.20}
        + Runge-Kutta-Verfahren 4. Ordnung {5.21, 5.22}
        + Anmerkungen {5.23}
    - Schrittweitensteuerung {5.24, 5.25, 5.26}
    - Integration steifer Differentialgleichungen {5.28, 5.29}
        + Beispiel {5.30, 5.31}
    - Integration von Zustands-DGLen mit Unstetigkeiten {5.35, 5.36}
        + Ursachen für Unstetigkeiten {5.37, 5.38}
        + Beispiel: Einfache Hysterese {5.39}
        + Schaltfunktionen {5.40}
            * Vorgehensweise {5.43}
            * Beispiel: Schwinger mit Schaltstellen {5.41, 5.42}
        + Anmerkungen {5.44}
* Teilschritte einer Simulationsstudie {6, 6.2, 6.5, 6.15, 6.30, 6.33, 1.63}
    - Problemspezifikation {1.38, 1.39}
    - Modellierung {1.41, 1.42}
        + Herleitung von Modellen {1.43, 1.44, 1.45}
            * Beziehungsgeflecht von Einflussgrößen {1.46}
            * Instrumentarien zur Beschreibung von Beziehungen {1.47, 1.48, 1.49}
            * Simulationsaufgabe {1.50}
        + Zustandsvariablen eines Modells {1.55}
        + Klassifikation der Zustandsänderungen {1.59}
    - Implementierung { }
        + Klassifikation zeitkontinuierlicher Simulationswerkzeuge {6.21, 6.22, 6.23}
    - Anwendung {6.34}
    - Beispiel: Schiffsschaukel { }
        + Problemspezifikation {6.4, 1.57, 1.58}
        + Modellierung {6.6, 6.7, 6.8, 6.9, 6.10, 6.11, 6.12, 6.13, 1.55, 1.56}
        + Implementierung {6.16, 6.17, 6.18, 6.19, 6.20, 6.24, 6.25, 6.26, 6.27, 6.28}
* Validierung {7, 7.3}
    - Fehlerquellen {7.4, 7.13}
    - Begriffe und Definitionen {7.6, 7.7, 7.12}
    - Vorgehensweise {7.14}
        + Validierung der Implementierung {7.15}
        + Validierung des Modells {7.16}
        + Validierung des Berechnungsverfahrens {7.17}
        + Tests auf Plausibilität und Konsistenz {7.18, 7.19}
* Identifikation von Modellen {8}
    - Systemidentifikation {8.1, 8.2, 8.3}
        + Unterarten {8.4, 8.5}
        + Hauptschritte der Systemidentifikation {8.6}
    - Parameteridentifikation {8.8, 8.9, 8.10, 8.11}
        + Gütekriterien {8.12, 8.13}
            * Nichtlineare, kleinste Quadrate {8.14}
        + Kalibrierung {8.19, 8.20}
* Physikalisch basierte Spiele {9}
    - Definition {9.5, 9.6}
    - Game Loop {9.7}
    - Game Engine {9.8}
    - Physics & Collision Engine {9.9, 9.10, 9.11}
    - Modellierung eines Objektes {9.12}
    - Kontake, Kollisionen, Kräfte und Impulse {9.13, 9.14}
* Simulation autonomer Roboter {10, 10.2}
    - Problemspezifikation {10.4}
    - Robotersimulation: Darmstadt Dribblers {10.7, 11.8}
