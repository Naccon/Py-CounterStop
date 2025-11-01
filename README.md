# 🕒 Py-CounterStop

**Py-CounterStop** is a simple **Python-based timer and stopwatch** program built for the terminal.  
It displays ASCII art at startup, gives users the option to set custom time durations,  
and can run in both **count-up (timer)** and **count-down (stopwatch)** modes.

---

## 🚀 Features

- 🖼️ Cool ASCII welcome banner  
- ⏳ Timer (counts **up** from 0 to a given time)  
- ⏱️ Stopwatch (counts **down** from a given time to 0)  
- ⌨️ User-friendly text-based interface  
- 💤 Real-time output  

---

## 🧩 How It Works

When you run the program:
1. It prints the **Py-CounterStop** ASCII art.
2. Displays a welcome message with a typing animation.
3. Asks you to select one of the options:
   - `[1]` Start Count (Timer mode)
   - `[2]` Start Stopwatch (Countdown mode)
   - `[0]` Exit the program
4. Prompts you to choose a **time unit** (seconds, minutes, or hours).
5. Starts counting up or down depending on your choice.

---

## 🖥️ Usage

### ▶️ Run the Program

```bash
python main.py
```

Make sure you have Python 3 installed.

### 🧮 Example Output

```
Welcome to Py-CounterStop
Please choose an option:
[1]	Start Count
[2]	Start Stopwatch
[0]	Exit Program
```

If you choose the timer option, the output will look like:

```
00:00:00
00:00:01
00:00:02
...
```

If you choose the stopwatch option, it will count down instead.

---

## 🧠 Requirements

- Python 3.8 or later

---

## 📦 File Structure

```
Py-CounterStop/
│
├── main.py          # Main Python script
├── README.md        # Project documentation
└── art.py           # ASCII art
```

---

## 🧑‍💻 Author

**naccon**  
📧 Feel free to connect or suggest improvements!  

---

## ⚖️ License

This project is open-source and free to use.
---

⭐ If you like this project, don’t forget to **star** the repo on GitHub!
