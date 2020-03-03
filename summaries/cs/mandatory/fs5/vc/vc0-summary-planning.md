# VC Cheatsheet :: Planung

## Foliensätze

Fertig/Strukturiert/Gesamt: 1218/1218/1218: 100%/100%/100%

* [X] Kapitel 1: Einführung (92)
* [X] Kapitel 2: Grundlagen der menschlichen Wahrnehmung (120)
* [X] Kapitel 3: Computer Vision, Erkennung (81)
* [X] Kapitel 4: Fouriertheorie (82)
* [X] Kapitel 5: Bilder (97)
* [X] Kapitel 6: Bildverarbeitung (92)
* [X] Kapitel 7: Grafikpipeline (105)
* [X] Kapitel 8: Transformationen (76)
* [X] Kapitel 9: 3D-Visualisierung (65)
* [X] Kapitel 10: X3DOM (41)
* [X] Kapitel 11: Informationsvisualisierung (164)
* [X] Kapitel 12: Farbe (69)
* [X] Kapitel 13a: User-Interfaces (65)
* [X] Kapitel 13b: Multimedia Information Retrieval (69)



## Themen

Siehe `vc0-summary.tex`.



## Typische Fragen

* Einführung
    - Was sind zwei Arten des 3D-Internets?
    - Was sind zwei Probleme des klassischen 3D-Laser-Scannens?
    - Was ist der Unterschied zwischen Object Detection und Object Tracking? Wieso werden beide häufig in Kombination verwendet?
* Wahrnehmung
    - Was ist die Hauptfunktion von Aufmerksamkeit?
    - Was sind die drei Typen von Aufmerksamkeit?
    - Wie heißt das Forschungsgebiet, welches sich mit der Beziehung zwischen mentalem Erleben und objektiven Reizen auseinandersetzt?
    - Was sind drei Zellen (mit Ausnahme der Photorezeptorzelle), die an der Signalverarbeitung in der Retina beteiligt sind und was sind deren Aufgaben?
    - In welchem Wellenlängenbereich werden Farben ungefährt wahrgenommen?
    - Wieso werden bei Videoaufnahmen mittlerweile Greenscreens statt anderen Farben bevorzugt?
    - Was bedeutet "skotopisches" und "photopisches" Sehen?
    - In welchem Bereich des Auges sind Stäbchen und in welchem Bereich Zapfen?
    - Was sind die drei Kategorien von Depth Cues (jeweils mit Beispiel)?
    - Was sind zwei Elemente der frühen Wahrnehmung, um die Aufmerksamkeit visuell zu lenken?
    - Wieso ist bei Dunkelheit eine grün beleuchtete Oberfläche besser zu erkennen als eine blau beleuchtete Oberfläche und was hat das mit photopischem und skotopischem Sehen zu tun?
    - Was sind zwei Pictorial Depth Cues (jeweils mit Beispiel)?
    - Kann das Fehlen eines Auges die Tiefenwahrnehmung beeinflussen?
* Objekterkennung
    - Sei ein Klassifizierer gegeben, der für ein Bild mit fester Größe entscheidet, ob auf einem Bild ein Gesicht zu sehen ist oder nicht. Wie kann dieser Klassifizierer verwendet werden, um auch größere Bilder zu klassifizieren?
    - Was sind zwei Merkmale von negativen Trainingsdaten?
    - Welche drei Schritte müssen durchgeführt werden, um einen Objekterkennungs-Detektion mit einem Erscheinungsmodell zu entwickeln? Was sind die wesentlichen Bestandteile?
    - Welchen der Situationen "Das Personal von Fraport darf den Flughafenbereich erst nach erfolgreichem Scan des Ausweises betreten." und "Bei einem Überfall könnte durch die Überwachungskameras das Gesicht des Täters gefilmt werden, wodurch die Polizei die Identität feststellen konnte." sollten die Begriffe "Identifikation" und "Verifikation" zugeordnet werden?
* Bayesian Decision Theory
    - Was nimmt der Naive Bayes Classifier an? Trifft diese Annahme immer zu?
    - Was ist die Entscheidungsregel, um einen Merkmalsvektor bei einem Zweiklassenproblem einer Klasse zuzuordnen?
    - Was bedeuten die Begriffe "Prior", "Likelihood" und "Posterior" und wie hängen diese zusammen?
