# Windows + Raspberry Pi Workflow

GitHub is the single source of truth for both environments.

## Home — Windows laptop

Use Windows for:
- NodeMCU firmware in Arduino IDE.
- Servo, motor and sensor bench tests.
- Python serial test scripts when hardware is connected to Windows.

Setup:
1. Install Git, Python 3.11+, Arduino IDE and GitHub Desktop.
2. Clone this repository.
3. Open `firmware/nodemcu/rover_controller/rover_controller.ino`.
4. Select **NodeMCU 1.0 (ESP-12E Module)** and the correct COM port.
5. Upload only after checking safe power and wiring.
6. Install Python requirements: `py -m pip install -r requirements.txt`.

## College — Raspberry Pi 4

Clone and prepare:
```bash
git clone https://github.com/Chiru-Boss/RoverOS.git
cd RoverOS
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If already cloned:
```bash
git pull --ff-only
```

## Every environment switch

1. Commit or stash local changes.
2. Push completed work.
3. On the other computer, pull the latest `main`.
4. Work on one feature at a time.
5. Record hardware test results in `docs/project-status.md`.

## Rules

- Never commit API keys, Wi-Fi passwords, tokens or private configuration.
- Do not commit `.venv`, Python caches or machine-specific settings.
- Do not edit the same file independently on Windows and Pi without synchronizing.
- Keep `main` stable; use feature branches for experiments.
- A software acknowledgement is not proof of physical actuator movement.
