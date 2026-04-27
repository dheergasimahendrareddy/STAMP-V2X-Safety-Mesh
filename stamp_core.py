import hashlib
import json

class ProxyIdentityEngine:
    """
    Layer 1 & 2: Sensor Fusion & Proxy ID Generation
    """
    @staticmethod
    def generate_proxy_id(shape: str, size: float, color: str, velocity: float) -> str:
        """
        Generates a 16-character Proxy ID hash based on physical attributes of the legacy vehicle.
        
        Args:
            shape (str): Vehicle shape/class (e.g., 'sedan', 'truck').
            size (float): Vehicle length/size in meters.
            color (str): Dominant vehicle color.
            velocity (float): Current velocity vector in m/s.
            
        Returns:
            str: 16-character hex string representing the Proxy Identity.
        """
        # Create a deterministic string representation of the physical attributes
        attribute_string = f"{shape}_{size:.2f}_{color}_{velocity:.2f}".encode('utf-8')
        
        # Generate SHA-256 hash
        hash_object = hashlib.sha256(attribute_string)
        
        # Extract the first 16 characters to serve as the Proxy ID
        proxy_id = hash_object.hexdigest()[:16]
        return proxy_id

class STAMPHandoffEngine:
    """
    Layer 4: Spatiotemporal Handoff Engine
    """
    @staticmethod
    def calculate_handoff_score(d_spatial: float, v_match: float, s_sim: float, r_sig: float, t_delta: float) -> float:
        """
        Calculates the Handoff Confidence Score (S) across edge nodes.
        
        S = 0.35*d_spatial + 0.25*v_match + 0.20*s_sim + 0.10*r_sig + 0.10*t_delta
        """
        S = (0.35 * d_spatial) + (0.25 * v_match) + (0.20 * s_sim) + (0.10 * r_sig) + (0.10 * t_delta)
        return S

    @staticmethod
    def authorize_handoff(score: float) -> bool:
        """
        Authorizes handoff if confidence score > 0.85
        """
        THRESHOLD = 0.85
        if score > THRESHOLD:
            print(f"[STAMP Handoff] SUCCESS: Handoff Authorized (Score: {score:.3f} > {THRESHOLD})")
            return True
        else:
            print(f"[STAMP Handoff] DENIED: Confidence too low (Score: {score:.3f} <= {THRESHOLD})")
            return False

# --- Simulation Execution ---
if __name__ == "__main__":
    print("--- Testing Layer 1 & 2: Proxy Identity Engine ---")
    proxy_id = ProxyIdentityEngine.generate_proxy_id(shape="sedan", size=4.8, color="blue", velocity=22.5)
    print(f"Generated Proxy ID for unseen legacy vehicle: {proxy_id}")
    
    print("\n--- Testing Layer 4: STAMP Handoff Engine ---")
    # Simulating normalized parameters (0 to 1 scale)
    confidence_score = STAMPHandoffEngine.calculate_handoff_score(
        d_spatial=0.92,  # Close spatial proximity mapping
        v_match=0.88,    # Velocity vectors align
        s_sim=0.95,      # High visual signature similarity
        r_sig=0.80,      # Good signal strength
        t_delta=0.90     # Tight temporal sync
    )
    
    STAMPHandoffEngine.authorize_handoff(confidence_score)
