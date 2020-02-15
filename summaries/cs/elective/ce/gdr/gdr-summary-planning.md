# GdR Zusammenfassung :: Planung

## Folien/Kapitel

* Folien: Fertig/Strukturiert/Gesamt: 734/1069/1069: 69%/100%/100%
* Skript: Fertig/Strukturiert/Gesamt: 65/177/177: 37%/100%/100%

- [x] Kapitel  1: Einleitung, Übersicht (Folien: 128; Skript: 10)
- [x] Kapitel  2: Räumliche Darstellung und Transformationen (Skript: 17; Folien: 43, vollständig redundant)
- [X] Kapitel  3: Manipulatorkinematik (Skript: 27)
- [X] Kapitel  4: Geschwindigkeit, Jacobi-Matrix (Skript: 38; Folien: 6)
- [x] Kapitel  5: Roboterdynamik (Skript: 65; Folien: 164)
- [X] Kapitel  6: Roboterregelungen und interne Sensoren (Folien: 259; Skript: 11)
- [X] Kapitel  7: Bahnplanung (Folien: 89)
- [X] Kapitel  8: Externe und intelligente Sensoren (Folien: 154)
- [X] Kapitel  9: Navigation mobiler Roboter (Folien: 113)
- [X] Kapitel 10: Middleware und Simulation (Folien: 41)
- [X] Kapitel 11: Steuerung autonomer Roboter (Folien: 50)
- [X] Kapitel 12: Verantwortung der Informatik und der Ingenieurwissenschaften (Folien: 22)
- [x] Anhang: Quaternionen, Notationen (Skript: 9)



## Themen

* Einleitung {1.8}
    - Was ist ein Roboter? {1.9, 1.10, 1.11, 1.12, 1.13, 1.14}
    - Was ist KI? {1.15, 1.16, 1.17, 1.18, 1.19}
    - Was ist Robotik? {1.20, 1.21, 1.22}
    - Sense -- Plan -- Act {1.27}
        + dummy
            * dummy
                - Act {N/A}
                    + Kinematik {1.28, 1.29, 1.30, 1.31, 2.32, 1.33, 1.34, 1.35}
                    + Dynamik {1.36, 1.37}
                    + Steuerung {1.38, 1.39, 1.40, 1.41}
                - Sense {N/A}
                    + Sensoren {1.42, 1.43, 1.44, 1.45}
                - Plan {N/A}
                    + Lokalisierung, Kartographie, Navigation, Bahnplanung {1.46, 1.47, 1.48, 1.49}
    - Geschichte der Robotik {1.50}
        + Historische Entwicklung {1.51, 1.54, 1.55}
        + Die drei Gebote der Robotik {1.52, 1.53}
        + Autonome Fahrzeuge {1.59}
        + Wntwicklungstrend {1.60}
    - Herausforderungen {1.61}
        + Humanoide Bewegung {1.61, 1.61, 1.63, 1.64, 1.65, 1.66, 1.67, 1.68, 1.69}
        + Roboter für menschliche Mobilität {1.112, 1.113, 1.114, 1.115, 1.116, 1.117, 1.118, 1.119, 1.120, 1.121, 1.122, 1.123}
        + Roboter-Avatare {1.70}
            * Beine {1.74, 1.75, 1.76, 1.77, 1.78, 1.79, 1.80, 1.81, 1.82, 1.83, 1.84}
            * Katastrophenbewältigung und -hilfe {1.71, 1.72, 1.73, 1.87, 1.88, 1.89, 1.90, 1.91, 1.92, 1.93, 1.94}
            * Objekt-Vorlagen {1.95, 1.96, 1.97, 1.98}
            * Geifen und Manipulation {1.99, 1.100, 1.101, 1.102, 1.103, 1.104, 1.105, 1.106, 1.107, 1.108, 1.109}
        + Die Robotik an sich {1.124, 1.125, 1.126, 1.127, 1.128}
