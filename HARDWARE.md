# 🔌 Circuit Wiring

## 📍 Connections

### TTP223 Touch Sensor

| TTP223 Pin | Raspberry Pi 4 Pin | GPIO |
|-------------|--------------------|------|
| VCC | Pin 1 | 3.3V |
| GND | Pin 6 | GND |
| SIG | Pin 11 | GPIO17 |

### LED

| LED Connection | Raspberry Pi 4 Pin | GPIO |
|----------------|--------------------|------|
| LED Anode (+) → 220Ω Resistor | Pin 12 | GPIO18 |
| LED Cathode (-) | Pin 14 | GND |

---

## ⚠️ Notes

- The **TTP223 touch sensor works with 3.3V**, which is safe for Raspberry Pi GPIO.
- Always use a **220Ω resistor with the LED** to prevent excess current that may damage the LED or Raspberry Pi.

---

## 📷 Circuit Diagram

![Circuit Diagram](circuit_diagram.png)
