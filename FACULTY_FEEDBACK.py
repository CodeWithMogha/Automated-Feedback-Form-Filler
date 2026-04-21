import pyautogui
import time

pyautogui.PAUSE = 0.2

TOTAL = 32
DOWN_PRESSES = 1   # 0=Strongly Agree, 1=Agree, etc.

print("⚠️ Click FIRST question option manually (Strongly Agree)")
time.sleep(5)

for i in range(TOTAL):
    print(f"Q{i+1}")

    # Move to desired option
    for _ in range(DOWN_PRESSES):
        pyautogui.press('down')
        time.sleep(0.1)

    # Select option
    pyautogui.press('enter')
    time.sleep(0.2)

    # Move to next question
    pyautogui.press('tab')
    time.sleep(0.3)

# Go to comment
time.sleep(1)
pyautogui.write("Good faculty", interval=0.1)

print("✅ Done")