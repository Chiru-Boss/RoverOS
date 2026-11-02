"""Cross-platform NodeMCU serial PING/PONG test."""

import argparse
import time

import serial


def main() -> None:
    parser = argparse.ArgumentParser(description="Test RoverOS serial link")
    parser.add_argument("--port", default="/dev/ttyUSB0", help="e.g. /dev/ttyUSB0 or COM6")
    parser.add_argument("--baud", type=int, default=115200)
    args = parser.parse_args()

    with serial.Serial(args.port, args.baud, timeout=2) as connection:
        time.sleep(2)
        connection.reset_input_buffer()
        for _ in range(5):
            connection.write(b"PING\n")
            connection.flush()
            reply = connection.readline().decode("utf-8", errors="replace").strip()
            print(f"NodeMCU: {reply or 'NO RESPONSE'}")
            time.sleep(0.5)


if __name__ == "__main__":
    main()
