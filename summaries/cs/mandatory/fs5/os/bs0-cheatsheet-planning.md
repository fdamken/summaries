# BS Cheatsheet :: Planung

## Foliensätze

* [x] Kapitel 1: Introduction
* [x] Kapitel 2: Processes and Inter-Process-Communication
* [x] Kapitel 3: Threads
* [x] Kapitel 4: Deadlocks
* [x] Kapitel 5: Scheduling
* [x] Kapitel 6: Mutual Exclusion, Races and Semaphores
* [x] Kapitel 7: Memory Management I
* [x] Kapitel 8: Memory Management II
* [x] Kapitel 9: I/O
* [x] Kapitel 10.1: File Systems I
* [x] Kapitel 10.2: File Systems I Extents
* [x] Kapitel 11: File Systems II
* [x] Kapitel 12: Virtualization
* [x] Kapitel 13: OS Security
* [x] Kapitel 14: Q&A



## Themen

* Introduction {1}
    - History {1.8, 1.9, 1.10, 1.11, 1.12, 1.13, 1.14}
    - Definition: Hardware Abstraction {1.15, 1.16, 1.17, 1.18, 1.19, 1.20, 1.21, 1.22, 1.23, 1.24, 1.25, 1.26, 1.27, 1.28, 1.32}
        + Portable Operating System Interface (POSIX) {1.33}
        + Linux Standard Base (LSB) {1.34}
        + x86 Rings {1.35}
        + Monolithic vs. Microkernel {1.36}
    - Definition: Coordinate {1.38, 1.39, 1.40, 1.41}
* Processes and Inter-Process-Communication {2.2}
    - Processes {2.3, 2.4, 2.5, 2.11}
        + Process Family and Hierarchy {2.15, 2.16, 2.17}
    - Concurrency {2.6, 2.7}
    - Process Management {2.8, 2.12, 2.18, 2.20, 2.36}
        + Process Control Block {2.8, 2.9, 2.10}
        + Process Creation {2.12, 2.13, 2.14}
        + Process Termination {2.18, 2.19}
        + Inter-Process-Communication {2.20, 2.21, 2.22, 2.23}
    - Inter-Process-Communication Models {2.24, 2.28}
        + Shared Memory {2.25, 2.26, 2.27}
        + Message Passing {2.28, 2.29}
            * Addressing {2.30, 2.31}
            * Synchronization {2.32}
            * Message Buffering {2.33}
        + Example: (A)LPC in Windows {2.34}
    - Client-Server: Pipes {2.35}
* Threads {3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.8, 3.9}
    - Example: Multi-Threaded Web Server {3.7}
    - Theoretical Speedup {3.10}
    - Implementations {3.11, 3.12}
        + Many-to-One {3.13}
        + One-to-One {3.14}
        + Many-to-Many {3.15}
        + Two-level Model {3.16}
    - Linux Threads/Tasks {3.17}
    - POSIX Threads (C) {3.18}
    - Single to Multi-Threaded {3.19, 3.20}
    - Threads vs. Processes {3.21, 3.22, 3.23}
    - Java Virtual Machine {3.24}
* Deadlocks and Resource Management {N/A}
    - Resource Management {4.1}
        + Google Chubby Lock Service {4.3}
        + Resource Sharing und Inter-Process-Interaction {4.4, 4.5}
            * Mutual Exclusion {4.6}
    - Deadlock/Livelock and Starvation {4.7}
    - Deadlock Conditions {4.8}
    - Deadlock Modeling und Visualization {4.12, 4.13, 4.14}
    - Deadlock Strategies {4.9, 4.10, 4.11}
        + Detection {4.20, 18.2, 18.3, 18.4, 18.5}
            * One Resource per Type {4.15, 4.16, 4.17}
            * Multiple Resources per Type {4.17, 4.18}
            * Process Selection {4.19}
        + Recovery {4.21}
        + Avoidance {4.22, 4.23, 4.24, 4.25, 4.26}
            * Banker's Algorithm for a Single Resource {4.27}
            * Banker's Algorithm for Multiple Resource {4.28, 4.29}
        + Prevention {4.31}
            * Attacking the Mutual Exclusion Condition {4.32}
            * Attacking the Hold and Wait Condition {4.33}
            * Attacking the No Preemption Condition {4.34}
            * Attacking the Circular Wait Condition {4.35}
