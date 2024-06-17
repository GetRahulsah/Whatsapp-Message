import pywhatkit
import pyautogui
import time

# Open WhatsApp Web and send an initial message to the target number
pywhatkit.sendwhatmsg("+9779848590208", "Hi, Laxman", time.localtime().tm_hour, (time.localtime().tm_min + 1) % 60)

# Wait for WhatsApp Web to open
time.sleep(15)

# Send 100 additional messages with minimal delay
for _ in range(99):
    pyautogui.typewrite("Hi, Laxman")
    pyautogui.press("enter")
    time.sleep(0.5)  # Short delay to ensure messages are sent properly

# Note: Make sure the WhatsApp Web window is in focus and the browser tab is open.
