import pyautogui as pt
import time as sec

sec.sleep(30)

for i in range(100):
    pt.write("Hello!")
    pt.press("enter")