* Scheduling {5.1, 5.2}
    - Scheduling Criteria (Optimizations) {5.3}
    - Issues {5.4, 5.5}
    - Determining Length of next CPU Burst {5.6}
    - Flavors of Scheduling {5.7, 5.23, 5.27}
        + First Come, First Serve (Non-Preemptive) (FCFS) {5.8, 5.9, 5.10}
        + Shortest-Job-First {5.17, 5.18}
            * Non-Preemptive (SJF) {5.11, 5.12, 5.13}
            * Preemptive (SJF-P) {5.14, 5.15}
            * Adaptive Preemptive (A.SJF/SRTF) {5.16}
        + Round Robin (RR/TDMA) with Fixed Slots {5.19, 5.20, 5.21, 5.22}
        + Priority Scheduling (PS) {5.24, 5.25}
    - OS Examples {5.28}
        + Multilevel Feedback Queue {5.29}
        + Solaris {5.30, 5.32}
        + Windows {5.33}
        + Linux {5.34}
    - Scheduler Location {5.35, 5.36, 5.37, 5.38, 5.39}
* Mutual Exclusion {6.1}
    - Concurrent Access to Shared Resources {6.2, 6.3}
    - Taxonomy of Software Misbehavior {6.4, 6.5, 6.6, 6.7}
    - Critical Sections {6.8}
    - Mutual Exclusion and Critical Sections {6.9, 6.10}
    - Mutual Exclusion Strategies {6.11}
        + Interrupts {6.12, 6.13}
        + Process Alternation {6.14, 6.15}
        + Locks {6.16, 6.17, 6.18, 6.19}
            * Spin Locks {6.20, 6.21, 6.22}
            * Barriers {6.23}
        + Semaphores {6.24}
            * Ordering {6.25}
            * Producer/Consumer {6.26, 6.27}
    - Classical Problems {6.28}
        + Dining Philosophers {6.29, 6.30, 6.31}
        + Readers-Writers Problem {6.32, 6.33, 6.34}
* Memory Management {7.1}
    - Abstraction {7.2, 7.3, 7.4, 7.5, 7.6, 8.2}
    - Avoiding Slow Disk Loads in Commodity Systems {7.7}
        + Solution: Address Spaces {7.8, 7.9}
    - Address Space Implementations {7.10}
    - Base and Bounds {7.11, 7.12, 7.13}
        + Memory Layout {7.14}
        + Memory Safety {7.15}
        + Requirements {7.16}
        + OS/Hardware Interactions {N/A}
            * Boot {7.17}
            * Process Creation {7.18}
            * Process Execution {7.19, 7.21}
            * Context Switch {7.20}
        + Pros and Cons {7.22}
    - Segmentation {7.23, 7.24, 8.6}
        + Memory Layout {7.25, 7.26, 8.3}
        + Address Translation {7.27, 7.28, 8.4}
        + Stack Address Calculation {8.5}
    - Paging {8.7, 8.27}
        + Address Translation {8.8}
        + Implementation {8.9}
        + Problems {8.10, 8.20}
        + Caching {8.13, 8.14, 8.15, 8.16, 8.17, 8.18, 8.19}
        + Combining Paging and Segmentation {8.21, 8.22}
    - Multi-Level Page Tables {8.23, 8.24, 8.25, 8.26}
    - Swapping Pages to Disk {8.28, 8.29, 8.40}
        + Page Replacement Policies {8.30, 8.37, 8.38, 8.39}
            * Belady's Optimal Page Replacement "MIN" {8.31}
            * FIFO Replacement {8.32}
            * Second Chance FIFO Replacement {8.33}
            * Random Replacement {8.34, 8.35}
            * LRU {8.36}
* Input/Output {9.1, 9.2, 9.31}
    - Hardware {9.4, 9.20}
        + Device Types {9.3}
        + Device Controllers {9.5}
        + Accessing Devices {9.6, 9.7, 9.8}
            * Direct Memory Access {9.18, 9.19}
        + Programmed I/O (Direct Memory Access, DMA) {9.9, 18.6, 18.7, 18.8, 18.9}
        + Interrupts {9.10, 9.11, 18.10}
            * Interrupt-Driven I/O {9.12, 9.13, 9.14}
        + Buffer Strategies {9.15, 9.16}
        + Reduce Data Shuffling Load {9.17}
    - Device Diversity and Drivers {9.21, 9.22, 9.23, 9.24, 9.25}
        + Uniform Interfacing {9.26}
        + Trustwothiness Problems {9.27}
        + Solution Attempts {9.28}
    - I/O Interfaces and Abstraction {9.29}
        + Example: Linux Device Interface {9.30}
