import sys
from time import sleep
import pygame 
import threading
def printLyrics():
    lines = [
        ("I wanna da-", 0.06),
        ("I wanna dance in the lights", 0.05),
        ("I wanna ro-", 0.07),
        ("I wanna rock your body", 0.08),
        ("I wanna go", 0.08),
        ("I wanna go for a ride", 0.068),
        ("Hop in the music and", 0.07),
        ("Rock your body", 0.08),
        ("Rock that body", 0.069),
        ("come on, come on", 0.035),
        ("Rock that body", 0.05),
        ("(Rock your body)", 0.03),
        ("Rock that body", 0.049),
        ("come on, come on", 0.035),
        ("Rock that body", 0.08),
    ]

    for line, delay in lines:
        for char in line:
            print(char, end='', flush=True)
            sleep(delay)
        print() 
if __name__ == "__main__":
    printLyrics()
    
def play_audio(self):
       try:
            pygame.mixer.music.load("اغيب واقول  .mp3")  # ← غيري الاسم حسب ملفك
            pygame.mixer.music.play()
       except Exception as e:
            print("خطأ في تشغيل الصوت:",e)
            def start_display(self):
        # 👇 نشغل الصوت في ثريد منفصل
             audio_thread = threading.Thread(target=self.play_audio)
             audio_thread.daemon = True
             audio_thread.start()
