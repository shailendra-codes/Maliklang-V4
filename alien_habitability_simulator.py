import math

class AlienHabitabilitySimulator:
    def __init__(self):
        print("🪐 Alien Habitability Simulator Active: Decoding Alien Lifestyles!")

    def simulate_exolife_environment(self, planet_mass: float, surface_temp_k: float, atmospheric_composition: dict) -> dict:
        verdict = {}
       
        # 1. श्वसन माध्यम (Hawa Check)
        max_gas = max(atmospheric_composition, key=atmospheric_composition.get) if atmospheric_composition else "Unknown"
        if max_gas == "O2":
            verdict["breathing_gas"] = "Oxygen-based aerobic respiration (Similar to Earth)"
        elif max_gas == "CO2":
            verdict["breathing_gas"] = "Carbon-Dioxide anaerobic parsing (Chemosynthetic life)"
        elif max_gas == "CH4" or max_gas == "N2":
            verdict["breathing_gas"] = "Liquid Methanotrophs (Extreme cold hydrogen reduction)"
        else:
            verdict["breathing_gas"] = f"Alternative element metabolism based on {max_gas}"

        # 2. पानी की जगह वे क्या पीते हैं (Liquid Solvent Check)
        temp_c = surface_temp_k - 273.15
        if 0 <= temp_c <= 100:
            verdict["liquid_solvent"] = "Liquid H2O (Standard Water-based biochemistry)"
            verdict["lifestyle"] = "Surface-dwelling, organic cell structures, reliant on agriculture."
        elif -180 <= temp_c <= -100:
            verdict["liquid_solvent"] = "Liquid Methane/Ethane (Cryo-life solvent)"
            verdict["lifestyle"] = "Sub-zero non-carbon based life in hydrocarbon lakes."
        elif -50 <= temp_c < 0:
            verdict["liquid_solvent"] = "Liquid Ammonia-Water mixture"
            verdict["lifestyle"] = "Sub-surface cave dwelling civilizations, dependent on geothermal heat."
        else:
            verdict["liquid_solvent"] = "Supercritical Fluids or Plasma state"
            verdict["lifestyle"] = "Energy-based or crystalline entities in floating cities."

        # 3. सभ्यता की गतिविधि (Civilization Activity)
        if planet_mass > 5.0 and surface_temp_k > 400:
            verdict["civilization_activity"] = "Deep crust mining, harvesting tectonic energy."
        else:
            verdict["civilization_activity"] = "Star-energy harvesting via orbital collectors (Kardashev Type 1.5)."

        return verdict
 
