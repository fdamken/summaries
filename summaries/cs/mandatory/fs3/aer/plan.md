# AER Cheatsheet: Planung

## Inhalt und Struktur

* Bluespec
    - Grundlagen [ab 3]
        + Vergleich zu anderen HDLs [5]
        + Zerlegungshierarchie [16, 17]
        + Methodenarten [23]
        + Zuweisungsoperatoren
    - Ausführungssemantik [ab 37]
        + `WILL_FIRE`
        + Parallelität [44]
        + Nebenläufigkeit
            * Ablaufplan [46, 47]
                - Ausführungsreihenfolge
                - Beeinflussung [118]
            * Konflikte [48]
                - Häufige Ursachen [60]
        + Pipelines [35, 87]
            * Dynamisch (vs. statisch)
            * Elastisch (vs. inelastisch/starr)
    - Synthetisierung [131]
        + Beeinflussung siehe Komponenten
    - Komponenten
        + FIFOs (Normal FIFO, Pipeline FIFO [113], Bypass FIFO [114]) [52]
        + Tagged Unions
        + Tupel
        + CReg [91, 101]
        + Scheduling Attributes
            * `descending_urgency` [123]
            * `execution_order` [124]
            * `preempts` [128]
            * `mutually_exklusive` [129, 130]
        + `synthesize` [137, 138]
* Teil 1: Hardware-Entwurfstechniken
    - Entwurfsebenen (Abstraktionsgrad) [39, 40]
    - Ablauf der Synthese [59]
    - Design Constraints (Einschränkungen) [62]
    - Verifikation [68]
        + Prä-Synthese-Simulation [69]
        + Post-Synthese-Simulation [69]
        + Post-Layout-Simulation [73]
* Teil 2: Rekonfigurierbare System-on-Chips am Beispiel des Xilinx Zynq 7000
    - ARM Cortex-A9 Prozessorkern [16, 17, 18, 19, 20, 21, 22, 23, 24]
    - SIMD Rechnungen mit NEON [25]
    - Speichersystem [26, 27, 28]
    - Programmierbare Logik (PL) [30, 31, 32]
    - Hard Core vs. Soft Core [35]
    - Schnittstellen PS <--> PL [41]
        + General Purpose Interface
        + High Performance Interface
        + ACP Interface
    - HP vs. ACP [51, 52]
    - AXI4 [54, 55, 56]
        + Signalisierung [57]
        + Beispiele [59, 60]
    - IP-Blöcke [64]
* Teil 3: Entwurfsverfahren und Werkzeuge für Hardware-Rechenbeschleuniger
    - Hardware Klassifikation [6, 7]
    - Hardware Anforderungen [16]
        + Performanz [17]
        + Energieverbrauch [18]
        + Einmalkosten [19, 20]
    - Moore's Law [8]
        + Death [9]
    - Patterson's Walls [10]
        + Power Wall [11]
        + Memory Wall [12]
        + Instruction-Level-Parallelism Wall [13]
        + Brick Wall [14]
    - FPGA Arbeitsablauf [24]
