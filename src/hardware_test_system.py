import csv
import random
from datetime import datetime
from pathlib import Path


# ---------------------------------------------------------
# Python-Based Automated Hardware Test System Simulation
# ---------------------------------------------------------
# This project simulates a real hardware validation workflow.
# It checks voltage, current, temperature, and sensor output
# and generates a PASS/FAIL test report.
# ---------------------------------------------------------


def generate_device_readings(device_id):
    """
    Simulates measurement readings from a Device Under Test.

    In real hardware testing, these values could come from:
    - Multimeter
    - Oscilloscope
    - Power supply
    - Sensor module
    - Microcontroller serial output
    """

    voltage = round(random.uniform(4.5, 5.5), 2)        # volts
    current = round(random.uniform(0.10, 0.80), 2)      # amps
    temperature = round(random.uniform(25, 85), 2)      # Celsius
    sensor_output = round(random.uniform(0.0, 3.3), 2)  # volts

    return {
        "device_id": device_id,
        "voltage": voltage,
        "current": current,
        "temperature": temperature,
        "sensor_output": sensor_output
    }


def run_tests(readings):
    """
    Checks whether each measurement is within the acceptable test limits.
    """

    test_results = {}

    # Voltage must be between 4.8V and 5.2V
    if 4.8 <= readings["voltage"] <= 5.2:
        test_results["voltage_test"] = "PASS"
    else:
        test_results["voltage_test"] = "FAIL"

    # Current must be between 0.20A and 0.60A
    if 0.20 <= readings["current"] <= 0.60:
        test_results["current_test"] = "PASS"
    else:
        test_results["current_test"] = "FAIL"

    # Temperature must be 70°C or lower
    if readings["temperature"] <= 70:
        test_results["temperature_test"] = "PASS"
    else:
        test_results["temperature_test"] = "FAIL"

    # Sensor output must be between 0.5V and 3.0V
    if 0.5 <= readings["sensor_output"] <= 3.0:
        test_results["sensor_test"] = "PASS"
    else:
        test_results["sensor_test"] = "FAIL"

    # Overall result
    if all(result == "PASS" for result in test_results.values()):
        test_results["overall_result"] = "PASS"
    else:
        test_results["overall_result"] = "FAIL"

    return test_results


def save_results_to_csv(all_results, filename):
    """
    Saves all test results into a CSV file.
    CSV files can be opened in Excel.
    """

    fieldnames = [
        "timestamp",
        "device_id",
        "voltage",
        "current",
        "temperature",
        "sensor_output",
        "voltage_test",
        "current_test",
        "temperature_test",
        "sensor_test",
        "overall_result"
    ]

    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for result in all_results:
            writer.writerow(result)


def print_result(result):
    """
    Prints one device test result clearly in the terminal.
    """

    print("-" * 60)
    print(f"Device ID: {result['device_id']}")
    print(f"Voltage: {result['voltage']} V -> {result['voltage_test']}")
    print(f"Current: {result['current']} A -> {result['current_test']}")
    print(f"Temperature: {result['temperature']} °C -> {result['temperature_test']}")
    print(f"Sensor Output: {result['sensor_output']} V -> {result['sensor_test']}")
    print(f"Overall Result: {result['overall_result']}")


def print_summary(all_results, number_of_devices):
    """
    Prints the final test summary.
    """

    passed_devices = sum(1 for result in all_results if result["overall_result"] == "PASS")
    failed_devices = number_of_devices - passed_devices

    pass_rate = (passed_devices / number_of_devices) * 100
    fail_rate = (failed_devices / number_of_devices) * 100

    print("-" * 60)
    print("Test Summary")
    print("-" * 60)
    print(f"Total Devices Tested: {number_of_devices}")
    print(f"Passed Devices: {passed_devices}")
    print(f"Failed Devices: {failed_devices}")
    print(f"Pass Rate: {pass_rate:.1f}%")
    print(f"Fail Rate: {fail_rate:.1f}%")


def main():
    print("Python-Based Automated Hardware Test System Simulation")
    print("=" * 60)

    number_of_devices = 10
    all_results = []

    for device_number in range(1, number_of_devices + 1):
        device_id = f"DUT_{device_number:03d}"

        readings = generate_device_readings(device_id)
        test_results = run_tests(readings)

        final_result = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "device_id": readings["device_id"],
            "voltage": readings["voltage"],
            "current": readings["current"],
            "temperature": readings["temperature"],
            "sensor_output": readings["sensor_output"],
            "voltage_test": test_results["voltage_test"],
            "current_test": test_results["current_test"],
            "temperature_test": test_results["temperature_test"],
            "sensor_test": test_results["sensor_test"],
            "overall_result": test_results["overall_result"]
        }

        all_results.append(final_result)
        print_result(final_result)

    # Create results folder if it does not exist
    project_root = Path(__file__).resolve().parent.parent
    results_folder = project_root / "results"
    results_folder.mkdir(exist_ok=True)

    output_file = results_folder / "hardware_test_results.csv"

    save_results_to_csv(all_results, output_file)

    print_summary(all_results, number_of_devices)

    print("-" * 60)
    print(f"Test completed. Results saved to: {output_file}")


if __name__ == "__main__":
    main()