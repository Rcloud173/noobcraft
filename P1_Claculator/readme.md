# Simple Python Calculator (CLI)

This is a basic command-line calculator written in Python. It takes arithmetic expressions in the form of `"number1 operator number2"` and outputs the result. The program continues accepting inputs until the user enters `=` to terminate it.

---

## 🚀 Features

- Accepts simple arithmetic expressions (e.g., `3 + 4`)
- Supports the following operators:
  - Addition `+`
  - Subtraction `-`
  - Multiplication `*`
  - Division `/` (with division-by-zero handling)
- Handles invalid input gracefully

---

# 🛠️ Future Improvements – Python Calculator

This document outlines the planned upgrades and enhancements for the Python calculator project. The current version is a command-line based calculator, and the goal is to gradually evolve it into a more powerful and user-friendly tool.

---

## ✅ To-Do / Future Improvements

Here are some of the key areas where this calculator will be improved:

---

### 🖼️ GUI Development

Upgrade from CLI to a full graphical user interface:

- [ ] Create a GUI using **Tkinter**, **PyQt**, or **Kivy**
- [ ] Design input field and operation buttons
- [ ] Add a clear, user-friendly layout
- [ ] Display calculation history for user reference
- [ ] Enable light/dark mode toggle (optional)

---

### 🧠 Functional Upgrades

Enhance core functionality for real-world use:

- [ ] Support **chained operations** (e.g., `3 + 4 * 2`)
- [ ] Implement an expression parser using `eval()` or the **`ast`** module to handle operator precedence safely
- [ ] Add **memory functionality**:
  - M+ (Memory Add)
  - M- (Memory Subtract)
  - MR (Memory Recall)
  - MC (Memory Clear)
- [ ] Include keyboard input support for the GUI

---

### 🧪 Testing & Code Structure

Make the application more robust and maintainable:

- [ ] Refactor code into **functions and classes** for readability and modularity
- [ ] Write **unit tests** using Python’s `unittest` or `pytest`
- [ ] Package the calculator as a **reusable Python module**
- [ ] Create configuration and settings management (optional)

---

## 🔮 Long-Term Vision

- [ ] Add scientific calculator mode (trigonometry, exponents, etc.)
- [ ] Enable result history export (e.g., to `.txt` or `.csv`)
- [ ] Build a web-based version using Flask or Django

---

## 👷 Contributions

Want to help bring these improvements to life? Feel free to fork the repo, make enhancements, and submit a pull request!

---

## 📌 Note

The roadmap above is flexible and will evolve as development progresses. Feedback and suggestions are always welcome!



## 🧑‍💻 Usage

Run the script from your terminal:

```bash
python calculator.py


