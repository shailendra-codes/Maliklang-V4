import time
import math
from collections import deque

class AirspaceDiscoveryEngine:
    def __init__(self, memory_threshold_mb=512):
        self.memory_threshold = memory_threshold_mb
        self.cosmic_telemetry_stream = deque(maxlen=100)
        print("🪐 Discovery Engine Active: Monitoring Unknown Space Anomalies!")

    def discover_unknown_anomaly(self, raw_signal_matrix: list) -> dict:
        current_timestamp = time.time()
        anomaly_detected = False
        threat_score = 0.0
        classification = "SYSTEM_STABLE"
       
        if not raw_signal_matrix:
            return {"status": False, "type": classification}

        mean = sum(raw_signal_matrix) / len(raw_signal_matrix)
        variance = sum((x - mean) ** 2 for x in raw_signal_matrix) / len(raw_signal_matrix)
        std_dev = math.sqrt(variance) if variance > 0 else 1.0
       
        for signal in raw_signal_matrix:
            z_score = abs(signal - mean) / std_dev
            if z_score > 4.5:
                anomaly_detected = True
                threat_score += 0.25

        if anomaly_detected and threat_score > 0.5:
            if std_dev > 100.0:
                classification = "SPACE_DEBRIS_OR_SOLAR_FLARE_INDUCED_CORRUPTION"
            else:
                classification = "ZERO_DAY_MILITARY_GRADE_JAMMING_ATTACK"
               
            print(f"🪐 [DISCOVERY ALERT]: Unknown Anomaly Discovered! Type: {classification}")
            return {
                "status": True,
                "type": classification,
                "threat_confidence": min(threat_score * 100, 100.0),
                "timestamp": current_timestamp,
                "suggested_action": "RE_ROUTE_AIRCRAFT_AND_FLUSH_MEM_CACHE"
            }

        return {"status": False, "type": "SYSTEM_STABLE", "threat_confidence": 0.0}
 