* Fouriertheorie
    - Was charakterisiert die Fourier-Wellen im Ortsbereich und im Frequenzbereich?
    - Wodurch werden die Punkte in der Ebene bei Polarkoordinaten beschrieben?
    - Was gilt für gerade/ungerade Funktionen?
    - Wann ist eine Funktion \(f(x)\) mit einer endlichen Grenzfrequenz \(u_G\) aus den Abtastwerten \(f(n \cdot \Delta x)\) fehlerfrei rekonstruierbar?
    - Nennt sich die Diskretisierung einer kontinuierlichen Funktion mit einer anderen kontinuierlichen Funktion "Abtastung"?
    - Durch was kann eine Funktion, die die Dirichlet-Bedingungen erfüllt, dargestellt werden?
    - Welcher Operation entspricht eine Faltung zweier Funktionen im Ortsraum im Frequenzraum?
    - Welche Operation wird genutzt, um die Frequenzanteile einer Funktion zu erhalten?
    - Angenommen, das Abtasttheorem von Shannon wird nicht eingehalten. Wie kann dennoch Aliasing verhindert werden ohne die Abtastfrequenz zu erhöhen?
* Bilder
    - Wie können redundante Daten bei der Bildkompression eliminiert werden?
    - Wie entsteht Aliasing?
    - Was sind Vor- und Nachteile von Frequenzraum-Filtern gegenüber Ortsraum-Filtern?
    - Was sind die fünf Teilschritte der JPEG-Kompression?
    - In welchem Teilschritt der JPEG-Kompression werden psychovisuelle Effekte verwendet, um besser zu komprimieren?
    - Welche Merkmale eines Bildes können anhand des dazugehörigen Histogramms erkannt werden?
    - Was sind zwei Aspekte der Maske eines Hochpassfilters im Ortsraum und was kann damit berechnet werden?
    - Ist ein Binomial- oder ein Median-Filter schneller?
    - Ist der Laplacian-Filter ein Hoch-, Tief- oder Bandpass-Filter?
    - Sei \(I\) ein Bild und \(J\) ein Filter. Wie kann die Faltung mit dem Filter so umgeformt werden, dass die Faltung im Fourierraum geschieht. Nutze dabei \( \mathcal{F}(\cdot) \), um eine Funktion zu Fourier-Transformieren.
* Bildverarbeitung
    - Was versteht man unter "Image Blurring"? Welcher Filter kann diesen Effekt \zB hervorrufen?
    - Was sind die beiden Probleme, die bei Deblurring auftreten können?
    - Was ist eine formale Lösung des ersten Problems?
    - Welche Auswirkung hat die Wahl des Parameters \(R\) auf das Rauschen und die Kanten eines Bildes? Welche Filter entstehen bei unterschiedlicher Wahl von \(R\)?
    - Was sind Vor- und Nachteile bei der Anwendung des "Scale-Space-Ansatzes"?
    - Wie lautet die Perona-Malik-Gleichung und was bedeutet der Parameter \(c\)?
    - Was sind zwei Vorteile von Menhrschrittverfahren bezogen auf die Stoppzeit und Image Blurring (insbesondere bei dem Verfahren der Totalen Variation)?
    - Zur Bildverbesserung können partielle Diffusionsgleichungen genutzt werden, sodass das Bild in jedem Zeitschritt verbessert oder vereinfach wird. Was wird bei Perona-Malik und der Totalen Varation gemacht, damit sich kein gleichmäßig graues Bild ergibt?
    - Laut Hadamard ist das Problem "Deblurring" nicht korrekt gestellt. Was wird (\bspw bei dem Wiener-Filter) dagegen getan, um dem entgegenzuwirken?
* Grafikpipeline
    - Wieso sollte die Darstellungsreihenfolge innerhalb eines Baumes konsistet bleiben?
    - Was ist der wesentliche Unterschied zwischen einem Quadtree und einem BSP-Tree?
    - Was ist die maximale Anzahl an Knoten (inklusive Blätter), die ein Quadtree haben kann, um ein \( 8 \times 8 \) Raster darzustellen?
    - Was ist die minimale Anzahl an Knoten, die ein Octree haben kann, um ein \( 4 \times 4 \times 4 \) Raster darzustellen?
    - Was ist der Unterschied zwischen VR und AR?
    - Was ist VR-Sickness und was sind die Ähnlichkeiten sowie Unterschiede zu Motion-Sickness?
    - Was sind Vor- und Nachteile des Painters Algorithmus?
    - Was ist Culling und wieso wird es verwendet?
    - Was ist Rasterisierung?
    - Wie viele Pixel (inklusive Start- und Endpixel) werden beim Bresenham-Algorithmus gezeichnet, wenn Starkpunkt \( (2, 4) \) und Endpunkt \( (6, 8) \) gegeben sind?
    - Aus welchen drei Komponenten setzt sich die Leuchtdichte \( I_\text{total} \) beim Phong-Shading zusammen?
    - Was ist ein weiteres Schattierungsverfahren (außer Phong-Shading)?
    - Auf welche der folgenden Aussagen trifft VR, AR oder beide (B) zu: [\dots ist ein detaillierter und physikalisch korrekter Nachbau der realen Welt.; \dots ermöglicht beim Betrachten über einen Monitor eine Veränderung der Farben eines realen Gemäldes.; \dots verwendet Methoden des Visual Computing.]
