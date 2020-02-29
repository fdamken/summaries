# VC Cheatsheet :: Planung

## Foliensätze

Fertig/Strukturiert/Gesamt: 283/1218/1218: 23%/100%/100%

* [x] Kapitel 1: Einführung (92)
* [X] Kapitel 2: Grundlagen der menschlichen Wahrnehmung (120)
* [X] Kapitel 3: Computer Vision, Erkennung (81)
* [X] Kapitel 4: Fouriertheorie (82)
* [x] Kapitel 5: Bilder (97)
* [x] Kapitel 6: Bildverarbeitung (92)
* [x] Kapitel 7: Grafikpipeline (105)
* [x] Kapitel 8: Transformationen (76)
* [x] Kapitel 9: 3D-Visualisierung (65)
* [x] Kapitel 10: X3DOM (41)
* [x] Kapitel 11: Informationsvisualisierung (164)
* [x] Kapitel 12: Farbe (69)
* [x] Kapitel 13a: User-Interfaces (65)
* [x] Kapitel 13b: Multimedia Information Retrieval (69)



## Themen

* Einführung {1.1, 1.10}
    - Visual Computing {1.1, 1.18, 1.30, 1.31, 1.32, 1.33, 1.34, 1.50}
        + 3D-Internet {1.35, 1.36, 1.37}
        + Skalierbare Objektmodellierung/-erkennung {1.38, 1.39, 1.40, 1.41, 1.42, 1.43}
        + Big Data, Visual Analytics {1.44, 1.45, 1.46}
        + Scene Understanding {1.47, 1.48, 1.49}
    - Generalisierte Dokumente {1.51, 1.52, 1.53, 1.54, 1.55, 1.56, 1.68}
        + Retro-Digitalisierung, Digital Creation {1.57, 1.58, 1.59}
        + Generative Modelling Language {1.62, 1.63, 1.64, 1.65, 1.66, 1.67}
* Wahrnehmung {2.1}
    - Human Computer Interaction {2.4, 2.5, 2.6, 2.7, 2.8, 2.9}
    - Überblick {2.10, 2.11, 2.12, 2.13}
        + Menschliche Informationsverarbeitung {2.14, 2.15, 2.16, 2.20}
            * Eingabe (Wahrnehmung) {2.15}
                - Klangwahrnehmung {2.17}
                - Brührungswahrnehmung {2.18}
            * Ausgabe {2.15, 2.19}
    - Wahrnehmung {2.25}
        + Das Auge {2.25}
            * Reiz {2.26, 2.27, 2.28}
            * Das visuelle System {2.29, 2.30, 2.31, 2.32, 2.33, 2.34}
            * Photorezeptoren {2.35, 2.36}
            * Skotopisches und Photopisches Sehen {2.37}
            * Zapfenverteilung {2.38, 2.39, 2.40, 2.41, 2.42, 2.43, 2.44}
        + Vorverarbeitung visueller Informationen {2.45, 2.46, 2.47}
            * Signalverarbeitung in der Retina {2.48}
            * Optische Täuschungen {N/A}
                - Peripheral Drift {2.53}
                - Mach Bänder {2.55}
                - Chevreul Illusion {2.57}
            * Helligkeit {2.59, 2.66}
                - Simultankontrast {2.60, 2.61, 2.62, 2.63}
                - Kontrast als Reizverhältnis {2.64, 2.65}
            * Erkennung von Details {2.67}
                - Bildschärfenbestimmung {2.68}
                - Kontrastempfindlichkeit {2.69, 2.70, 2.71}
            * Frühe Wahrnehmung {2.73, 2.74, 2.75, 2.76, 2.77, 2.78, 2.79}
        + Informationsextraktion {2.80, 2.81, 2.82}
            * Raumwahrnehmung {2.83, 2.84, 2.85, 2.103, 2.104}
            * Depth Cue Theorie {2.86}
                - Stereoskopie {2.87, 2.88}
                - Picorial Depth Cues {2.89}
                    + Linearperspektive {2.90}
                    + Texturgradient {2.91}
                    + Fokus und Blur {2.92}
                    + Atmosphärische Tiefe {2.93}
                    + Schattenwurf {2.94, 2.95}
                    + Vertraute Größen {2.96}
                - Dynamische Depth Cues {2.97}
                    + Motion Parallax {2.98}
                    + Raumwahrnehmung durch Bewegung {2.99}
                    + Kinetic Depth Effect, Structure from Motion {2.100}
                - Auswertung von Depth Cues {2.101}
            * Mögliche Tasks {2.102}
    - Aufmerksamkeit {2.105}
        + Veränderungsblindheit {2.106}
        + Limitierung der Wahrnehmung {2.115}
        + Das Gedächtnis und "Gateway to Memory" {2.116, 2.117, 2.118}
