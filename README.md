# 🕒 Digital Clock - Tkinter GUI

A sleek and simple **Digital Clock** application built using **Python** and the **Tkinter GUI library**.  
It displays the current time in **both 12-hour and 24-hour formats** and updates every second in real-time.

---

## 🚀 Features

- ⏱️ Real-time clock updates every second
- 🌓 Displays time in:
  - **12-Hour Format** (with AM/PM)
  - **24-Hour Format** (military time)
- 🎨 Modern dark theme UI using `ttk` styles
- 🐍 Built entirely with Python — no external dependencies required

---

## 📸 Preview

> *(You can add a screenshot of the app here if desired)*

---

## 🖥️ How to Run

1. **Clone this repository**
```bash
git clone https://github.com/Mohankirushna/digital-clock.git
cd digital-clock
```
Run the Python script
python digital_clock.py

💡 Code Overview
update_time() function:
Fetches the current system time using datetime.now()
Formats it in both 12-hour (%I:%M:%S %p) and 24-hour (%H:%M:%S) styles
Updates the clock labels every second using root.after(1000, update_time)

GUI Highlights:
Uses ttk.Style() to apply a modern dark-themed UI
Dynamic labels to show both time formats
Responsive and minimal design

📦 Requirements
Python 3.x
Tkinter (comes pre-installed with Python)

📄 License
This project is licensed under the MIT License — free for personal or commercial use.

