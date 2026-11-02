"""Raspberry Pi serial interface for RoverOS PAN/TILT servos."""

from __future__ import annotations

import time

import serial


class RoverServoController:
    """Control PAN/TILT with logical angles from -90 to +90 degrees."""

    def __init__(
        self,
        port: str = "/dev/ttyUSB0",
        baud: int = 115200,
        timeout: float = 2.0,
        step: int = 3,
        step_delay: float = 0.08,
        initial_pan: int = 0,
        initial_tilt: int = 0,
    ) -> None:
        if step < 1:
            raise ValueError("step must be at least 1")
        if step_delay < 0:
            raise ValueError("step_delay cannot be negative")
        self.ser = serial.Serial(port, baudrate=baud, timeout=timeout)
        # Opening ESP8266 serial may reset the board.
        time.sleep(2)
        self.ser.reset_input_buffer()
        self.step = step
        self.step_delay = step_delay
        self.pan_angle = self._validate(initial_pan)
        self.tilt_angle = self._validate(initial_tilt)

    @staticmethod
    def _validate(angle: int) -> int:
        if not -90 <= angle <= 90:
            raise ValueError("Logical angle must be between -90 and +90")
        return int(angle)

    def _send(self, axis: str, logical_angle: int) -> str:
        command_angle = self._validate(logical_angle) + 90
        self.ser.write(f"{axis}:{command_angle}\n".encode("ascii"))
        self.ser.flush()
        response = self.ser.readline().decode("utf-8", errors="replace").strip()
        if not response.startswith("PAN:") or "TILT:" not in response:
            raise RuntimeError(f"Unexpected NodeMCU response: {response!r}")
        return response

    def _smooth_move(self, axis: str, target: int) -> None:
        target = self._validate(target)
        current = self.pan_angle if axis == "PAN" else self.tilt_angle
        while current != target:
            delta = min(self.step, abs(target - current))
            current += delta if target > current else -delta
            response = self._send(axis, current)
            print(f"NodeMCU: {response}", flush=True)
            if axis == "PAN":
                self.pan_angle = current
            else:
                self.tilt_angle = current
            if self.step_delay:
                time.sleep(self.step_delay)

    def move_pan(self, angle: int) -> None:
        """-90 left, 0 center, +90 right."""
        self._smooth_move("PAN", angle)

    def move_tilt(self, angle: int) -> None:
        """-90 down, 0 center, +90 up."""
        self._smooth_move("TILT", angle)

    def center(self) -> None:
        self.move_pan(0)
        self.move_tilt(0)

    def close(self) -> None:
        if getattr(self, "ser", None) and self.ser.is_open:
            self.ser.close()

    def __enter__(self) -> "RoverServoController":
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.close()