* File Systems {10.1, 10.2, 10.24, 10.40, 11.33}
    - Abstraction {10.3}
        + Files, Files and Paths {10.4}
        + File Extensions {10.5}
    - Common File Operations {10.6, 10.8, 10.11, 10.15, 10.17}
        + File Descriptors {10.8}
        + \texttt{open()} {10.7}
        + \texttt{read()} {10.10}
        + \texttt{write()} {10.11}
        + \texttt{close()} {10.16}
        + POSIX File Redirection {10.12, 10.13}
    - File Information (\texttt{stat}) {10.18}
    - Links {N/A}
        + Hard Links {10.19, 10.20, 10.21}
        + Symbolic Links {10.22, 10.23}
    - Reducing Operation Latencies {10.27, 10.28, 10.29}
    - Associating Files with Data Blocks {10.30}
    - Indices (inodes) {10.32, 10.33, 10.34, 11.2}
    - Indirect Addressing {10.35}
    - Extents {10.38, 18.11}
    - Performance and Timing {11.3, 11.4 11.5, 11.6, 11.7, 11.14}
        + Scheduling {11.8}
            * First Come, First Serve (FCFS) {11.9}
            * Shortest Seek Time First (SSTF) {11.10}
            * SCAN or Elevator Algorithm (SCAN) {11.11}
            * Circular SCAN (C-SCAN) {11.12}
            * LOOK and C-LOOK Variants of SCAN and C-SCAN (LOOK and C-LOOK) {11.13}
    - Common File Systems {N/A}
        + vsfs: Very Simple File System {10.25, 10.26}
        + FAT {10.31, 10.1.1, 18.12, 18.13, 18.14, 18.15, 18.16, 18.17}
        + ext3 {10.36, 10.37}
        + ext4 {10.29}
        + FFS: The Fast File System {11.15, 11.16, 11.17, 11.18, 11.19, 11.20, 11.21, 11.22, 11.23, 11.24, 11.25, 11.26, 11.27}
        + VFS: Virtual File System {11.28, 11.29, 11.30, 11.31, 11.32, 11.33}
* Virtualization {12.1, 12.2, 12.3, 12.35}
    - Reasons for Virtual Machines (VMs) {12.4, 12.5, 12.6}
    - Virtualization Differences {12.7, 12.8}
    - VM Implementation Requirements {12.9}
    - Safety/Liveness {12.10, 12.11}
    - Trap and Emulate {12.12, 12.13, 12.14, 12.18}
        + Paravirtualization {12.15}
        + Binary Rewriting {12.16}
        + Hardware Extensions (Intel VT-x, AMD SVM) {12.17}
    - Memory {12.19, 12.22, 12.23, 12.24, 12.25}
        + Shadow Page Tables {12.20}
        + Extended Page Tables {12.21}
        + Ballooning {12.26}
    - I/O {12.27, 12.28, 12.29, 12.30, 12.31, 12.32, 12.33, 12.34}
* OS Security {13.1, 13.2, 13.5, 13.13, 13.22, 13.30, CSS-Summary Chapter 7}
    - Bell-LaPadula Model {13.3}
    - Biba Model {13.4}
    - Multiuser System Model {13.6}
    - Inter-Process-Protection {13.7}
        + Access Control Lists (ACLs) {13.8}
        + UID and GID {13.9}
        + The Superuser {13.10}
        + Alternative: Capabilities {13.11}
    - Protected from Processes {13.12}
    - Hardware Bug: Meltdown {13.14, 13.18, 13.19}
        + Pipelining and Data Dependencies {13.15}
        + Out-of-Order and Speculative Execution {13.16, 13.17}
        + Mitigation: KPTI {13.20}
    - Exploitable Software Bugs {13.23}
        + Buffer Overflow {13.24, 13.25}
        + String Format Vulnerabilities {13.26, 13.27}
        + Return-Oriented Programming (ROP) {13.28, 13.29}
