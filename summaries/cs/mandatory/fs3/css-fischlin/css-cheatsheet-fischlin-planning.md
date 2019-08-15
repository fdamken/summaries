# CSS Zusammenfassung :: Planung

## Foliensätze

* [x] Kapitel 0: Orga
* [x] Kapitel 1: Einleitung
* [x] Kapitel 2: Verschlüsselung
* [x] Kapitel 3: Digitale Signaturen
* [x] Kapitel 4: Authentisierung und Autorisierung
* [x] Kapitel 5: Netzwerksicherheit
* [x] Kapitel 6: Betriebssystem-Sicherheit
* [x] Kapitel 7: Web-Sicherheit
* [x] Kapitel 8: Zusammenfassung



## Themen

* Einleitung {1.1, 8.4, 8.12}
    - Um was geht es? {1.10, 1.11, 1.14, 1.15}
    - Begriffe {1.13}
    - Risiko {1.16}
    - Schutzziele {1.17, 1.18}
    - Fragen {1}
* Grundlagen {CNuvS, InfMan}
    - Modulare Arithmetik {2.50, 2.51}
    - Modulo als Struktur vs. Operator {2.52, 2.53}
    - Hashwerte {3.13, 3.14, 3.15}
        + MD5-Kollisionen {3.37, 3.38, 3.39}
    - Netzwerkgrundlagen {5.2}
        + Schichtenmodell {5.3}
        + Kennzeichnungen {5.4}
        + Übersetzung IP \(\leftrightarrow\) MAC {5.6}
        + Routing {5.7}
        + DHCP {5.10}
        + DNS {5.12}
        + Ports {5.16}
        + ICMP {5.23}
        + TCP {5.26}
    - SQL {7.29}
* Verschlüsselung {2.1, 2.2, 2.4, 8.5}
    - Kerckhoffs-Prinzip {2.5}
    - Symmetrische Verschlüsselung {2.3, 2.36}
        + Klassiche Verschlüsselungsverfahren {2.6}
            * Skytale {2.7}
            * Caesars Shift-Cipher {2.8, 2.9, 2.10, 2.11, 2.12}
            * Vigenere-Chiffre {2.18, 2.19}
        + Zwischen klassischen und modernen Verfahren {2.20}
            * One-Time-Pad nach Shannon {2.21, 2.22, 2.23}
        + Moderne Verschlüsselungsverfahren {2.25}
            * Data Encryption Standard (DES) {2.26, 2.27}
            * Advanced Encryption Standard (AES) {2.28, 2.29}
            * Blockcipher {2.30}
                - Electronic Code Block (ECB) {2.30, 2.31}
                - ECB mit Zähler (GCM) {2.32}
                - Cipher Block Chaining (CBC) {2.33, 2.34, 2.35}
                - Angriffe auf CBC-Padding {2.37, 2.38, 2.39, 2.40, 2.41}
    - Asymmetrische Verschlüsselungen {2.43, 2.44, 2.45, 2.46}
        + Schlüsselaustausch {2.47}
            * Diffie-Hellman {2.61, 2.62, 2.63}
        + Public Key vs. Schlüsselaustausch {2.48}
        + RSA {2.49, 2.54, 2.60}
            * Sicherheit {2.55, 2.56}
            * Wahl der RSA-Parameter {2.57  }
    - Hybride Verschlüsselung {2.58, 2.59}
    - Pseudozufallsgeneratoren {2.68, 2.69}
        + RSA-Schlüsselerzeugung {2.70, 2.71}
    - Fragen {2}
