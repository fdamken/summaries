# CNuvS Cheatsheet :: Planung

## Foliensätze

* [x] Kapitel 0: Orga
* [x] Kapitel 1: Quick Tour
* [x] Kapitel 2: Routing
* [x] Kapitel 3: Internetworking
* [x] Kapitel 4: Transport Layer
* [x] Kapitel 5: Queueing Theory
* [x] Kapitel 6: Multicast
* [x] Kapitel 7: Application Layer



## Themen

* Introduction {1}
    - Information vs. Data vs. Signal {1.11, 1.12}
    - Properties of Communication {1.13}
    - Simplex {1.16}
    - Half Duplex {1.16}
    - Full Duplex {1.17, 1.18}
    - Switching {1.23}
        + Circuit Switching {1.24}
        + Packet Switching {1.25, 1.26}
    - Multiplexing {1.27}
        + Time Division Multiplexing {1.28}
        + Frequency Division Multiplexing {1.28}
        + CDM, SDM {1.29}
    - Broadcast Medium {1.30, 1.31}
    - Network Types {1.52}
        + Connection-Oriented {1.53, 1.54}
        + Connectionless-Oriented {1.55}
* OSI Layer Architecture {1.44, 1.45, 1.46, 1.47, 1.48, 1.49, 1.50, 1.51}
* Routing {1.5, 2.10}
    - Forwarding {2.6, 2.7}
    - Optimization Criteria {2.12, 2.13}
    - Routing Algorithms {2.14}
        + Flooding {2.15, 2.16}
        + Hot Potato {1.33}
        + Static Routing {1.34, 1.35, 2.17}
        + Adaptive Routing Algorithms {2.18}
            * Centralized Adaptive Routing {2.20}
            * Isolated Adaptive Routing {2.22}
                - Backward Learning Routing {2.23}
            * Distributed Adaptive Routing {2.25}
        + Distance Vector Routing {2.27+}
            * Poisened Reverse {2.38, 2.39}
            * Split Horizon {2.40}
        + Link-State Routing {2.42, 2.43, 2.44}
        + DVR/LSR {2.44}
        + Hierarchical Routing {2.49}
            * Autonomous Systems (AS) {2.50, 2.51, 2.52}
            * Intra-AS/Inter-AS {2.53, 2.54}
            * Inter-AS {2.55, 2.56}
        + Border Gateway Protocol {2.64, 2.65, 2.66, 2.67, 2.68, 2.69}
            * Scale {2.70, 2.72, 2.73}
            * Security {2.75, 2.81, 2.82, 2.83, 2.84, 2.85}
        + Mobile Routing {"/Mobile Networks/Routing"}
        + Overlay Routing {2.97, 2.98, 2.99, 2.101}
* Mobile Networks {2.87}
    - Routing {2.86, 2.88, 2.89}
        + Dynamic Source Routing {2.92, 2.93, 2.94, 2.95}
    - Clustering {2.96}
* Internetworking {1.5, 3.7, 3.12}
    - Datagrams {3.8}
    - IP Packet Format {3.13, 3.14, 3.15}
    - Addressing {3.16, 3.19, 3.20, 3.26}
        + Classes {3.21, 3.22, 3.32}
            * CIDR {3.33, 3.34}
        + Special Addresses {3.23}
        + Netmask {3.24}
        + Subnet {3.27, 3.30}
        + VLSM {3.31}
    - DHCP {3.39}
    - NAT {3.40, 3.41, 3.43, 3.44}
    - ARP/RARP {3.45, 3.46}
    - IPv6 {3.48}
        + Packet Format {3.49}
        + Addressing {3.50}
        + Transition from IPv4 {3.51, 3.52}
        + More IPv6 {3.53}