* Räumliche Darstellungen und Transformationen {S.11}
    - Mathematische Grundlagen und Notation {S.11, 2.1}
        + Vektoren {S.11, 2.2, 2.3}
        + Matrizen {S.12, S.13, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 2.10, 2.11}
    - Koordinatensysteme {S.14, 2.12, 2.13}
        + Position {S.15, 2.14}
        + Orientierung {S.16, 2.15, 2.16}
    - Klassische Transformationsbeziehungen {S.17, 2.17, 2.18}
    - Rotation eines Koordinatensystems {S.18, 2.20}
        + Rotationsmatrizen {S.18, S.19, 2.21, 2.22, 2.23}
        + Verkettete Rotationen {S.19, S.20, S.21, 2.24, 2.25, 2.26, 2.27, 2.28}
        + Winkelparameter {S.22, 2.29, 2.35, 2.36}
            * RPY-Winkel {S.22, S.22, 2.30, 2.31, 2.32, 2.33}
            * Euler-Winkel {S.23, S.24, 2.34}
            * Kardan-Winkel {S.23, S.24, 2.35}
    - Homogene Transformationen {S.24, S.25, S.26, 2.19, 2.37, 2.38, 2.39, 2.40, 2.41, 2.42, 2.43}
    - Berechnungseffizienz {S.26, S.27}
* Roboterkinematik {S.28}
    - Vorwärtskinematik {S.28}
        + Kinematische Ketten {S.28, S.29}
        + Kinematische Modellbildung {S.30, S.31}
        + Denavit-Hartenberg (DH) Konventionen {S.31, S.32, S.33, S.34, S.35}
            * Beispiel: SCARA-Manipulator {S.36, S.37, S.38}
            * Beispiel: 2-DOF-Schub-Drehgelenk-Arm {S.38, S.39}
    - Rückwärtskinematik (Inverse Kinematik) {S.40, S.41, S.42}
        + Numerische Berechnung {S.43, S.44}
        + Analytische Lösung {S.45, S.46}
            * Beispiel: Ebener SCARA-Manipulator {S.46, S.47}
        + Geometrische Ermittlung der analytischen Lösung {S.48}
        + Algorithmische Ermittlung der analytischen Lösung {S.49}
    - Genauigkeit des kinematischen Modells {S.50}
    - Modellierung von Roboterbeinen und -armen {S.51}
        + Dreigelenkiges Bein eines vierbeinigen Roboters {S.51}
        + Sechgelenkiges Bein eines humanoiden Roboters {S.52, S.53}
        + Arm eines humanoiden Roboters {S.54}
* Geschwindigkeit, Jacobi-Matrix und statische Kräfte {S.55, S.56, S.57, S.58, S.59}
    - Schiefsymmetrische Matrizen, Vektoren der Winkelgeschwindigkeiten und -beschleunigungen {S.60, S.61, S.62}
        + Relative Beschleunigung zwischen \(S_n\) und \(S_0\) {S.63}
    - Jacobi-Matrix eines Manipulators {S.64}
        + Addition von Winkelgeschwindigkeiten {S.64, S.65}
        + Herleitung {S.66}
            * Drehwinkelgeschwindigkeit {S.67, S.68}
            * Lineare Geschwindigkeit {S.69, S.70, S.71}
            * Zusammenfassung {S.72}
        + Beispiel: Ebener SCARA-Manipulator {S.73, S.74}
    - Inverses Jacobi-Modell {S.75}
        + Geschwindigkeitssteuerung {S.75, S.76, S.77}
            * Beispiel: SCARA-Manipulator {S.77, S.78, S.79}
    - Kinematische Singularitäten {S.79, S.80, S.83}
        + Beispiel: SCARA-Manipulator {S.80, S.81}
        + Beispiel: Typischer Industrieroboter mit 6 Drehgelenken {S.81, S.82}
        + Weitere Beispiele {S.82}
        + Vermeidung {S.82, S.83}
        + Umgang mit unvermeidbaren Singularitäten {S.83}
    - Nicht-holonome Kinematik mehrrädriger Fahrzeuge {S.84, S.85}
        + Differentialantrieb {S.86, S.87, 4.2}
        + Allgemeines Vorwärtskinematikproblem für Fahrzeuge {S.87, S.88, S.89, S.90}
        + Inverses Kinematikproblem {S.90, S.91}
        + Omnidirektionale Dreirad-Kinematik {S.91, S.92}
        + Weitere Antriebsarten von Fahrzeugen {S.92, 4.5}
    - Statische Kräfte bei Manipulatoren {S.92}