* Digitale Signaturen {3.1, 3.2, 3.3, 3.4, 3.6, 8.6, 8.12}
    - Sicherheit {3.7, 3.9}
    - Moderne Signaturverfahren {3.10, 3.11}
        + Hash-and-Sign {3.12}
        + RSA-Signaturen {3.17, 3.18}
        + DSA-Signaturen {3.19, 3.20}
    - Zertifikate {3.25, 3.26, 3.27, 3.28, 3.29, 3.30}
        + Zertifikatsinhalt {3.31}
        + Schlüssel- und Zertifikatsverteilung {3.32}
        + Zertifikatsprüfung {3.33}
        + Certificate Authority (CA) {3.34, 3.35}
        + Revozierung von Zertifikaten {3.41}
    - Elektronische Signaturen {3.44, 3.45, 3.46, 3.47}
    - Message Authentication Code (MAC) {3.49}
        + Prinzip {3.50, 3.51, 3.52}
        + Authenticated Encryption {3.53}
    - Prüfsummen {3.55, 3.56}
        + Paritätsprüfsumme {3.57}
        + Cyclic Redundant Check (CRC) {3.58, 3.59, 3.60}
    - Fragen {3}
* Authentisierung und Autorisierung {4.1, 4.2, 4.3, 4.4, 8.7, 8.12}
    - Mittel zur Authentisierung {4.5, 4.6, 4.7, 4.8}
    - 2-Faktor-Authentisierung {4.9}
    - Passwörter {4.10}
        + Speicherungsmethoden {N/A}
            * Klartext {4.11}
            * Verschlüsselung {4.13, 4.14}
            * Hashing {4.15, 4.16, 4.18}
            * Salted Hashing {4.19, 4.20}
        + Pass-the-Hash-Angriffe (PtH) {4.22}
        + Stärke von Passwörter {4.24, 4.25, 4.26, 4.27, 4.28, 4.29}
            * Passwörter Testen {4.30}
        + Phishing {4.32, 4.33}
    - Tokens {4.35, 4.36}
        + Replay-Angriffe {4.37}
        + Challenge-Response {4.38}
        + Implementierung per Signaturen {4.39}
        + Implementierung per Verschlüsselung {4.40}
        + Nicht-Abstreitbarkeit von Signaturen {4.42}
        + Abstreitbarkeit von MACs {4.43}
    - Biometrie {4.44, 4.45, 4.48}
        + Fingerabdruck-Minutien {4.46}
        + Fehler {4.47}
    - CAPTCHAs {4.50, 4.51, 4.52, 4.53, 4.54, 4.55, 4.56}
    - Autorisierung {4.57, 4.58}
        + Access Control List (ACL) {4.59}
        + Modelle für Zugriffskontrollen {4.60}
            * Bell-LaPadula (BLP) {4.61, 4.62, 4.63, 4.64}
    - Federated Identity Management {4.65, 4.66}
        + Security Assertion Markup Language (SAML) {4.67, 4.68, 4.69}
        + Oauth 2.0 {4.70}
        + Single-Sign-On (SSO) {4.71}
        + Kerberos {4.73, 4.74, 4.75, 4.76, 4.77, 4.78}
    - Fragen {4}
* Netzwerksicherheit {5.1, 8.8, 8.12}
    - MAC-Spoofing {5.5}
    - ARP Spoofing {5.9}
    - Rogue DHCP {5.11}
    - DNS Spoofing (und Cache Poisoning) {5.13}
        + Gegenmaßnahmen {5.15}
    - Port Scan (Nmap) {5.17}
    - (Distributed) Denial-of-Service-Angriffe (DoS/DDoS) {5.19, 5.20, 5.22}
    - Ping of Death (PoD) {5.24}
    - Smurf Attack {5.25}
    - SYN Flood {5.27}
    - SYN-ACK Flood {5.28}
    - Firewalls {5.30, 5.31, 5.32, 5.33, 5.34}
    - Intrusion Detection und Prevention Systems {5.30, 5.36, 5.37}
    - Sichere Verbindungen {5.39, 5.40}
        + Transport Layer Security (TLS) {5.41, 5.42, 5.43, 5.44}
            * TLS 1.2: Ablauf {5.45}
    - Virtual Private Network (VPN) {5.47}
        + Transportieren vs. Tunneln {5.48}
        + Tunneln {5.49}
        + VPN {5.50, 5.51}
    - Anonymität {5.52, 5.53}
        + Onion-Routing (TOR) {5.54, 5.55}
        + Anonymität durch TOR {5.56}
    - Fragen {5}
