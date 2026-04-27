# STAMP: Spatial-Temporal Anchored Mesh Proxy System

## 🚀 Overview
STAMP is an advanced V2X (Vehicle-to-Everything) framework designed to integrate **legacy vehicles** (non-connected cars) into modern safety networks. It focuses on low-latency, infrastructure-independent perception and messaging via a mesh of smart observers.

## 🛠️ Technical Implementation Justification
This project uses a six-layer architecture designed for infrastructure independence:

* **Perception (Layer 1):** Uses **YOLOv8** for real-time Edge AI detection (~30 FPS), enabling local processing without cloud latency.
* **Proxy Engine (Layer 2):** Generates **Temporal Proxy IDs** (multi-sensor hashing) to track unconnected vehicles.
* **Communication (Layer 3):** Leverages **C-V2X PC5 Mode 4** for direct sidelink communication and efficient message dissemination.
* **Handoff Logic (Layer 4):** Uses a probabilistic **Confidence Scoring Algorithm** (e.g., $S > 0.85$) to maintain identity continuity across observers.
* **Security (Layer 5):** Employs **ECDSA** hardware-bound signing to mitigate Sybil and replay attacks.
* **Forensics (Layer 6):** Maintains a **Distributed Forensic Ledger** with SHA-256 event hashes for tamper-evident incident evidence.

## 📊 Performance Metrics (Simulation Validated)
* **Detection Accuracy:** ≥ 93%
* **Warning Lead Time:** 10–15 seconds
* **Network Latency:** < 20 ms

## 📁 Repository Structure
* `/docs`: Technical disclosure and architecture diagrams.
* `/sim`: NS-3 and SUMO simulation configurations for mesh behavior.
* `/models`: YOLOv8 object detection configuration for legacy vehicle tagging.