* Roboterdynamik {S.93, S.94, S.95}
    - Massenverteilung eines Starrkörpers {S.96, S.97, S.98}
    - Newton-Euler Formulierung der Roboterdynamik {S.99, S.100, S.110, S.118, S.119}
        + Iterative Berechnung von INV DYN {S.101, S.102, S.103, S.104, S.105, S.106, S.107, S.108, S.109}
        + Zusammenfassung {S.109, S.110}
        + Beispiel: SCARA-Manipulator {S.111, S.112, S.113, S.114, S.115, S.116, S.117}
    - Lagrangesche Formulierung der Roboterdynamik {S.120}
        + Kinetische und potentielle Energie, Lagrangefunktion {S.120, S.122}
            * Kinetische Energie {S.120}
            * Potentielle Energie {S.121}
            * Lagrangefunktion {S.121, S.122}
        + Beispiel: SCARA-Manipulator {S.123, S.124, S.125, S.126, S.127, S.128, S.129}
    - Numerische Aspekte {S.130}
        + Modularität {S.130}
        + Simulation {S.131}
    - Rekursive Verfahren zur Berechnung der Vorwärtsdynamik {S.131}
        + Verfahren mit expliziter Berechnung der Massenmatrix {S.132}
            * Verfahren 1: Berechnung von \(M\) durch wiederholte Auswertung des Newton-Euler-Verfahrens {S.132, 5.20}
            * Verfahren 2: Ausnutzen der Symmetrie von \(M\) {S.132, S.133, 5.20}
            * Verfahren 3: Aggregation von Teilmanipulatoren (CRBA) {S.133, S.134, 5.20}
            * Vergleich der Verfahren {S.135}
        + Verfahren ohne explizite Berechnung der Massenmatrix {S.135, 5.22, 5.23, 5.24}
        + Multibody Systems Library MBSlib {5.25, 5.26, 5.27, 5.28, 5.29, 5.31, 5.32}
            * Beispiele {5.29, 5.30, 5.33, 5.34, 5.35, 5.36, 5.37}
    - Geschlossene kinematische Ketten {S.136}
    - Berücksichtigung von Nichtstarrkörpereffekten {S.137, 5.39}
        + Reibung {S.137, S.138, 5.40, 5.41}
            * Reibungsmodell {5.42}
                - Haftung {5.43}
                - Stribeck-Reibung {5.44}
                - Coloumbsche Reibung {S.138}
                - Viskose Gleitreibung {S.138, S.139}
        + Elastizität {S.139, 5.45, 5.46}
            * Grundlagen {S.139, S.140, 5.47, 5.48, 5.49}
            * Elastizitäten in der Robotik {S.141, S.142, S.143, S.144, 5.50, 5.51}
                - Ersatzmodell {5.52}
                - Dynamikgleichungen {5.53, 5.54, 5.55, 5.56}
            * Berechnung von INV DYN bei Drehgelenkelastizitäten {S.145, 5.57, 5.58}
            * Elastizitäten in der Biologie {S.146, 5.59, 5.60}
                - Menschlicher Bewegungsapparat {5.61, 5.62, 5.63}
                    + Gelenkmodelle {5.64, 5.65}
                    + Skelettmuskulatur {5.66}
                    + Muskel-Sehnen-Komplex {5.67, 5.68, 5.69}
                - Muskelaktivierungsdynamik {5.70}
                    + Muskelmodell {5.71, 5.72, 5.73}
                    + Hebelarme {5.74}
                - Weichteilmodelle {5.75, 5.76}
                - Dynamikmodell {5.77}
                    + Dynamiksimulation {5.78, 5.79, 5.80, 5.81, 5.82, 5.83}
                - Software und Daten {5.84}
                - Einschränkungen {5.85}
            * Steuerung und Regelung bei Mensch und Tier {5.87, 5.88}
                - Reafferenzprinzip {5.89, 5.90, 5.91}
    - Spezielle Dynamikmodelle für zweibeinige, humanoide Roboter und deren Stabilitätsregelung {S.147, 5.97, 5.98, 5.99}
        + Stabilität zweibeiniges Laufen {5.100, 5.101, 5.102}
        + Dynamik im Roboterstandfuß {5.104, 5.105, 5.106, 5.107, 5.108}
        + Zero-Moment-Point {S.148, S.149, S.149, S.150, 5.109}
        + Center of Pressure (CoP) {5.110}
        + ZMP Preview Walking {5.111, 5.112, 5.113, 5.114, 5.115, 5.116}
        + Globale Stabilitätsbegriffe {S.156, S.157}
        + Ausblicke {N/A}
            * Capture Steps {5.117, 5.118}
            * Whole Body Control {5.119, 5.120, 5.121, 5.122}
            * Unebenes Terrain {5.123}
    - Spezielle Dynamikmodelle für zweibeinige, nichthumanoide Roboter und deren Stabilitätsregelung {5.125, 5.126}
        + Inverses Pendel {S.150, S.151, S.152, S.153, 5.127}
        + Erweitertes Modell des menschlichen Gehens und Rennens {S.153, 5.128, 5.129}
            * Feder-Masse-Modell (Rennen) {S.153, S.154, S.155}
            * Feder-Masse-Modell (Gehen) {S.153, S.155}
        + Hüpfende Roboter mit Teleskop-Beinen {5.130, 5.131, 5.132, 5.138}
            * Ein Modell dynamischer Stabilität {5.134, 5.135, 5.136, 5.137}
        + Passive Dynamic Walkers {5.142, 5.143, 5.144, 5.145, 5.147, 5.148, 5.149}
        + Elastische Roboter {5.150, 5.151, 5.152, 5.153, 5.154, 5.160, 5.164}
