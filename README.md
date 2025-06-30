# Wireless Voice Controlled Car

An offline, real-time, wireless voice-controlled car powered by **Raspberry Pi 4**, integrating **CMU PocketSphinx** for speech recognition and **ultrasonic sensors** for obstacle avoidance.

## Overview

This project enables a car to respond to **voice commands** such as:

* `forward`
* `backward`
* `left`
* `right`
* `auto` (autonomous mode)

All processing is performed **offline on-device** without relying on cloud services, ensuring low latency and data privacy.
## Software Architecture
![螢幕擷取畫面 2025-03-21 150758](https://github.com/user-attachments/assets/80f0f572-51cf-4171-963c-c8b011c555ff)

The system is composed of three core modules:

* **Ultrasonic Sensor + Signal Processing**: Responsible for obstacle detection and decision-making based on measured distance.
* **Bluetooth Voice Input + Pocketsphinx**: Performs offline speech recognition to interpret user voice commands.
* **Motor Control**: Receives direction instructions and drives the motors via the L298N motor driver.

---

## Features

* Offline voice control using **PocketSphinx**
* Real-time obstacle avoidance with **HC-SR04 ultrasonic sensor**
* Autonomous mode that detects obstacles and navigates safely
* Low-cost and suitable for education or embedded system prototyping

## Hardware Components

| Component               | Description                        |
| ----------------------- | ---------------------------------- |
| Raspberry Pi 4          | Main processing unit               |
| L298N Motor Driver      | Controls two DC motors             |
| HC-SR04                 | Ultrasonic distance sensor         |
| WH-1000XM5              | Bluetooth microphone (voice input) |
| Two DC Motors + Chassis | For movement                       |
| Power supply            | For Pi and motor driver            |

## Voice Recognition (PocketSphinx)

The system uses **PocketSphinx** with a custom dictionary (`command.dic`) and language model (`command.lm`) to detect specific keywords.

Example:

```bash
pocketsphinx_continuous -dict command.dic -lm command.lm -inmic yes
```

When a command is recognized, it is passed as an argument to `two-motor.py`, e.g.:

```bash
python3 two-motor.py f    # forward
python3 two-motor.py b    # backward
python3 two-motor.py r    # turn right
python3 two-motor.py l    # turn left
python3 two-motor.py auto # enter autonomous mode
```

## Autonomous Mode

* When triggered with the `auto` command, the system:

  1. Continuously measures distance with `HC-SR04`.
  2. If no obstacle is detected (>30cm), it moves forward.
  3. If an obstacle is detected, it stops and turns left.

## How to Test

1. Connect hardware according to the wiring table (see documentation).
2. Run:

   ```bash
   python3 test.py         # To test ultrasonic sensor
   python3 two-motor.py f  # To test forward motion
   ```

## GPIO Pin Mapping

| Device      | Raspberry Pi Pin |
| ----------- | ---------------- |
| ENA         | 12               |
| ENB         | 13               |
| IN1 / IN2   | 16 / 18          |
| IN3 / IN4   | 23 / 21          |
| TRIG / ECHO | 7 / 11           |

## Authors

* 賴仲倫
* 張祐瑜
* 江英碩
