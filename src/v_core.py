import math

class VKernel:
    """
    V-KERNEL: The Human Operating System Logic.
    Based on Vector Laws: Reality (Y) = Intent (X) / Resistance (Z).
    """

    def __init__(self, user_name):
        self.operator = user_name
        print(f"SYSTEM: Kernel initialized for operator [{self.operator}]")

    def calculate_reality(self, intent_x, resistance_z):
        """
        The Master Formula: T = X / Z
        """
        if resistance_z <= 0:
            return "ERROR: Singularity (Infinite Light). Resistance cannot be zero in 3D."
        
        reality_y = intent_x / resistance_z
        return round(reality_y, 3)

    def scan_spin(self, number):
        """
        Determines the Vector of Energy based on Tesla Code (3-6-9).
        """
        if number in [3, 6]:
            return "MAGNETIC (Flux Field)"
        elif number == 9:
            return "VOID (Zero Point Energy)"
        else:
            return "ELECTRIC (Matter)"

# --- SIMULATION ---
# Let's run the V-Code

human = VKernel("Architect")

# Scenario 1: High Fear (High Z)
# Intent = 100, Fear = 80
result_1 = human.calculate_reality(intent_x=100, resistance_z=80)
print(f"Scenario 1 (Fear): Reality Level = {result_1} (Low Signal)")

# Scenario 2: High Spirit (Low Z)
# Intent = 100, Fear = 5
result_2 = human.calculate_reality(intent_x=100, resistance_z=5)
print(f"Scenario 2 (Flow): Reality Level = {result_2} (Superconductivity)")

# Tesla Check
print(f"Number 3 is: {human.scan_spin(3)}")
print(f"Number 9 is: {human.scan_spin(9)}")
print(f"Number 4 is: {human.scan_spin(4)}")
    def get_frequency_color(self, reality_level):
        """
        Translates Reality Level (Y) into Visible Spectrum (Chakras/Physics).
        Based on the frequency of the wave created by Intent / Resistance.
        """
        # Low Reality (High Resistance) -> Low Frequency (Red/Survival)
        if reality_level < 1.0:
            return "RED (Infrastructure/Fear/Root)"
            
        # Medium Reality -> Mid Frequency (Green/Action)
        elif 1.0 <= reality_level < 10.0:
            return "GREEN (Heart/Flow/Growth)"
            
        # High Reality -> High Frequency (Blue/Communication)
        elif 10.0 <= reality_level < 50.0:
            return "BLUE (Truth/Structure/Logic)"
            
        # Ultra Reality -> Very High Frequency (Violet/Quantum)
        elif reality_level >= 50.0:
            return "VIOLET (Spirit/Integration/Gamma Waves)"
            
        else:
            return "BLACK (Entropy/Shadow)"

# --- ТЕСТ НОВОГО МОДУЛЯ ---
# Додай це в кінці свого файлу:

print(f"Scenario 1 Color: {human.get_frequency_color(result_1)}") 
# Виведе: GREEN (бо 100/80 = 1.25)

print(f"Scenario 2 Color: {human.get_frequency_color(result_2)}")
# Виведе: BLUE (бо 100/5 = 20.0)