* Antriebssysteme {6.6}
    - Gebräuchliche Antriebssysteme {6.6}
        + Hydraulische Antriebe {6.7}
        + Pneumatische Antriebe {6.8}
        + Elektrische Antriebe {6.9}
    - DC-Motoren {6.10, 6.11, 6.12, 6.13}
    - Getriebe {6.14, 6.15, 6.16}
        + Gewinde {6.17}
        + Riemen-/Seilzug-Getriebe {6.18}
        + Rädergetriebe {6.19}
            * Stirnradgetriebe {6.20}
            * Planetengetriebe {6.21, 6.22, 6.23, 6.24}
            * Harmonic Drive Getriebe {6.25, 6.26, 6.27, 6.28}
            * Wittenstein Galaxie Getriebe {6.29}
    - Alternative und elastische Antriebskonzepte {6.30, 6.31, 6.32}
        + Beine {6.33, 6.34}
        + Neue Materialien {6.35, 6.36, 6.36, 6.37, 6.42}
        + Compliant Robot Actuation {6.38}
        + Elastische Antriebskonzepte {6.43, 6.44, 6.45}
            * Variable Stiffness Actuator {6.46}
            * Variable Impedance Actuators {6.47, 6.48, 6.49, 6.50, 6.51}
        + Vom Muskel-Skelett-Apparat inspirierte Roboter {6.52, 6.53}
