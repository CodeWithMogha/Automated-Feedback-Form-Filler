# 🤖 Automated Feedback Form Filler

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?style=for-the-badge&logo=python)
![Automation](https://img.shields.io/badge/Automation-PyAutoGUI-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A simple yet effective Python script to automate the tedious process of filling out repetitive faculty feedback forms. It uses keyboard simulation to navigate and select options, saving you minutes of clicking.

## 🧠 How It Works

The script leverages the **PyAutoGUI** library to simulate human keyboard interactions. Here is the step-by-step logic:

1.  **Initial Wait**: Once started, the script pauses for 5 seconds to give you time to switch to your browser and focus on the feedback form.
2.  **Navigation Loop**: It iterates through a specified number of questions (default is 32).
3.  **Selection**: For each question, it simulates 'Down' arrow key presses to move to your desired rating (e.g., Agree, Strongly Agree).
4.  **Confirmation**: It presses 'Enter' to lock in the selection.
5.  **Tabbing**: It presses 'Tab' to move the focus to the next question automatically.
6.  **Auto-Comment**: After completing the ratings, it moves to the text area and types a predefined feedback comment (e.g., "Good faculty").

## 🛠️ Requirements

- Python 3.x
- `pyautogui` library

## ⚙️ Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/CodeWithMogha/Automated-Feedback-Form-Filler.git
    cd Automated-Feedback-Form-Filler
    ```

2.  **Install dependencies**:
    ```bash
    pip install pyautogui
    ```

## 🚀 How to Use

1.  **Configure the script**: Open `FACULTY_FEEDBACK.py` and adjust the variables if needed:
    *   `TOTAL`: The number of questions on the form.
    *   `DOWN_PRESSES`: How many times to press 'Down' to reach your desired rating (0 for the first option, 1 for the second, etc.).
2.  **Prepare the form**: Open your feedback form in your browser.
3.  **Run the script**:
    ```bash
    python FACULTY_FEEDBACK.py
    ```
4.  **Take Action**: Immediately switch to your browser and **click on the first option of the first question** to ensure the script has the correct starting focus.
5.  **Wait**: Hands off! The script will take it from there.

## ⚠️ Important Notes

- **Initial Focus**: The script relies on the cursor being in the right place. Manual clicking of the first option is crucial.
- **Timing**: Small `time.sleep()` intervals are added between presses to ensure the browser/form can keep up with the automated inputs.
- **Failsafe**: If something goes wrong, move your mouse to any corner of the screen to trigger PyAutoGUI's failsafe and stop the script.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---
Developed with ❤️ by [CodeWithMogha](https://github.com/CodeWithMogha)
