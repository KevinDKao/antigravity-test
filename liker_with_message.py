import pyautogui
import time
import signal
import sys

def signal_handler(sig, frame):
    print("\nStopped.")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

counter = 1
message = "men would go to war for you but i'm willing to risk more: going to the george bush presidential library for you"


while True:
    time.sleep(1)
    # 1. Scroll down for -200
    start_time = time.time()
    while time.time() - start_time < 2:
        pyautogui.scroll(-200)
    
    # 2. Sleep for 3 seconds
    time.sleep(2)
    
    # 3. Click at 300, 660
    pyautogui.click(300, 660)
    pyautogui.click(300, 660)
    
    # 4. Type the message
    pyautogui.typewrite(message, interval=0.005)
    
    # 5. Scroll down for 1 second
    start_time = time.time()
    while time.time() - start_time < 0.5:
        pyautogui.scroll(-200)
    
    # 6. Click at 255, 650
    time.sleep(0.75)
    pyautogui.click(255, 650)
    
    # 7. Print the counter
    print("Message " + str(counter))
    counter += 1
    
    # 8. Wait 2.5 seconds
    time.sleep(2.5)