* Sensoren {6.54, 8.1}
    - Interne Sensoren {6.54, 6.55, 6.56}
        + Positionssensoren {6.56}
            * Potentiometer {6.57}
            * Optische Codierer {6.58}
                - Inkrementell {6.59, 6.60}
                - Absolut {6.61, 6.62}
            * Resolver {6.63}
        + Geschwindigkeitssensoren {6.64}
        + Beschleunigungssensoren {6.65}
            * Silizium-Beschleunigungssensor {6.66}
        + Inertial Navigation System (INS) {6.67, 6.71}
            * Gyroskop {6.68, 6.69, 6.70}
            * Mikromechanische Gyroskope {6.72}
            * Drift- und Fehlerkompension {6.73}
        + Kraft-Momenten-Sensor {6.74, 6.75, 6.76, 6.77, 6.78}
    - Externe und intelligente Sensoren {8.1, 8.2, 8.3, 8.4, 8.5}
        + Abstandssensoren {8.6, 8.7}
            * Akustische Abstandssensoren {8.8, 8.17}
                - Ultraschall {8.9, 8.10, 8.11}
                - Messsituationen {8.12, 8.13}
                - Abhilfe der Schwierigkeiten {8.14}
                - Natur {8.15, 8.16}
            * Optische Abstandssensoren {8.18, 8.19}
                - Laufzeitermittlung {8.20, 8.21}
                - 2D-Laserscanner {8.22, 8.23, 8.24, 8.25}
        + Visuelle Sensoren {8.26, 8.27, 8.28, 8.29, 8.30, 8.31}
            * Bilderzeugung {8.32, 8.33, 8.34, 8.35}
            * Grundlagen {8.38, 8.39, 8.40, 8.41, 8.42, 8.43}
            * Bildvorverarbeitung {8.44, 8.45, 8.46}
                - Nachbarschaftsbildverarbeitung {8.47, 8.48, 8.49, 8.50}
            * Bildverarbeitung {8.51, 8.52, 8.53}
                - Kantendetektion {8.54, 8.55, 8.56, 8.57}
                    + Prewitt-Operator {8.58, 8.59, 8.60, 8.61}
                    + Zusammenfassung {8.62, 8.63}
                - Konturerkennung {8.64}
                    + Lokale Analyse {8.65, 8.66}
                    + Globale Analyse {8.67, 8.68, 8.69, 8.70}
                - Segmentierung {8.71, 8.72}
                    + Schwellwertabfrage {8.73, 8.74}
                    + Bereichswachstum {8.75}
            * Merkmalsextraktion {8.76, 8.77, 8.78, 8.79}
            * Objektklassifikation {8.80, 8.81, 8.82, 8.83, 8.84, 8.85, 8.86, 8.87, 8.88, 8.89, 8.90, 8.91, 8.92}
        + 3D-Sensoren und Perzeption {8.93, 8.94, 8.95, 8.96}
            * Bildbasierte 3D-Sensoren {8.97, 8.98}
                - Stereo Vision {8.99, 8.100, 8.101, 8.102, 8.103, 8.104, 8.105, 8.106}
                - Structured Light Kamera {8.107, 8.108, 8.109, 8.110, 8.111, 8.112, 8.113, 8.114}
                - Stereo Vision + Structured Light {8.115, 8.116, 8.117}
                - Time-of-Flight (ToF) Kamera {8.118, 8.119, 8.120, 8.121, 8.122, 8.123, 8.124, 8.125}
            * Laserbasierte 3D-Sensoren {8.126, 8.127, 8.128, 8.129}
            * Datenstrukturen und -Repräsentation {8.130, 8.131}
                - kd-Baum {8.132, 8.133}
                - Octree {8.134, 8.135, 8.136}
                - Truncated Signed Distance Fields (TSDF) {8.137, 8.138}
            * Point-Cloud Processing {8.139, 8.140, 8.141, 8.142, 8.143, 8.144, 8.145, 8.146, 8.147}
            * Point-Cloud Registration {8.148, 8.149, 8.150, 8.151, 8.152, 8.153, 8.154}