* Betriebssystem-Sicherheit {6.1, 8.9, 8.12}
    - Malware {6.2, 6.3, 6.4}
        + Verbreitung {6.6, 6.7}
        + Antivirenprogramme {6.8}
            * Reaktives Scannen {6.9}
            * EICAR-Test {6.10}
            * Effektivität {6.11}
    - (Stack) Buffer Overflow {6.12, 6.13}
        + Smashing the Stack {6.15, 6.16, 6.17}
        + Beispiel {6.14, 6.18, 6.19, 6.20, 6.21, 6.22}
        + Gegenmaßnahmen {6.23, 6.24, 6.25}
        + Return-Orientierte Programmierung (ROP) {6.26, 6.27}
    - Isolation {6.29, 6.30}
        + Sandboxing durch VMs {6.31}
        + Container {6.32}
        + Trusted Platform Module (TPM) {6.33, 6.34}
    - Testen und Verifizieren {6.35, 6.36}
        + Arten des Testens {6.37}
        + Security Testing {6.38}
    - Spectre und Meltdown {6.43, 6.44, 6.45}
        + Effekte {6.46}
    - Fragen {6}
* Web-Sicherheit {7.1, 7.2, 8.10, 8.12}
    - Angriffspunkte {7.3, 7.4, 7.5, 7.6}
    - Cookies und Cross-Site Request Forgery (CSRF) {7.7, 7.8, 7.9}
        + Cross-Site Request Forgery {7.11}
    - Cross-Site Scripting (XSS) {7.14, 7.15, 7.16}
        + Unterarten {7.17}
            * DOM XSS {7.18, 7.19}
            * Reflected XSS Angriff {7.20}
            * Persistent XSS Angriff {7.21, 7.22, 7.23}
    - SQL-Injection {7.27, 7.28, 7.30}
        + Variationen {7.31, 7.32}
    - Verbindungssicherheit mit SSL/TLS {7.35, 7.36}
        + SSL/TLS-Heartbeat {7.38}
        + Heartbleed {7.37, 7.39}
        + Apples \texttt{goto fail;} {7.40, 7.41, 7.42}
        + Cookie-Cutter Angriff {7.43, 7.44}
        + Missverständliche SSL-APIs {7.45}
        + cURL {7.46}
    - Fragen {7}
* Weiterführende Themen {8.13}
    - Privacy: Datenanalysen {8.13}
        + Differential Privacy {7.14}
    - Usablity {8.15}
    - Availability {8.16}
    - Reliability {8.17}
    - Fragen {8}



## Fragen

* Einleitung
    - Exerzieren Sie am Beispiel Vulnerability="Systemadministrator wählt Passwort 12345678" die Sicherheitsbegriffe.
    - Bennen Sie die drei großen Schutzziele. Welche Ziele erreichen Sie z.B. mit Festplattenverschlüsselung oder Backups?
    - Unter welchem Schutzziel würden Sie Anonymität einordnen (und warum)?
* Verschlüsselung
    - Erklären Sie den Unterschied zwischen mono-alphabetischer und poly-alphabetischer Substitution. Was ist das One-Time-Pad-Verfahren für ein Typ?
    - Entwerfen Sie ein absolut sicheres Verschlüsselungssystem, das aber keine Korrektheit garantieren muss.
    - C. Lever möchte Shannons Verfahren noch sicherer machen. Er nimmt dazu zwei Schlüssel k0 und k1 und bildet Enc((k0, k1), m) = k0 xor k1 xor m. Was halten Sie davon?
    - Nennen Sie drei technische Unterschiede zwischen DES und AES.
    - Bestimmen Sie die Umkehrfunktion zu Triple: 3DES(k1|k2|k3, m) = DES(k3, DES-1(k2, DES(k1, m)))
    - Warum müssen Sie bei AES-CBC-Verschlüsselung mit Paddingauch noch 16-mal 0x10 anhängen, selbst wenn der letzte Nachrichtenblock schon auf Blocklänge ist?
    - Beschreiben Sie kurz das RSA-Verschlüsselungssystem.
    - Kann man aus jedem Public-Key-Verschlüsselungssystem ein Schlüsselaustauschverfahren konstruieren? Und umgekehrt?
    - Überlegen Sie sich, dass der Angreifer beim DH-Schlüsselaustausch den Wert gx+y berechnen kann.