* Transport {1.5, 4.3, 4.5}
    - Addressing (Ports) {4.7, 4.8, 4.9}
        + Trivia {4.10}
    - Multiplexing/Demultiplexing {4.12, 4.13}
    - Segmenting, Reassembling {4.14}
    - Connection Control {4.15, 4.16, 4.17, 4.18, 4.19, 4.20, 4.21, 4.22, 4.23}
        + Three-Way Handshake {4.24, 4.25, 4.26, 4.32}
        + Connection Rejection {4.27}
        + Connection Release {4.29}
        + Two-Army Problem {4.30}
    - Reliable Delivery {4.33}
        + Error Control {4.44}
        + ARQ {4.45, 4.46}
    - Flow Control {4.34}
        + Buffer Allocation {4.35}
        + Alternating-Bit Protocol {4.36, 4.38}
        + Stop/Continue Messages {4.39}
        + Rate Based {4.40}
        + Credit Based {4.41}
            * Sliding Window {4.43}
    - Congestion Control {4.47, 4.48, 4.54, 4.55, 4.66}
        + Design Properties/Options {4.56, 4.57, 4.58, 4.59}
        + Packet Dropping, Implicit Feedback {4.60, 4.61}
        + Proactive Actions {4.62}
            * Choke Packets {4.63}
            * Warning Bits {4.64}
            * Random Early Detection {4.65}
    - UDP {4.68}
        + Segment Format {4.69, 4.72}
        + Demultiplexing {4.70, 4.71}
    - TCP {4.74}
        + Segment Format {4.75}
        + Demultiplexing {4.76, 4.77, 4.78}
        + Sequence Numbers, ACKs {4.79}
            * Retransmission {4.92, 4.93}
                - Fast Retransmit {4.95, 4.96}
        + Connection Control {4.81, 4.86}
        + Send/Receive Buffers {4.97}
        + Flow Control: Advertised Window {4.98, 4.99}
        + Congestion Control {4.100, 4.111, 4.112}
            * ACK-Clocking {4.101, 4.102, 4.103, 4.104}
            * Additive/Multiplicative Increase/Decrease {4.105, 4.106}
            * Slow Start {4.107, 4.108}
    - SCTP {4.127}
    - DCCP {4.128}
    - RTP {4.129, 4.131}
    - RTCP {4.129}
    - QUIC {4.137, 4.138, 4.139}
* Queueing Theory {1.5, 5.9}
    - Definitions, Notations {5.10}
        + Time Diagrams {5.11}
        + Arrivals/Departures {5.12, 5.15, 5.16}
        + Utilization {5.14}
        + Kendall's Notation {5.29}
            * M/M/1 Queues {5.30, 5.31, 5.32, 5.33, 5.34, 5.35}
            * M/M/m Queues {5.36, 5.37}
            * M/M/1/N Queues {5.39}
            * Summary {5.43}
            * M/M/1 vs. M/M/m {5.45, 5.50}
    - Little's Law {5.13}
    - Stochastic Processes {5.17, 5.18}
        + Markov Process {5.19}
        + Birth-Death Process {5.20, 5.21}
            * Equilibrium {5.27, 5.28}
    - Queueing Problems {5.22, 5.23, 5.24}
    - Poissen Process {5.25, 5.26}
* Multicast {1.5, 6.4, 6.5}
    - Methods {6.9}
        + Multicast via Unicast {6.6}
        + Network Multicast {6.7}
        + Application-Layer Multicats {6.8}
    - Internet Multicast Service Model {6.10}
    - Multicast Group {6.10, 6.11, 6.14}
        + Addressing {6.12}
        + Joining {6.15}
        + IGMP {6.16, 6.17, 6.18}
    - Transmission/Delivery (LSN/TttI) {6.13}
    - Routing {6.21, 6.22}
        + Flooding {6.22, 6.23}
        + Spanning Trees {6.24}
        + Shared Tree: Steiner Tree {6.25, 6.26}
        + Core Based Trees {6.27}
        + Shortes Path Tree {6.29}
        + Reverse Path Forwarding {6.30}
            * Pruning {6.31}
    - Reliable Multicast (NACK) {6.34, 6.35, 6.36}
* Applications/Distributed Systems {1.5, 7.3, 7.4}
    - Definition of Distributed {7.6, 7.7}
    - Client-Server Model {7.8, 7.9, 7.171}
        + Iterative Server {7.10}
        + Concurrent Server {7.11}
    - Peer-to-Peer {7.172, 7.173}
    - Client-Server vs. Peer-to-Peer {7.170}
    - Berkeley Socket-Interface API {7.12, 7.13}
        + Connectionless {7.14}
        + Connectionloss connect {7.15}
        + Connection-Oriented {7.16}
    - DNS {7.30, 7.31, 7.32}
        + Zones {7.33}
        + TLD, Authority {7.34}
        + Resolver {7.35}
            * Caching Servers {7.35, 7.41}
        + Hierarichal Database {7.36}
            * Root Name Servers {7.37}
        + Message Format {7.38, 7.39}
        + Records {7.40, 7.43}
        + Queries {7.49, 7.50}
    - HTTP {7.78, 7.79, 7.80}
        + Persistent {7.81, 7.85}
        + Non-Persistent {7.81, 7.82, 7.83}
        + Response Time Modelling {7.84}
        + HTTP Request {7.86, 7.89}
        + HTTP Response {7.90, 7.91}
        + HTTP/2 {7.96}
    - Usages of Decentralization {7.174}
        + P2P File Sharing {7.175}
        + P2P Centralized Directory {7.176, 7.177}
        + Query Flooding {7.178}
        + Gnutella {7.178, 7.179, 7.180}
        + KaZaA {7.181, 7.182}
        + DHT {7.183}
        + Chord {7.184}
