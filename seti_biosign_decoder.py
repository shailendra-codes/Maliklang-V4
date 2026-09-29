import math
from collections import Counter

class SETIBioSignDecoder:
    def __init__(self):
        print("🛸 Alien Life Detection Shield Active: Tuning into Interstellar Frequencies!")

    def decode_interstellar_signal(self, frequency_stream: list) -> dict:
        if len(frequency_stream) < 10:
            return {"life_detected": False, "confidence": 0.0, "reason": "Signal too weak"}

        data_counts = Counter(frequency_stream)
        total_elements = len(frequency_stream)
        entropy = -sum((count / total_elements) * math.log2(count / total_elements) for count in data_counts.values())

        unique_patterns = list(data_counts.keys())
       
        if entropy < 3.0 and len(unique_patterns) > 2:
            confidence_score = (3.0 - entropy) * 40.0 + 20.0
            print("🛸 [EXTRATERRESTRIAL ALERT]: Confirmed Non-Natural Signal Pattern Discovered!")
            return {
                "life_detected": True,
                "confidence": min(confidence_score, 100.0),
                "signal_entropy": round(entropy, 4),
                "classification": "INTELLIGENT_ALIEN_BEACON",
                "recommended_action": "ALERT_UN_AND_GLOBAL_SPACE_AGENCIES"
            }

        return {
            "life_detected": False,
            "confidence": 0.0,
            "signal_entropy": round(entropy, 4),
            "classification": "NATURAL_COSMIC_NOISE"
        }
 
