import sys
import traceback
from collections import deque

class AirspaceSelfHealer:
    def __init__(self, target_engine):
        self.target_engine = target_engine
        self.error_logs = deque(maxlen=50)
        print("🤖 Self-Healing Robot Shield Activated: Monitoring Airspace Core Live!")

    def execute_safely(self, func_name, *args, **kwargs):
        try:
            func = getattr(self.target_engine, func_name)
            return func(*args, **kwargs)
        except Exception as e:
            error_msg = traceback.format_exc()
            print(f"🚨 CRITICAL ERROR CAPTURED IN AIRSPACE LOGIC:\n{error_msg}")
            self.error_logs.append(error_msg)
            return self._auto_heal_and_retry(func_name, e, *args, **kwargs)

    def _auto_heal_and_retry(self, func_name, error_instance, *args, **kwargs):
        print("🛠️ Initiating Self-Healing Protocol...")
        if isinstance(error_instance, (LookupError, AttributeError, ValueError)):
            print("🔄 Self-Healer Action: Memory corruption suspected. Resetting Cache...")
            if hasattr(self.target_engine, 'aircraft_registry'):
                self.target_engine.aircraft_registry.clear()
            try:
                func = getattr(self.target_engine, func_name)
                return func(*args, **kwargs)
            except Exception:
                print("🛑 Fallback Stage 2: Emergency mode.")
                return "EMERGENCY_SAFE_MODE_ACTIVE"
        return False
 