* Objekterkennung und Bayes {3.1, 3.3, 3.4, 3.6}
    - Computer Vision {3.8}
        + Lochkamera {3.9, 3.10, 3.11}
        + Digitale Bilder {3.12, 3.13}
        + Konfluenz {3.14}
        + Fallstudie {3.17 ff.}
        + Intuitionen {3.31}
        + Bildaufbau {3.33}
    - Bayesian Decision Theory {3.36, 3.37}
        + Konzepte und Bayes Theorem {3.38, 3.39, 3.40, 3.44}
        + Problemstellung {3.41, 3.42, 3.43, 3.45, 3.46}
        + Entscheidungsregel {3.47, 3.48, 3.49, 3.50}
        + Naive Bayes Classifier {3.51, 3.52, 3.53}
    - Probability Density Estimation {3.54, 3.55, 3.56, 3.57, 3.58, 3.59}
    - Gesichtsdetektion {3.60}
        + Appearance-Based Methods {3.61}
        + Sliding Window Approach {3.62, 3.63}
        + Beispiel: Gesichtsdetektion {3.64, 3.65, 3.66, 3.67}
        + Naive Bayes Classifier {3.68, 3.69}
        + Erkennungsarten {3.74, 3.75}
    - Diskussion und Ausblick {3.76, 3.77, 3.79}
* Fouriertheorie {4.1, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 4.10, 4.11}
    - Mathematische Grundlagen {4.12}
        + Vektorraum {4.13, 4.14}
        + Basis eines Vektorraums {4.15}
        + Krummlinige Koordinatensysteme {4.16, 4.17}
        + Andere Räume {4.18}
        + Komplexe Zahlen {4.20, 4.48}
        + Gerade/Ungerade Funktionen {4.41}
    - Fourier-Reihe {4.19, 4.21}
        + Dirichlet-Bedingungen {4.22}
        + \(2\pi\)-periodische Funktion {4.23}
        + Skalarprodukt, Orthogonale Basis {4.24, 4.25, 4.26, 4.27, 4.28}
        + Berechnung der Koeffizienten \(a_n\), \(b_n\) {4.29, 4.30, 4.31}
        + Beispiel: Rechteck-Schwingung {4.32, 4.33, 4.34, 4.35, 4.36, 4.37, 4.38, 4.39, 4.40}
    - Fourier-Transformation {4.46, 4.47}
        + Mathematische Herleitung {4.49, 4.50, 4.51, 4.52}
        + Zusammenfassung {4.53}
        + Beispiel: Rechteckimpuls {4.54, 4.55}
        + Fourier-Darstellung {4.56}
        + Transformationspaare {4.57, 4.58, 4.59}
    - 2D-Fourier-Transformation {5.56, 5.57, 5.58, 5.59, 5.60, 5.61}
    - Faltung {4.60, 4.63, 4.64, 4.65}
        + Anwendung: Filter {4.68}
    - Abtastung {4.69, 4.70, 4.71}
        + Diskrete Abtastung {4.72, 4.73}
        + Abtasttheorie {4.74, 4.75}
        + Abtasttheorem von Whittaker-Shannon {4.78}