* Regelung {6.1, S.158, S.159, S.160}
    - Lineare Regelung {6.1, 6.2, 6.3, 6.4, 6.5, 6.79, 6.85, 6.86, 6.87, S.160}
        + dummy
            * Begriffe {6.80, 6.81, 6.82, 6.83, 6.84, 6.88, 6.89, 6.90}
        + Lineare Systemdynamik und Feder-Masse-System {6.91, 6.92, S.161}
            * Untersuchung des Bewegungsverhaltens {6.93, S.161, S.162, S.163}
                - Erwartetes Bewegungsverhalten {6.94, 6.95, 6.96, 6.97, 6.98}
                - Gewünschtes Bewegungsverhalten {6.99}
        + PD-Regelung linearer Systeme 2. Ordnung {6.100, 6.101, 6.102, S.163, S.164}
            * Feder-Masse-System {6.103, 6.104, 6.105, 6.106}
        + Partinionierung des Regelgesetzes durch Feedback-Linearisierung {6.107, 6.108, S.165, S.166}
        + Sollwerttrajektorien-Folgeregelung {6.109, 6.110, S.166, S.167}
        + PID-Regelung linearer Systeme {6.111, 6.112, 6.115, S.167, S.168}
            * Windup-Effekt {6.113, 6.114}
        + Kaskadenregelung {6.116, 6.117, 6.118, 6.119, 6.120}
            * PID-Bahnregelung eines Servomotors {6.121, 6.122}
            * Laufbewegungen {6.123, 6.124, 6.125, 6.126, 6.127, 6.128, 6.129, 6.130}
        + Stabilität als Sprungantwortverhalten und PID-Parameter {6.131, 6.132, 6.133}
            * Drehmotor {6.134, 6.135, 6.136, 6.137, 6.138, 6.139, 6.140, 6.141}
            * Einstellung der PID-Parameter {6.142, 6.143}
        + Digitale Implementierung eines PID-Reglers {6.144, 6.145}
    - Nichtlineare Regelung {6.147, 6.148}
        + Systemlinearisierung {6.149}
        + Modellbasierte Manipulatorregelung {6.150, 6.151, 6.152}
        + Adaptive Manipulatorregelung {6.153}
        + Bahnreglung in Weltkoordinaten {6.154}
    - Kraft-/Momenten-Regelung {6.155, 6.156, 6.157, 6.158, 6.159, 6.160, 6.161, 6.162}
    - Bahn-/Kraft-Regelung {6.163}
        + Hybride Regelung {6.163, 6.164, 6.165}
        + Parallele Regelung {6.166, 6.167}
    - Nachgiebigkeitsregelung (Compliant Control) {6.168, 6.169, 6.170, 6.171}
        + Verallgemeinerte Betrachtung nach Hogan {6.172, 6.173}
        + Impedanzregelung {6.174, 6.175}
            * Greifen {6.179, 6.180, 6.181, 6.182, 6.183, 6.184}
        + Admittanzregelung {6.185, 6.186, 6.187, 6.188, 6.191, 6.192}
            * Implementierung {6.189, 6.190}
        + Aktiv-passive Konzepte für Impedanz/Admittanz {6.193, 6.194}
    - Bildgeführte Regelung {6.195, 6.196, 6.197, }
        + Positionsbasiert {6.198}
        + Bildbasiert {6.199, 6.200}
    - Multimodale Regelung physikalischer Interaktionen {6.202, 6.203, 6.204, 6.205, 6.206}
    - Regelung und Steuerung bei Mensch und Tier {6.207, 6.208, 6.228}
        + Propriozeption {6.209}
        + Sensoren {6.210}
        + Zentrales Nervensystem {6.211, 6.212, 6.213, 6.214, 6.215, 6.216, 6.217}
        + Neurale Integration {6.218, 6.219}
        + Informationsverarbeitung {6.220}
            * Reflexe {6.221, 6.222, 6.223}
        + Sonstiges {6.224, 6.225, 6.226, 6.227}
    - Elementare Roboterbewegungen {6.229}
        + Elementare Bewegungsarten für Industrieroboter {6.230, 6.231}
            * Lineare Interpolation in Gelenkkoordinaten {6.232, 6.233, 6.234}
            * Lineare Interpolation in Weltkoordinaten {6.235}
            * Kreisbogen-Interpolation {6.236}
            * Spline-Interpolation {6.236}
        + Schwierigkeiten bei kartesischer Bahnvorgabe {6.237, 6.238}
        + Programmierung einer Bahn als Folge elementarer Bewegungen {6.239, 6.240, 6.241, 6.242, 6.243}
        + Elementare Bewegungsarten für fahrende Roboter {6.244, 6.245, 6.246}
        + Elementare Bewegungsarten für laufende Roboter {6.247, 6.248, 6.249, 6.250, 6.251, 6.252, 6.253, 6.254, 6.255, 6.256, 6.257, 6.258}
