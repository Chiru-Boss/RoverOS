"""Conservative PAN/TILT bench test.

Run from repository root:
  python -m tests.test_servos --port /dev/ttyUSB0
  python -m tests.test_servos --port COM6

Use only after verifying the servo supply and clearing the mechanism.
The ±30 degree test range is intentionally conservative.
"""
import argparse
import time

from app.servo_controller import RoverServoController


def main() -> None:
    parser = argparse.ArgumentParser(description="RoverOS servo bench test")
    parser.add_argument("--port", default="/dev/ttyUSB0")
    parser.add_argument("--baud", type=int, default=115200)
    args = parser.parse_args()

    with RoverServoController(port=args.port, baud=args.baud) as rover:
        print("Centering")
        rover.center()
        time.sleep(1)

        print("PAN: left, right, center")
        rover.move_pan(-30)
        time.sleep(1)
        rover.move_pan(30)
        time.sleep(1)
        rover.move_pan(0)
        time.sleep(1)

        print("TILT: down, up, center")
        rover.move_tilt(-30)
        time.sleep(1)
        rover.move_tilt(30)
        time.sleep(1)
        rover.move_tilt(0)
        print("Bench test complete")


if __name__ == "__main__":
    main()