* Transformationen
    - Was sind uwei Unterschiede zwischen perspektischer und paralleler Projektion?
    - Was sind jeweils zwei Anwendungen von perspektischer und paralleler Projektion und weshalb?
    - Ist die Verkettung beliebiger affiner Abbildungen kommutativ?
    - Sind Projektionstransformationen affine Abbildungen?
    - Ist die Transformationsmatrix einer Skalierung eine Diagonalmatrix?
    - Welche drei Schritte müssen durchgeführt werden, um ein beliebiges Objekt im Raum um eine beliebige Raumache zu drehen?
    - In welcher Stelle der Grafikpipeline werden Transformationen genutzt und wie?
    - Wie viele Dimensionen haben homogene Koordinaten, wenn die assoziierten inhomogenen Koordinaten \(n\)-dimensional sind?
* 3D-Visualisierung
    - Wie kann eine Lehmfigur am besten in ein 3D-Modell umgewandelt werden, ohne diese zu berühren?
    - Was sind die Unterschiede zwischen direkter und undirekter Volumenvisualisierung (\bzgl Komplexität und Metadarstellung)?
    - Was sind drei Arten von Culling und was bewirken diese?
    - Wie wird eine Delaunay-Triangulation aus einem Voronoi-Diagramm erstellt und umgekehrt?
    - Was sind drei Basisoperationen der Volumen-Rendering-Pipeline?
    - Für welche zwei Dinge wird ein Transferfunktion verwendet?
    - Was sind zwei Einsatzgebiete, in denen 3D-Daten vorkommen?
    - Wozu wird der Marching Squares Algorithmus verwendet?
    - Ist die Anzahl Dreiecke ein geeignetes Maß für die Komplexität eines Objekts? Wie viele Dreiecke werden benötigt, um eine Kugel exakt darzustellen?
* Szenengraphen
    - Welche vier Informationen werden zum Rendering einer 3D-Szene benötigt?
    - Was sind die Vorteile des Szenengraph-Konzepts?
    - Was wird unter dem Begriff "X3DOM" verstanden?
* Informationsvisualisierung
    - Was sind Vor- und Nachteile einer multivariaten Scatterplotmatrix?
    - Was sind zwei Beispiele für hierarchische Daten und wie können diese visualisiert werden?
    - Wie lauten die vier Schritte sowie die drei "Interaktionen" im Referenzmodell von Card in der korrekten Reihenfolge?
    - Welche zwei Visualisierungstechniken eignen sich, um 1D-Daten ohne Zeit darzustellen? Welche ist besser?
    - Können 1D-Daten durch parallele Koordinaten dargestellt werden?
* Farbe
    - Was sind die Unterschiede der in der Vorlesung genannten technischen Farbräume \bzgl der Farbdarstellung?
    - Was sind möglich Arten der Metamerie und was bedeuten diese?
    - Was ist der Unterschied zwischen bezogenen und unbezogenen Farben?
    - Was bedeuten die Begriffe "Weißpunkt", "Farbton", "Farbsättigung" und "Komplementfarbe" \bzgl eines CIE~XY~Chromaticity Diagramms?
    - Was sind drei Attribute der Farbwahrnehmung?
    - Welcher Begriff wird durch die Aussage "Ob zwei verschiedene Farbreize bei gleichen Betrachtungsbedingungen für zwei verschiedene Personen unterschiedliche Farbreize erzeugen, hängt von den Spektralwertmatrizen der Personen ab." beschrieben?
    - Welcher Begriff wurd durch die Aussage "Dieser Gegenfarbraum modelliert Nichtlinearitäten des visuellen Systems und ist nahezu wahrnehmungsgleichabständig." beschrieben?
    - Welcher Begriff wird durch die Auusage "Eine Erhöhung der Leuchtdichte erhöht den Kontrast." beschrieben?
    - Welcher Begriff wird durch die Aussage "Eine Erhöhung der Leuchtdichte erhöht die Farbigkeit." beschrieben?
    - Welcher Begriff wird durch die Aussage "Eine Gegenfarbe im Hintergrund verstärkt die Farbwirkung." beschrieben?
* Interaktion und User Interfaces
    - Was sind, neben der Kommandozeile, vier weitere Interaktionsmöglichkeiten?
    - Was ist das Problem bei 3D-Interaktion mit 2D-Eingabegeräten?
    - Wofür steht "WIMP"?
* Multimedia Information Retrieval
    - Welche Möglichkeiten der Spezifizierung einer Suchanfrage gibt es (neben Text) noch?
    - Was ist eine Möglichkeit, den Inhalt eines Multimediaobjekts zu beschreiben?
    - Welche vier Bedingungen muss eine Metrik \( d : S \times S \to \R \) erfüllen muss?
    - Zu welchen dieser Bedingungen können Beispiele gefunden werden, bei denen die menschliche Wahrnehmung von Unterschieden nicht einer Metrik entspricht?
    - Was sind generalisierte Dokumente?