* Bilder {5.1, 5.3, 5.4}
    - Bildverbesserung {5.8, 5.9, 5.10, 5.11}
        + Histogramm {5.14, 5.15, 5.16, 5.17, 5.18, 5.19}
        + Pixeloperationen {5.12, 5.13, 5.20}
            * Bildnegativ {5.21}
            * Binärisierung/Thresholding {5.22}
            * Graufensterung {5.23}
        + Kontrastspreizung {5.24}
        + Histogrammausgleich {5.25, 5.26, 5.27}
        + Mittelung {5.28}
    - Bildfilterung {5.29, 5.30}
        + Ortsraum {5.31}
            * Lineare Filterung (Faltung) {5.32}
            * Tiefpass-Filter {5.33}
            * Mittelwert-Filter {5.34, 5.35}
            * Gauss-Filter {5.36, 5.37, 5.38}
            * Median-Filter {5.39}
            * Hochpass-Filter {5.40}
            * Diskretisierte Ableitungen {5.42, 5.43}
                - Laplacian-Filter {5.44, 5.47, 5.48}
                - Laplacian of Gaussian Filter {5.45, 5.46}
            * Bilateral Filter {6.10}
        + Frequenzraum {5.51, 5.52, 5.62, 5.63, 5.64, 5.65}
            * Idealer Tiefpass-Filter {5.66}
            * Gaussscher Tiefpass-Filter {5.67, 5.68}
            * Idealer Hochpass-Filter {5.70}
        + Vergleich: Orts- und Frequenzraum-Filter {5.71}
    - Bildkompression {5.72, 5.73, 5.74, 5.75, 5.76, 5.77, 5.96}
        + Harmonische Transformation {5.78}
            * JPEG {5.79, 5.95}
                - Schritt 1: Umwandlung in den YCC-Farbraum {5.80}
                - Schritt 2: Farb-Subsampling {5.81}
                - Schritt 3: Diskrete Kosinustransformation {5.82, 5.83, 5.84}
                - Schritt 4: Quantisierung {5.85}
                - Schritt 5: Kodierung der Koeffizienten {5.86, 5.87}
            * MH17 {6.6, 6.8}
* Bildverarbeitung {6.1, 6.90}
    - Deblurring {6.13, 6.15, 6.41}
        + Inverser Operator {6.19, 6.20}
        + Rekonstruktion {6.17, 6.21}
        + Rauschen {6.23, 6.26}
        + Korrekt gestellte Probleme {6.27, 6.28, 5.29}
    - Einschrittverfahren {6.30, 6.41}
        + Wiener Filter {6.31, 6.32, 6.33, 6.34, 6.35, 6.36}
        + Ansatz mit mehreren Komponenten {6.37}
            * Scale-Space-Ansatz {6.38, 6.39, 6.40, 6.43}
            * Gaussscher Scale-Space {6.44, 6.45}
    - Mehrschrittverfahren (Iterative Methoden) {6.47, 6.67}
        + Variationsableitung {6.48, 6.49, 6.50}
        + Alternativen {6.53}
        + Perona-Malik {6.54}
            * Nichtlineare Diffusionsgleichungen {6.55}
            * Die Perona-Malik-Gleichung {6.56, 6.57, 6.58}
            * Implementierung {6.59, 6.60}
            * Einfluss und Wahl von \(k\) {6.61}
            * Stoppzeit {6.62, 6.63, 6.64}
        + Eingeschränkte Evolution: Totale Variation {6.68, 6.69}
            * Distance Penalty {6.69, 6.70, 6.71}
            * Basisenergien {6.72}
            * Totale Variation {6.73, 6.74}
            * Erweiterungen {6.81}
