import pyautogui
import time

counter = 1

print("Press Ctrl+C to stop.")
try:
    while True:
        # Scroll down fast for 2 seconds
        start_time = time.time()
        while time.time() - start_time < 2:
            pyautogui.scroll(-100)

        time.sleep(1.5)

        # Left click at 313, 643
        pyautogui.click(300, 650)
        pyautogui.click(300, 650)
        
        # Wait 1 seconds
        time.sleep(0.5)
        
        # Left click again same coordinates
        pyautogui.click(300, 630)
        pyautogui.click(300, 630)

        # Wait 2.5 seconds
        print("Like " + str(counter))
        counter += 1
        time.sleep(1.5)
except KeyboardInterrupt:
    print("\nStopped.")
