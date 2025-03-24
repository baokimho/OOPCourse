from tool import Tool
from drill import Drill
from drillbit import DrillBit
from cordlessdrill import CordlessDrill

def run_tests():
    print("\nTesting Tools and Drills...")

    tool = Tool("Bosch", "T100")
    print(tool.get_info())
    tool.use()

    drill = Drill("Makita", "D200", 1500, False)
    print(drill.get_info())
    drill.use()
    drill.set_rpm(2000)
    print(f"Updated RPM: {drill.get_rpm()}")

    cordless = CordlessDrill("DeWalt", "C300", 1200, 5)
    print(cordless.get_info())
    cordless.charge_battery(2)

    small_bit = DrillBit(8)
    large_bit = DrillBit(12)

    print(f"Small bit compatible with cordless: {small_bit.is_compatible(cordless)}")  
    print(f"Large bit compatible with cordless: {large_bit.is_compatible(cordless)}") 

    # try:
    #     DrillBit(-5)  
    # except AssertionError as e:
    #     print(f"✔ Diameter validation works: {e}")

    # try:
    #     Drill("Makita", "D200", -100, False)  
    # except AssertionError as e:
    #     print(f"✔ RPM validation works: {e}")

run_tests()