* Digitale Signaturen
    - Welche Hash-Funktionen von MD5, SHA-1, SHA-2 und SHA-3 können Sie noch als kollisionsresistent ansehen?
    - Ist folgende Hashfunktion H(m1, m2) = m1 xor m2 für m1, m2 in {0, 1}^256 kollisionsresistent?
    - Was ist mit folgender Idee? Da H(m) quasi eindeutig ist, kann man H(m) als Signatur zur Nachricht m benutzen.
    - Wie funktioniert eine RSA-Signatur?
    - Diskutieren Sie folgende Aussage: "Signaturen sind die Umkehrung von Verschlüsselung.""
    - Diskutieren Sie folgende Aussage: "Jedes Signatur-Verfahren ist vom Typ Hash-and-Sign."
    - Nennen Sie (die) drei Möglichkeiten, um einen öffentlichen Schlüssel zu prüfen.
    - Können Sie sich vorstellen, warum Zertifizierungsinstanzen anno 2009 noch MD5 verwendet haben, obwohl MD5 quasi 2005 gebrochen war?
    - Diskutieren Sie Vor-und Nachteile von CRLs gegenüber OSCP zur Zertifikationsüberprüfung.
    - Warum kann man MACs nicht als elektronische Signaturen verwenden?
    - Warum ist folgendes "hybride" Signaturverfahren keine gute Idee? Um m zu signieren wähle man Schlüssel k, berechne s = Sig(sk, k) und t = MAC(k, m) und gebe (s, t, k) aus.
    - Warum kann man nicht den letzten Block einfach soals CBC-MAC der Nachricht m nehmen?
* Authentisierung und Autorisierung
    - Beschreiben Sie den Unterschied zwischen der One-Way-Eigenschaft und der Kollisionsresistenzeiner Hashfunktion.
    - Warum verwendet man nicht ein Public-Key-Verschlüsselungssystem zum Hashen, H(pw) := Enc(pk, pw), und "wirft" den geheimen Schlüssel sk weg?
    - Warum ist iteriertes Passwort-Hashing h_{j+1} = H(pw, S, hj) besser als folgende Lösung: Hash(pw, S) = H(pw, S, 1) xor H(pw, S, 2) xor ... xor H(pw, S, n)
    - Ist  #gfFhH5/Un1.gg& ein gutes Passwort?
    - Was halten Sie von folgender Vorgehensweise, um Passwörter zu erzeugen: date| md5sum Wie viel Entropie erwarten Sie?
    - Welche 2-Faktor-Authentisierungsmethoden kennen Sie noch?
    - Beschreiben Sie Challenge-Response mit Private-Key-Verschlüsselung.
    - Was ist bei folgendem 1-Runden Challenge-Response-Verfahren problematisch? Alice wählt sich ein zufälliges r selbst und sendet s = Sig(sk, r).
    - Benutzen Sie biometrische Authentisierung?
* Netzwerksicherheit
    - Erklären Sie den Unterschied zwischen einer IP-Adresse und MAC.
    - Was ist ein ARP-Spoofing-Angriff?
    - Warum kann man nicht einfach die Nachricht eines DHCP-Servers signieren, um einen Angriff zu verhindern?
    - Was ist der Unterschied zwischen einem DoS- und einem DDoS-Angriff?
    - Was ist der Unterschied zwischen einem SYN-Flood-Angriff und einem SYN-ACK-Flood-Angriff?
    - Nennen Sie einen Unterschied zwischen einer Netzwerk-Firewall und einem IDS.
    - Welche beiden Methoden zur Ableitung des gemeinsamen Schlüssels gibt es in TLS?
    - Können Sie sich den Sinn einer TLS-Verbindung ohne Client und ohne Server-Authentisierung vorstellen?
    - Erklären Sie den Unterschied zwischen Transportieren und Tunneln bei sicheren Verbindungen.
    - Wie funktioniert Onion-Verschlüsselung bei TOR?
    - Warum muss bei TOR der Sender die Route vorab wählen und überlässt die Wahl nicht den Knoten?
