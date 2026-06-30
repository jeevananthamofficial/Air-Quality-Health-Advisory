import sys
import os

# Add the current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import calc_pm25_aqi

def test_aqi():
    test_cases = [
        # Concentration, Expected AQI, Expected Category
        (5.0, 28, "Good"),
        (12.0, 56, "Moderate"),
        (35.4, 100, "Moderate"),
        (35.5, 101, "Unhealthy for Sensitive Groups"),
        (55.4, 150, "Unhealthy for Sensitive Groups"),
        (125.4, 200, "Unhealthy"),
        (125.5, 201, "Very Unhealthy"),
        (225.4, 300, "Very Unhealthy"),
        (300.0, 355, "Hazardous")
    ]
    
    print("Running AQI calculation tests...")
    all_passed = True
    for conc, expected_aqi, expected_cat in test_cases:
        aqi, cat, col, adv = calc_pm25_aqi(conc)
        passed = (aqi == expected_aqi) and (cat == expected_cat)
        status = "PASSED" if passed else "FAILED"
        print(f"Conc: {conc:5.1f} | Expected: AQI {expected_aqi} ({expected_cat}) | Got: AQI {aqi} ({cat}) -> {status}")
        if not passed:
            all_passed = False
            
    if all_passed:
        print("\nAll calculation tests passed successfully!")
    else:
        print("\nSome calculation tests failed.")
        sys.exit(1)

if __name__ == '__main__':
    test_aqi()
