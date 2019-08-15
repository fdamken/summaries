# Mathe 3 Zusammenfassung (Statistik, Stochastik) :: Planung

## Foliensätze

- [x] Kapitel 7: Statistik
- [x] Kapitel 8: Schätzer
- [x] Kapitel 9: Tests
- [x] Kapitel 10: Robuste Statistik
- [x] Kapitel 11: Multivariante Verteilungen



## Themen

* Einführung {7.2, 7.3}
* Grundbegriffe {7.4}
    - Messreihen {7.5, 7.6, 7.7}
        + Klassen {7.8}
        + Zweidimensionale Messreihen {7.22, 7.23}
    - Maßzahlen {7.13, 7.14}
        + Lagemaßzahlen {7.15}
            * Eindimensional {7.16, 7.17, 7.18}
            * Zweidimensional {7.24}
        + Streuungsmaße {7.19}
            * Eindimensional {7.20, 7.21}
            * Zweidimensional {7.25, 7.26, 7.27, 7.28}
        + Regressionsgerade {7.31, 7.32, 7.33, 7.34, 7.35, 7.36, 7.37, 7.38, 7.39}
    - Zufallsexperimente und Wahrscheinlichkeit {7.44}
        + Zufallsexperimente {7.45, 7.46}
            * Ereignisse {7.48, 7.50}
                - Ereignissysteme {7.51, 7.52, 7.53, 7.54}
                - Ereignispartition {7.68}
        + Wahrscheinlichkeit {7.49}
            * Formeln der Kombinatorik {7.57}
                - Geordnete Probe mit Wiederholungen {7.58}
                - Geordnete Probe ohne Wiederholungen {7.59}
                - Ungeordnete Probe mit Wiederholungen {7.61}
                - Ungeordnete Probe ohne Wiederholungen {7.60}
            * Bedingte Wahrscheinlichkeit {7.64, 7.65}
                - Formel von Bayes {7.69}
                - Multiplikationsformel {7.79}
            * Unabhängigkeit {7.80, 7.81, 7.82}
    - Zufallsvariablen und Verteilungsfunktion {7.83}
        + Zufallsvariablen {7.84, 7.85}
            * Messreihen {7.129, 7.130}
        + Verteilungsfunktion {7.87, 7.88}
            * Quantile {7.140}
        + Diskret/Stetig verteilte Zufallsvariablen {7.90}
            * Beispiele für diskrete Verteilungen {7.91}
                - Geometrische Verteilung {7.92, 7.113}
                - Binomialverteilung {7.94, 7.113}
                - Poissonverteilung {7.96, 7.113}
            * Beispiele für stetige Verteilungen {7.97}
                - Rechteckverteilung {7.98}
                - Exponentialverteilung {7.99, 7.113}
                - Normalverteilung {7.100, 7.101, 7.102, 7.113}
                - \( \mathcal{X}_r^2 \)-Verteilung {7.135, 7.138}
                - \( t_r \)-Verteilung {7.136, 7.138}
                - \( F_{r,s} \)-Verteilung {7.137, 7.138}
        + Erwatungswert und Varianz {7.103}
            * Erwartungswert {7.104, 7.106}
                - Rechenregeln {7.109, 7.110}
            * Varianz {7.107}
                - Rechenregeln {7.111, 7.112, 7.117}
        + Tschebyschevsche Ungleichung {7.114, 7.115}
        + Unabhängigkeit {7.116}
    - Einige Sätze {7.118}
        + Das schwache gesetz der großen Zahlen {7.120}
        + Zentraler Grenzwertsatz {7.122, 7.123, 7.124, 7.125}
        + Zentralsatz der Statistik {7.131}
        + Quantilapproximation {7.142}
* Schätzverfahren und Konfidenzintervalle {8.1}
    - Grundlagen {8.2, 8.3, 8.5, 8.6}
        + Mittlerer quadratischer Fehler {8.12, 8.13}
        + (Asymptotische) Erwartungstreue {8.7, 8.11}
        + Konsistenz {8.14, 8.15, 8.16}
    - Maximum-Likelihood-Schätzer {8.20, 8.21, 8.22}
    - Konfidenzintervalle {8.31, 8.32, 8.33}
        + Konstruktion {8.34}
                - Für normalverteilte Zufallsvariablen {8.35}
                - Für \(\mu\) bei bekannter Varianz {8.37, 8.38}
                - Für \(\mu\) bei unbekannter Variant {8.41, 8.42}
                - Für \(\sigma^2\) bei bekanntem Erwartungswert {8.44, 8.45}
                - F+r \(\sigma^2\) bei unbekanntem Erwartungswert {8.47, 8.48}
* Tests bei Normalverteilungsannahmen {9.1, 9.46}
    - Grundlagen {9.2, 9.3, 9.4}
        + Testgröße {9.5}
        + Tests {9.6}
        + Konstruktionsprinzip zum Niveau \(\alpha\) {9.7}
    - Wichtige Tests bei Normalverteilungsannahme {9.8, 9.9}
                - Gauß-Test (\(\mu\), \(\sigma_0^2\) bekannt) {9.10, 9.11, 9.12}
                - \(t\)-Test (\(\mu\), \(\sigma_0^2\) unbekannt) {9.15, 9.16, 9.17}
                - Unbekannte Varianz, bekannter Erwartungswert {9.19}
                - \(\mathcal{X}^2\)-Test {9.20}
    - Verteilungstests {9.25, 9.26}
                - \(\mathcal{X}^2\)-Anpassungstest {9.28, 9.29}
                - \(\mathcal{X}^2\)-Test auf Unabhängigkeit (Kontigenztest) {9.35, 9.36}
                - \(\mathcal{X}^2\)-Homogenitätstest {9.39, 9.40}
                - Wilcoxon Vorzeichen-Rang-Test {9.41, 9.43}
                - Weitere statische Tests {9.45}
* Robuste Statistik {10.1, 10.2}
    - Median {10.3, 10.4, 10.5, 10.6}
        + Schätzer {10.7, 10.8, 10.9}
    - M-Schätzer {10.12, 10.13, 10.14, 10.16}
* Multivariante Verteilungen und Summen von Zufallsvariablen {11.1, 11.2}
    - Grundlagen {11.3, 11.4, 11.5, 11.6, 11.7}
        + Kovarianz: Rechenregeln {11.8, 11.9, 11.10, 11.11}
        + Unabhängigkeit {11.17}
        + Korrelation {11.18, 11.19, 11.20, 11.21}
    - Verteilung der Summe von Zufallsvariablen {11.22, 11.23, 11.25}
        + Faltung {11.24, 11.26}
        + Anwendung
                - Binomialverteilten Zufallsvariablen {11.28}
                - Poissonverteilte Zufallsvariablen {11.29, 11.30}
                - Poisson Verteilung und bedingte Wahrscheinlichkeit {11.32}
                - Geometrische Verteilung und bedingte Wahrscheinlichkeit {11.33}