* Betriebssystem-Sicherheit
    - Nennen Sie die Unterschiede zwischen Würmern, Viren und Trojanern.
    - Erklären Sie die grundlegende Idee von Buffer-Overflow-Angriffen.
    - Nennen Sie weitere C-Operationen wie strcpy, die Sie für unsicher halten.
    - Was ist Sandboxing?
    - Diskutieren Sie Nachteile von Ansätzen, bei denen man vertrauenswürdige Hardware-Komponenten hat.
    - Nennen Sie Unterschiede zwischen Intels SGX-Technologie und dem TPM-Ansatz.
* Web-Sicherheit
    - Nennen Sie 5 der Top-Ten-Web-Angriffe von OWASP.
    - Erklären Sie das Prinzip der CSRF-Angriffe.
    - Angenommen, der Anwender schließt alle anderen Tabs, während er eine Session aufrecht erhält. Schützt das vor CSRF-Angriffen?
    - Nennen Sie die drei Arten von XSS-Angriffen.
    - Was ist der Unterschied zwischen einem persistenten und einem nicht-persistenten XSS-Angriff?
    - Welche Art der XSS-Angriffe ist am Schwierigsten zu verhindern?
    - Beschreiben Sie das Prinzip von SQL-Injection-Angriffen.
    - Was vermuten Sie hinter "Blind" und "Time-Based"-SQL-Injection-Angriffen?



## Lernziele

* Verschlüsselung
    - Symmetrische Verschlüsselung
    - Kandidaten in der Praxis und Verarbeitungsmodi
    - Asymmetrische Verschlüsselung
    - Kandidaten in der Praxis
    - Unterschied symmetrische und asymmetrische Verschlüsselung
    - Hybrid-Verschlüsselung
    - Schlüsselaustauschverfahren
    - Kandidaten in der Praxis
    - Unterschied asymmetrische Verschlüsselung und Schlüsselaustausch
    - Pseudozufallsgeneratoren
* Digitale Signaturen
    - Digitale Signaturen
    - Hashfunktionen
    - Kandidaten in der Praxis (Signaturverfahren + Hashfunktionen)
    - Zertifizierung von öffentlichen Schlüsseln
    - Elektronische Signaturen
    - Message Authentication Codes (MACs)
    - Kandidaten in der Praxis
    - Prüfsummen
    - Unterschied Prüfsummen vs. Signaturen und MACs
* Authentisierung und Autorisierung
    - Unterschiede Identifikation, Authentisierung, Autorisierung
    - Mittel zur Authentisierung
    - Speicherung von Passwörtern
    - Angriffe auf Passwörter
    - Challenge-Response-Verfahren
    - Vor- und Nachteile von Biometrie
    - CAPTCHAs
    - Autorisierung
    - Prinzipien van Bella-LaPaluda
    - Federated Identity Management
    - Kerberos
* Netzwerksicherheit
    - Schichtenmodell
    - IP-Adressen, MACs, Ports, ARP, DHCP, DNS
    - Wireshark und Nmap
    - DoS und DDoS-Angriffe
    - Bekannte Vertreter von (D)DoS-Angriffen
    - Firewalls und Intrusion Prevention/Detection Systems
    - iptables und Snort
    - Sichere Verbindungen per TLS (SSH, IPSec)
    - Virtual Private Networks
    - TOR
* Betriebssystem-Sicherheit
    - Unterschied Würmer, Viren, Trojaner
    - Funktionsweise von Virenscannern
    - Buffer Overflows
    - Gegenmaßnahmen zu Buffer Overflows
    - Return-Oriented Programming
    - Isolation und Sandboxing
    - Trusted Platform Modules
    - Spectre & Meltdown
* Web-Sicherheit
    - Angriffspunkte (Client, Server, Netzwerk)
    - Cookies
    - Cross-Site Request Forgery (CSRF)
    - Cross-Site Scripting (XSS)
    - SQL Injection
    - Ausgewählte TLS-Probleme (Heartbleed, Cookie Cutter, goto fail, APIs)
