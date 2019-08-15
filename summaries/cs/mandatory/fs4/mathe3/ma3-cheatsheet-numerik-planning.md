# Mathe 3 Zusammenfassung (Numerik) :: Planung

## Foliensätze

* [x] Kapitel 1: Interpolation
* [x] Kapitel 2: Integration
* [x] Kapitel 3: Differentialgleichungen
* [x] Kapitel 4: Lineare Gleichungssysteme
* [x] Kapitel 5: Nichtlineare Gleichungssysteme
* [x] Kapitel 6: Eigenwerte



## Themen

* Grundlagen {N/A}
    - Vektornormen {4.63}
    - Induzierte Matrixnormen {4.64, 4.65, 4.66, 4.67}
    - Konditionszahl {4.68}
    - Hermitesche Matrizen {6.11}
    - Eigenwerte und Eigenvektoren {6.5}
        + Charakterisches Polynom {6.6, 6.7}
        + Eigenschaften {6.8}
        + Diagonalisierbarkeit {6.10}
        + Diagonalmatrizen {6.33}
* Interpolation {1.3, 1.4, 1.5, 1.7}
    - Polynominterpolation {1.8, 1.9, 1.43, 1.44}
        + Eindeutigkeit {1.21}
        + Naiver Lösungsansatz {1.10, 1.11}
        + Lagrange-Interpolation {1.12, 1.13, 1.23}
        + Newtonsche Interpolationsformel {1.24, 1.25, 1.26, 1.27, 1.29, 1.32}
        + Fehlerabschätzungen {1.33, 1.34, 1.35}
        + Runges Phänomen {1.38, 1.39}
        + Tschebyschev-Abszissen {1.40}
    - Spline-Interpolation {1.45, 1.46, 1.47, 1.48}
        + Lineare Splines {1.51, 1.52, 1.53}
            * Fehlerabschätzung {1.55}
        + Kubische Splines {1.58, 1.59, 1.60, 1.61, 1.62, 1.63, 1.64}
            * Minimaleigenschaften {1.70}
            * Fehlerabschätzung {1.71, 1.72}
* Integration {2.1, 2.2, 2.8}
    - Geschlossene Newton-Cotes-Quadratur {2.5, 2.6, 2.7, 2.9, 2.10}
    - Offene Newton-Cotes-Quadratur {2.15, 2.16}
    - Vergleich Geschlossene vs. Offene Newton-Cotes-Quadratur {2.17}
    - Summierte Newton-Cotes-Formeln {2.20, 2.22, 2.23}
        + Summierte Trapezregel (geschlossen) {2.24}
        + Summierte Simpson-Regel (geschlossen) {2.25}
        + Summierte Rechteck-Regel (offen) {2.26}
* Gewöhnlichen Differentialgleichungen {3.1, 3.2, 3.3}
    - Existenz- und Eindeutigkeit {3.5}
    - Numerische Verfahren {3.7, 3.8, 3.9}
        + Explizites Euler-Verfahren {3.10}
        + Implizites Euler-Verfahren {3.11}
        + Verfahren von Heun {3.12}
        + Modifiziertes Euler-Verfahren {3.13}
        + Klassisches Runge-Kutta-Verfahren {3.14}
        + Explizite Runge-Kutta-Verfahren und Butcher-Schema {3.29, 3.30, 3.31}
        + Implizite Runge-Kutta-Verfahren und Butcher-Schema {3.61, 3.62, 3.63}
    - Konvergenz und Konsistenz {3.18, 3.19, 3.20}
        + Konsistenzordnungen {3.21, 3.22}
            * Konsistenzordnungen von Runge-Kutta-Verfahren {3.32, 3.33, 3.34}
        + Konvergenzsatz {3.24}
    - Steife Differentialgleichungen {3.35, 3.36, 3.37, 3.38, 3.43, 3.44, 3.45}
        + Modellgleichung {3.46, 3.47}
        + Stabilität {3.48, 3.49, 3.50, 3.51}
        + Stabilitätsgebiete {3.52}
            * Explizites Euler-Verfahren {3.53}
            * Implizites Euler-Verfahren {3.54}
            * Klassisches Runge-Kutta-Verfahren {3.57}
            * Implizite Trapezregel {5.60}
* Lineare Gleichungssysteme {4.1, 4.2, 4.3, 4.4}
    - Lösungstheorie {4.5}
    - Gaußsches Eliminationsverfahren, Dreieckszerlegung {4.6, 4.7}
        + Lösung gestaffelter Gleichungssysteme {4.8, 4.9, 4.10, 4.11}
        + Gaußsches Eliminationsverfahren {4.12, 4.13}
            * Grundkonzept {4.14, 4.15, 4.16, 4.17}
            * Privotstrategie {4.20, 4.21}
                - Spaltenpivotsuche {4.22}
                - Vollständige Pivotsuche {4.23}
            * Algorithmen {4.17, 4.22, 4.23, 4.28, 4.34}
        + LR-Zerlegung {4.25, 4.26, 4.27, 4.28, 4.29, 4.30, 4.37}
            * Vollständige Pivotsuche {4.33, 4.34}
        + Matrixdarstellung {4.38, 4.39, 4.40, 4.41, 4.42, 4.43}
        + Matrixklassen ohne Pivotsuche {4.47}
    - Cholsky-Verfahren {4.48, 4.49, 4.50, 4.51, 4.52}
        + Cholsky-Verfahren \(\leftrightarrow\) LR-Zerlegung {4.53}
        + Verfahren {4.54, 4.55, 4.56}
        + Eigenschaften {4.57}
    - Fehlerabschätzungen und Rundungsfehlereinfluss {4.58, 4.59}
        + Fehlerabschätzungen für gestörte Gleichungssysteme {4.60, 4.61, 4.62, 4.69}
        + Rundungsfehleranalyse {4.73, 4.74, 4.75}
            * Spaltenpivotsuche {4.76}
            * Vollständige Pivotsuche {4.77}
* Nichtlineare Gleichungssysteme {5.1, 5.2, 5.3, 5.4, 5.6}
    - Newton-Verfahren {5.7, 6.8}
        + Lokales Newton-Verfahren {5.16, 5.17}
        + Lokale Konvergenz {5.18, 5.19, 5.20, 5.21, 5.22}
        + Globalisierung {5.25, 5.26, 5.27, 5.28}
            * Schrittweitenwahl nach Armijo {5.30}
            * Globalisiertes Newton-Verfahren {5.32}
            * Globale Konvergenz {5.33}
* Eigenwert- und Eigenvektorberechnung {6.1, 6.2, 6.3}
    - Störungstheorie {6.25, 6.26, 6.27}
    - Gershgorin-Kreise {6.28, 6.32}
    - Numerische Verfahren {6.22, 6.23, 6.24}
        + Vektoriteration {6.36, 6.37}
            * Konvergenz {6.38, 6.41, 6.42}
            * Vektoriteration von Mises {6.43, 6.44}
            * Vektoriteration von Wiedlandt {6.43, 6.45}
            * Inverse Vektoriteration von Wiedlandt {6.46, 6.47}
        + QR-Verfahren {6.48, 6.49, 6.50}
            * Grundlegende Eigenschaften {6.51, 6.52}
            * Konvergenz {6.53, 6.54, 6.55, 6.56, 6.57, 6.58, 6.59, 6.60}
            * Shift-Techniken {6.61, 6.62, 6.63}
                - Verbreitete Shift-Strategie {6.64}
                - Berechnung der Eigenvektoren {6.65}
            * Householder-Verfahren zur Berechnung {6.66, 6.67, 6.68, 6.69, 6.70, 6.71, 6.72, 6.73}
