from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import keyboard
from time import sleep

muted = False # DeezerMuted

def set_app_volume(app_name, volume_level):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process and session.Process.name() == app_name:
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            volume.SetMasterVolume(volume_level, None)
            print(f"Volume for {app_name} set to {volume_level * 100}%")
            return
    print(f"Application {app_name} not found")

# Example usage
set_app_volume("chrome.exe", 0.5)  # Set volume to 50% for Chrome  

while True:
    if keyboard.is_pressed("space"):
        print("space")
        if muted:
            set_app_volume("Deezer.exe", 0.5)
            muted = False
        else:
            set_app_volume("Deezer.exe", 0)
            muted = True
        sleep(0.5)  