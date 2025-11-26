import pyautogui
import time
import threading
from pynput import keyboard

# Global configuration
WAIT_TIME_BETWEEN_CLICKS = 1
WAIT_TIME_BETWEEN_PROFILES = 4

# Control flag
running = True

def run_automation():
    global running
    print("Automation started. Press Ctrl+X to stop.")
    
    while running:
        try:
            # Move to 298, 713
            pyautogui.moveTo(298, 713)
            time.sleep(WAIT_TIME_BETWEEN_CLICKS)
            if not running: break
            
            # Left click once
            pyautogui.click()
            time.sleep(WAIT_TIME_BETWEEN_CLICKS)
            if not running: break
            
            # Move to 236, 647
            pyautogui.moveTo(236, 647)
            
            # Left click
            pyautogui.click()
            
            # Wait 4 seconds (WAIT_TIME_BETWEEN_PROFILES)
            # We check running status periodically to allow faster exit
            for _ in range(WAIT_TIME_BETWEEN_PROFILES * 10):
                if not running: break
                time.sleep(0.1)
                
        except pyautogui.FailSafeException:
            print("\nFailSafe triggered (mouse to corner). Stopping.")
            running = False
            break
        except Exception as e:
            print(f"\nError: {e}")
            running = False
            break

    print("Automation stopped.")

def on_press(key):
    global running
    try:
        # Check for Ctrl+X
        if key == keyboard.KeyCode.from_char('x') and (keyboard.Key.ctrl in _current_keys or keyboard.Key.ctrl_l in _current_keys or keyboard.Key.ctrl_r in _current_keys):
             print("\nKill switch (Ctrl+X) activated.")
             running = False
             return False # Stop listener
    except AttributeError:
        pass

# Helper to track currently pressed keys for combination detection
_current_keys = set()

def on_key_press(key):
    _current_keys.add(key)
    # Check for Ctrl+X
    if hasattr(key, 'char') and key.char == 'x' and (keyboard.Key.ctrl in _current_keys or keyboard.Key.ctrl_l in _current_keys or keyboard.Key.ctrl_r in _current_keys):
        print("\nKill switch (Ctrl+X) activated.")
        global running
        running = False
        return False

def on_key_release(key):
    if key in _current_keys:
        _current_keys.remove(key)

if __name__ == "__main__":
    # Start the keyboard listener in a non-blocking way
    listener = keyboard.Listener(on_press=on_key_press, on_release=on_key_release)
    listener.start()
    
    # Run automation in the main thread (or separate if needed, but main is fine here)
    try:
        run_automation()
    except KeyboardInterrupt:
        running = False
    
    listener.stop()
