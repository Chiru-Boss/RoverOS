# Hardware and Power Safety

This records the current prototype wiring and safety constraints. Verify every board/module label and rating before applying power; module variants differ.

## PAN/TILT signal pins

| Function | NodeMCU ESP8266 pin | GPIO |
|---|---|---|
| PAN signal | D5 | GPIO14 |
| TILT signal | D6 | GPIO12 |

Common SG90 wire colors:
- Orange/yellow: signal
- Red: positive servo supply
- Brown/black: ground

Confirm the actual servo lead; do not rely on color if the cable differs.

## Servo power

- Never power SG90 servos from NodeMCU 3V3.
- Do not assume NodeMCU VIN can safely power a servo.
- Use a verified regulated 5V supply with sufficient current capacity for the connected servos.
- Servo supply negative (GND) must connect to NodeMCU GND (common ground).
- Servo +5V goes to servo red leads only. Do not connect the external +5V rail to NodeMCU VIN or 3V3.
- Test one unloaded servo at a time first.
- Verify buck converter output with a multimeter before connecting servos. If voltage cannot be verified, do not guess or connect the load.
- Stop if a servo stalls, chatters continuously, heats up, or the NodeMCU resets.

## Li-ion cells

Two 18650 cells in parallel form a 1S2P pack (nominal around 3.6–3.7V; fully charged around 4.2V), not a 2S pack. Cells connected in parallel must be matched in chemistry, model, age, state of charge and voltage before connection. Use a suitable protection circuit and a charger designed for the actual pack configuration. Never short cells, connect mismatched cells, or bypass protection.

Identify the exact converter model and its input/output ratings. Module names such as TP4056, TP450 and generic buck/boost boards are not interchangeable. Confirm the module supports the battery input range and required output current.

## Raspberry Pi and NodeMCU

- Raspberry Pi remains powered from its appropriate USB-C supply.
- NodeMCU may be powered by USB for serial bring-up.
- Do not tie two independent positive supply rails together.
- Share ground between external servo supply and NodeMCU.
- Disconnect power before changing wiring.

## Motor power

Do not connect the battery pack to the L298N or motors until motor voltage/current, driver limits, battery protection and wiring are checked. The L298N has two channels; multiple motors per channel increase current demand. Keep motor outputs disabled during software/serial tests.

## Bring-up checklist

- [ ] Confirm exact battery configuration and cell condition.
- [ ] Confirm appropriate protection and charger.
- [ ] Identify converter model and ratings.
- [ ] Measure regulated output with a multimeter.
- [ ] Confirm common ground.
- [ ] Test one unloaded servo at a time.
- [ ] Confirm no resets, overheating, binding or continuous buzzing.
