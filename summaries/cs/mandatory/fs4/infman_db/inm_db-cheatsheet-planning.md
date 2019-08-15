# InfMan DB Cheatsheet :: Planung

## Foliensätze

* [x] Kapitel 0: Organisatorisches
* [x] Kapitel 1: Grundlagen
* [x] Kapitel 2: Datenbankarchitekturen
* [x] Kapitel 3: Konzeptionelle Datenmodellierung
* [x] Kapitel 4: Logische Datenmodellierung
* [x] Kapitel 5: Logische Abfragemodelle
* [x] Kapitel 6: Anfragesprachen
* [x] Kapitel 7: SQL und Programmiersprachen
* [x] Kapitel 8: Transaktionen und Mehrbenutzerbetrieb
* [x] Kapitel 9: Indexstrukturen und Performanz
* [x] Kapitel 10: Neuere Datenbankkonzepte



## Themen

* Einführung {1}
    - Daten, Informationen und Wissen {1.3, 1.5, 1.6, 1.7}
        + Informationskreislauf {1.9}
        + Strukturierungsgrad {1.10}
            * Strukturierte Daten {1.11}
            * Semistrukturierte Daten {1.12}
            * Unstrukturierte Daten {1.13, 1.14}
    - Informationsmanagement {1.15, 1.16}
        + Informationssystem {1.17}
        + Typischer Entwurfsprozess {1.18, 1.19, 1.20}
        + Datenzugang {1.21}
* Datenbankarchitekturen {2}
    - Datenbanksysteme {2.3}
        + Ehemalige Systeme, Nachteile und Probleme {2.4, 2.5, 2.6}
        + Datenintegration, -unabhängigkeit {2.7, 2.8, 2.11}
        + Abgrenzung: DB vs. DBMS vs. DBS {2.9, 2.10}
        + DBMS {2.13}
            * Aufgaben eines DBMS {2.12}
        + DBS {2.14}
    - Architekturmodelle {2.16, 2.17, 2.18}
        + Schemaarchitektur {2.18, 2.19, 2.23}
            * Datenunabhängigkeit {2.20, 2.21}
            * Anfragenbearbeitung und -ergebnis {2.22}
        + Systemarchitektur {2.18}
        + Anwendungsarchitektur {2.18}
* Konzeptionelle Datenmodellierung {3, 3.3}
    - Wissensrepräsentation {3.5}
        + Semiotisches Dreieck {3.7, 3.8}
            * Intension, Merkmale, Extension, Instanz {3.8, 3.9}
        + Merksmalsrepräsentation {3.10}
        + Objektbeschreibung {3.11}
    - Datenmodellierung {3.12, 3.13, 3.14, 3.15, 3.16}
        + Konzeptuelle Datenmodellierung {3.17, 3.18}
    - Entitäten-Beziehungsmodell (ERM) {3.19, 3.20}
        + Entitätstypen {3.22, 3.23}
            * Abhängiger/Schwacher Entitätstyp {3.42}
        + Beziehungstypen {3.24, 3.25}
            * Stelligkeit/Grad {3.32}
            * Ternäre Beziehungstypen {3.33, 3.34, 3.35}
            * Rekursive Beziehungen und Rollennamen {3.36}
            * Kardinalitäten {3.37, 3.38, 3.39, 3.40}
            * Funktionale Beziehungen {3.41}
        + Attribute {3.26, 3.27}
            * Schlüsselattribute {3.29, 3.30}
        + Notationsübersicht {3.43}
