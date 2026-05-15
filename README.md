# Python-Based Automated Hardware Test System Simulation

## Project Overview

This project simulates an automated hardware test system using Python. It represents a real engineering workflow where a Device Under Test is measured, validated against test limits, and reported as PASS or FAIL.

The system generates simulated hardware readings such as voltage, current, temperature, and sensor output. Each reading is checked against predefined acceptance limits, and the final result is saved into a CSV test report.

This project demonstrates how Python can be used for hardware validation, automated testing, measurement logging, and engineering test report generation.

## Tools Used

- Python
- Command Prompt
- CSV file generation
- Microsoft Excel
- Automated test logic
- Hardware validation concepts

## Key Features

- Simulates multiple Devices Under Test
- Generates voltage, current, temperature, and sensor output readings
- Applies pass/fail limits to each measurement
- Calculates overall device test result
- Generates a CSV test report
- Provides a final pass/fail summary
- Demonstrates a real engineering test workflow

## Test Parameters

| Test Parameter | Acceptable Range | Unit |
|---|---:|---|
| Voltage | 4.8 to 5.2 | V |
| Current | 0.20 to 0.60 | A |
| Temperature | ≤ 70 | °C |
| Sensor Output | 0.5 to 3.0 | V |

## Test Workflow

```text
Simulated Device Under Test
        ↓
Measurement Generation
        ↓
Test Limit Checking
        ↓
PASS / FAIL Decision
        ↓
CSV Test Report
        ↓
Final Test Summary
```

## System Block Diagram

![Hardware Test System Block Diagram](images/hardware_test_system_block_diagram.png)

## Project Structure

```text
hardware_test_system_simulation
│
├── README.md
├── src
│   └── hardware_test_system.py
├── results
│   ├── hardware_test_results.csv
│   ├── test_summary_output.png
│   ├── csv_test_results.png
│   └── hardware_test_code.png
├── images
│   └── hardware_test_system_block_diagram.png
└── docs
    └── hardware_test_system_project_report.pdf
```

## Console Output

The program prints individual test results for each device and displays a final test summary.

![Test Summary Output](results/test_summary_output.png)

## CSV Test Results

The generated CSV file stores the measured values and pass/fail status for each device.

![CSV Test Results](results/csv_test_results.png)

## Source Code Screenshot

The Python script simulates hardware readings, applies test limits, and saves results into a CSV file.

![Hardware Test Code](results/hardware_test_code.png)

## Example Test Summary

```text
Total Devices Tested: 10
Passed Devices: 1
Failed Devices: 9
Pass Rate: 10.0%
Fail Rate: 90.0%
```

## Project Report

A detailed project report is available here:

- [Project Report PDF](docs/hardware_test_system_project_report.pdf)

## How to Run the Project

1. Open the project folder.
2. Go to the `src` folder.
3. Open Command Prompt inside the `src` folder.
4. Run the Python file using:

```text
py hardware_test_system.py
```

5. Check the generated CSV file inside the `results` folder.

## Source Files

- [Hardware Test System Python Code](src/hardware_test_system.py)
- [Hardware Test Results CSV](results/hardware_test_results.csv)
- [Project Report PDF](docs/hardware_test_system_project_report.pdf)

## What I Learned

- How automated hardware test systems work
- How to simulate a Device Under Test using Python
- How to apply engineering pass/fail limits
- How to generate CSV test reports
- How to create a basic hardware validation workflow
- How Python can support electronics and test engineering tasks

## Future Improvements

- Add graphical pass/fail charts
- Generate a fully automatic PDF test report directly from Python
- Add support for more simulated devices
- Add fault classification for failed devices
- Include test limit configuration using a separate file
- Connect the script to real hardware instruments in the future