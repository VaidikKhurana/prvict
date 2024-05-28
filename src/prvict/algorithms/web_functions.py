import pywhatkit as kit
import pyautogui as gui
from time import sleep
import webbrowser as net
import os



def join_google_meting(URL):
    net.open(URL)
    gui.press('enter')

def create_meeting():
    net.open('meet.new')

def open_youtube():
    net.open('youtube.com')

def play_youtube_vid(URL):
    net.open(URL)
 
def play_spotify_song(URL):
    net.open(URL)

def google_search(text):
    net.open(text)

def open_spotify():
    net.open('open.spotify.com')

def open_whatsapp():
    net.open('web.whatsapp.com')

def open_gmail():
    net.open('mail.google.com')

def compose_mail(receipent, CC, text ):
    net.open('https://mail.google.com/mail/u/0/#inbox?compose=new')
    sleep(12)
    gui.write(receipent)
    gui.press('tab')
    sleep(2)
    gui.write(CC)
    sleep(2)
    gui.press('tab')
    gui.write(text)
    gui.hotkey('ctrl', 'enter')
    gui.hotkey('ctrl', 'enter')

def search_wiki(text):
    net.open_new()
    gui.typewrite('https://en.wikipedia.org/wiki/' + text)

def open_settings():
    gui.press('win')
    gui.typewrite('settings')
    gui.press('enter')

def open_file_explorer():
    gui.press('win')
    gui.typewrite('file explorer')
    gui.press('enter')

def shutdown_system():
    kit.shutdown()

def open_app(appname):
    gui.press('win')
    gui.typewrite(appname)
    gui.press('enter')

def open_website(URL):
    net.open(URL)  

def lock_computer():
    gui.hotkey('win', 'l')

def close_app():
    gui.hotkey('alt', 'f4')