import hashlib
import time
import json
from typing import List, Dict

class CV2XBroadcaster:
    """
    Layer 3: C-V2X PC5 Mode 4 Metadata Broadcasting
    """
    def __init__(self, node_id: str):
        self.node_id = node_id

    def broadcast_metadata(self, proxy_id: str, velocity: float, location: tuple) -> Dict:
        """
        Skeleton logic for broadcasting C-V2X PC5 Mode 4 metadata.
        This approach reduces bandwidth by 95% by sending lightweight cryptographic
        identities and kinematics instead of raw edge video feeds.
        """
        payload = {
            "node_id": self.node_id,
            "timestamp": time.time(),
            "proxy_id": proxy_id,
            "kinematics": {
                "velocity_ms": velocity,
                "gps_coord": location
            }
        }
        
        # Simulate network broadcast
        encoded_payload = json.dumps(payload)
        payload_size_bytes = len(encoded_payload.encode('utf-8'))
        
        print(f"[{self.node_id}] Broadcasting PC5 Mode 4 Payload ({payload_size_bytes} bytes): {encoded_payload}")
        return payload

class DistributedForensicLedger:
    """
    Layer 6: Distributed Forensic Ledger
    """
    def __init__(self):
        self.ledger = []

    def evaluate_kinematics(self, deceleration_g: float, node_logs: List[Dict]) -> str:
        """
        Triggers on a sudden deceleration (> 0.6g) to generate an immutable SHA-256 Event Hash.
        """
        CRITICAL_DECELERATION_THRESHOLD = 0.6 # in g-force
        
        if deceleration_g > CRITICAL_DECELERATION_THRESHOLD:
            print(f"[Forensic Ledger] ALERT: Sudden deceleration detected ({deceleration_g}g). Triggering consensus logging.")
            event_hash = self._generate_event_hash(node_logs)
            self._commit_to_ledger(event_hash, deceleration_g, node_logs)
            return event_hash
        else:
            print(f"[Forensic Ledger] Normal operation ({deceleration_g}g). No event triggered.")
            return ""

    def _generate_event_hash(self, node_logs: List[Dict]) -> str:
        """
        Generates an immutable SHA-256 hash from an aggregation of multiple node logs.
        """
        # Sort logs to ensure deterministic hashing across decentralized nodes
        serialized_logs = json.dumps(node_logs, sort_keys=True).encode('utf-8')
        return hashlib.sha256(serialized_logs).hexdigest()

    def _commit_to_ledger(self, event_hash: str, deceleration_g: float, node_logs: List[Dict]):
        entry = {
            "timestamp": time.time(),
            "event_hash": event_hash,
            "trigger_event": f"Hard Braking ({deceleration_g}g)",
            "log_evidence": node_logs
        }
        self.ledger.append(entry)
        print(f"[Forensic Ledger] Event successfully committed to immutable ledger. Hash: {event_hash}")

# --- Simulation Execution ---
if __name__ == "__main__":
    print("--- Testing Layer 3: C-V2X Metadata Broadcast ---")
    broadcaster = CV2XBroadcaster("RSU_NODE_01")
    # Simulating a generated Proxy ID for a legacy vehicle
    proxy_id = "f47b2e9c1a5d6f83" 
    broadcast_log = broadcaster.broadcast_metadata(proxy_id, velocity=22.5, location=(34.0522, -118.2437))
    
    print("\n--- Testing Layer 6: Distributed Forensic Ledger ---")
    ledger = DistributedForensicLedger()
    
    # Simulate a network of logs representing the legacy vehicle's state from multiple perspectives
    network_logs = [
        broadcast_log,
        {"node_id": "VEHICLE_NODE_A", "timestamp": time.time(), "proxy_id": proxy_id, "kinematics": {"velocity_ms": 10.0, "gps_coord": (34.0523, -118.2438)}}
    ]
    
    # Simulate an emergency braking event (e.g., 0.8g deceleration)
    generated_hash = ledger.evaluate_kinematics(deceleration_g=0.82, node_logs=network_logs)