* Bahnplanung {7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8}
    - Bahnplanungsarten {7.9, 7.10}
    - Topologische Wegeplanung {7.11, 7.12, 7.13, 7.14}
    - Konfigurationsraum {7.15, 7.16, 7.17, 7.18, 7.19, 7.20, 7.21, 7.22, 7.23, 7.24}
    - Geometrische Bahnplanung {7.25, 7.26, 7.27}
        + Metrische Darstellung {7.28, 7.29}
        + Roadmap-Verfahren {7.30, 7.31}
            * Sichtbarkeitsgraph {7.32, 7.33}
            * Tangentengraph {7.34, 7.35}
            * Voronoi-Diagramme {7.36, 7.37, 7.38}
        + Exakte Zellzerlegung {7.39, 7.40, 7.41, 7.42, 7.43, 7.44, 7.45}
        + Approximative Zellzerlegung {7.46, 7.47, 7.48, 7.49}
        + Potentialfeld-Methoden {7.50, 7.51, 7.52, 7.53, 7.54, 7.55, 7.56}
        + Komplexität {7.57, 7.58, 7.59}
        + Stichprobenverfahren {7.61, 7.62, 7.63, 7.64, 7.65}
        + Rapidly Exploring Random Trees (RRTs) {7.66}
        + Beispiele {7.67, 7.68, 7.69}
            * MINERVA {7.70}
                - Umweltmodell: Belegungskarte {7.71, 7.72, 7.73, 7.74}
                - "Küstennahe" Bahnplanung {7.75}
                - Kollisionsvermeidung {7.76, 7.77}
    - Kinematische und dynamische Trajektorienplanung {7.78, 7.79, 7.80, 7.81, 7.82}
        + Allgemeine Formulierung {7.83, 7.84, 7.85}
        + Beispiel: Industrieroboter {7.86, 7.87, 7.88}
* Navigation mobiler Roboter {9.1, 9.2, 9.3, 9.4}
    - Lokalisierung und Positionierung {9.5}
        + Relative Positionsbestimmung {9.6}
        + Absolute Positionsbestimmung {9.7, 9.8, 9.9}
            * Nichtlineare Ausgleichsrechnung {9.10}
            * Erkennung künstlicher Landmarken {9.11, 9.12, 9.13, 9.14}
        + Stochastische Positionsbestimmung {9.15, 9.15, 9.16}
    - Selbstlokalisierung und Navigation {9.17, 9.18, 9.19, 9.20}
        + Metrische Beschreibung des Aufenthaltsortes {9.21, 9.22}
        + Topologische Beschreibung des Aufenthaltsortes {9.23}
        + Lokalisierung mit einer Hypothese {9.24, 9.25}
            * Koppelnavigation {9.26}
            * (Erweitertes) Kalman-Filter {9.27, 9.28, 9.29, 9.30, 9.33, 9.37}
                - Time-Update {9.31, 9.32}
                - Measurement-Update {9.34, 9.35, 9.36}
        + Lokalisierung mit mehreren Hypothesen {9.41}
            * Verwendung mehrerer Kalman-Filter {9.42, 9.43, 9.44, 9.45, 9.46, 9.47, 9.48, 9.49}
            * Diskretisierte Wahrscheinlichkeitsverteilung {9.50, 9.51, 9.52, 9.53, 9.54, 9.55, 9.56, 9.57, 9.58, 9.59, 9.60}
            * Monte-Carlo Lokalisierung {9.61, 9.62, 9.63, 9.64, 9.65, 9.66, 9.67, 9.68, 9.69, 9.70, 9.71, 9.72, 9.73}
        + Simultaneous Localization and Mapping (SLAM) {9.74, 9.75, 9.76, 9.77, 9.78, 9.79}
            * EKF SLAM {9.80, 9.81, 9.82, 9.83, 9.84}
            * FastSLAM {9.85, 9.86, 9.87, 9.88}
            * Graph-basiertes SLAM {9.89}
            * Limitierungen {9.90, 9.91}
            * Visual SLAM {9.92, 9.93, 9.94, 9.95}
            * Team HECTOR {9.96, 9.97, 9.98, 9.99, 9.100, 9.101, 9.102, 9.103}
            * Google Cartographer {9.104, 9.105, 9.106}
            * 3D SLAM {9.107, 9.108, 9.109, 9.110, 9.111, 9.112, 9.113}