* Grafikpipeline {7.1}
    - Hardware {7.8, 7.9, 7.14}
        + Large-Scale-Computing {7.10}
        + Personal/Desktop Computing {7.11}
        + Networked Computing {7.12}
        + Mobile Computing {7.13}
        + Collaborative Computing {7.15}
        + Virtual Reality {7.16}
        + Augmented Reality {7.18, 7.19, 7.20}
        + Ambient/Invisible {7.21}
        + Wearable/Ubiquitous {7.22}
    - Computergrafik {7.23, 7.24, 7.25}
        + Geschichte {N/A}
            * Die Anfänge {7.26, 7.27}
            * 60er Jahre {7.28}
            * 70er Jahre {7.29}
            * 80er Jahre {7.31}
            * 90er Jahre {7.32}
            * 2000 bis 2005 {7.33}
            * 2006 bis 2020 {7.34, 7.35}
        + Virtuelle Charaktere {7.36, 7.37, 7.38, 7.39}
    - Grafikpipeline {7.41, 7.42, 7.43, 7.61, 7.87, 7.98, 7.100}
    - Eingabe grafischer Daten {7.44, 7.45, 7.46}
    - Repräsentation von 3D-Daten {N/A}
        + Grafische Primitive {7.47, 7.48, 7.49, 7.50}
        + Transformationen {7.51, 7.52}
    - Räumliche Datenstrukturen {7.53, 7.54, 7.55}
        + Hüllkörper (Bounding Volumes) {7.56}
        + Hüllkörperhierarchien {7.57}
        + Raumunterteilung {N/A}
            * Achsenparallele Gitter (Grids) {7.58}
            * Quadtree/Octree {7.59}
            * Binary Space Partition {7.60}
    - Geometrieverarbeitung {N/A}
        + Modelltransformation (Ortientierung, Position) {7.62, 7.63}
        + Simulation der Beleuchtung {7.64, 7.65}
            * Phong-Beleuchtungsmodell {7.66, 7.67}
        + Perspektivische Transformation und Clipping (Abschneiden) {7.78, 7.79}
            * Painters Algorithmus {7.80}
        + Culling (Verdeckungsrechnung im Objektraum) {7.81, 7.82, 8.83}
        + Projektion {7.85, 7.86}
    - Rasterisierung {7.88}
        + Scan-Konvertierung {7.89}
            * Rasterisierung von Linien (Bresenham-Algorithmus) {7.90, 7.91}
            * Rasterisierung von Polygonen (Scanline Algorithmus) {7.92}
        + Verdeckungsrechnung {7.93}
            * z-Buffer-Algorithmus {7.94, 7.95, 7.96, 7.97}
    - Ausgabe {7.99}
    - Beispiele {7.101, 7.102, 7.103}
* Transformationen {8.1}
    - Affine Abbildungen {8.7, 8.8, 8.9, 8.12, 8.13}
        + Eigenschaften {8.14, 8.15, 8.16}
        + Translation {8.17, 8.18}
        + Homogene Koordinaten {8.19, 8.20}
            * Translation {8.21, 8.22, 8.23, 8.24, 8.25}
        + Matrizenschreibweise {8.26, 8.27}
    - Skalierung, Scherung, Rotation {8.28, 8.29, 8.30, 8.31}
        + Skalierung {8.34, 8.35, 8.36}
        + Scherung {8.37, 8.38}
        + Rotation {8.39, 8.40, 8.41, 8.42}
            * Rotation um beliebige Achse {8.43, 8.44, 8.45}
            * Rotation um beliebige Raumachse {8.46, 8.47}
        + Nicht-Kommutativität von Transformationen {8.48}
        + Rechenaufwand {8.49}
    - Projektion {8.50, 8.52, 8.53, 8.54}
        + Perspektive Projektion {8.55, 8.59, 8.60}
            * Kanonisches Sichtvolumen {8.61, 8.62}
            * Allgemeine perspektische Transformation {8.63}
        + Parallele Projektion {8.56}
        + Ein-, Zwei- und Dreipunktperspektive {8.65}
    - 3D-Interaktion {8.68, 8.69, 8.70}
        + Manipulatoren {8.71, 8.72, 8.73, 8.74}
* 3D-Visualisierung {9.1}
    - 3D-Daten {9.4}
        + placeholder; subsection
            * placeholder; subsubsection
                - Terrain {9.5}
                - Laser Scanning {9.6}
                - Range Images {9.7}
                - Medizinische Bilddaten {9.8, 9.9}
                - Schneiden {9.10}
                - Wetter {9.11}
                - Klimaforschung {9.12}
    - Triangulation von Punktwolken {9.13, 9.14}
        + Ideal Triangulation {9.15}
        + Voronoi-Diagramm und Delaunay-Triangulation {9.16, 9.17, 9.18}
    - Indirekte Volumenvisualisierung {9.22, 9.25}
        + 3D-Volumen und Nachbarschaft {9.23, 9.24}
        + 2D: Konturlinien {9.26}
        + 3D: Isoflächen {9.27, 9.28}
        + 2D: Marching Squares {9.29, 9.30}
        + 3D: Marching Cubes {9.31}
        + Große Polygonmodelle und Performanz {9.33, 9.34}
            * Culling von Geometrie {9.35}
            * Meshreduktion {9.36, 9.37}
            * Mesh-Glättung {9.38, 9.39}
    - Direkte Volumenvisualisierung {9.40, 9.41}
        + Density Emitter Model {9.42}
        + Volumen-Rendering-Gleichung {9.43, 9.44}
    - Volumen-Rendering-Pipeline {9.45}
        + Pipeline {N/A}
            * placeholder; subsubsection
                - Abtastung {9.46, 9.47, 9.48}
                - Klassifikation und Beleuchtung {9.50}
                - Komposition {9.51}
                    + Back-to-Front-Komposition {9.52}
                    + Front-to-Back-Komposition {9.53, 9.54, 9.55}
        + Transferfunktion {9.56, 9.57, 9.58, 9.59, 9.60}