* Logische Datenmodellierung {4}
    - Relationales Modell {4.4, 4.5, 4.13}
        + Tupel {4.6}
        + Relationenschema {4.7}
        + Relation {4.8, 4.9}
        + Notation {4.10}
    - Schlüssel {4.14, 4.15}
        + Formale Definition {4.16, 4.18}
            * Superschlüssel {4.16, 4.17}
            * Schlüsselkandidat {4.17}
            * Primärschlüssel (PK) {4.17}
        + Attribut- und Schlüsselmengen {4.21}
        + Künstliche Schlüssel {4.23}
        + Schlüsselbeziehungen {4.24}
    - Logischer Entwurf {4.26, 4.27}
        + Notation für Relationenschemata {4.29}
        + Abbildung von Entitätstypen {4.30, 4.33}
        + Abbildung von Beziehungstypen {4.35}
        + Schlüssel von Beziehungsrelationen {4.37, 4.38, 4.39}
    - Datenbanknormalisierung {4.42, 4.43, 4.44}
        + Redundanz und Anomalien {4.45}
            * Update-Anomalie {4.46}
            * Einfüge-Anomalie {4.47}
            * Lösch-Anomalie {4.48}
        + Funktionale Abhängigkeit (FD) {4.52, 4.53}
            * Semantik {4.54}
            * FD-Hülle {4.55}
            * Attributhülle {4.83}
            * Armstrong-Axiome {4.56, 4.57}
            * Volle/Partielle Funktionale Abhängigkeiten {6.64}
        + Transitive Abhängigkeit {4.68}
        + Normalformen {4.60, 4.75, 4.81}
            * Erste Normalform {4.61, 4.62, 4.63}
            * Zweite Normalform {4.65, 4.66, 4.67}
            * Dritte Normalform {4.69, 4.70, 4.71}
            * Boyce-Codd Normalform {4.72, 4.73}
    - Syntheseverfahren {4.82, 4.84, 4.85}
* Logische Abfragemodelle {5, 5.3, 5.4}
    - Relationenalgebra (RA) {5.5, 5.6}
        + Grundlegende Operatoren {5.13}
            * Vereinigung {5.7}
            * Mengendifferenz {5.8}
            * Kartesisches Produkt {5.9}
            * Spaltenumbenennung {5.10}
            * Projektion {5.11}
            * Selektion {5.12}
        + Abgeleitete Operatoren {-}
            * Schnittmenge {5.14}
            * Quotient {5.15}
            * Verbund (Join) {5.16}
                - Theta-Join {5.17}
                - Equijoin {5.18}
                - Natural Join {5.19}
                - Semijoin {5.20}
                - Entarteter Join {5.36}
        + Select-Project-Join-Queries (SPJ-Queries) {5.23}
    - Relationenkalküle {5.27, 5.28}
    - Relationentupelkalkül (RTK) {5.30}
    - Relationenwertebereichkalkül (RWK) {5.37, 5.38, 5.41}
    - RA vs. RTK {5.33, 5.34}
    - RA, RTK, RWK vs. Anfragesprachen {5.42}
        + Mächtigkeit {5.43}
    - Änderungsoperationne {5.44, 5.55}
        + Einfügen {5.46}
        + Löschen {5.47}
        + Verändern {5.48}
* Anfragesprachen {6}
    - Structured Query Language (SQL) {6.3, 6.4}
        + Datentypen {6.11}
        + Wertebereiche {6.12}
        + `NULL` {6.16, 6.18}
    - Datendefinitionssprache (DDL) {6.7}
        + Relationen vs. Tabellen {6.8}
        + Tabellen Erstellen {6.9}
        + Tabellen Löschen {6.13}
        + Tabellen Ändern {6.14}
        + Integritätsbedingungen {6.19, 6.20}
            * Eindeutigkeit {6.21}
            * Primärschlüssel {6.22}
            * Fremdschlüssel {6.23, 6.24, 6.26, 6.27}
        + Tabellentypen {6.28}
    - Datenabfragesprachen (DQL) {6.34, 6.35}
        + `SELECT` {6.36, 6.43}
        + Projektion {6.37}
        + Selektion {6.38}
        + Selektionsbedingung {6.39}
            * Ähnlichkeitsbedingung {6.40}
        + Mengenoperationen {6.44}
        + Duplikate {6.46}
        + Sortierung {6.47}
        + Verschaltete Abfragen {6.48, 6.49}
            * Alternative Formulierung {6.50}
        + Tupelvariablen und Produkt {6.51}
        + Relationentupelkalkül {6.52}
        + Verbund (Join) {6.53, 6.55}
            * Cross Join {6.56}
            * Union Join {6.57}
            * Natural Join {6.58}
            * Inner Join {6.59}
            * Left Outer Join {6.60}
            * Right Outer Join {6.61}
            * Natural Full Outer Join {6.62}
        + Spaltenumbenennung {6.63}
        + Funktionen {6.63}
        + Aggregatfunktionen {6.64}
        + Gruppierung {6.66}
    - Datenmanipulationssprache (DML) {6.69, 6.70}
        + Daten Löschen {6.71}
            * Alle Daten Löschen {6.73}
        + Daten Ändern {6.74}
        + Daten Einfügen {6.76}
    - Weiterführende Themen {6.78}
        + Sichten (Views) {6.79, 6.80, 6.81, 6.82}
