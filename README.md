# STAMP: Spatial-Temporal Anchored Mesh Proxy System

## 🚀 Overview
[cite_start]STAMP is an advanced V2X (Vehicle-to-Everything) framework designed to integrate **legacy vehicles** (non-connected cars) into modern safety networks[cite: 39, 45]. [cite_start]It solves the 94% adoption gap by using smart vehicles as digital proxies[cite: 46, 82].

## 🛠️ Technical Implementation Justification
[cite_start]This project implements a six-layer architecture designed for infrastructure independence[cite: 57, 75, 115]:

* [cite_start]**Perception (Layer 1):** Uses **YOLOv8** for real-time Edge AI detection at 30 FPS, ensuring local processing without cloud latency[cite: 59, 117].
* [cite_start]**Proxy Engine (Layer 2):** Generates unique **Temporal Proxy IDs** using multi-sensor hashing to track unconnected vehicles[cite: 48, 121].
* [cite_start]**Communication (Layer 3):** Leverages **C-V2X PC5 Mode 4** for direct sidelink communication, reducing bandwidth by 95% compared to raw video[cite: 67, 129].
* [cite_start]**Handoff Logic (Layer 4):** A probabilistic **Confidence Scoring Algorithm** ($S > 0.85$) ensures seamless identity continuity across multiple smart observers[cite: 64, 131].
* [cite_start]**Security (Layer 5):** Employs **ECDSA** hardware-bound signing to prevent Sybil and replay attacks[cite: 69, 135].
* [cite_start]**Forensics (Layer 6):** A **Distributed Forensic Ledger** creates immutable SHA-256 event hashes for tamper-proof incident evidence[cite: 53, 146].

## 📊 Performance Metrics (Simulation Validated)
* [cite_start]**Detection Accuracy:** ≥ 93% [cite: 161]
* [cite_start]**Warning Lead Time:** 10–15 Seconds [cite: 100, 161]
* [cite_start]**Network Latency:** < 20ms [cite: 161]

## 📁 Repository Structure
* `/docs`: Technical Patent Disclosure and architecture diagrams.
* `/sim`: NS-3 and SUMO simulation configurations for mesh behavior.
* `/models`: YOLOv8 object detection configuration for legacy vehicle tagging.
