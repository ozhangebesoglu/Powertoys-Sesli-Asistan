import pyautogui as pag
import time
import os

def open_new_tab():
    pag.hotkey('ctrl', 't')
    time.sleep(1)
    
def close_current_tab():
    pag.hotkey('ctrl', 'w')
    time.sleep(1)

def refresh_page():
    pag.hotkey('ctrl', 'r')
    time.sleep(1)

def navigate_to_url():
    pag.hotkey('ctrl', 'l')
    time.sleep(0.5)

def enter_url(url):
    navigate_to_url()
    pag.write(url)
    time.sleep(0.5)
    pag.press('enter')
    time.sleep(2)  # Wait for the page to load
    
def bookmark_page():
    pag.hotkey('ctrl', 'd')
    time.sleep(0.5)
    pag.press('enter')  # Confirm bookmark
    time.sleep(1)

def open_bookmarks():
    pag.hotkey('ctrl', 'shift', 'b')
    time.sleep(1)

def clear_browser_cache():
    time.sleep(1)
    pag.hotkey('ctrl', 'shift', 'delete')
    time.sleep(1)
    pag.press('enter')  # Confirm clear cache
    time.sleep(2)  # Wait for the process to complete
    x, y = pag.locateCenterOnScreen('verileri_sil.png')
    pag.click(x, y)
    
    


clear_browser_cache()