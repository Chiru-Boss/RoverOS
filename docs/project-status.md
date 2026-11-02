# RoverOS Project Status

Last updated: 2026-11-02

## Completed and observed

- Raspberry Pi 4 running Debian 12 and accessed through VS Code Remote SSH.
- NodeMCU ESP8266 identified as NodeMCU 1.0 (ESP-12E Module).
- USB serial bridge detected as CP2102.
- Raspberry Pi received periodic NodeMCU serial messages at 115200 baud.
- Two-way serial test passed: Pi sent `PING`, NodeMCU returned `PONG`.
- PAN/TILT text command acknowledgements worked for servo command values 0–180.
- Python logical angle conversion was tested: logical -45° -> command 45°, 0° -> 90°, +45° -> 135°.
- Physical movement was reported after connecting SG90 servos to an external converter supply. Later, one axis appeared not to move consistently; diagnosis remains open.

## Current pin mapping

- PAN: D5 / GPIO14.
- TILT: D6 / GPIO12.

## Open issues

- Diagnose intermittent PAN/TILT movement and verify each servo and signal pin independently.
- Confirm exact converter model, input range, output rating and output voltage with a multimeter.
- Confirm protection/charging arrangement for the two 18650 cells in parallel.
- Establish mechanically safe servo limits and confirm directions after installation.
- Add robust serial protocol framing, command validation, STOP, heartbeat and timeout behavior before motor control.
- Implement NodeMCU motor control and obstacle safety.
- Integrate Pi application and phone web interface.
- Integrate ESP32-CAM.
- Add Gemini only after deterministic safety layer is established.

## Completion rule

Software acknowledgements do not prove physical actuator movement. Record software tests and physical hardware tests separately. Do not mark PAN/TILT calibration complete until each axis has been independently tested in both directions with stable power and no mechanical binding.
