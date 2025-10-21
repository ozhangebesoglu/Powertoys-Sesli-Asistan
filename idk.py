import pyautogui as pag
import time
import os

def open_shortcut_menu():
    # Simulate pressing 'Win + X' to open the shortcut menu
    pag.hotkey('alt','space')
    time.sleep(1)  # Wait for the menu to open
    
def open_link(app_link):
    open_shortcut_menu()
    pag.write('//')
    time.sleep(0.5)
    pag.write(app_link)
    time.sleep(0.5)
    pag.press('enter')

def open_app(app_name):
    open_shortcut_menu()
    pag.write(app_name)
    time.sleep(0.5)
    pag.press('enter')
    
def terminal_command(command):
    open_shortcut_menu()
    pag.write('>')
    time.sleep(0.5)
    pag.write(command)
    time.sleep(0.5)
    pag.press('enter')

def screenshot():
    image=pag.screenshot()
    os.makedirs('screenshots', exist_ok=True)
    image.save(f'screenshots/screenshot_{int(time.time())}.png')
        
