# RoverOS

AI-assisted mobile rover project using a Raspberry Pi 4 as the high-level coordinator, a NodeMCU ESP8266 for deterministic low-level control and safety, and a separate ESP32-CAM for video capture/streaming.

## Current status

- Raspberry Pi ↔ NodeMCU USB serial communication tested at 115200 baud.
- PING/PONG two-way serial test passed.
- PAN/TILT command acknowledgements and logical-angle conversion tested.
- SG90 physical movement has been observed, but axis reliability, power integrity, and mechanical calibration remain under diagnosis. Serial acknowledgements do not prove physical movement.

## Hardware roles

- Raspberry Pi 4: Python coordinator, phone web UI, camera coordination, future Gemini integration.
- NodeMCU ESP8266: local servo/motor control, bounded commands, deterministic safety and stop behavior.
- ESP32-CAM: separate camera capture/streaming device; no direct motor control.
- Phone: manual controls, task requests, camera view and emergency stop.

AI proposals must be validated by the Raspberry Pi and constrained by NodeMCU safety logic. AI must never directly bypass the local controller.

## Repository layout

```text
RoverOS/
├── app/                         # Raspberry Pi Python application
├── config/                      # Safe example configuration only
├── docs/                        # Architecture, safety, workflow and status
├── firmware/nodemcu/             # ESP8266 Arduino firmware
├── tests/                        # Serial and actuator tests
├── .gitignore
├── requirements.txt
└── README.md
```

## PAN/TILT convention

- PAN: logical -90° = left, 0° = center, +90° = right.
- TILT: logical -90° = down, 0° = center, +90° = up.
- Python converts logical angles to servo command angles by adding 90°.
- PAN signal: D5 (GPIO14). TILT signal: D6 (GPIO12).
- Bench tests use conservative ±30° movement until physical limits are calibrated.

## Quick start — Windows

1. Install Git, Python 3.11+, Arduino IDE and GitHub Desktop.
2. Clone this repository.
3. Open `firmware/nodemcu/rover_controller/rover_controller.ino` in Arduino IDE.
4. Select **NodeMCU 1.0 (ESP-12E Module)** and the correct COM port.
5. Upload only with safe power/wiring confirmed.
6. Install Python requirements: `py -m pip install -r requirements.txt`.

## Quick start — Raspberry Pi

```bash
git clone https://github.com/Chiru-Boss/RoverOS.git
cd RoverOS
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m app.serial_test --port /dev/ttyUSB0
```

Run the servo bench test only after checking the power and mechanism:

```bash
python -m tests.test_servos --port /dev/ttyUSB0
```

Close Arduino Serial Monitor before opening the same serial port from Python. Only one process should own a serial port at a time.

## Safety essentials

- Never power SG90 servos from NodeMCU 3V3.
- Do not assume VIN can safely power a servo.
- Use a verified regulated 5V supply with sufficient current capacity.
- Connect external servo supply GND to NodeMCU GND; do not connect external +5V to VIN or 3V3.
- Verify converter output with a multimeter before connecting servos. If it cannot be verified, do not guess.
- Use correctly protected Li-ion cells and a charger appropriate to the pack configuration. Never bypass protection.
- Disconnect power before changing wiring. Stop for stalling, continuous buzzing, overheating, or controller resets.
- Keep motors disabled until voltage/current ratings and the safety controller are verified.

See `docs/hardware-and-safety.md` before powering actuators.

## Two-environment workflow

- Home / Windows: NodeMCU firmware, servo calibration, motor/sensor bench tests.
- College / Raspberry Pi: Python coordinator, serial integration, web UI, camera and AI integration.
- Pull before starting; commit and push after a tested milestone. Never edit the same file independently in both places without synchronizing.

See `docs/development-workflow.md` and `docs/project-status.md`.
