# RoverOS Architecture

## Device responsibilities

### Raspberry Pi 4 — high-level coordinator
- Runs the Python application and phone-facing web server.
- Accepts operator input and high-level task requests.
- Validates bounded commands before forwarding them to NodeMCU.
- Future: Gemini vision/reasoning and camera coordination.
- Must not bypass NodeMCU safety logic.

### NodeMCU ESP8266 — low-level controller
- Receives bounded commands from the Pi.
- Controls motor-driver inputs and servo signal outputs.
- Owns deterministic local safety, command timeout and emergency stop.
- Must start with actuator outputs in a safe stopped state.
- Future: local obstacle checks and sensor handling.

### ESP32-CAM — camera subsystem
- Handles image capture and video streaming.
- Does not directly control rover motors.
- Provides image/video to the Raspberry Pi over the local network.

### Phone — operator interface
- Manual driving, camera pan/tilt, task requests, camera view and emergency stop.

## Initial communication

USB serial between Raspberry Pi and NodeMCU at 115200 baud. Commands are newline-terminated. Current prototype commands: `PING`, `PAN:<0..180>`, `TILT:<0..180>`.

This is a bring-up protocol, not the final safety protocol. Before motor actuation, add command validation, explicit STOP, heartbeat/lease timeout, watchdog behavior and bounded command schema.

## Camera coordinates

- PAN: -90° left, 0° center, +90° right.
- TILT: -90° down, 0° center, +90° up.
- Python maps logical angles to servo command angles by adding 90°.
- Physical limits must be calibrated to the actual camera mount. Do not assume the full nominal SG90 range is safe when mounted.