* Middleware und Simulation {10.1, 10.2, 10.3, 10.4, 10.5, 10.6}
    - Szenarien, Eigenschaften und Herausforderungen {10.7, 10.8, 10.9, 10.10, 10.11}
    - Middleware {10.12, 10.13, 10.14, 10.15}
        + Nachrichtenbasierte Kommunikation {10.16, 10.17}
        + Laufzeit-Effizienz {10.18, 10.19}
    - Sicherstellung von Korrektheit und Zuverlässigkeit {10.20, 10.21, 10.22, 10.25, 10.26}
        + Simulation {10.27}
        + Automatisierte Testabläufe {10.30, 10.31, 10.32}
        + Monitoring {10.33}
        + Visuelles Debuggen {10.34, 10.35}
        + Offline Analyse {10.36, 10.37}
        + Kooperierendes Verhalten {10.38, 10.39, 10.40}
* Steuerung autonomer Roboter {11.1, 11.2}
    - Steuerungsarchitekturen {11.3}
        + Hierarchisches Steuerungsparadigma {11.4, 11.5, 11.6}
        + Reaktives Steuerungsparadigma {11.7, 11.8}
        + Hybrid deliberativ-reaktives Steuerungsparadigma {11.9, 11.10, 11.11}
        + Beispiel: Subsumption Architecture {11.12, 11.13, 11.14, 11.18}
            * Schicht 0 {11.15}
            * Schicht 1 {11.16}
            * Schicht 2 {11.17}
    - Programmierung von Verhalten {11.19, 11.20, 11.21, 11.22, 11.23}
        + XABSL {11.24, 11.25, 11.26, 11.27, 11.28, 11.29, 11.30}
        + FlexBE {11.31, 11.32}
            * Autonomy Level {11.33}
            * Beispiel: TurtleBot3 {N/A}
                - Move Arm {11.34, 11.35, 11.36, 11.37, 11.38, 11.39, 11.40, 11.41, 11.42, 11.43, 11.44, 11.45}
                - Move Base {11.46, 11.47, 11.48}
* Verantwortung der Informatik und der Ingenieurwissenschaften {12.1}
    - Zivilklausel der TU Darmstadt {12.2}
    - Beispiele {N/A}
        + Kugelschreiber {12.3}
        + DARPA Robotics Challenge {12.4, 12.5, 12.6, 12.7, 12.8}
        + Roboter und Arbeitsplätze {12.9, 12.10, 12.11, 12.12, 12.13}
    - Sonstiges {12.14, 12.15, 12.16, 12.17}
* Anhang {N/A}
* Quaternionen {S.176}
    - Einleitung {S.176}
    - Rechenregeln {S.176}
    - Umrechnung: Quaternionen \(\leftrightarrow\) Rotationsmatrizen {S.177}
    - Verkettung von Drehungen {S.177}
    - Repräsentation der Koordinaten eines Punktes bei Rotation {S.177, S.178}
    - Vergleich mit anderen Darstellungsarten {S.179}
* Zusammenhang zwischen Rotationsmatrix, Drehvektor und Drehwinkel {S.179}
    - Drehvektor und Drehwinkel \(\to\) Rotationsmatrix {S.179}
    - Rotationsmatrix \(\to\) Drehvektor und Drehwinkel {S.179, S.180, S.181}
* Notationen {S.183, S.184}