* Szenengraphen am Beispiel X3DOM {10.1, 10.2, 10.3, 10.40}
    - Strukturierung von 3D-Szenendaten {10.4, 10.5, 10.6}
    - Szenengraph {10.10, 10.11, 10.12, 10.14}
    - X3DOM {10.16, 10.17, 10.19}
* Informationsvisualisierung {11.1, 11.2, 11.15, 11.16, 11.17, 11.18, 11.19, 11.20}
    - Informationsdesign {11.23, 11.24, 11.25, 11.34, 11.56, 11.57}
        + Referenzmodell von Card {11.26, 11.27, 11.28, 11.29, 11.30, 11.31, 11.32, 11.33}
    - Datentypen {N/A}
        + 1D-Daten, Zeitreihen {11.62, 11.63}
        + 2D-Daten {11.73}
        + mD-Daten (multidimensional) {11.77, 11.78}
        + Hierarchien {11.91}
        + Graphen/Netzwerke {11.155}
    - Kuchendiagramm (1D) {11.64, 11.65}
    - Balkendiagramm (1D) {11.68}
    - Liniendiagramm (Zeitreihe) {11.67, 11.68, 11.69}
        + placeholder; subsubsection
            * placeholder; subsubsection
                - Problem: Viele Zeitreihen {11.70, 11.71}
                - Problem: Länge {11.72}
    - Scatterplot (2D, 3D) {11.74, 11.75}
        + placeholder; subsubsection
            * placeholder; subsubsection
                - Problem: Overplotting {11.76}
    - Scatterplotmatrix (nD) {11.79, 11.80, 11.81}
    - Parallele Koordinaten (3D, nD) {11.82, 11.83, 11.84, 11.85, 11.86, 11.87, 11.88}
        + placeholder; subsubsection
            * placeholder; subsubsection
                - Problem: Overplotting {11.89}
                - Problem: Viele Dimensionen {11.90}
    - Node-Link-Diagramm (Hierarchien, Graphen) {11.92, 11.156}
        + placeholder; subsection
            * placeholder; subsubsection
                - Problem: Layout {11.93, 11.157, 11.158}
                - Problem: Viele Knoten {11.94, 11.159}
    - Treemap (Hierarchien) {11.95, 11.96, 11.97, 11.98, 11.99, 11.100, 11.101, 11.102}
        + placeholder; subsection
            * placeholder; subsubsection
                - Problem: Überlappung {11.105}
                - Problem: Größendarstellung {11.106, 11.107}
    - Zusammenfassung {11.160}
