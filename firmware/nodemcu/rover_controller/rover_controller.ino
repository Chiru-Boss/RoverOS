/*
 * RoverOS NodeMCU ESP8266 controller
 * Serial: 115200 baud, newline-terminated commands
 * Commands: PING, PAN:<0..180>, TILT:<0..180>
 * Pins: PAN D5/GPIO14, TILT D6/GPIO12
 *
 * Logical angle mapping lives on the Pi:
 * PAN -90 left, 0 center, +90 right
 * TILT -90 down, 0 center, +90 up
 *
 * Servo power must use a verified regulated external supply.
 * Share its GND with NodeMCU GND. Never use the 3V3 pin for servo power.
 */
#include <Servo.h>

Servo panServo;
Servo tiltServo;

const uint8_t PAN_PIN = D5;
const uint8_t TILT_PIN = D6;
int panAngle = 90;
int tiltAngle = 90;

void setup() {
  Serial.begin(115200);
  delay(300);
  panServo.attach(PAN_PIN);
  tiltServo.attach(TILT_PIN);
  panServo.write(panAngle);
  tiltServo.write(tiltAngle);
  Serial.println("RoverOS NodeMCU Ready");
}

void loop() {
  if (!Serial.available()) return;

  String command = Serial.readStringUntil('\n');
  command.trim();

  if (command == "PING") {
    Serial.println("PONG");
    return;
  }

  if (command.startsWith("PAN:")) {
    panAngle = constrain(command.substring(4).toInt(), 0, 180);
    panServo.write(panAngle);
  } else if (command.startsWith("TILT:")) {
    tiltAngle = constrain(command.substring(5).toInt(), 0, 180);
    tiltServo.write(tiltAngle);
  } else {
    Serial.println("ERR:UNKNOWN_COMMAND");
    return;
  }

  Serial.print("PAN:");
  Serial.print(panAngle);
  Serial.print(" TILT:");
  Serial.println(tiltAngle);
}