* SQL und Programmiersprachen {7}
    - Datenbankanfragen {7.3}
    - Relation vs. Tupel {7.7}
    - Cursor {7.8}
    - Zugriff aus Java {7.4, 7.5}
        + Abfragen {7.6}
        + Cursor {7.9}
        + Wiederkehrende Anfragen {7.10}
        + Vorbereitete Anfragen (Prepared Statements) {7.11}
        + Parametrisierte Anfragen {7.12, 7.13}
    - SQL Injection {7.14}
    - Objektrelationale Abbildung (ORM) {7.15}
* Transaktionen und Mehrbenutzerbetrieb {8}
    - Transaktionen {8.3, 8.4}
        + Terminierung {8.5, 8.7}
        + Konsistenz {8.8}
        + ACID-Eigenschaften {8.9}
    - Anomalien im Mehrbenutzerbetrieb {8.11, 8.12}
        + Inkonsistentes Lesen {8.13, 8.14}
        + Verlorene Updates {8.15, 8.16}
        + Schreib-Lese Konflikt {8.17, 8.18}
        + Phantomproblem {8.19, 8.20}
    - Serialisierbarkeit {8.21}
        + Serielle vs. Verschränkte Ausführung {8.22}
        + Serialisierbarkeit {8.23}
        + Sperren {8.24, 8.25}
        + Verklemmung (Deadlock) {8.26, 8.27}
            * Detektion {8.29}
    - Sperrprotokolle {8.21}
        + Zwei-Phasen Sperrprotokoll (2PL) {8.30, 8.31}
        + Konservative Sperrprotokolle {8.32}
        + Strikte Sperrprotokolle {8.33}
    - Isolationsgrade {8.35, 8.36, 8.47, 8.48}
        + `SERIALIZABLE` {8.37, 8.38}
        + `REPEATABLE READ` {8.39, 8.42}
        + `READ COMMITTED` {8.40, 8.41, 8.43, 8.46}
        + `READ UNCOMMITTED` {8.44, 8.45}
* Indexstrukturen und Performanz {9, 9.3}
    - Datenbankindizierung {9.4, 9.5}
        + Binäre Suche {9.7}
        + Sortierte Tabellen {9.8}
        + Index {9.9, 9.11, 9.12, 9.13}
            * Indexverwaltung in SQL {9.10}
    - Indexanatomie {9.14}
        + Binärer Suchbaum {9.15, 9.16}
            * Entarteter Binärer Suchbaum {9.17}
            * Balancierter Binärer Suchbaum {9.18}
        + B-Baum {9.19}
        + \( \text{B}^+ \)-Baum Index {4.20}
        + Zusammengesetzter Index {4.21}
    - Ausführungspläne {9.22, 9.23}
        + Optimizer {9.24, 9.25}
        + Zugriffe {-}
            * Durchsuchen der Tabelle {9.27, 9.28}
            * Eindeutiger Indexzugriff {9.29}
            * Verfolgen von Indexknoten {9.30}
            * Verfolgen der RID {9.31}
        + Probleme {9.32, 9.33, 9.34}
    - Indexdesign {9.35, 9.36, 9.38}
        + 1-Sterne Index {9.39}
        + 2-Sterne Index {9.40}
        + 3-Sterne Index {9.41}
* Neuere Datenbankkonzepte (Ausblick) {10}
    - In-Memory Datenbanken {10.3}
        + Zeitvergleich {10.4, 10.5}
        + Kompression {10.6, 10.7}
    - Spaltenorientierte Datenbanken {10.8}
        + Partitionierung {10.9}
    - NoSQL {10.12}
        + Key-Value Datenbanken {10.13}
        + Triple Speicher {10.14}
        + Graphdatenbanken {10.15, 10.16}
        + Dokumentenorientierte Datenbanken {10.17}
    - CAP-Theorem {10.10}