* Farbe {12.1, 12.2, 12.3, 12.6, 12.6}
    - Dimensionalität {12.8, 12.9}
    - Wahrnehmungskorrelate {12.10, 12.11, 12.12}
    - Reproduktion {12.13}
    - Berechnung von Farbattributen {12.14}
        + Das Auge {12.15, 12.16, 12.17}
        + Sepktrale Charaktertisierung des Auges {12.18, 12.19, 12.20, 12.21, 12.22}
        + Sepktralwertfunktion {12.23, 12.24}
        + Cone Fundamentals {12.25}
    - Objektfarben, Lichtmatrix under XIEXYZ-Farbraum {12.26, 12.27, 12.28, 12.29}
    - Metamerie {12.30, 12.31, 12.32, 12.33}
    - Gegenfarbtheorie {12.35}
    - Stevenssche Potenzfunktion {12.36}
    - CIELAB Farbraum {12.37, 12.38}
    - Technische Farbräume {12.39}
        + Geräte RGB {12.40}
        + Geräteunabhängige RGB {12.40}
        + YCbCr {12.41}
        + HSI/HSV/HSL {12.41}
        + CMY/CMYK {12.42}
    - Komplexität von Farbe {12.43}
        + Chromatische Adaptation {12.45, 12.46}
            * Modellbildung {12.47, 12.48}
        + Farbwahrnehmungsphänomene {12.49}
            * Simultankontrast {12.49}
            * Crispening Effekt {12.50}
            * Stevens Effekt {12.51}
            * Hunt Effekt {12.52}
        + Farbwahrnehmungsmodelle {12.54}
            * CIECAM02 {12.55, 12.56, 12.57}
        + Kontrastsensitivität {12.58, 12.59, 12.60}
            * S-CIELAB (Spacial-CIELAB) {12.61, 12.62, 12.63}
            * iCAM (Image Color Appearance Model) {12.64, 12.65, 12.66}
* User Interfaces {13a.1, 13a.64}
    - Interaktion {13a.7}
        + Möglichkeiten {13a.8}
            * Kommandozeile {13a.9}
            * Menüs {13a.10, 13a.11}
            * Formulare {13a.12}
            * Fragen und Antworten {13a.13}
            * Direkte Manipulation {13a.14, 13a.15}
            * 3D-Umgebungen {13a.17}
            * Natürliche Sprache {13a.18}
            * Gesten {13a.19}
        + Designprozess {13a.20, 13a.21, 13a.22}
            * Wasserfallmodell {13a.24}
            * Spiralmodell {13a.25}
            * V-Modell {13a.26}
            * Dynamic Systems Development Method (DSDM) {13a.27}
            * Design Process Model {13a.28}
    - GUI: Benutzeroberflächen {13a.30}
        + Das WIMP-Interface {13a.31}
            * Fenster-Komponenten {13a.32}
                - Multiple Document Interface (MDI) {13a.33}
                - Single Document Interface (SDI) {13a.34}
                - Tabbed Document Interface {13a.35}
            * Dialogboxen {13a.36}
                - Checkboxen {13a.37}
                - Radio Buttons {13a.38}
                - Listboxen {13a.39}
                - Comboboxen {13a.40}
                - Spinner {13a.41}
                - Slider {13a.42}
                - Weiteres {13a.43}
        + Menübasierte Programme {13a.44, 13a.45, 13a.46}
            * Untermenüs {13a.47}
            * Auswahl (if-then-else-Struktur) {13a.48, 13a.49}
                - Verschachtelte Entscheidungsstrukturen {13a.50}
            * Die case-Struktur {13a.51}
            * Modularisierung {13a.52}
        + GUI-Anwendungen und eventbasiertes Programmieren {13a.53, 13a.54}
            * Graphical User Interfaces (GUIs) {13a.55}
            * Event-Handler {13a.56, 13a.57}
            * Nutzerinteraktionen {13a.58}
            * Das Delegationsmodell {13a.59}
    - 3D-Interaktion {13a.61, 13a.62}
* Multimedia Information Retrieval {13b.1, 13b.7, 13b.8, 13b.64}
    - Inhaltsbasierte Suche {13b.10, 13b.11, 13b.14, 13b.17}
        + Mathematische Beschreibung {13b.15}
        + Retrieval Ergebnis {13b.16}
    - Distanzmaße {13b.19, 13b.20, 13b.21, 13b.22, 13b.23, 13b.24}
    - Query-Modalitäten {13b.25, 13b.30, 13b.31}
        + Text {13b.32, 13b.33, 13b.34, 13b.35, 13b.36, 13b.37}
        + Example {13b.38, 13b.39, 13b.40, 13b.41, 13b.42}
        + Example-Bilder {13b.43}
        + Sketch {13b.44, 13b.45, 13b.46, 13b.47, 13b.48, 13b.49, 13b.50, 13b.51, 13b.52, 13b.53}
    - Explorative Suche {13b.54, 13b.55}
        + Research Data {13b.56, 13b.57, 13b.58, 13b.59, 13b.60}
