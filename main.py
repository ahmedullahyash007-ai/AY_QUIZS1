


# from kivy.clock import Clock
# from kivy.graphics import Color, Rectangle, Ellipse
# from kivy.lang import Builder
# from kivy.uix.popup import Popup

# from kivy.graphics import (
#     Rectangle,
#     Color,
#     Line,
#     Ellipse,
#     RoundedRectangle
# )

# from kivy.animation import Animation
# from kivy.clock import Clock
# from kivy.core.audio import SoundLoader

# from kivy.uix.screenmanager import (
#     ScreenManager,
#     Screen,
#     FadeTransition
# )

# # PIL
# from PIL import (
#     Image as PILImage,
#     ImageDraw,
#     ImageFilter,
#     ImageFont
# )

# # Kivy Image Widget
# # from kivy.uix.image import Image as KivyImage
# from kivy.uix.image import Image as KivyImage
# from kivy.uix.spinner import Spinner
# from kivy.app import App
# from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.scrollview import ScrollView
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.togglebutton import ToggleButton
# from kivy.uix.button import Button
# from kivy.uix.label import Label
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.widget import Widget
# from kivy.uix.textinput import TextInput
# from kivy.uix.progressbar import ProgressBar

# from kivy.core.clipboard import Clipboard
# from kivy.core.window import Window
# # from kivy.core.image import Image as CoreImage

# from kivy.storage.jsonstore import JsonStore



# from textwrap import wrap
# import textwrap
# import platform
# import random
# import threading

# import os
# import requests
# import shutil
# import math
# import uuid
# import os
# # import subprocess
# from PIL import Image, ImageDraw, ImageFont
# from PIL import Image as PILImage


# from kivy.core.window import Window



# === CLEAN IMPORTS FOR APK ===
from kivy.app import App
from kivy.core.window import Window
from kivy.core.clipboard import Clipboard
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image as KivyImage
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.progressbar import ProgressBar
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Ellipse, Line, RoundedRectangle
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.storage.jsonstore import JsonStore
import json
# Python libs
# import os, math, random, uuid, shutil, requests, threading, platform, textwrap, wrap
import os, math, random, uuid, shutil, requests, threading, platform, textwrap

from PIL import Image as PILImage, ImageDraw, ImageFont, ImageFilter

# Window Size (APK ke liye zaroori)
Window.softinput_mode = "below_target"









FONT_PATH = os.path.join(
    os.path.dirname(__file__),
    "fonts",
    "Roboto.ttf"
)


print("SERVER1 FILE LOADED")
Window.title = "AY QuizS"
print("SERVER1 TITLE LOADED")
Window.set_icon("ahmed_logo13.png")
print("SERVER1 ICON LOADED")


FPS = 24
COUNTDOWN_TIME = 3
ANSWER_TIME = 2

print("SERVER1 fps LOADED")












from kivy.core.audio import SoundLoader
import os

BASE = "/mnt/d/ahtiyat.py"

# correct_sound = SoundLoader.load(os.path.join(BASE, "dragon.mp3"))
# print("SERVER1 DRAGON LOADED")
# wrong_sound   = SoundLoader.load(os.path.join(BASE, "wrong.mp3"))
# print("SERVER1 WRONG LOADED")
# click_sound   = SoundLoader.load(os.path.join(BASE, "click.mp3"))
# print("SERVER1 CLICK LOADED")




print("BEFORE DRAGON LOAD", flush=True)
# correct_sound = SoundLoader.load(os.path.join(BASE, "dragon.mp3"))
correct_sound = None
print("AFTER DRAGON LOAD:", correct_sound, flush=True)

print("BEFORE WRONG LOAD", flush=True)
# wrong_sound = SoundLoader.load(os.path.join(BASE, "wrong.mp3"))
wrong_sound = None
print("AFTER WRONG LOAD:", wrong_sound, flush=True)

print("BEFORE CLICK LOAD", flush=True)
# click_sound = SoundLoader.load(os.path.join(BASE, "click.mp3"))
click_sound = None
print("AFTER CLICK LOAD:", click_sound, flush=True)





def play(sound):
    if sound:
        sound.stop()
        sound.play()



print("SERVER1 PLAY LOADED")
stars = None
fire_bg = None
frame_size = "youtube_shorts"

Window.size = (360, 800)


import pyrebase

Config = {
  "apiKey": "AIzaSyC8AZRL2LFl3vI9zVpi31xWoZuoJMANtP4",
  "authDomain": "ahmedapps-e4f12.firebaseapp.com",
  "databaseURL": "https://ahmedapps-e4f12-default-rtdb.firebaseio.com/",
  "storageBucket": "ahmedapps-e4f12.firebasestorage.app",
  
};
firebase = pyrebase.initialize_app(Config)
db = firebase.database()


SERVER_URL = db.child("config").child("server_url").get().val()


try:
    SERVER_URL = db.child("config").child("server_url").get().val()
    print("SERVER URL =", SERVER_URL)
except Exception as e:
    print("Server URL Error:", e)












# class GlassButton(Button):

#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

#         # Default Kivy background completely remove
#         self.background_normal = ""
#         self.background_down = ""

#         # Colors
#         self.normal_color = (1, 0.2, 0.2, 1)
#         self.press_color = (0.75, 0.05, 0.05, 1)

#         # Normal color
#         self.background_color = self.normal_color

#         # Text
#         self.color = (1, 1, 1, 1)
#         self.font_size = "20sp"

#         # Click events
#         self.bind(
#             on_press=self.button_pressed,
#             on_release=self.button_released
#         )

#     def button_pressed(self, *args):
#         self.background_color = self.press_color

#     def button_released(self, *args):
#         self.background_color = self.normal_color







from kivy.graphics import Color, RoundedRectangle
from kivy.uix.button import Button

class GlassButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Default Kivy background completely remove
        self.background_normal = ""
        self.background_down = ""
        self.background_color = (0,0,0,0)

        # Colors - Luxury Red
        self.normal_color = (0.75, 0.15, 0.15, 1)  # Bright Red
        self.press_color = (0.45, 0.05, 0.05, 1)  # Dark Press Red
        self.gold_color = (1, 0.84, 0.2, 1)       # Gold #FFD633

        # Text
        self.color = (1, 1, 1, 1)
        self.font_size = "18sp"
        self.bold = True
        self.size_hint_y = None
        self.height = 50

        # Canvas - Luxury Pill
        with self.canvas.before:
            # Gold outer border
            Color(*self.gold_color)
            self.gold_bg = RoundedRectangle(radius=[27], pos=(self.x-3, self.y-3), size=(self.width+6, self.height+6))
            # Main red background
            Color(*self.normal_color)
            self.main_bg = RoundedRectangle(radius=[24], pos=self.pos, size=self.size)
        
        with self.canvas.after:
            # White glossy shine on top
            Color(1, 1, 1, 0.35)
            self.shine = RoundedRectangle(radius=[24], pos=(self.x+10, self.y+self.height*0.55), size=(self.width-20, self.height*0.35))

        # Bind for resize + Click events
        self.bind(pos=self.update_all, size=self.update_all)
        self.bind(on_press=self.button_pressed, on_release=self.button_released)

    def update_all(self, *args):
        self.gold_bg.pos = (self.x-3, self.y-3)
        self.gold_bg.size = (self.width+6, self.height+6)
        self.main_bg.pos = self.pos
        self.main_bg.size = self.size
        self.shine.pos = (self.x+10, self.y+self.height*0.55)
        self.shine.size = (self.width-20, self.height*0.35)

    def button_pressed(self, *args):
        # Press pe dark red
        self.canvas.before.remove(self.main_bg)
        with self.canvas.before:
            Color(*self.gold_color)
            # gold already hai
            Color(*self.press_color)
            self.main_bg = RoundedRectangle(radius=[24], pos=self.pos, size=self.size)

    def button_released(self, *args):
        # Wapas normal red
        self.canvas.before.remove(self.main_bg)
        with self.canvas.before:
            Color(*self.gold_color)
            Color(*self.normal_color)
            self.main_bg = RoundedRectangle(radius=[24], pos=self.pos, size=self.size)

# TOP ke chote EDIT/QUIZs ke liye same class, bas size chota:
class SmallLuxuryButton(GlassButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.height = 18
        self.width = 95
        self.font_size = "16sp"
        self.size_hint_x = None








# from kivy.uix.button import Button

# class GlassButton(Button):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

#         # Default Kivy background remove
#         self.background_normal = ""
#         self.background_down = ""

#         # Colors - Pehle wala simple red
#         self.normal_color = (0.85, 0.2, 0.2, 1)   # #D93333 Simple Red
#         self.press_color = (0.6, 0.1, 0.1, 1)     # Dark Red on press

#         # Normal color
#         self.background_color = self.normal_color

#         # Text - Pehle wala
#         self.color = (1, 1, 1, 1)
#         self.font_size = "20sp"
#         self.bold = True
#         self.size_hint_y = None
#         self.height = 55

#         # Click events
#         self.bind(
#             on_press=self.button_pressed,
#             on_release=self.button_released
#         )

#     def button_pressed(self, *args):
#         self.background_color = self.press_color

#     def button_released(self, *args):
#         self.background_color = self.normal_color

# # Top ke chote EDIT / QUIZs ke liye
# class TopRedButton(GlassButton):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.height = 38
#         self.width = 80
#         self.font_size = "16sp"
#         self.size_hint_x = None














class AppButton3D(Button):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.background_normal = ""
        self.background_color = (0, 0, 0, 0)
        self.color = (1, 1, 1, 1)
        self.font_size = "18sp"

        # 🔥 Shadow + Button
        with self.canvas.before:

            # Shadow (dark layer)
            Color(0, 0, 0, 0.25)
            self.shadow = RoundedRectangle(
                pos=(self.x, self.y - 4),
                size=self.size,
                radius=[20]
            )

            # Main Button
            Color(0.2, 0.7, 1, 1)
            self.bg = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[20]
            )

        self.bind(pos=self.update_graphics, size=self.update_graphics)

        # 🔥 press effect
        self.bind(on_press=self.press_effect)
        self.bind(on_release=self.release_effect)

    def update_graphics(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

        self.shadow.pos = (self.x, self.y - 4)
        self.shadow.size = self.size

    # 🔥 Button press animation
    def press_effect(self, *args):
        Animation.cancel_all(self)

        anim = Animation(y=self.y - 3, duration=0.05)
        anim.start(self)

    def release_effect(self, *args):
        Animation.cancel_all(self)

        anim = Animation(y=self.y + 3, duration=0.05)
        anim.start(self)






















class GlassInput(TextInput):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Simple style
        self.multiline = False
        # self.hint_text = "Enter text"

        # Text color
        self.foreground_color = (0, 0, 0, 1)

        self.bg = RoundedRectangle(
    pos=self.pos,
    size=self.size,
    radius=[20]
)

        # Background color (Yellow)
        self.background_normal = ""
        self.background_active = ""
        self.background_color = (1, 1, 1, 1)














from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.progressbar import ProgressBar
from kivy.graphics import Color, RoundedRectangle
from kivy.clock import Clock


# 🔥 MODERN 3D GREEN PROGRESS BAR
class ModernProgressBar(ProgressBar):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.max = 100
        self.value = 0

        # make it look clean (no default bar)
        self.background_color = (0, 0, 0, 0)

        with self.canvas.before:

            # 🌑 soft shadow
            Color(0, 0, 0, 0.35)
            self.shadow = RoundedRectangle(
                pos=(self.x, self.y - 3),
                size=self.size,
                radius=[15]
            )

            # 🟣 dark track (background)
            Color(0.12, 0.05, 0.18, 1)   # dark purple
            self.bg = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[15]
            )

            # 💜 glow (soft neon)
            Color(0.75, 0.2, 1, 0.25)
            self.glow = RoundedRectangle(
                pos=self.pos,
                size=(0, self.height),
                radius=[15]
            )

            # ✨ main purple fill (neon)
            Color(0.80, 0.25, 1, 1)
            self.fill = RoundedRectangle(
                pos=self.pos,
                size=(0, self.height),
                radius=[15]
            )

        self.bind(
            pos=self.update_graphics,
            size=self.update_graphics,
            value=self.update_graphics
        )

    def update_graphics(self, *args):

        # background
        self.bg.pos = self.pos
        self.bg.size = self.size

        # shadow
        self.shadow.pos = (self.x, self.y - 3)
        self.shadow.size = self.size

        # width fill
        width = (self.value / self.max) * self.width

        # fill bar
        self.fill.pos = self.pos
        self.fill.size = (width, self.height)

        # glow layer
        self.glow.pos = self.pos
        self.glow.size = (width, self.height)


   





import os
import json

# Ye line sab se important hai - main.py ka folder nikalna
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "QUESTIONS_AD.json")

QUESTIONS_PER_PAGE = 10






class QuizScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.page = 0
        self.groups = []
        self.all_questions = []
        self.make_ui()
        self.bind_buttons()
        self.load_questions()

    # def load_questions(self):
    #     try:
    #         # path = r"D:ahtiyat.py/QUESTIONS_AD.json"
    #         # # path = os.path.join(os.path.dirname(__file__), "QUESTIONS_AD.json")
    #         base_path = os.path.dirname(os.path.abspath(__file__))
    #         json_path = os.path.join(base_path, "QUESTIONS_AD.json")
    #         print("Loading from:", json_path) # ye check karne ke liye


    #         with open(path, 'r', encoding='utf-8') as f:
    #             data = json.load(f)
    #             self.groups = data
    #             self.questions = data

    #             print(f"Loaded: {len(self.groups)} Questions")
                
    #             if self.groups:
    #                 self.show_question(0)

    #     except FileNotFoundError:
    #         print(f"File nahi mili: {path}")
    #     except Exception as e:
    #         print(f"Error: {e}")
    # def load_questions(self):
    #     try:
    #         base_path = os.path.dirname(os.path.abspath(__file__))
    #         json_path = os.path.join(base_path, "QUESTIONS_AD.json")
    #         print("Loading from:", json_path)

    #         # YAHAN json_path use karo, path nahi
    #         with open(json_path, 'r', encoding='utf-8') as f:
    #             data = json.load(f)
    #             # Aapke baaki code ke hisab se ye naam sahi hai
    #             self.all_questions = data 

    #             print(f"Loaded: {len(self.all_questions)} Questions")

    #     except FileNotFoundError:
    #         print(f"File nahi mili: {json_path}") # Yahan bhi json_path
    #         print(f"Folder main hain: {os.listdir(base_path)}")
    #         self.all_questions = []
    #     except Exception as e:
    #         print(f"Error: {e}")
    #         self.all_questions = []

    #     # Neeche aapka card wala code waisa hi rahega - return mat lagana
    #     self.container.clear_widgets()
    #     self.groups.clear()
    #     start = self.page * QUESTIONS_PER_PAGE
    #     end = start + QUESTIONS_PER_PAGE
    #     for q in self.all_questions[start:end]:
    #         card = BoxLayout(
    #             orientation="vertical",
    #             size_hint_y=None,
    #             spacing=10,
    #             padding=12
    #         )
    #         card.bind(minimum_height=card.setter("height"))
    #         with card.canvas.before:
    #             Color(0.10, 0.12, 0.18, 1)
    #             card.bg = RoundedRectangle(pos=card.pos, size=card.size, radius=[20])
    #         def update_card(instance, *args):
    #             instance.bg.pos = instance.pos
    #             instance.bg.size = instance.size
    #         card.bind(pos=update_card, size=update_card)
    #         # ... baaki aapka lbl aur button wala code


    # def load_questions(self):
    #     try:
    #         base_path = os.path.dirname(os.path.abspath(__file__))
    #         json_path = os.path.join(base_path, "QUESTIONS_AD.json")
    #         print("Loading from:", json_path)

    #         with open(json_path, 'r', encoding='utf-8') as f:
    #             self.all_questions = json.load(f)

    #         print(f"Loaded: {len(self.all_questions)} Questions")

    #     except FileNotFoundError:
    #         print(f"File nahi mili: {json_path}")
    #         self.all_questions = []
    #     except Exception as e:
    #         print(f"Error: {e}")
    #         self.all_questions = []

    #     self.container.clear_widgets()
    #     self.groups.clear()
    #     start = self.page * QUESTIONS_PER_PAGE
    #     end = start + QUESTIONS_PER_PAGE
    #     for q in self.all_questions[start:end]:
    #         card = BoxLayout(orientation="vertical", size_hint_y=None, spacing=10, padding=12)
    #         card.bind(minimum_height=card.setter("height"))
    #         with card.canvas.before:
    #             Color(0.10, 0.12, 0.18, 1)
    #             card.bg = RoundedRectangle(pos=card.pos, size=card.size, radius=[20])
    #         def update_card(instance, *args):
    #             instance.bg.pos = instance.pos
    #             instance.bg.size = instance.size
    #         card.bind(pos=update_card, size=update_card)
    #         from kivy.uix.label import Label
    #         from kivy.uix.togglebutton import ToggleButton
    #         lbl = Label(text=q["question"], color=(1,1,1,1), size_hint_y=None, text_size=(400, None), halign="left")
    #         lbl.bind(texture_size=lambda i, v: setattr(i, "height", v[1] + 20))
    #         card.add_widget(lbl)
    #         btns = []
    #         for opt in q["options"]:
    #             btn = ToggleButton(text=opt, group=q["question"], size_hint_y=None, height=45, background_normal="", background_color=(0.18, 0.25, 0.45, 1))
    #             btns.append(btn)
    #             card.add_widget(btn)
    #         self.container.add_widget(card)
    #         self.groups.append((btns, q["answer"]))
    #     self.scroll.scroll_y = 1




    






    # iske baad aapke baaki functions ayenge
    def make_ui(self):
        pass

    def bind_buttons(self):
        pass







    # ================= UI =================
    def make_ui(self):

        from kivy.core.window import Window
        from kivy.uix.floatlayout import FloatLayout
        from kivy.uix.scrollview import ScrollView
        from kivy.uix.gridlayout import GridLayout
        from kivy.uix.label import Label
        from kivy.graphics import Color, RoundedRectangle
        from kivy.effects.dampedscroll import DampedScrollEffect

        # FIXED MOBILE FRAME SIZE (IMPORTANT)
        Window.size = (350, 650)

        self.root_layout = FloatLayout()

        # ================= BACKGROUND =================
        with self.canvas.before:
            Color(0.04, 0.05, 0.09, 1)
            self.bg = RoundedRectangle(pos=self.pos, size=self.size)

        self.bind(pos=self.update_bg, size=self.update_bg)

        # ================= TOP SPACE (IMPORTANT FIX) =================
        self.top_spacer = Label(size_hint=(1, None), height=60)
        self.root_layout.add_widget(self.top_spacer)

        # ================= SCROLL =================
        self.scroll = ScrollView(
            size_hint=(0.95, 0.79),
            pos_hint={"center_x": 0.5, "top": 0.91},
            do_scroll_x=False,
            do_scroll_y=True,
            effect_cls=DampedScrollEffect,
            bar_width=4
        )

        # ================= CONTAINER =================
        self.container = GridLayout(
            cols=1,
            spacing=15,
            padding=[10, 10, 10, 80],
            size_hint_y=None,
            width=350
        )

        self.container.bind(minimum_height=self.container.setter("height"))

        self.scroll.add_widget(self.container)
        self.root_layout.add_widget(self.scroll)

        # ================= BOTTOM BUTTONS =================

        # self.prev_btn = GlassButton(text="Prev", size_hint=(None, None), size=(120, 50), pos=(50, 10))
        # self.next_btn = GlassButton(text="Next", size_hint=(None, None), size=(120, 50), pos=(400, 10))
        # self.check_btn = GlassButton(text="Check", size_hint=(None, None), size=(120, 50), pos=(400, 900))
        # self.home_btn = GlassButton(text="Back", size_hint=(None, None), size=(120, 50), pos=(50, 900))



        self.prev_btn = GlassButton(
    text="Prev",
    size_hint=(None, None),
    size=(100, 45),
    pos_hint={"x": 0.05, "y": 0.05}
)

        self.next_btn = GlassButton(
    text="Next",
    size_hint=(None, None),
    size=(100, 45),
    pos_hint={"x": 0.75, "y": 0.05}
)

        self.check_btn = GlassButton(
    text="Check",
    size_hint=(None, None),
    size=(100, 45),
    pos_hint={"x": 0.75, "y": 0.9}
)

        self.home_btn = GlassButton(
    text="Back",
    size_hint=(None, None),
    size=(100, 45),
    pos_hint={"x": 0.05, "y": 0.9}
)







        self.page_label = Label(
            text="Page 1",
            size_hint=(None, None),
            size=(300, 30),
            pos=(140, 10),
            color=(1, 1, 1, 1),
            bold=True
        )


        self.root_layout.add_widget(self.prev_btn)
        self.root_layout.add_widget(self.next_btn)
        self.root_layout.add_widget(self.check_btn)
        self.root_layout.add_widget(self.home_btn)
        self.root_layout.add_widget(self.page_label)



        self.add_widget(self.root_layout)


    # ================= BACKGROUND UPDATE =================
    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

#     # ================= BIND =================
#     def bind_buttons(self):
#         self.prev_btn.bind(on_press=self.prev_page)
#         self.next_btn.bind(on_press=self.next_page)


    def bind_buttons(self):

        self.prev_btn.bind(on_press=self.prev_page)
        self.next_btn.bind(on_press=self.next_page)
        self.check_btn.bind(on_press=self.check_quiz_result)
        self.home_btn.bind(on_press=self.go_home)


    # # ================= LOAD QUESTIONS =================
    # def load_questions(self):

    #     from kivy.uix.boxlayout import BoxLayout
    #     from kivy.uix.togglebutton import ToggleButton
    #     from kivy.core.window import Window
    #     from kivy.graphics import Color, RoundedRectangle
       
    #     self.container.clear_widgets()
    #     self.groups.clear()

    #     start = self.page * QUESTIONS_PER_PAGE
    #     end = start + QUESTIONS_PER_PAGE

    #     for q in QUESTIONS_AD[start:end]:
    #     # for q in self.all_questions[start:end]:
    #         # ================= CARD =================
    #         card = BoxLayout(
    #             orientation="vertical",
    #             size_hint_y=None,
    #             spacing=10,
    #             padding=12
    #         )

    #         card.bind(minimum_height=card.setter("height"))

    #         # background
    #         with card.canvas.before:
    #             Color(0.10, 0.12, 0.18, 1)
    #             card.bg = RoundedRectangle(pos=card.pos, size=card.size, radius=[20])

    #         def update_card(instance, *args):
    #             instance.bg.pos = instance.pos
    #             instance.bg.size = instance.size

    #         card.bind(pos=update_card, size=update_card)

    #         # ================= QUESTION =================
    #         lbl = Label(
    #             text=q["question"],
    #             color=(1, 1, 1, 1),
    #             size_hint_y=None,
                
    #             text_size=(320, None),
    #             halign="left",
    #             valign="middle"
    #         )

    #         lbl.bind(texture_size=lambda i, v: setattr(i, "height", v[1] + 10))
    #         card.add_widget(lbl)

    #         # ================= OPTIONS =================
    #         btns = []

    #         for opt in q["options"]:

    #             btn = ToggleButton(
    #                 text=opt,
    #                 group=q["question"],
    #                 size_hint_y=None,
    #                 height=45,
    #                 background_normal="",
    #                 background_color=(0.18, 0.25, 0.45, 1),
    #                 color=(1, 1, 1, 1),
               
    #             )

    #             btns.append(btn)
    #             card.add_widget(btn)

    #         self.container.add_widget(card)
    #         self.groups.append((btns, q["answer"]))

    #     self.scroll.scroll_y = 1

    # def load_questions(self):
    #     import json
    #     import os
    #     from kivy.uix.boxlayout import BoxLayout
    #     from kivy.uix.togglebutton import ToggleButton
    #     from kivy.graphics import Color, RoundedRectangle
    #     from kivy.uix.label import Label

    #     # --- 1. Sahi Path Nikalna ---
    #     try:
    #         # Ye file main.py ke sath hi dhoondega
    #         base_path = os.path.dirname(os.path.abspath(__file__))
    #         path = os.path.join(base_path, "QUESTIONS_AD.json")
    #         print(f"DEBUG: Trying to load from: {path}")

    #         with open(path, 'r', encoding='utf-8') as f:
    #             data = json.load(f)
    #             # Agar JSON {"questions": [...]} ke format main hai to
    #             if isinstance(data, dict) and "questions" in data:
    #                 self.all_questions = data["questions"]
    #             else:
    #                 self.all_questions = data # Agar direct list hai to

    #         print(f"DEBUG: SUCCESS! Loaded {len(self.all_questions)} questions")
        
    #     except FileNotFoundError:
    #         print(f"DEBUG FAILED: File nahi mili {path}")
    #         print(f"DEBUG: Folder main ye files hain: {os.listdir(base_path)}")
    #         self.all_questions = []
    #         return
    #     except Exception as e:
    #         print(f"DEBUG FAILED: JSON Error {e}")
    #         self.all_questions = []
    #         return

    #     # --- 2. Screen Par Dikhana ---
    #     self.container.clear_widgets()
    #     self.groups.clear()

    #     start = self.page * QUESTIONS_PER_PAGE
    #     end = start + QUESTIONS_PER_PAGE

    #     for q in self.all_questions[start:end]:
    #         card = BoxLayout(orientation="vertical", size_hint_y=None, spacing=10, padding=12)
    #         card.bind(minimum_height=card.setter("height"))
    #         with card.canvas.before:
    #             Color(0.10, 0.12, 0.18, 1)
    #             card.bg = RoundedRectangle(pos=card.pos, size=card.size, radius=[20])
    #         def update_card(instance, *args):
    #             instance.bg.pos = instance.pos
    #             instance.bg.size = instance.size
    #         card.bind(pos=update_card, size=update_card)
    #         lbl = Label(text=q["question"], color=(1,1,1,1), size_hint_y=None, text_size=(400, None), halign="left")
    #         lbl.bind(texture_size=lambda i, v: setattr(i, "height", v[1] + 20))
    #         card.add_widget(lbl)
    #         btns = []
    #         for opt in q["options"]:
    #             btn = ToggleButton(text=opt, group=q["question"], size_hint_y=None, height=45, background_normal="", background_color=(0.18, 0.25, 0.45, 1))
    #             btns.append(btn)
    #             card.add_widget(btn)
    #         self.container.add_widget(card)
    #         self.groups.append((btns, q["answer"]))
    #     self.scroll.scroll_y = 1








    def load_questions(self):

        try:
            print("Loading questions from Firebase...", flush=True)

            response = db.child("questions").get()
            data = response.val()

            print("FIREBASE DATA TYPE:", type(data), flush=True)

            if not data:
                print("FIREBASE ERROR: No questions found!", flush=True)
                self.all_questions = []
                return

            # Agar Firebase mein {"questions": [...]} format hai
            if isinstance(data, dict) and "questions" in data:
                self.all_questions = data["questions"]

            # Agar Firebase se direct list aaye
            elif isinstance(data, list):
                self.all_questions = data

            # Agar Firebase numeric keys wala dictionary return kare
            elif isinstance(data, dict):
                self.all_questions = [
                    data[key]
                    for key in sorted(data.keys(), key=lambda x: int(x))
                ]

            else:
                raise ValueError("Firebase questions format is invalid")

            print("Firebase Questions Loaded:", len(self.all_questions), flush=True)

        except Exception as e:
            print("FIREBASE QUESTIONS ERROR:", repr(e), flush=True)
            self.all_questions = []
            return



        self.container.clear_widgets()
        self.groups.clear()

        start = self.page * QUESTIONS_PER_PAGE
        end = start + QUESTIONS_PER_PAGE

        for q in self.all_questions[start:end]:

            card = BoxLayout(
                orientation="vertical",
                size_hint_y=None,
                spacing=10,
                padding=12
            )

            card.bind(minimum_height=card.setter("height"))

            with card.canvas.before:
                Color(0.10, 0.12, 0.18, 1)
                card.bg = RoundedRectangle(
                    pos=card.pos,
                    size=card.size,
                    radius=[20]
                )

            def update_card(instance, *args):
                instance.bg.pos = instance.pos
                instance.bg.size = instance.size

            card.bind(pos=update_card, size=update_card)

            # lbl = Label(
            #     text=q["question"],
            #     color=(1, 1, 1, 1),
            #     size_hint_y=None,
            #     text_size=(400, None),
            #     halign="left"
            # )

            # lbl.bind(
            #     texture_size=lambda i, v: setattr(i, "height", v[1] + 20)
            # )



            lbl = Label(
                text=q["question"],
                color=(1, 1, 1, 1),
                size_hint=(1, None),
                halign="left",
                valign="middle",
                padding=(10, 10)
            )

            lbl.bind(width=lambda instance, value: setattr(
                instance, "text_size", (value - 20, None)
            ))

            lbl.bind(texture_size=lambda instance, value: setattr(
                instance, "height", value[1] + 20
            ))            





            card.add_widget(lbl)

            btns = []

            for opt in q["options"]:
                btn = ToggleButton(
                    text=opt,
                    group=q["question"],
                    size_hint_y=None,
                    height=45,
                    background_normal="",
                    background_color=(0.18, 0.25, 0.45, 1)
                )

                btns.append(btn)
                card.add_widget(btn)

            self.container.add_widget(card)
            self.groups.append((btns, q["answer"]))

        self.scroll.scroll_y = 1









    # ================= NEXT =================
    # def next_page(self, instance):
    #     total = ((len(QUESTIONS_AD) - 1) // QUESTIONS_PER_PAGE) + 1
    #     if self.page < total - 1:
    #         self.page += 1
    #         self.load_questions()

    def next_page(self, instance):
        total = (
            (len(self.all_questions) - 1) // QUESTIONS_PER_PAGE
        ) + 1

        if self.page < total - 1:
            self.page += 1
            self.load_questions()




    # ================= PREV =================
    def prev_page(self, instance):
        if self.page > 0:
            self.page -= 1
            self.load_questions()


    def check_quiz_result(self, instance):
        for buttons, ans in self.groups:
            for b in buttons:
                b.background_color = (0.15, 0.25, 0.45, 1)

                if b.text == ans:
                    b.background_color = (0, 0.8, 0.3, 1)
                elif b.state == "down":
                    b.background_color = (1, 0.2, 0.2, 1)

    def go_home(self, instance):
        self.manager.current = "home"










from kivy.uix.spinner import SpinnerOption
from kivy.graphics import Color, RoundedRectangle


def style_glass_spinner(spinner):

    # Remove default background
    spinner.background_normal = ""
    spinner.background_down = ""
    spinner.background_color = (0, 0, 0, 0)

    # Text color
    spinner.color = (0, 0, 0, 1)
    spinner.font_size = "16sp"

    # Rounded yellow background
    with spinner.canvas.before:
        Color(1, 0.85, 0, 1)

        spinner.bg = RoundedRectangle(
            pos=spinner.pos,
            size=spinner.size,
            radius=[20]
        )

    # Update background
    def update_bg(*args):
        spinner.bg.pos = spinner.pos
        spinner.bg.size = spinner.size

    spinner.bind(pos=update_bg, size=update_bg)

    # Dropdown option style
    class Option(SpinnerOption):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            self.background_normal = ""
            self.background_color = (1, 0.85, 0, 1)
            self.color = (0, 0, 0, 1)

    spinner.option_cls = Option

    return spinner






# ================= DATA =================
quiz_data = []
# APP_DURATION = 5


def wrap(text, max_len=30):
    words = str(text).split()
    lines = []
    line = ""

    for w in words:
        if len(line + w) < max_len:
            line += w + " "
        else:
            lines.append(line)
            line = w + " "

    if line:
        lines.append(line)

    return lines










# from moviepy.editor import VideoClip
import colorsys


# =========================================
# BACKGROUND MODE
# =========================================
# bg_mode = "simple"


# # =========================================
# # MODE FUNCTIONS
# # =========================================
# def set_simple():
#     global bg_mode
#     bg_mode = "simple"


# def set_galaxy():
#     global bg_mode
#     bg_mode = "galaxy"
#     print("Galaxy Selected:", bg_mode)


# def set_matrix():
#     global bg_mode
#     bg_mode = "matrix"
#     print("Matrix Selected:", bg_mode)


# def set_fire():
#     global bg_mode
#     bg_mode = "fire"
#     print("fire Selected:", bg_mode)


# def set_neon():
#     global bg_mode
#     bg_mode = "neon"
#     print("Neon Selected:", bg_mode)


# def set_cyberpunk():
#     global bg_mode
#     bg_mode = "cyberpunk"
#     print("Cyberpunk Selected:", bg_mode)








# def box(img, x1, y1, x2, y2, color=(255,255,255), text="", font=None):

#     # cv2 remove version
#     h, w = img.shape[:2]

#     if isinstance(color, str):
#         color = (255,255,255)

#     if len(color) >= 3:
#         r = min(255, int(color[0]))
#         g = min(255, int(color[1]))
#         b = min(255, int(color[2]))
#     else:
#         r, g, b = 255, 255, 255

#     # background fill
#     img[y1:y2, x1:x2] = (
#         int(r * 0.25),
#         int(g * 0.25),
#         int(b * 0.25)
#     )

#     # border
#     img[y1:y1+3, x1:x2] = (r, g, b)
#     img[y2-3:y2, x1:x2] = (r, g, b)
#     img[y1:y2, x1:x1+3] = (r, g, b)
#     img[y1:y2, x2-3:x2] = (r, g, b)

#     pil_img = PILImage.fromarray(img)
#     draw = ImageDraw.Draw(pil_img)

#     # try:
#     #     font_size = 120
#     #     # font_size = int(h * 0.06)
#     #     # font = ImageFont.truetype("arial.ttf", font_size        )
#     # except:
#     #     font = ImageFont.load_default()

#     # try:
#     #     font_size = int(h * 0.06)
#     #     font = ImageFont.truetype(
#     #        FONT_PATH,
#     #        font_size
#     # )
        
        
#     #     print("ARIAL FONT LOADED")
#     # except Exception as e:
#     #     print("FONT ERROR:", e)
#     #     font = ImageFont.load_default()    


#     # padding = 25

#     # font = get_fit_font(
#     #     draw,
#     #     text,
#     #     (x2 - x1) - padding * 2,
#     #     (y2 - y1) - padding * 2
#     # )

#     padding = 25

#     if font is None:

#         font = get_fit_font(
#             draw,
#             text,
#             (x2 - x1) - padding * 2,
#             (y2 - y1) - padding * 2
#         )








#     # draw.text(
#     #     (x1 + 20, y1 + 20),
#     #     text,
#     #     fill=(255, 255, 255),
#     #     font=font
#     # )


#     bbox = draw.multiline_textbbox(
#         (0,0),
#         text,
#         font=font
#     )

#     text_w = bbox[2] - bbox[0]
#     text_h = bbox[3] - bbox[1]

#     tx = x1 + ((x2 - x1) - text_w) // 2
#     ty = y1 + ((y2 - y1) - text_h) // 2

#     draw.multiline_text(
#         (tx, ty),
#         text,
#         fill=(255,255,255),
#         font=font,
#         align="center"
#     )






#     img[:] = np.array(pil_img)    






#     return img














# def draw_quiz(img, q, opts, correct):

#     h, w = img.shape[:2]
#     pil_img = PILImage.fromarray(img)
#     draw = ImageDraw.Draw(pil_img)

#     all_text = "Q: " + str(q) + " " + " ".join(opts)

#     font = get_fit_font(
#         draw,
#         all_text,
#         int(w * 0.80) - 50,
#         int(h * 0.20) - 50
#     )    

#     box_w = int(w * 0.80)      # Screen ki width ka 80%
#     box_h = int(h * 0.12)      # Height ka 7%
#     gap = int(h * 0.02)
#     q_h = int(h * 0.20)

#     total_h = q_h + (box_h + gap) * 4

#     start_y = (h - total_h) // 2

#     qx1 = (w - box_w) // 2
#     qx2 = qx1 + box_w

#     qy2 = start_y + q_h

#     question_text = "\n".join(
#         textwrap.wrap("Q: " + str(q), width=25)
#     )



#     # QUESTION
#     # box(
#     #     img,
#     #     qx1,
#     #     start_y,
#     #     qx2,
#     #     qy2,
#     #     (255, 223, 0 ,1),
#     #     question_text
#     # )

#     box(
#         img,
#         qx1,
#         start_y,
#         qx2,
#         qy2,
#         (255, 223, 0 ,1),
#         question_text,
#         font
#     )    
  
  
  
  
#     # QUESTION
#     # box(
#     #     img,
#     #     qx1,
#     #     start_y,
#     #     qx2,
#     #     qy2,
#     #     (255, 223, 0 ,1),
#     #     "Q: " + str(q)
#     # )

#     colors = [
      
#         (82, 32, 129,1),
#         (82, 32, 129,1),
#         (82, 32, 129,1),
#         (82, 32, 129,1)
#     ]

#     labels = ["A","B","C","D"]

#     for i in range(4):

#         y1 = qy2 + 20 + i * (box_h + gap)
#         y2 = y1 + box_h


#         opt = "\n".join(
#             textwrap.wrap(
#                 f"{labels[i]}) {opts[i]}",
#                 width=28
#             )
#         )

#         # box(
#         #     img,
#         #     qx1,
#         #     y1,
#         #     qx2,
#         #     y2,
#         #     colors[i],
#         #     opt
#         # )


#         box(
#             img,
#             qx1,
#             y1,
#             qx2,
#             y2,
#             colors[i],
#             opt,
#             font
#         )



#         # opt = opts[i] if i < len(opts) else ""

#         # box(
#         #     img,
#         #     qx1,
#         #     y1,
#         #     qx2,
#         #     y2,
#         #     colors[i],
#         #     f"{labels[i]}) {opt}"
#         # )










# def get_fit_font(draw, text, max_width, max_height):

#     size = 100

#     while size > 20:

#         font = ImageFont.truetype(FONT_PATH, size)

#         bbox = draw.multiline_textbbox((0,0), text, font=font)

#         w = bbox[2]-bbox[0]
#         h = bbox[3]-bbox[1]

#         if w <= max_width and h <= max_height:
#             return font

#         size -= 2

#     return ImageFont.truetype(FONT_PATH,20)












# def get_frame_size(frame_size):

#     if frame_size == "youtube_shorts":
#         return 1080, 1920

#     elif frame_size == "tiktok":
#         return 1080, 1920

#     elif frame_size == "square":
#         return 1080, 1080

#     elif frame_size == "wide":
#         return 1920, 1080

#     else:
#         return 1080, 1920




# def draw_frame(draw, frame_style, w, h):

#     # ======================
#     # CLEAN WHITE
#     # ======================
#     if frame_style == "clean":

#         draw.rounded_rectangle(
#             [(20,20),(w-20,h-20)],
#             radius=25,
#             outline=(255,255,255),
#             width=6
#         )

#     # ======================
#     # TIKTOK
#     # ======================
#     elif frame_style == "tiktok":

#         draw.rounded_rectangle(
#             [(15,15),(w-15,h-15)],
#             radius=40,
#             outline=(255,0,120),
#             width=10
#         )

#         draw.rounded_rectangle(
#             [(30,30),(w-30,h-30)],
#             radius=40,
#             outline=(0,255,255),
#             width=5
#         )

#     # ======================
#     # YOUTUBE
#     # ======================
#     elif frame_style == "youtube":

#         draw.rounded_rectangle(
#             [(20,20),(w-20,h-20)],
#             radius=20,
#             outline=(255,0,0),
#             width=10
#         )

#     # ======================
#     # GOLD PREMIUM
#     # ======================
#     elif frame_style == "gold":

#         draw.rounded_rectangle(
#             [(20,20),(w-20,h-20)],
#             radius=30,
#             outline=(255,215,0),
#             width=10
#         )

#     # ======================
#     # NEON
#     # ======================
#     elif frame_style == "neon":

#         draw.rounded_rectangle(
#             [(15,15),(w-15,h-15)],
#             radius=40,
#             outline=(0,255,255),
#             width=10
#         )

#         draw.rounded_rectangle(
#             [(30,30),(w-30,h-30)],
#             radius=40,
#             outline=(255,0,255),
#             width=5
#         )

#     # ======================
#     # GAMING
#     # ======================
#     elif frame_style == "gaming":

#         draw.rectangle(
#             [(20,20),(w-20,h-20)],
#             outline=(0,255,0),
#             width=8
#         )

#         draw.rectangle(
#             [(40,40),(w-40,h-40)],
#             outline=(0,150,255),
#             width=4
#         )

#     # ======================
#     # ROYAL
#     # ======================
#     elif frame_style == "royal":

#         draw.rounded_rectangle(
#             [(20,20),(w-20,h-20)],
#             radius=50,
#             outline=(180,120,255),
#             width=12
#         )

#     # ======================
#     # DEFAULT
#     # ======================
#     else:

#         draw.rounded_rectangle(
#             [(20,20),(w-20,h-20)],
#             radius=25,
#             outline=(255,255,255),
#             width=5
#         )










# def make_frame(q, opts, correct, ):

#     def frame(t):

#         print("FRAME SIZE VALUE =", frame_size)

#         h, w = get_frame_size()
        
#         print("WIDTH =", w)
#         print("HEIGHT =", h)    

#         global bg_mode
#         global stars
#         global matrix_drops

#         # =========================================
#         # SIMPLE BACKGROUND
#         # =========================================
         
#         print("FRAME BG =", bg_mode)

        

#         if bg_mode == "simple":

#     # create blank image
  

#     # fill green background
#            img[:] = (0, 180, 0)

#     # ❌ cv2.GaussianBlur removed
#     # 🔥 instead: simple soft effect simulation (light smoothing)

#     # fake "soft blur" effect (safe approximation)
#            img = (img * 0.95 + 20).astype(np.uint8)
       





#     #     elif bg_mode == "galaxy":

#     # #
#     #       img[:] = (10, 0, 25)

   
#     #       if stars is None:
#     #          stars = []

#     #          for i in range(300):

#     #             stars.append({
#     #             "x": random.randint(0, w),
#     #             "y": random.randint(0, h),
#     #             "speed": random.uniform(0.2, 1.8),
#     #             "size": random.randint(1, 3),
#     #             "twinkle": random.uniform(0.5, 1.5)
#     #         })

    
#     #       for s in stars:

#     #         s["y"] += s["speed"]

#     #         if s["y"] > h:
#     #            s["y"] = 0
#     #            s["x"] = random.randint(0, w)

           
#     #         brightness = min(255, int(180 + 75 * s["twinkle"]))

#     #         x = int(s["x"])
#     #         y = int(s["y"])
#     #         size = s["size"]

#     #         for i in range(-size, size + 1):
#     #             for j in range(-size, size + 1):

#     #                 if 0 <= x+i < w and 0 <= y+j < h:

               

#     #                     img[y+j, x+i] = np.clip(
#     #                     (brightness, brightness, 255),
#     #                     0,
#     #                     255
#     #                     ).astype(np.uint8)







#     # # 🌠 glow effect (soft center light)
#     #       cx, cy = w // 2, h // 2
#     #       radius = min(w, h) // 3

#     #       for i in range(-radius, radius):

#     #         for j in range(-radius, radius):
   
#     #             if 0 <= cx+i < w and 0 <= cy+j < h:

#     #                 dist = (i*i + j*j) ** 0.5

#     #                 if dist < radius:

#     #                     factor = 1 - (dist / radius)

#     #                     img[cy+j, cx+i] = (
#     #                     int(80 * factor),
#     #                     int(40 * factor),
#     #                     int(180 * factor)
#     #                 )

#     # # 🌫️ fake blur (cv2.GaussianBlur replacement)
#     #     #   img = (img * 0.9 + np.roll(img, 1, axis=0) * 0.1).astype(np.uint8)
#     #       img = np.clip(img, 0, 255).astype(np.uint8)
        


#         # elif bg_mode == "galaxy":

#         #     global galaxy_bg, stars

#         #     if galaxy_bg is None:

#         #         galaxy_bg = np.zeros((h, w, 3), dtype=np.uint8)

#         # # Gradient
#         #         for y in range(h):
#         #             c = int(15 + (40 * y / h))
#         #             galaxy_bg[y, :] = (c, 0, c + 25)

#         #     img = galaxy_bg.copy()

#         #     if stars is None:

#         #         stars = []

#         #         for _ in range(150):
#         #             stars.append({
#         #                 "x": random.randint(0, w - 1),
#         #                 "y": random.randint(0, h - 1),
#         #                 "speed": random.uniform(0.2, 1.2),
#         #                 "size": random.randint(2, 4),
#         #                 "brightness": random.randint(200, 255)
#         #             })

#         #     for s in stars:

#         #         s["y"] += s["speed"]

#         #         if s["y"] >= h:
#         #             s["y"] = 0
#         #             s["x"] = random.randint(0, w - 1)

#         #         x = int(s["x"])
#         #         y = int(s["y"])

#         #         if 0 <= x < w and 0 <= y < h:
#         #             img[y, x] = (
#         #                 s["brightness"],
#         #                 s["brightness"],
#         #                 255
#         #             )

#         #             if s["size"] == 2:

#         #                 if x + 1 < w:
#         #                     img[y, x + 1] = (180, 180, 255)

#         #                 if y + 1 < h:
#         #                     img[y + 1, x] = (180, 180, 255)        






#         # elif bg_mode == "galaxy":

#         #     global galaxy_bg, stars



#         #     if galaxy_bg is None:

#         #         galaxy_bg = np.zeros((h, w, 3), dtype=np.uint8)

#         #         for y in range(h):

#         #             t = y / h

#         #             r = int(8 + 18 * t)
#         #             g = int(0 + 3 * t)
#         #             b = int(30 + 55 * t)

#         #             galaxy_bg[y, :] = (r, g, b)

#         #         cx = w // 2
#         #         cy = h // 2
#         #         radius = int(min(w, h) * 0.42)

#         #         for yy in range(max(0, cy-radius), min(h, cy+radius)):
#         #             for xx in range(max(0, cx-radius), min(w, cx+radius)):

#         #                 dx = xx - cx
#         #                 dy = yy - cy

#         #                 dist = (dx*dx + dy*dy) ** 0.5

#         #                 if dist < radius:

#         #                     factor = 1 - dist / radius

#         #                     galaxy_bg[yy, xx][0] = min(
#         #                         255,
#         #                         galaxy_bg[yy, xx][0] + int(35 * factor)
#         #                     )

#         #                     galaxy_bg[yy, xx][1] = min(
#         #                         255,
#         #                         galaxy_bg[yy, xx][1] + int(8 * factor)
#         #                     )

#         #                     galaxy_bg[yy, xx][2] = min(
#         #                         255,
#         #                         galaxy_bg[yy, xx][2] + int(70 * factor)
#         #                     )

#         #     img = galaxy_bg.copy()


#         #     if stars is None:

#         #         stars = []

#         #         for _ in range(140):

#         #             stars.append({

#         #                 "x": random.randint(0, w-1),

#         #                 "y": random.randint(0, h-1),

#         #                 "speed": random.uniform(0.25, 0.8),

#         #                 "size": random.choice([
#         #                     2,2,2,
#         #                     3,3,
#         #                     4,
#         #                     5
#         #                 ]),

#         #                 "brightness": random.randint(210,255),

#         #                 "twinkle": random.uniform(0.94,1.0)

#         #             })


#         #     for s in stars:

#         #         s["y"] += s["speed"]

#         #         if s["y"] >= h:

#         #             s["y"] = 0

#         #             s["x"] = random.randint(0, w-1)

#         #         brightness = int(
#         #             s["brightness"] * s["twinkle"]
#         #         )

#         #         x = int(s["x"])
#         #         y = int(s["y"])
#         #         size = s["size"]

#         #         for dx in range(-size, size+1):

#         #             for dy in range(-size, size+1):

#         #                 nx = x + dx
#         #                 ny = y + dy

#         #                 if 0 <= nx < w and 0 <= ny < h:

#         #                     dist = dx*dx + dy*dy

#         #                     if dist <= size*size:

#         #                         fade = 1 - (
#         #                             dist /
#         #                             (size*size + 1)
#         #                         )

#         #                         b = int(brightness * fade)

#         #                         img[ny, nx] = (
#         #                             b,
#         #                             b,
#         #                             255
#         #                         )






#         elif bg_mode == "galaxy":

#             global galaxy_bg, stars



#             if galaxy_bg is None:

#                 galaxy_bg = np.zeros((h, w, 3), dtype=np.uint8)

#                 # for y in range(h):

#                 #     t = y / h

#                 #     # r = int(8 + 18 * t)
#                 #     # g = int(0 + 3 * t)
#                 #     # b = int(30 + 55 * t)

#                 #     r = int(4 + 12 * t)
#                 #     g = int(0 + 2 * t)
#                 #     b = int(40 + 45 * t)                                            


#                 #     galaxy_bg[y, :] = (r, g, b)
#                 galaxy_bg[:] = (8, 0, 32)
#                 cx = w // 2
#                 cy = h // 2
#                 radius = int(min(w, h) * 0.42)

#                 for yy in range(max(0, cy-radius), min(h, cy+radius)):
#                     for xx in range(max(0, cx-radius), min(w, cx+radius)):

#                         dx = xx - cx
#                         dy = yy - cy

#                         dist = (dx*dx + dy*dy) ** 0.5

#                         if dist < radius:

#                             factor = 1 - dist / radius

#                             galaxy_bg[yy, xx][0] = min(
#                                 255,
#                                 galaxy_bg[yy, xx][0] + int(45 * factor)
#                             )

#                             galaxy_bg[yy, xx][1] = min(
#                                 255,
#                                 galaxy_bg[yy, xx][1] + int(6 * factor)
#                             )

#                             galaxy_bg[yy, xx][2] = min(
#                                 255,
#                                 galaxy_bg[yy, xx][2] + int(95 * factor)
#                             )

#             img = galaxy_bg.copy()


#             if stars is None:

#                 stars = []

#                 for _ in range(140):

#                     stars.append({

#                         "x": random.randint(0, w-1),

#                         "y": random.randint(0, h-1),

#                         "speed": random.uniform(0.25, 0.8),

#                         "size": random.choice([
#                             3,3,
#                             4,4,
#                             5,5,
#                             6
#                         ]),

#                         "brightness": random.randint(210,255),

#                         "twinkle": random.uniform(0.94,1.0)

#                     })


#             for s in stars:

#                 s["y"] += s["speed"]

#                 if s["y"] >= h:

#                     s["y"] = 0

#                     s["x"] = random.randint(0, w-1)

#                 brightness = int(
#                     s["brightness"] * s["twinkle"]
#                 )

#                 x = int(s["x"])
#                 y = int(s["y"])
#                 size = s["size"]

#                 for dx in range(-size, size+1):

#                     for dy in range(-size, size+1):

#                         nx = x + dx
#                         ny = y + dy

#                         if 0 <= nx < w and 0 <= ny < h:

#                             dist = dx*dx + dy*dy

#                             if dist <= size*size:

#                                 fade = 1 - (
#                                     dist /
#                                     (size*size + 1)
#                                 )

#                                 b = int(brightness * fade)

#                                 img[ny, nx] = (
#                                     b,
#                                     b,
#                                     255
#                                 )







#     #     elif bg_mode == "matrix":

#     #        img = np.zeros((h, w, 3), dtype=np.uint8)

#     #        img[:] = (5, 8, 5)

#     #        letters = "01"

#     #        if "matrix_drops" not in globals():

#     #             matrix_drops = []

#     #             for i in range(180):

#     #                  matrix_drops.append({
#     #             "x": random.randint(0, w - 1),
#     #             "y": random.randint(-h, 0),
#     #             "speed": random.uniform(2, 6),
#     #             "char": random.choice(letters)
#     #         })

#     #        for d in matrix_drops:

#     #            d["y"] += d["speed"]

#     #            if d["y"] > h:

#     #                d["y"] = random.randint(-50, 0)
#     #                d["x"] = random.randint(0, w - 1)
#     #                d["speed"] = random.uniform(2, 6)

#     #            if random.random() < 0.02:

#     #                d["char"] = random.choice(letters)

#     #            x = int(d["x"])
#     #            y = int(d["y"])

#     #     # ❌ cv2.putText replaced with pixel-based rendering
#     #            if 0 <= x < w and 0 <= y < h:

#     #         # main bright pixel (like text center)
#     #                img[y, x] = (0, 255, 120)

#     #         # shadow pixel (like +1 +1 effect)
#     #                if x + 1 < w and y + 1 < h:
#     #                    img[y + 1, x + 1] = (0, 120, 255)

#     #         # small vertical trail effect (matrix feel)
#     #                if y + 2 < h:
#     #                    img[y + 2, x] = (0, 180, 80)

#     # # ❌ cv2.GaussianBlur replaced with simple smoothing logic

#     #            for y in range(1, h - 1):
#     #             for x in range(1, w - 1):

#     #                r, g, b = img[y, x]

#     #         # simple fade / glow smoothing
#     #                img[y, x] = (
#     #             int(r * 0.92),
#     #             int(g * 0.92),
#     #             int(b * 0.92)
#     #         )


        
#         elif bg_mode == "matrix":

#             img = np.zeros((h, w, 3), dtype=np.uint8)
#             img[:] = (5, 8, 5)

#             letters = "01"

#             if matrix_drops is None:

#                 matrix_drops = []

#                 for i in range(180):

#                     matrix_drops.append({
#                         "x": random.randint(0, w - 1),
#                         "y": random.randint(-h, 0),
#                         "speed": random.uniform(2, 6),
#                         "char": random.choice(letters)
#                     })

#             for d in matrix_drops:

#                 d["y"] += d["speed"]

#                 if d["y"] > h:
#                     d["y"] = random.randint(-50, 0)
#                     d["x"] = random.randint(0, w - 1)
#                     d["speed"] = random.uniform(2, 6)

#                 if random.random() < 0.02:
#                     d["char"] = random.choice(letters)

#                 x = int(d["x"])
#                 y = int(d["y"])

#                 if 0 <= x < w and 0 <= y < h:

#                     img[y, x] = (0, 255, 120)

#                     if x + 1 < w and y + 1 < h:
#                         img[y + 1, x + 1] = (0, 120, 255)

#                     if y + 2 < h:
#                         img[y + 2, x] = (0, 180, 80)        





#         elif bg_mode == "fire":

#             img = np.zeros((h, w, 3), dtype=np.uint8)

#     # dark background
#             img[:] = (5, 5, 15)

#     # animated flames
#             for i in range(35):

#                 flame_x = random.randint(0, w)

#         # flames neeche se start hongi
#                 flame_y = random.randint(int(h * 0.55), h)

#         # upar move animation
#                 flame_y -= int((t * 8 + i * 15) % 250)

#                 radius = random.randint(30, 90)

#                 fire_colors = [
#                     (0, 80, 255),    # orange
#                     (0, 140, 255),   # light orange
#                     (0, 200, 255),   # yellow
#                     (40, 255, 255)   # bright yellow
#                 ]

#                 color = random.choice(fire_colors)

#         # flame shape
#                 for dy in range(-radius, radius):

#                     yy = flame_y + dy

#                     if yy < 0 or yy >= h:
#                         continue

#                     for dx in range(-radius // 2, radius // 2):

#                         xx = flame_x + dx

#                         if xx < 0 or xx >= w:
#                             continue

#                 # flame oval shape
#                         dist = (dx * dx) / 1.8 + (dy * dy)

#                         if dist < radius * radius:

#                             fade = 1 - dist / (radius * radius)

#                             img[yy, xx][0] = min(
#                                 255,
#                                 img[yy, xx][0] + int(color[0] * fade * 0.45)
#                             )

#                             img[yy, xx][1] = min(
#                                 255,
#                                 img[yy, xx][1] + int(color[1] * fade * 0.45)
#                             )

#                             img[yy, xx][2] = min(
#                                 255,
#                                 img[yy, xx][2] + int(color[2] * fade * 0.45)
#                             )

#     # soft glow effect
#             img = np.clip(img * 1.08, 0, 255).astype(np.uint8)        






#         elif bg_mode == "neon":

#             img = np.zeros((h, w, 3), dtype=np.uint8)

#     # dark purple background
#             img[:] = (18, 10, 35)

#             colors = [
#                 (255, 0, 180),
#                 (0, 255, 255),
#                 (140, 0, 255),
#                 (0, 255, 120),
#                 (255, 220, 0)
#             ]

#             for i in range(18):

#                 x = random.randint(0, w)
#                 y = random.randint(0, h)

#                 radius = random.randint(25, 70)

#                 color = random.choice(colors)

#                 for dy in range(-radius, radius):

#                     yy = y + dy

#                     if yy < 0 or yy >= h:
#                         continue

#                     for dx in range(-radius, radius):

#                         xx = x + dx

#                         if xx < 0 or xx >= w:
#                             continue

#                         d = dx * dx + dy * dy

#                         if d < radius * radius:

#                             fade = 1 - d / (radius * radius)

#                             img[yy, xx][0] = min(
#                                 255,
#                                 img[yy, xx][0] + int(color[0] * fade * 0.25)
#                             )

#                             img[yy, xx][1] = min(
#                                 255,
#                                 img[yy, xx][1] + int(color[1] * fade * 0.25)
#                             )

#                             img[yy, xx][2] = min(
#                                 255,
#                                 img[yy, xx][2] + int(color[2] * fade * 0.25)
#                             )

#     # halki animation
#             offset = int((t * 4) % w)

#             img = np.roll(img, offset, axis=1)        







#         elif bg_mode == "cyberpunk":

#             img = np.zeros((h, w, 3), dtype=np.uint8)


#             img[:] = (25, 10, 35)


#             spacing = 70

#             offset = int((t * 2) % spacing)

#             for y in range(-spacing, h + spacing, spacing):

#                 yy = y + offset

#                 if 0 <= yy < h:

#                     img[yy:yy+2, :] = (255, 40, 180)

#                     if yy + 2 < h:
#                         img[yy+2:yy+4, :] = (120, 20, 80)


#             spacing = 70

#             offset = int((t * 2) % spacing)

#             for x in range(-spacing, w + spacing, spacing):

#                 xx = x + offset

#                 if 0 <= xx < w:

#                     img[:, xx:xx+2] = (0, 255, 255)

#                     if xx + 2 < w:
#                         img[:, xx+2:xx+4] = (0, 120, 120)


#             scan = int((t * 8) % h)

#             img[max(0, scan-2):min(h, scan+2), :] = (255, 80, 220)

 
#             for i in range(12):

#                 x = (i * 170 + t * 5) % w
#                 y = (i * 130) % h

#                 x = int(x)
#                 y = int(y)

#                 img[max(0,y-2):min(h,y+2),
#                     max(0,x-2):min(w,x+2)] = (255,255,255)

 
#             img = (img * 0.96).astype(np.uint8)        






#         # elif bg_mode == "fire":

#         #     global fire_bg

#         #     if fire_bg is None:

#         #         fire_bg = np.zeros((h, w, 3), dtype=np.uint8)

#         # # Dark background
#         #         for y in range(h):

#         #             t = y / h

#         #             r = int(5 + 25 * t)
#         #             g = int(5 + 8 * t)
#         #             b = int(10 + 5 * t)

#         #             fire_bg[y, :] = (r, g, b)

#         # # Fire glow
#         #         for _ in range(25):

#         #             x = random.randint(0, w - 1)
#         #             y = random.randint(int(h * 0.45), h - 1)

#         #             radius = random.randint(40, 90)

#         #             color = random.choice([
#         #                 (0, 70, 255),
#         #                 (0, 130, 255),
#         #                 (0, 180, 255),
#         #                 (0, 220, 255),
#         #                 (80, 255, 255)
#         #             ])

#         #             for dy in range(-radius, radius):

#         #                 yy = y + dy

#         #                 if yy < 0 or yy >= h:
#         #                     continue

#         #                 for dx in range(-radius, radius):

#         #                     xx = x + dx

#         #                     if xx < 0 or xx >= w:
#         #                         continue

#         #                     dist = dx * dx + dy * dy

#         #                     if dist <= radius * radius:

#         #                         fade = 1 - dist / (radius * radius + 1)

#         #                         fire_bg[yy, xx][0] = min(
#         #                             255,
#         #                             fire_bg[yy, xx][0] + int(color[0] * fade * 0.35)
#         #                         )

#         #                         fire_bg[yy, xx][1] = min(
#         #                             255,
#         #                             fire_bg[yy, xx][1] + int(color[1] * fade * 0.35)
#         #                         )

#         #                         fire_bg[yy, xx][2] = min(
#         #                             255,
#         #                             fire_bg[yy, xx][2] + int(color[2] * fade * 0.35)
#         #                         )

#         #     img = fire_bg.copy()








#     #     elif bg_mode == "fire":

#     #        img = np.zeros((h, w, 3), dtype=np.uint8)

#     #        img[:] = (5, 5, 10)

#     #        colors = [
#     #        (0, 0, 255),
#     #        (0, 80, 255),
#     #        (0, 140, 255),
#     #        (0, 200, 255),
#     #        (40, 255, 255),
#     #        ]

#     # # helper function (soft blur replacement)
#     #        def soft_blend(src, strength=0.85):
#     #            for y in range(h):
#     #                for x in range(w):

#     #                    r, g, b = src[y, x]

#     #                    src[y, x] = (
#     #                 int(r * strength),
#     #                 int(g * strength),
#     #                 int(b * strength)
#     #             )
#     #            return src

#     #        for i in range(40):

#     #            x = np.random.randint(0, w)
#     #            y = np.random.randint(int(h * 0.3), h)

#     #            radius = np.random.randint(10, 60)

#     #            color = colors[np.random.randint(0, len(colors))]

#     #     # simple fire glow simulation (no cv2 circle)
#     #            for dy in range(-radius, radius):

#     #                for dx in range(-radius, radius):

#     #                    nx = x + dx
#     #                    ny = y + dy

#     #                    if 0 <= nx < w and 0 <= ny < h:

#     #                        dist = (dx*dx + dy*dy) ** 0.5

#     #                        if dist < radius:

#     #                            intensity = 1 - (dist / radius)

#     #                            r, g, b = color

#     #                            existing = img[ny, nx]

#     #                            img[ny, nx] = (
#     #                         min(255, existing[0] + int(r * intensity * 0.3)),
#     #                         min(255, existing[1] + int(g * intensity * 0.3)),
#     #                         min(255, existing[2] + int(b * intensity * 0.3)),
#     #                     )

#     # # soft blur replacement (fire glow smoothing)
#     #        img = soft_blend(img, 0.88)

#     #        img = soft_blend(img, 0.95)





        


#     #     elif bg_mode == "neon":

#     #        img = np.zeros((h, w, 3), dtype=np.uint8)

#     #        img[:] = (12, 8, 25)

#     #        colors = [
#     #     np.array([255, 0, 180]),
#     #     np.array([0, 255, 255]),
#     #     np.array([140, 0, 255]),
#     #     np.array([0, 255, 120]),
#     #     np.array([255, 200, 0]),
#     # ]

#     # # pre-generate coordinate grid (FAST optimization)
#     #        yy, xx = np.mgrid[0:h, 0:w]

#     #        for i in range(10):

#     #            cx = np.random.randint(0, w)
#     #            cy = np.random.randint(0, h)
#     #            radius = np.random.randint(90, 200)

#     #            color = colors[np.random.randint(0, len(colors))]

#     #     # distance matrix (modern fast glow)
#     #            dist = np.sqrt((xx - cx)**2 + (yy - cy)**2)

#     #            mask = dist < radius

#     #            intensity = (1 - (dist / radius))
#     #            intensity = np.clip(intensity, 0, 1)
   
#     #            for c in range(3):

#     #                img[:, :, c] += (mask * intensity * color[c] * 0.35).astype(np.uint8)

#     # # soft fade (modern glow smoothing)
#     #        img = (img * 0.92).astype(np.uint8)






#     #     elif bg_mode == "cyberpunk":

#     #        img = np.zeros((h, w, 3), dtype=np.uint8)

#     # # dark cyberpunk background
#     #        img[:] = (35, 5, 25)

#     # # ==========================
#     # # HORIZONTAL NEON GRID
#     # # ==========================

#     #        for i in range(40):

#     #            y = int(i * 30 + (t * 50) % 30)

#     #            if 0 <= y < h:

#     #         # main pink line
#     #                img[max(0, y-1):min(h, y+2), :, :] = (
#     #                    255, 0, 180
#     #             )

#     #         # glow effect
#     #                if y + 3 < h:
#     #                    img[y+3, :, :] = (
#     #                  180, 0, 120
#     #             )

#     # # ==========================
#     # # VERTICAL CYAN LINES
#     # # ==========================

#     #        for i in range(20):

#     #            x = np.random.randint(0, w)

#     #            if 0 <= x < w:

#     #                img[:, x, :] = (
#     #             0, 255, 255
#     #         )

#     #         # soft glow
#     #                if x + 1 < w:
#     #                    img[:, x+1, :] = (
#     #                 0, 120, 120
#     #             )

#     # # ==========================
#     # # RANDOM NEON NODES
#     # # ==========================

#     #        for i in range(30):

#     #            x = np.random.randint(0, w)
#     #            y = np.random.randint(0, h)

#     #            size = np.random.randint(2, 5)

#     #            color = random.choice([
#     #         (255, 0, 180),
#     #         (0, 255, 255),
#     #         (255, 255, 0)
#     #     ])

#     #            x1 = max(0, x-size)
#     #            x2 = min(w, x+size)

#     #            y1 = max(0, y-size)
#     #            y2 = min(h, y+size)

#     #            img[y1:y2, x1:x2] = color

#     # # ==========================
#     # # SIMPLE GLOW FADE
#     # # ==========================

#     #        img = (img * 0.95).astype(np.uint8)


        




# # =========================================
# # QUIZ TIMING SYSTEM (FIXED)
# # =========================================

#         # global APP_DURATION

#         # duration = APP_DURATION

#         # COUNTDOWN_TIME = 3
#         # ANSWER_TIME = 2

#         # QUESTION_TIME = duration - COUNTDOWN_TIME - ANSWER_TIME


        

#         duration = APP_DURATION

      

#         QUESTION_TIME = duration - COUNTDOWN_TIME - ANSWER_TIME

#         QUESTION_FRAMES = QUESTION_TIME * FPS
#         COUNTDOWN_FRAMES = COUNTDOWN_TIME * FPS
#         ANSWER_FRAMES = ANSWER_TIME * FPS

#         TOTAL_FRAMES = QUESTION_FRAMES + COUNTDOWN_FRAMES + ANSWER_FRAMES

        
         

# # =========================================
# # 1️⃣ QUESTION SCREEN
# # =========================================

#         # if t < QUESTION_TIME:
#         if t < QUESTION_FRAMES:
#             draw_quiz(img, q, opts, correct)

# # =========================================
# # 2️⃣ COUNTDOWN SCREEN
# # =========================================

#         # elif t < QUESTION_TIME + COUNTDOWN_TIME:
#         elif t < QUESTION_FRAMES + COUNTDOWN_FRAMES:
#             draw_quiz(img, q, opts, correct)

#     #         remaining = int(
#     #             QUESTION_TIME + COUNTDOWN_TIME - t
#     # )    
#             # remaining = int(
#             #       (QUESTION_FRAMES + COUNTDOWN_FRAMES - t) / FPS           
#             # )
#             remaining = max(0, COUNTDOWN_TIME - (t - QUESTION_FRAMES) // FPS)
#             text = str(remaining) if remaining > 0 else "GO!"

#             center = (w // 2, h // 2)

#             # scale = 1 + 0.5 * abs(np.sin(t * 2))
#             scale = 1 + 0.08 * np.sin((t / FPS) * 2 * np.pi)

#             pil_img = PILImage.fromarray(img)
#             draw = ImageDraw.Draw(pil_img)

#             radius = round(240 * scale)

#             draw.ellipse(
#         (
#             center[0] - radius,
#             center[1] - radius,
#             center[0] + radius,
#             center[1] + radius
#         ),
#                 fill=(255, 255, 0)
#     )

#     #         pil_img = pil_img.filter(
#     #             ImageFilter.GaussianBlur(radius=4)
#     # )

#             draw = ImageDraw.Draw(pil_img)



#             try:
#                 font = ImageFont.truetype(
#                    FONT_PATH,
#                    320
#                 )
#                 print("COUNTDOWN FONT LOADED")
#             except Exception as e:
#                 print("COUNTDOWN FONT ERROR:", e)
#                 font = ImageFont.load_default()            





#     #         draw.text(
#     #             (center[0] - 80, center[1] + 30),
#     #             text,
#     #             fill=(0, 0, 0),
#     #             font=font
#     # )

#     #         draw.text(
#     #     (center[0] - 85, center[1] + 25),
#     #     text,
#     #     fill=(255, 215, 0),
#     #     font=font
#     # )






            
#             bbox = draw.textbbox((0, 0), text, font=font)

#             text_w = bbox[2] - bbox[0]
#             text_h = bbox[3] - bbox[1]

#             # x = (w - text_w) // 2
#             # y = (h - text_h) // 2
             
#             x = (w - text_w) // 2 - bbox[0]
#             y = (h - text_h) // 2 - bbox[1]


#             draw.text(
#                 (x + 6, y + 6),
#                 text,
#                 fill=(0, 0, 0),
#                 font=font
#             )

# # Main text
#             draw.text(
#                 (x, y),
#                 text,
#                 fill=(255, 215, 0),
#                 font=font
#             )















#             img = np.array(pil_img)

#         else:

#             draw_quiz(img, q, opts, correct)

#             pil_img = PILImage.fromarray(img)

#             overlay = PILImage.new(
#         "RGB",
#         (w, h),
#         (0, 0, 0)
#     )

#             overlay_draw = ImageDraw.Draw(overlay)

#             overlay_draw.rectangle(
#         (
#             w // 2 - 350,
#             h // 2 - 120,
#             w // 2 + 350,
#             h // 2 + 120
#         ),
#                 fill=(48, 25, 52)
#     )

#             pil_img = PILImage.blend(
#         pil_img,
#         overlay,
#         0.25
#     )

#             pil_img = pil_img.filter(
#                 ImageFilter.GaussianBlur(radius=2)
#     )

#             draw = ImageDraw.Draw(pil_img)

#             text = "ANSWER: " + correct




#             padding = 80

#             font = get_fit_font(
#                 draw,
#                 text,
#                 w - padding * 2,
#                 300
#             )


#             bbox = draw.textbbox((0, 0), text, font=font)

#             text_w = bbox[2] - bbox[0]
#             text_h = bbox[3] - bbox[1]

#             x = (w - text_w) // 2
#             y = (h - text_h) // 2            









#             # x = w // 2 - 260
#             # y = h // 2

#             glow = PILImage.new(
#         "RGB",
#         (w, h),
#         (0, 0, 0)
#     )

#             glow_draw = ImageDraw.Draw(glow)

#             glow_draw.ellipse(
#         (
#             w // 2 - 220,
#             h // 2 - 220,
#             w // 2 + 220,
#             h // 2 + 220
#         ),
#                 fill=(0, 180, 255)
#     )

#             glow = glow.filter(
#                 ImageFilter.GaussianBlur(radius=35)
#     )

#             pil_img = PILImage.blend(
#         pil_img,
#         glow,
#         0.18
#     )

#             draw = ImageDraw.Draw(pil_img)

      

#             # try:

#             #     font = ImageFont.truetype(
#             #         FONT_PATH,
#             #         250
#             #     )
                
                
#             #     print("ANSWER FONT LOADED")
#             # except Exception as e:
#             #     print("ANSWER FONT ERROR:", e)
#             #     font = ImageFont.load_default()            



#             draw.text(
#         (x, y + 6),
#         text,
#         fill=(0, 0, 0),
#         font=font
#     )

#             draw.text(
#         (x, y),
#         text,
#         fill=(0, 255, 255),
#         font=font
#     )

#             draw.text(
#         (x, y),
#         text,
#         fill=(255, 255, 255),
#         font=font
#     )

#             img = np.array(pil_img)







#         return img

#     return frame







from kivy.uix.button import Button


class TickButton(Button):

    # sab buttons ka record
    all_buttons = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # state
        self.selected = False

        # style
        self.font_size = "22sp"

        self.background_normal = ""

        # default color
        self.background_color = (
            0.25,
            0.25,
            0.25,
            1
        )

        # list main add karo
        TickButton.all_buttons.append(self)

        # click event
        self.bind(on_press=self.toggle_tick)

    # =====================================
    # SINGLE SELECT FUNCTION
    # =====================================
    def toggle_tick(self, *args):

        # pehle sab buttons ko normal karo
        for btn in TickButton.all_buttons:

            btn.selected = False

            btn.background_color = (
                0.25,
                0.25,
                0.25,
                1
            )

        # sirf current button active hoga
        self.selected = True

        self.background_color = (
            0.1,
            0.7,
            0.3,
            1
        )


















KV = '''
<SplashScreen>:
    name: "splash"

    FloatLayout:

        canvas.before:
            Color:
                rgba: 0.02, 0.02, 0.05, 1
            Rectangle:
                pos: self.pos
                size: self.size

        Image:
            id: logo
            source: "ahmed_logo13.png"
 
            size_hint: None, None
            size: 150, 150
            pos_hint: {"center_x": 0.5, "center_y": 0.6}
            opacity: 1   # ✔ IMPORTANT CHANGE

        Label:
            id: title
            text: "AY quiz creator"
            font_size: 24
            color: 1, 1, 1, 1
            pos_hint: {"center_x": 0.5, "center_y": 0.35}
            opacity: 0
'''




class SplashScreen(Screen):

    def on_kv_post(self, base_widget):
        Clock.schedule_once(self.animate, 0.3)
        print("DEBUG: KV POST STARTED")

    def animate(self, dt):
        print("DEBUG: ANIMATE STARTED")
        logo = self.ids.get("logo")
        title = self.ids.get("title")
        print("DEBUG: LOGO =", logo)
        print("DEBUG: TITLE =", title)

        # safety check
        if not logo or not title:
            print("Missing logo/title in KV")
            self.go_main()
            return

        drop = Animation(
            pos_hint={"center_x": 0.5, "center_y": 0.55},
            opacity=1,
            size=(180, 180),
            duration=1.0,
            t='in_quad'
        )

        squash = Animation(size=(220, 120), duration=0.12)
        bounce = Animation(size=(170, 170), duration=0.2, t='out_back')
        settle = Animation(size=(180, 180), duration=0.25)

        anim = drop + squash + bounce + settle

        anim.bind(on_complete=lambda *x: self.zoom_to_camera(logo))
        anim.start(logo)

        Animation(opacity=1, duration=1).start(title)

    def zoom_to_camera(self, logo):

        def zoom(*args):
            anim = Animation(
                size=(self.width * 2, self.height * 2),
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                opacity=0,
                duration=0.6,
                t='out_quad'
            )

            anim.bind(on_complete=lambda *x: self.go_main())
            anim.start(logo)

        Clock.schedule_once(zoom, 0.4)

    def go_main(self):
        self.manager.current = "home"









class Home(Screen):
    pass





def blur_image(input_file, output_file):

    img = PILImage.open(input_file)

    img = img.filter(
        ImageFilter.GaussianBlur(radius=14)
    )

    img.save(output_file)
















TOTAL = len(quiz_data)









class LimitTextInput(TextInput):

    def insert_text(self, substring, from_undo=False):

        if len(self.text) < 12:
            remaining = 12 - len(self.text)
            substring = substring[:remaining]

            return super().insert_text(
                substring,
                from_undo
            )

        return





class Home(Screen):


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.profile_name = ""
        self.profile_country = ""

    
        self.welcome_shown = False

        # self.auto_login(0)
        # Clock.schedule_once(self.show_welcome_popup, 0.5)

        with self.canvas.before:

            self.bg = Rectangle(
                source="ahmed_background.jpeg",
                # source="/mnt//ahtiyat.py/ahmed_background.jpeg",

                size=self.size,
                pos=self.pos
            )
            
            
        # self.add_widget(self.bg)

            Color(0, 0, 0, 0.20)
            

            self.overlay = Rectangle(
                size=self.size,
                pos=self.pos
            )

        self.bind(size=self.update_bg, pos=self.update_bg)





        # self.bg_character = Image(
        #     source="ahmed_background_character.png",
        #     size_hint=(1, 1),
        #     pos_hint={"center_x": 0.48, "center_y": 0.35},
        #     opacity=1
        # )
        # self.add_widget(self.bg_character)

       
       
        
        # self.bg_character = Image(
        #     source="ahmed_frame.png",
        #     size_hint=(1.5, 1.8),
        #     pos_hint={"center_x": 0.51, "center_y": 0.60},
        #     opacity=1
        # )

        # self.add_widget(self.bg_character)
        # self.add_widget(self.layout)


       
   


        self.user_uuid = None
        # layout = FloatLayout()
        # self.add_widget(layout)

        self.layout = FloatLayout()
        self.add_widget(self.layout)




    #     self.my_rank_lbl = Label(
    #         text="Loading your rank...",
    #         font_size="18sp",
    #         bold=True,
    #         color=(1, 1, 1, 1),
    #         size_hint=(0.75, None),
    #         height=35,
    #         pos_hint={
    #           "center_x": 0.50,
    #           "center_y": 0.47
    #         }
    #     )

    #     layout.add_widget(self.my_rank_lbl)        

    #     with self.canvas.before:

    #         Color(0.05, 0.08, 0.18, 1)

           



    #         self.box = RoundedRectangle(
    #     pos=(100, 280),
    #     size=(300, 50),
    #     radius=[20]
    # )


        
    #     self.bind(pos=self.update_box, size=self.update_box)

    # def update_box(self, *args):
    #    self.my_rank_lbl.pos = (100, 280)
    #    self.rank_box.pos = (20, 680)


        

        # self.my_rank_lbl = Label(
        #     text="Loading your rank...",
        #     font_size="18sp",
        #     bold=True,
        #     color=(1, 1, 1, 1),
        #     size_hint=(None, None),
        #     size=(300, 50),
        #     pos=(100, 280)
        # )

        # layout.add_widget(self.my_rank_lbl)

        # with self.canvas.before:
        #     Color(0.05, 0.08, 0.18, 1)

        #     self.rank_box = RoundedRectangle(
        #         pos=(100, 280),
        #         size=(300, 50),
        #         radius=[20]
        #     )
        



        # self.rank_box.bind(pos=self.update_box, size=self.update_box)









        self.profile_lbl = Label(
            text=" ",
            font_size="24sp",
            color=(1,1,1,1),
            halign="center",
            valign="middle",
            size_hint=(None, None),
            size=(300, 100),
            pos_hint={"center_x": 0.5, "center_y": 0.65}
        )

        self.profile_lbl.text_size = self.profile_lbl.size
        self.layout.add_widget(self.profile_lbl)        



       

        self.profile_lbl.opacity = 1
        Clock.schedule_once(lambda dt: self.hide_profile_label(), 2)
        Clock.schedule_once(self.hide_welcome, 10)

   

        # self.my_rank_lbl = Label(
        #     text="Loading your rank...",
        #     font_size="18sp",
        #     bold=True,
        #     color=(1, 1, 1, 1),
        #     size_hint=(None, None),
        #     size=(300, 50),
        #     pos=(30, 525)

        # )
        # self.my_rank_lbl.text_size = (None, None)
        # self.my_rank_lbl.halign = "center"
        # self.my_rank_lbl.valign = "middle"        


        # self.layout.add_widget(self.my_rank_lbl)


       
        # bg_box = BoxLayout(
        #     size_hint=(0.78, 0.40),
        #     pos_hint={"center_x": 0.50, "center_y": 0.530}
        # )

        # with bg_box.canvas.before:
        #     Color(1, 0.85, 0, 1) 
        #     # Color(0.92, 0.90, 1, 0.75) # dark blue background
        #     bg_box.bg = RoundedRectangle(pos=bg_box.pos, size=bg_box.size, radius=[18])

        # def update_bg(instance, value):
        #     instance.bg.pos = instance.pos
        #     instance.bg.size = instance.size

        # bg_box.bind(pos=update_bg, size=update_bg)

        # self.layout.add_widget(bg_box)

        bg_box = BoxLayout(
            size_hint=(0.94, 0.55),  # <-- Isko 0.78, 0.40 se bada kiya
            pos_hint={"center_x": 0.50, "center_y": 0.440}
        )
        with bg_box.canvas.before:
            Color(0.18, 0.12, 0.30, 0.88) # Luxury purple (aap wala dark blue hataya)
            bg_box.bg = RoundedRectangle(pos=bg_box.pos, size=bg_box.size, radius=[22])
            # Gold border add kiya taake bahar nikla hua pata chale
            from kivy.graphics import Line
            Color(1, 0.85, 0, 1)
            bg_box.border = Line(rounded_rectangle=(bg_box.x, bg_box.y, bg_box.width, bg_box.height, 22), width=1.2)

        def update_bg(instance, value):
            instance.bg.pos = instance.pos
            instance.bg.size = instance.size
            instance.border.rounded_rectangle = (instance.x, instance.y, instance.width, instance.height, 22)
        bg_box.bind(pos=update_bg, size=update_bg)
        self.layout.add_widget(bg_box)

        self.scroll = ScrollView(
            do_scroll_x=False,
            do_scroll_y=True,
            size_hint=(0.78, 0.40),
   
            pos_hint={
                "center_x": 0.50,
                "center_y": 0.440
            }
        )   
        
       
        # self.scroll.opacity = 0
        # self.scroll.disabled = True
        self.layout.add_widget(self.scroll)






        self.my_rank_lbl = Label(
            text="Loading your rank...",
            font_size="18sp",
            bold=True,
            color=(1, 1, 1, 1),
            size_hint=(None, None),
            size=(300, 40),
            pos=(20, 110),
            halign="center",
            valign="middle"
        )

        self.my_rank_lbl.text_size = self.my_rank_lbl.size


        self.layout.add_widget(self.my_rank_lbl)


        # with self.canvas.before:

          
        #     Color (0.25, 0.41, 0.88, 1)
            
        #     self.q_shadow = RoundedRectangle(
        #         pos=(27, 110),
        #         size=(315, 34),
        #         radius=[3]
        #     )

        
        
        # self.layout.remove_widget(self.scroll)
       
    

        



        self.rank_layout = BoxLayout(
           orientation="vertical",
           size_hint_y=None,
           spacing=2
           )


        self.rank_layout.bind(
        minimum_height=self.rank_layout.setter("height")
        )

        self.scroll.add_widget(self.rank_layout)
       











        
        for i in range(60):

             btn_scroll = Button(
        text=f"Level {i}",
        size_hint_y=None,
        height=60
    )

             btn_scroll.bind(on_press=self.level_click)  # 🔥 IMPORTANT

             self.rank_layout.add_widget(btn_scroll)






        # =================================
        # TITLE
        # =================================


        # =================================
        # WELCOME LABEL
        # =================================
        



        # Clock.schedule_once(self.auto_login, 1)






        # self.profile_lbl.opacity = 1
        # Clock.schedule_once(self.hide_welcome, 10)




        # Clock.schedule_once(self.auto_login, 1)




    
    #     content = Label(
    #     text=message,
    #     markup=True,
    #     font_size="21sp",
    #     color=(1, 0.85, 0, 1),
    #     halign="center",
    #     valign="middle"
    #     )

    #     popup = Popup(
    #     title="",
    #     content=content,
    #     size_hint=(0.75, 0.35),
    #     auto_dismiss=True
    #     )

    #     popup.open()

    #     content.opacity = 0
    #     Animation(opacity=1, duration=1).start(content)
   
    def on_enter(self, *args):

        if not self.welcome_shown:

            self.welcome_shown = True
            Clock.schedule_once(self.auto_login, 0)    







    def fit_font(self, label):

        size = 28

        while size > 10:

            label.font_size = size
            label.texture_update()

            if label.texture_size[0] <= label.width - 10:
                break

            size -= 1    


    def fit_font1(self, label):

        label.font_size = 28
        label.texture_update()

        while label.texture_size[0] > label.width and label.font_size > 15:

            label.font_size -= 1
            label.texture_update()       







    def close_popup(self, instance):
        if hasattr(self, "popup"):
            self.popup.dismiss()
    


    
    # def fit_font(self, label):

    #     label.font_size = 18
    #     label.texture_update()

    #     while label.texture_size[0] > label.width and label.font_size > 16:

    #         label.font_size -= 1
    #         label.texture_update()       






    def show_welcome_popup(self, message):

        message = str(message)

        layout = FloatLayout()


        content = Label(
            text=message,
            markup=True,
            font_size="21sp",
            color=(1, 0.85, 0, 1),
            halign="center",
            valign="middle",
            size_hint=(0.9, 0.55),
            pos_hint={
                "center_x": 0.5,
                "top": 0.85
            }
        )


        content.bind(
            size=lambda instance, value: setattr(
                instance,
                "text_size",
                (instance.width - 20, instance.height)
            )
        )


        close_btn = Button(
            text="Close",
            size_hint=(0.35, 0.15),
            pos_hint={
                "center_x": 0.5,
                "y": 0.05
            },
            background_color=(0.8, 0.1, 0.1, 1)
        )


        close_btn.bind(
            on_press=self.close_popup
        )


        layout.add_widget(content)
        layout.add_widget(close_btn)


        self.popup = Popup(
            title="",
            content=layout,
            size_hint=(0.80, 0.45),
            auto_dismiss=False,
            background="",
            background_color=(0.12, 0.03, 0.20, 1)
        )


        self.popup.open()


        content.opacity = 0
        Animation(
            opacity=1,
            duration=1
        ).start(content)    












    # def show_welcome_popup(self, message):
    #     message = str(message)

    #     content = Label(
    #         text=message,
    #         markup=True,
    #         font_size="21sp",
    #         color=(1, 0.85, 0, 1),
    #         halign="center",
    #         valign="middle",


    #     )

    #     popup = Popup(
    #         title="",
    #         content=content,
    #         size_hint=(0.80, 0.45),
    #         auto_dismiss=True,
    #         background="",
    #         background_color = (0.12, 0.03, 0.20, 1)
    #     )



    #     close_btn = Button(
    #         text="Close",
    #         size_hint=(0.3, 0.12),
    #         pos_hint={"center_x": 0.5, "y": 0.03},
    #         background_color=(0.8, 0.1, 0.1, 1)
    #     )

    #     close_btn.bind(on_press=self.close_popup)        

    #     content.bind(
    #         size=lambda instance, value: setattr(
    #             instance,
    #             "text_size",
    #             (instance.width - 20, None)
    #         )
    #     )

    #     popup.open()

    #     content.opacity = 0
    #     Animation(opacity=1, duration=1).start(content)        

    def hide_profile_label(self):
        self.profile_lbl.opacity = 0



    def show_vip_popup(self, message):

        layout = FloatLayout()

        blur_image(
            "vip_piture.jpeg",
            "vip_blur.jpeg"
        )        


        bg = Image(
            source="vip_blur.jpeg",
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1,1),
            pos_hint={"x":0,"y":0}
        )

        layout.add_widget(bg)          

        # label = Label(
        #     text=message,
        #     markup=True,
        #     font_size="24sp",
        #     bold=True,
        #     color=(1,1,0,1),
        #     halign="center",
        #     valign="middle",
        #     size_hint=(1,1)        
        # )

        label = Label(
            text=message,
            markup=True,
            font_size="24sp",
            bold=True,
            color=(1, 1, 1, 1),
            halign="center",
            valign="middle",
            size_hint=(0.9,0.9),
            pos_hint={"center_x":0.5,"center_y":0.5}
        )

        label.bind(
            size=lambda instance, value: setattr(
                instance,
                "text_size",
                (instance.width, None)
            )
        )


        
        close_btn1 = Button(
            text="X",
            size_hint=(0.15, 0.1),
            pos_hint={"center_x": 0.1, "y": 0.9},
            background_color=(0.8, 0.1, 0.1, 1)
        )


        layout.add_widget(close_btn1)

        layout.add_widget(label)   
        popup = Popup(
            title="",
            separator_height=0,
            background="",
            background_color=(0,0,0,0),
            content=layout,
            size_hint=(0.8,0.6),
            auto_dismiss=True
        )

        close_btn1.bind(on_press=popup.dismiss) 
        popup.open()                  



    
    # def close_popup(self, instance):
    #     if hasattr(self, "popup"):
    #         self.popup.dismiss()



    def level_click(self, instance):
        print("Clicked:", instance.text)

 

    def update_bg(self, *args):

        self.bg.size = self.size
        self.bg.pos = self.pos

        # self.overlay.size = self.size
        # self.overlay.pos = self.pos


    # def show_scroll(self, dt):
    #     Animation(opacity=1, duration=0.6).start(self.scroll)

    # def show_scroll(self, dt):
       
    #      self.scroll.opacity = 1
    #      self.scroll.disabled = False



    def hide_welcome(self, dt):
        from kivy.animation import Animation
        Animation(opacity=0, duration=0.6).start(self.profile_lbl)



















    # =====================================
    # AUTO LOGIN
    # =====================================

    

    def auto_login(self, dt):

      try:
        with open("user_uuid.txt", "r") as f:
            user_uuid = f.read().strip()

        if not user_uuid:
            self.open_profile_popup(0)
            return

        data = db.child("users").child(user_uuid).get().val()
        # name = data.get("name", "Player")

        if data: 



            self.user_uuid = user_uuid

            name = str(data.get("name", "")).strip().lower()
            country = str(data.get("country", "")).strip().lower()
            bio = str(data.get("bio", "")).strip().lower()

            self.profile_name = name
            print("PROFILE NAME =", repr(self.profile_name))

            

            first_login = data.get("first_login", True)

            flag = self.country_flag(country)
            self.load_ranking()            







            # self.user_uuid = user_uuid
            
            # name = data.get("name", "Player")
            # name = data.get("name", "")
            # country = data.get("country", "")
            # bio = data.get("bio", "")
            # name = name.strip().lower()
            # country = country.strip().lower()
            # bio = bio.strip().lower()            

            # self.profile_name = name
            # first_login = data.get("first_login", True)         

            # flag = self.country_flag(country)
            # self.load_ranking()

            # vip_users1 = ("naik.alam104","naik.alam.14",)

            vip_users2 = {                           
                            "naik.alam104": {
                               "bio": "brother ahmed"
                           },
                           "naik.alam.14": {
                               "bio": "czn ahmed"
                           }
                       }
           
            # vip_users2 = ("ahmed.786","miniboy.786",)
            
            vip_users1 = {                           
                            "me.ahmed.": {
                               "bio": "my app"
                           },
                           "me.app.786": {
                               "bio": "owner"
                           }
                       }

          

            # vip_users = ("yash.786", "myapp.786",)
            vip_users = {
                           "yashfa.786": {
                               "bio": "my husband"
                           },
                           "me.one.786": {
                               "bio": "co-owner"
                           }
                       }
            user_name = name
            # if name.lower() in vip_users:
            # if name.upper() in vip_users:
            if (
                user_name in vip_users
                and bio == vip_users[user_name]["bio"]
            ):

                if first_login:

                    msg = f"Welcome, my Love, I welcome you to your own app {name.upper()}"

                    db.child("users").child(user_uuid).update({
                        "first_login": False
                    })

                else:

                    msg = f"Welcome, my Love, I welcome you to your own app {name.upper()}"            
               
                self.welcome_message = msg
                self.welcome_type = "vip"
                
               




            # elif  name.upper() in vip_users1:
            elif (
                user_name in vip_users1
                and bio == vip_users1[user_name]["bio"]
            ):

                if first_login:

                    msg = f"Welcome, Boss; welcome to your own App. {name.upper()}"

                    db.child("users").child(user_uuid).update({
                        "first_login": False
                    })

                else:

                    msg = f"Welcome, Boss; welcome to your own App. {name.upper()}" 
                
                self.welcome_message = msg
                self.welcome_type = "vip"
                
             




            elif (
                user_name in vip_users2
                and bio == vip_users2[user_name]["bio"]
            ):
            
            
                if first_login:

                    msg = f"Welcome, brother, and congratulations on your wedding. {name.upper()}"

                    db.child("users").child(user_uuid).update({
                        "first_login": False
                    })

                else:

                    msg = f"Welcome, brother, and congratulations on your wedding. {name.upper()}"     
               
                self.welcome_message = msg
                self.welcome_type = "normal"
               
               
           



            else:

                if first_login:

                    msg = f"WELCOME  {name}"

                    db.child("users").child(user_uuid).update({
                        "first_login": False
                    })

                else:

                    msg = f"WELCOME BACK  {name}"            
               
                self.welcome_message = msg
                self.welcome_type = "normal"












            self.profile_lbl.text_size = self.profile_lbl.size
            self.profile_lbl.halign = "center"
            self.profile_lbl.valign = "middle"
            self.profile_lbl.texture_update()
            self.profile_lbl.opacity = 1            
           
            if hasattr(self, "welcome_message"):

                if self.welcome_type == "vip":
                    self.show_vip_popup(self.welcome_message)

                else:
                    self.show_welcome_popup(self.welcome_message)

                del self.welcome_message
                del self.welcome_type            


        else:
            self.open_profile_popup(0)

      except Exception as e:
        print("Firebase error:", e)
        self.open_profile_popup(0)
        










    # =====================================
    # PROFILE POPUP
    # =====================================

    def open_profile_popup(self, dt):

       popup_layout = FloatLayout()

    # ================= NAME =================
       self.name_input = LimitTextInput(
        hint_text="Enter Name",
        size_hint=(0.8, 0.12),
        pos_hint={"center_x": 0.5, "center_y": 0.80}
    )

       popup_layout.add_widget(self.name_input)

    # ================= COUNTRY =================
       self.edit_country = Spinner(
        text="Select Country",
        values=("Pak", "Ind", "USA", "UK", "SA", "AE", "CA"),
        size_hint=(0.5, 0.12),
        pos_hint={"center_x": 0.5, "center_y": 0.38}
    )

       popup_layout.add_widget(self.edit_country)

    # ================= BIO =================
       self.bio_input = TextInput(
        hint_text="Write About Yourself",
        multiline=True,
        size_hint=(0.8, 0.12),
        pos_hint={"center_x": 0.5, "center_y": 0.60}
    )

       popup_layout.add_widget(self.bio_input)

    # ================= SAVE BUTTON =================
       save_btn = Button(
        text="SAVE PROFILE",
        size_hint=(0.5, 0.13),
        pos_hint={"center_x": 0.5, "center_y": 0.10},
        background_normal="",
        background_color=(0, 0.7, 0.5, 1)
    )

       popup_layout.add_widget(save_btn)

    # ================= POPUP =================
       self.popup = Popup(
         title="Create Profile",
        content=popup_layout,
        size_hint=(0.90, 0.75),
        auto_dismiss=False
    )

    # SAVE FUNCTION BIND
       save_btn.bind(on_press=self.save_profile)

       self.popup.open()


    def open_edit_popup(self, instance):

       layout = FloatLayout()

    # ================= NAME =================
       self.edit_name = LimitTextInput(
        hint_text="Enter Name",
        size_hint=(0.8, 0.12),
        pos_hint={"center_x": 0.5, "center_y": 0.78},
        multiline=False
    )

       layout.add_widget(self.edit_name)

    # ================= COUNTRY =================
       self.edit_country = Spinner(
        text="Select Country",
        values=("PK", "IN", "US", "UK", "SA", "AE", "CA"),
        size_hint=(0.5, 0.12),
        pos_hint={"center_x": 0.5, "center_y": 0.40}
    )

       layout.add_widget(self.edit_country)

    # ================= BIO =================
       self.edit_bio = TextInput(
        hint_text="Bio",
        size_hint=(0.8, 0.12),
        pos_hint={"center_x": 0.5, "center_y": 0.6}
    )

       layout.add_widget(self.edit_bio)

    # ================= SAVE BUTTON =================
       save_btn = Button(
        text="SAVE PROFILE",
        size_hint=(0.5, 0.12),
        pos_hint={"center_x": 0.5, "center_y": 0.12},
        background_normal="",
        background_color=(0, 0.7, 0.5, 1)
    )

       layout.add_widget(save_btn)
      
       close_btn = Button(
             text="X",
             size_hint=(None, None),
             size=(40, 40),
             pos_hint={"right": 1, "top": 1.1},
             background_normal="",
             background_color=(1, 0, 0, 1),   # Red
             color=(1, 1, 1, 1)               # White X
)
       layout.add_widget(close_btn)
       close_btn.bind(on_release=self.close_popup)

    # ================= POPUP =================
       self.popup = Popup(
        title="Edit Profile",
        content=layout,
        size_hint=(0.7, 0.5),
        auto_dismiss=False
    )

    # bind save function
       save_btn.bind(on_press=self.save_profile_edit)

       self.popup.open()

    def close_popup(self, instance):
         self.popup.dismiss()

    def save_profile_edit(self, instance):

       name = self.edit_name.text.strip()
       self.profile_name = name
       country = self.edit_country.text.strip().upper()
       self.profile_country = country
       bio = self.edit_bio.text.strip()

       if self.user_uuid is None:
        return

    # ================= FIREBASE UPDATE (PYREBASE) =================
       db.child("users").child(self.user_uuid).update({
        "name": name,
        "country": country,
        "bio": bio
    })

       flag = self.country_flag(country)

    # ================= SPECIAL WELCOME LOGIC =================
       if name.lower() == "yashfa ashfaq":
        welcome_msg = "Welcome, my love, I welcome you to my app."
       elif name.lower() == "yashfa ashfaq":
        welcome_msg = "How does it feel to be logged into your husband app and show my love?"
       else:
        welcome_msg = f"WELCOME {name}"

    # ================= UI UPDATE =================
       self.profile_lbl.text = (
        f"{welcome_msg} {flag}\n\n"
        f"🌍 {country}\n\n"
        f"💬 {bio}"
    )

       self.popup.dismiss()
       self.load_ranking()





    def save_profile(self, instance):

       name = self.name_input.text.strip()
       self.profile_name = name
       country = self.edit_country.text.strip().upper()
       self.profile_country = country
       bio = self.bio_input.text.strip()

       if name == "" or country == "":
        return

    # ================= UUID =================
       user_uuid = str(uuid.uuid4())
       self.user_uuid = user_uuid

    # ================= USER DATA =================
       user_data = {
        "uuid": user_uuid,
        "name": name,
        "country": country,
        "bio": bio,
        "high_score": 0,
        "first_login": True
    }

    # ================= SAVE FIREBASE (PYREBASE) =================
       db.child("users").child(user_uuid).set(user_data)

    # ================= SAVE LOCAL UUID =================
       with open("user_uuid.txt", "w") as f:
        f.write(user_uuid)

    # ================= FLAG =================
       flag = self.country_flag(country)

    # ================= SHOW PROFILE =================
       self.profile_lbl.text = (
        f"👋 WELCOME {name} {flag}\n\n"
        f"🌍 Country: {country}\n\n"
        f"💬 {bio}"
    )

    # ================= SHOW UUID POPUP =================
       self.show_uuid_popup(user_uuid)

       self.popup.dismiss()

    # ================= LOAD LEADERBOARD =================
       self.load_ranking()


 

    # =====================================
    # UUID POPUP
    # =====================================

   

     

    def show_uuid_popup(self, user_uuid):

       layout = FloatLayout()

    # ================= LABEL =================
       lbl = Label(
        text=(
            "SAVE THIS UUID\n\n"
            f"{user_uuid}\n\n"
            "Next time login will work."
        ),
        halign="center",
        size_hint=(0.9, 0.5),
        pos_hint={"center_x": 0.5, "center_y": 0.65}
    )

       layout.add_widget(lbl)

    # ================= COPY BUTTON =================
       copy_btn = Button(
        text="COPY UUID",
        size_hint=(0.5, 0.18),
        pos_hint={"center_x": 0.5, "center_y": 0.20},
        background_normal="",
        background_color=(0, 0.7, 1, 1)
    )

       layout.add_widget(copy_btn)

    # ================= POPUP =================
       popup = Popup(
        title="IMPORTANT",
        content=layout,
        size_hint=(0.85, 0.45),
        auto_dismiss=True
    )

    # ================= COPY ACTION =================
       copy_btn.bind(
        on_press=lambda x: Clipboard.copy(str(user_uuid))
    )

       popup.open()










    # =====================================
    # COUNTRY FLAG
    # =====================================

    def country_flag(self, code):

        flags = {

            "pak":"pak",

            "IN":"Ind",

            "US":"🇺sa",

            "UK":"Uk",

            "SA":"Sa",

            "AE":"🇦e",

            "CA":"Ca"
        }

        return flags.get(code, "🌍")

    # =====================================
    # PLAY GAME
    # =====================================

    def play_game(self, instance):

        import random

        # RANDOM SCORE

        new_score = random.randint(0,200)

        self.update_score(new_score)

    # =====================================
    # UPDATE HIGH SCORE
    # =====================================

    def update_score(self, new_score):

      if self.user_uuid is None:
        return

    # ================= GET USER DATA =================
      data = db.child("users").child(self.user_uuid).get().val()

      if not data:
        return

      old_score = data.get("high_score", 0)

    # ================= ONLY SAVE HIGH SCORE =================
      if new_score > old_score:

        db.child("users").child(self.user_uuid).update({
            "high_score": new_score
        })

        popup = Popup(
            title="NEW HIGH SCORE",
            content=Label(
                text=f"⭐ NEW HIGH SCORE\n\n{new_score}"
            ),
            size_hint=(0.7, 0.3)
        )

        popup.open()

      else:

        popup = Popup(
            title="GAME OVER",
            content=Label(
                text=(
                    f"YOUR SCORE: {new_score}\n\n"
                    f"HIGH SCORE: {old_score}"
                )
            ),
            size_hint=(0.7, 0.3)
        )

        popup.open()

    # ================= REFRESH LEADERBOARD =================
      self.load_ranking()



    






    def load_ranking(self):

    # ================= SAFETY CHECK =================
      if not hasattr(self, "rank_layout"):
        print("rank_layout missing")
        return

      self.rank_layout.clear_widgets()

      try:
        users = db.child("users").get().val()
      except Exception as e:
        print("Firebase error:", e)
        return

      if not users:
        return

      leaderboard = []


    #   for key, data in users.items():

    #     leaderboard.append({
    #         "name": data.get("name", "Unknown"),
    #         "score": data.get("high_score", 0),
    #         "country": data.get("country", "Pak"),
    #         "flag": self.country_flag(data.get("country", "Pak"))
    #     })
    
    
      for key, data in users.items():

          # Invalid Firebase data ko skip karo
          if not isinstance(data, dict):
              print("SKIPPING INVALID USER:", key, repr(data), flush=True)
              continue

          country = data.get("country", "Pak")

          leaderboard.append({
              "name": data.get("name", "Unknown"),
              "score": data.get("high_score", 0),
              "country": country,
              "flag": self.country_flag(country)
          })
        

   

      leaderboard.sort(key=lambda x: x["score"], reverse=True)

  
      rank = 1
      for user in leaderboard:

        crown = ""
        color = (1, 1, 1, 1)   

        if rank == 1:
            crown = "1st"
            color = (0, 0, 0, 1)       

        elif rank == 2:
            crown = "2nd"
            color = (0, 0, 0, 1) 

        elif rank == 3:
            crown = "3rd"
            color = (0, 0, 0, 1)   

        elif rank == 4:
            crown = "4th"
            color = (0, 0, 0, 1) 

        elif rank == 5:
            crown = "5th"
            color = (0, 0, 0, 1) 

        elif rank == 6:
            crown = "6th"
            color = (0, 0, 0, 1) 

        elif rank == 7:
            crown = "7th"
            color = (0, 0, 0, 1)

        elif rank == 8:
            crown = "8th"
            color = (0, 0, 0, 1) 

        elif rank == 9:
            crown = "9th"
            color = (0, 0, 0, 1)  

        elif rank == 10:
            crown = "10th"
            color = (0, 0, 0, 1)     

      

        else:
            crown = ""
            color = (0, 0, 0, 1) 



        # if user["name"] == self.profile_name:
        #     self.my_rank_lbl.text = (
        #       f"YOU | Rank #{rank} | "
        #       f" {user['name']} | "
        #       f"Score: {user['score']}"
        # )
        
        # self.fit_font(self.my_rank_lbl)





        if str(user.get("name", "")).strip().lower() == str(self.profile_name).strip().lower():

            print("MY RANK FOUND!")
            print("FIREBASE NAME =", repr(user.get("name")))
            print("PROFILE NAME =", repr(self.profile_name))
            print("RANK =", rank)
            print("SCORE =", user.get("score", 0))

            self.my_rank_lbl.text = (
                f"YOU | Rank #{rank} | "
                f"{user.get('name', 'Unknown')} | "
                f"Score: {user.get('score', 0)}"
            )

            self.my_rank_lbl.text_size = self.my_rank_lbl.size
            self.my_rank_lbl.texture_update()

            # self.fit_font(self.my_rank_lbl)    







        # txt = (
        #     f"{crown} | Rank #{rank} | "
        #     f"{user['name']} | "
        #     f"Score: {user['score']}"
        #  )


        txt =(
              f"{crown} | {rank} # {user['name']} | "
              f"Score: {user['score']}"
        )
       
        row = BoxLayout(
              size_hint=(2, None),
              height=30,
              pos_hint={"center_x": 0.5}
            )

 


        if rank == 1:
            # bg_color = (0.72, 0.90, 1.00, 1)
            bg_color = (1, 0.85, 0, 1)
                        

        elif rank == 2:
            bg_color = (1, 0.85, 0, 1)
            # bg_color = (0.74, 0.96, 0.78, 1)
          

        elif rank == 3:
            bg_color = (1, 0.85, 0, 1) 
            # bg_color = (1.00, 0.96, 0.68, 1)
        

        elif rank == 4:
            bg_color = (0.92, 0.90, 1, 0.75)
            # bg_color = (1.00, 0.82, 0.68, 1)
 

        elif rank == 5:
            bg_color = (0.92, 0.90, 1, 0.75) 
            # bg_color = (0.86, 0.80, 1.00, 1)
        
           


        elif rank == 6:
            bg_color = (0.92, 0.90, 1, 0.75)
            # bg_color = (1.00, 0.80, 0.88, 1)
     

        elif rank == 7:
            bg_color = (0.92, 0.90, 1, 0.75)
            # bg_color = (0.72, 0.96, 0.94, 1)
      

        elif rank == 8:
            bg_color = (0.92, 0.90, 1, 0.75)
            # bg_color = (1.00, 0.87, 0.65, 1)
          

        elif rank == 9:
            bg_color = (0.92, 0.90, 1, 0.75)
            # bg_color = (0.82, 0.94, 0.72, 1)


        elif rank == 10:
            bg_color = (0.92, 0.90, 1, 0.75)  
            # bg_color = (1.00, 0.74, 0.74, 1)



        else:
            bg_color = (0.92, 0.90, 1, 0.75)



        with row.canvas.before:
            Color(*bg_color)  
            row.bg = RoundedRectangle(
                pos=row.pos,
                size=row.size,
                radius=[6]
            )

        def update_rect(instance, value):
            instance.bg.pos = instance.pos
            instance.bg.size = instance.size

        row.bind(pos=update_rect, size=update_rect)

     
        
        # lbl = Label(
        #     text=txt,
        #     font_size="17sp",
        #     size_hint_y=None,
        #     height=25,
        #     color=color
        # )


        lbl = Label(
            text=txt,
            font_size="30sp",
            size_hint_y=None,
            height=25,
            color=color,
            halign="left",
            valign="middle"
        )        





       
        
        




        # lbl.bind(size=lambda inst, val: setattr(inst, "text_size", val))
        self.fit_font1(lbl)
        row.add_widget(lbl)

        self.rank_layout.add_widget(row)        

        rank += 1





    
        











        title = Label(

            text="QUIZVERSE",

            font_size="36sp",

            bold=True,

            color=(0.3,1,0.7,1),

            pos_hint={
                "center_x":0.5,
                "center_y":0.85
            }
        )

        self.layout.add_widget(title)





































        live_title = Label(

            text="PLAYER RANKING",

            font_size="19sp",

            bold=True,

            color=(1, 1, 0, 1),

            pos_hint={
                "center_x": 0.50,
                "center_y": 0.68
            }
        )

        self.layout.add_widget(live_title)

          





        
        start = GlassButton(
            text="QUIZs",
            size_hint=(0.2, 0.02),
            pos_hint={"center_x": 0.86, "center_y": 0.95}
        )




        edit_btn = GlassButton(
          text="EDIT",
          size_hint=(0.2, 0.02),
          pos_hint={"center_x": 0.15, "center_y": 0.95},
          background_normal="",
        #   background_color=(1, 0.6, 0.0, 1)
        )


          
        play_btn = GlassButton(
        text="∞",
        font_size="24sp",
        size_hint=(0.29,0.04),
        pos_hint={
        "center_x":0.18,
        "center_y":0.10
         }
        # background_normal="",
        # background_color=(0,0.8,0.5,1)
        )


        
        btn_kids = GlassButton(
        text="Levels",
        font_size="22sp",
        size_hint=(0.29,0.02),
        pos_hint={
        "center_x":0.50,
        "center_y":0.10
         }
        # background_normal="",
        # background_color=(0,0.8,0.5,1)
        )






        btn = GlassButton(
            text="Generate",
            font_size="22sp",
            size_hint=(0.29, 0.02),
            pos_hint={
                "center_x": 0.82, 
                "center_y": 0.10}
        )
 




        edit_btn.bind(on_press=self.open_edit_popup)
        self.layout.add_widget(edit_btn)
        
  
        play_btn.bind(on_press=self.open_quiz)
        btn_kids.bind(on_press=self.start)

        self.layout.add_widget(play_btn)
        self.layout.add_widget(btn_kids)
       
       
        
        start.bind(on_press=self.start_quiz)
        self.layout.add_widget(start)
        
        btn.bind(on_press=lambda x: setattr(self.manager, "current", "setup"))
        self.layout.add_widget(btn)


       
        
  





    def start(self, instance):
        self.manager.current = "quiz1"
        self.manager.get_screen("quiz1").start_game()
# 
    def open_quiz(self, instance):
       quiz = self.manager.get_screen("Quiz")
       quiz.start_game()
       self.manager.current = "Quiz"


    def start_quiz(self, instance):
        self.manager.current = "quiz"


  
    def update_rank_bg(self, instance, value):

        self.rank_bg.pos = instance.pos

        self.rank_bg.size = instance.size

   




































import random


class Quiz00(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


  
        
        self.menu_popup = None
        self.gameover_popup = None

        # self.popup = None

        # self.correct_sound = SoundLoader.load("dragon.ogg.mp3")
        # self.wrong_sound = SoundLoader.load("wrong.ogg.mp3")
        # self.click_sound = SoundLoader.load("click.ogg.mp3")

         

 

        import os

        BASE = "/mnt/d/ahtiyat.py"

        # self.correct_sound = SoundLoader.load(os.path.join(BASE, "dragon.mp3"))
        # self.wrong_sound = SoundLoader.load(os.path.join(BASE, "wrong.mp3"))
        # self.click_sound = SoundLoader.load(os.path.join(BASE, "click.mp3"))



        print("BEFORE DRAGON LOAD", flush=True)
        # correct_sound = SoundLoader.load(os.path.join(BASE, "dragon.mp3"))
        correct_sound = None
        print("AFTER DRAGON LOAD:", correct_sound, flush=True)

        print("BEFORE WRONG LOAD", flush=True)
        # wrong_sound = SoundLoader.load(os.path.join(BASE, "wrong.mp3"))
        wrong_sound = None
        print("AFTER WRONG LOAD:", wrong_sound, flush=True)

        print("BEFORE CLICK LOAD", flush=True)
        # click_sound = SoundLoader.load(os.path.join(BASE, "click.mp3"))
        click_sound = None
        print("AFTER CLICK LOAD:", click_sound, flush=True)



        


        self.index = 0
        self.score = 0
        self.questions = []
        self.correct = ""

        self.colors = [
            (0.10, 0.60, 1, 0.95),   
            (0.90, 0.30, 0.30, 0.95), 
            (0.30, 0.80, 0.40, 0.95), 
            (0.80, 0.50, 1, 0.95)    
        ]


        with self.canvas.before:

            self.bg = Rectangle(
                source="ahmed_background.jpeg",
                size=self.size,
                pos=self.pos
            )

            Color(0, 0, 0, 0.20)

            self.overlay = Rectangle(
                size=self.size,
                pos=self.pos
            )

        self.bind(size=self.update_bg, pos=self.update_bg)

   

        self.layout = FloatLayout()

        self.add_widget(self.layout)



        with self.layout.canvas.before:

           
            Color(0, 0, 0, 0.85)

            self.q_shadow = RoundedRectangle(
                pos=(10, 435),
                size=(325, 135),
                radius=[2]
            )

           
            Color(1, 1, 1, 87)

            self.q_box = RoundedRectangle(
                pos=(10, 440),
                size=(330, 140),
                radius=[2]
            )

   

        self.q_lbl = Label(
            text="",
            font_size="20sp",
            bold=True,
            color=(0, 0, 0, 1),

            halign="center",
            valign="middle",

            text_size=(330, None),

            pos_hint={
                "center_x": 0.5,
                "center_y": 0.83
            }
        )

        self.layout.add_widget(self.q_lbl)



        self.menu_btn = AppButton3D(
            text="menu",
            size_hint=(0.24, 0.05),
            pos_hint={
              "center_x": 0.87,
              "center_y": 0.95
            })

   

        self.menu_btn.bind(on_press=self.toggle_popup)
        self.layout.add_widget(self.menu_btn)




        self.score_lbl = Label(
            text="Score : 0",
            font_size="22sp",
            bold=True,
            color=(1, 1, 1, 1),

            pos_hint={
                "center_x": 0.15,
                "center_y": 0.97
            }
        )

        self.wrong_lbl = Label(
            text="Wrong : 0/1",
            font_size="20sp",
            bold=True,
            color=(1, 0.2, 0.2, 1),

            pos_hint={
        "center_x": 0.17,
        "center_y": 0.93
            }
        )

        self.layout.add_widget(self.wrong_lbl)


        self.level_lbl = Label(
            text="Level : 1",
            font_size="20sp",
            bold=True,
            color = (0.0, 0.8, 0.0, 1),
            size_hint=(None, None),
            size=(180, 40),
            pos_hint={
                "center_x": 0.50,
                "center_y": 0.97
            }
        )

        self.layout.add_widget(self.level_lbl)        






        self.quiz_count_lbl = Label(
            text="1/20",
            font_size="20sp",
            bold=True,
            color=(1, 0.85, 0, 1),

            pos_hint={
        "center_x":0.5,
        "center_y":0.93
            }
        )

        self.layout.add_widget(
        self.quiz_count_lbl
      )

         












        self.result = Label(
            text="",
            font_size="24sp",
            bold=True,

            pos_hint={
                "center_x": 0.5,
                "center_y": 0.08
            }
        )

        self.layout.add_widget(self.result)
        self.layout.add_widget(self.score_lbl)

       

        











        self.buttons = []

        positions = [0.55, 0.55, 0.42, 0.42]

        x_positions = [0.24, 0.77, 0.24, 0.77]

        for i in range(4):

            btn = Button(

                text="",

                size_hint=(0.46, 0.10),

                pos_hint={
                    "center_x": x_positions[i],
                    "center_y": positions[i]
                },

                background_normal="",

                background_color=(0, 0, 0, 0),

                color=(1, 1, 1, 1),

                bold=True,

                font_size="20sp",

                halign="center",
                
                valign="middle",
                
                text_size=(150, None)
                )




 






            with btn.canvas.before:

              
                Color(0, 0, 0, 0.88)

                btn.shadow = RoundedRectangle(
                    pos=(btn.x - 5, btn.y - 5),
                    size=(btn.width + 10, btn.height + 10),
                    radius=[25]
                )

                btn.bg_color = Color(*self.colors[i])

                btn.bg = RoundedRectangle(
                    pos=btn.pos,
                    size=btn.size,
                    radius=[25]
                )



        






            def update_graphics(instance, value):

                instance.bg.pos = instance.pos
                instance.bg.size = instance.size

                instance.shadow.pos = (
                    instance.x - 5,
                    instance.y - 5
                )

                instance.shadow.size = (
                    instance.width + 10,
                    instance.height + 10
                )

            btn.bind(
                pos=update_graphics,
                size=update_graphics
            )


            def press_effect(instance):

                anim1 = Animation(
                    size_hint=(0.34, 0.09),
                    duration=0.05
                )

                anim2 = Animation(
                    size_hint=(0.46, 0.10),
                    duration=0.05
                )

                (anim1 + anim2).start(instance)

            btn.bind(on_press=press_effect)

         
            btn.bind(on_press=self.check_answer)

            self.layout.add_widget(btn)
            self.buttons.append(btn)


        




        self.show_think1 = Image(
            source="ahmed_think.png",
            size_hint=(0.8, 0.8),
            pos_hint={"center_x": 0.5, "center_y": 0.20},
            opacity=1
        )
        self.layout.add_widget(self.show_think1)

        self.show_correct1 = Image(
            source="ahmed_correct.png",
            size_hint=(0.5, 0.5),
            pos_hint={"center_x": 0.5, "center_y": 0.20},
            opacity=0
        )
        self.layout.add_widget(self.show_correct1)


        self.show_wrong1 = Image(
            source="ahmed_wrong.png",
            size_hint=(0.55, 0.55),
            pos_hint={"center_x": 0.5, "center_y": 0.20},
            opacity=0
                )
        self.layout.add_widget(self.show_wrong1)



    def on_enter(self, *args):
        self.show_notes_popup() 


    def update_bg(self, *args):

        self.bg.size = self.size
        self.bg.pos = self.pos

        self.overlay.size = self.size
        self.overlay.pos = self.pos


    

          
    # def show_notes_popup(self):

    #     layout = FloatLayout()

    #     content = Label(
    #         text=" Read these conditions carefully before starting the game.\n\n1. Each level has its own wrong limit. Complete the levels before reaching the wrong limit.\n\n2. After completing level 10 of the game, you will be given a name rank list.",
    #         font_size="18sp",
    #         color=(1,1,1,1),
    #         halign="center",
    #         valign="middle",
    #         size_hint=(1,0.9),
    #         pos_hint={"x":0,"top":1}
    #     )

    #     layout.add_widget(content)


    #     close_btn = Button(
    #         text="Close",
    #         size_hint=(0.3,0.12),
    #         pos_hint={"center_x":0.5,"y":0.05},
    #         background_color=(0.8,0.1,0.1,1)
    #     )


    #     popup = Popup(
    #         title="Notes",
    #         content=layout,
    #         size_hint=(0.8,0.5),
    #         auto_dismiss=False,
    #         background_color=(0.1,0.02,0.2,1)
    #     )


    #     close_btn.bind(
    #         on_press=popup.dismiss
    #     )

    #     layout.add_widget(close_btn)


    #     content.bind(
    #         size=lambda instance, value: setattr(
    #             instance,
    #             "text_size",
    #             value
    #         )
    #     )


    #     popup.open()    








    def show_notes_popup(self):

        layout = FloatLayout()

        scroll = ScrollView(
            size_hint=(1,0.78),
            pos_hint={"x":0, "top":1},
            do_scroll_x=False,
            do_scroll_y=True
        )

        content = Label(
            text="""Read these conditions carefully before starting the game.

    1. Each level has its own wrong limit. Complete the levels before reaching the wrong limit.

    2. After completing level 10 of the game, you will be given a name rank list.

    3. Play carefully and try to complete all levels.

    4. Wrong answers will reduce your chances of completing the level.""",

            font_size="18sp",
            color=(1,1,1,1),
            halign="left",
            valign="top",
            size_hint_y=None
        )



        content.bind(
            width=lambda instance, value:
            setattr(instance, "text_size", (value, None))
        )


# ye height ko text ke hisab se barhaye gi
        content.bind(
            texture_size=lambda instance, value:
            setattr(instance, "height", value[1])
        )








        scroll.add_widget(content)

        layout.add_widget(scroll)


        close_btn = Button(
            text="Close",
            size_hint=(0.3,0.12),
            pos_hint={"center_x":0.5,"y":0.03},
            background_color=(0.8,0.1,0.1,1)
        )


        popup = Popup(
            title="Game Rules",
            content=layout,
            size_hint=(0.85,0.75),
            auto_dismiss=False,
            background_color=(0.1,0.02,0.2,1)
        )


        close_btn.bind(
            on_press=popup.dismiss
        )


        layout.add_widget(close_btn)

        popup.open()    





    # def load_quiz_data(self):
        

    #     file_path = os.path.join(
    #         os.path.dirname(__file__),
    #         "quiz_data1.json"
    #     )

    #     with open(file_path, "r", encoding="utf-8") as file:
    #         data = json.load(file)

    #     return data["questions"]






    def load_quiz_data(self):

        try:
            # Firebase se questions download karein
            data = db.child("questions").get().val()

            if not data:
                raise Exception("Firebase mein questions nahi mile")

            # Firebase ke numbered questions ko list mein convert karein
            if isinstance(data, dict):
                questions = [
                    data[key] for key in sorted(data, key=lambda x: int(x))
                ]
            else:
                questions = data

            print("Firebase Questions Loaded:", len(questions))

            return questions

        except Exception as e:
            print("Firebase Error:", e)

            # Internet/Firebase fail ho to local JSON use karein
            file_path = os.path.join(
                os.path.dirname(__file__),
                "quiz_data1.json"
            )

            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            return data["questions"]













    def load_question(self):


        self.show_wrong1.opacity = 0

        # if self.index >= len(self.questions):
        if self.index >= len(self.questions):

            self.total_score += self.score

            for b in self.buttons:
                b.disabled = True

            Clock.schedule_once(lambda dt: self.show_level_complete(), 0.3)
            return        



        q = self.questions[self.index]
        self.correct = q["answer"]


        self.quiz_count_lbl.text = (
           f"Q: {self.index + 1}/{len(self.questions)}"
)
        self.show_think()


        options = q["options"][:]
        random.shuffle(options)


        self.q_lbl.text = q["question"]
        # self.score_lbl.text = f"Score : {self.score}"
        self.score_lbl.text = f"Score : {self.total_score}"
        self.result.text = ""


        for i, btn in enumerate(self.buttons):

            btn.text = options[i]
            btn.disabled = False

            r, g, b, a = self.colors[i]

            btn.bg_color.r = r
            btn.bg_color.g = g
            btn.bg_color.b = b
            btn.bg_color.a = a





    def check_answer(self, instance):

         # 🔘 CLICK SOUND
        if hasattr(self, "click_sound") and self.click_sound:
           self.click_sound.stop()
           self.click_sound.play()

        for b in self.buttons:
            b.disabled = True

        if instance.text == self.correct:

            
            self.score += 1
            self.total_score += 1
            self.result.text = "Correct!"
            self.result.color = (0, 1, 0, 1)

            self.show_correct()

            if hasattr(self, "correct_sound") and self.correct_sound:
                self.correct_sound.stop()
                self.correct_sound.play()


        else:

            self.result.text = "Wrong!"
            self.result.color = (1, 0, 0, 1)
            
            
            
            self.show_wrong()
            self.wrong_count += 1
            self.wrong_lbl.text = (
                f"Wrong : {self.wrong_count}/{self.max_wrong}"
            )

            if self.wrong_count > self.max_wrong:
               self.show_level_failed()
               return           

            if hasattr(self, "wrong_sound") and self.wrong_sound:
                self.wrong_sound.stop()
                self.wrong_sound.play()


         

 
        Clock.schedule_once(self.next_q, 1.5)





    def next_q(self, dt):

        self.index += 1
        self.load_question()



 



    def show_think(self):

        print("think SHOW")

        self.show_think1.opacity = 1
        self.show_correct1.opacity = 0
        self.show_wrong1.opacity = 0


    def show_correct(self):

        print("CORRECT SHOW")

        self.show_think1.opacity = 0
        self.show_correct1.opacity = 1
        self.show_wrong1.opacity = 0


    def show_wrong(self):

        print("wrong SHOW")

        self.show_think1.opacity = 0
        self.show_correct1.opacity = 0
        self.show_wrong1.opacity = 1






    

    def show_level_complete(self):

       total = len(self.questions)

       wrong = total - self.score

       percentage = 0

       if total > 0:
           percentage = (self.score / total) * 100

    # ====================================
    # FLOAT LAYOUT
    # ====================================

       layout = FloatLayout()

    # TITLE

       title = Label(
        text="[b] Level Complete  [/b]",
        markup=True,
        font_size="28sp",
        color=(1, 0.85, 0, 1),
        pos_hint={
            "center_x": 0.5,
            "center_y": 0.82
        }
    )

    # RESULT

       result_lbl = Label(
        text=
        # f" Correct : {self.score}\n\n"
        # f" Wrong : {wrong}\n\n"
        # f" Score : {self.score}/{total}\n\n"
        # f" Percentage : {percentage:.1f}%",

        f"[color=00ff00][b]Correct : {self.score}[/b][/color]\n"
        f"[color=ff0000][b]Wrong : {wrong}[/b][/color]\n"
        f"[color=00aaff][b]Score : {self.score}/{total}[/b][/color]\n"
        f"[color=ff9900][b]Percentage : {percentage:.1f}%[/b][/color]",

        font_size="20sp",
        color=(1, 1, 1, 1),
        halign="center",
        pos_hint={
            "center_x": 0.5,
            "center_y": 0.52
        }
    )

    # PLAY AGAIN

       play_again = Button(
        text="Play Again",
        size_hint=(0.35, 0.12),
        pos_hint={
            "center_x": 0.3,
            "center_y": 0.15
        },
        background_normal="",
        background_color=(0.1, 0.7, 0.3, 1)
    )

    # HOME

       home_btn = Button(
        text="Home",
        size_hint=(0.25, 0.12),
        pos_hint={
            "center_x": 0.3,
            "center_y": 0.92
        },
        background_normal="",
        background_color=(1, 0, 0, 1)
    )



       next_level2 = Button(
        text="Next",
        size_hint=(0.35, 0.12),
        pos_hint={
            "center_x": 0.7,
            "center_y": 0.15
        },
        background_normal="",
        background_color=(0.2, 0.5, 1, 1)
    )

       layout.add_widget(title)
       layout.add_widget(result_lbl)
       layout.add_widget(play_again)
       layout.add_widget(home_btn)
       layout.add_widget(next_level2)

    # POPUP

       self.level_popup = Popup(
        title="",
        content=layout,
        size_hint=(0.9, 0.6),
        separator_height=0,
        auto_dismiss=False
    )

    # EVENTS

       play_again.bind(
        on_press=self.restart_game
    )

       play_again.bind(
        on_press=self.level_popup.dismiss
    )

       home_btn.bind(
        on_press=self.go_home
    )

       home_btn.bind(
        on_press=self.level_popup.dismiss
    )
       next_level2.bind(on_press=self.next_level)
       next_level2.bind(on_press=self.level_popup.dismiss)

       self.level_popup.open()


    


    
    

    def show_level_failed(self):

       total = len(self.questions)

       wrong = total - self.score

       percentage = 0

       if total > 0:
           percentage = (self.score / total) * 100

    # ====================================
    # FLOAT LAYOUT
    # ====================================

       layout = FloatLayout()

    # TITLE
       
       title1 = Label(
        text="[b] Oops! [/b]",
        markup=True,
        font_size="32sp",
        color=(1, 0, 0, 1),
        pos_hint={
            "center_x": 0.5,
            "center_y": 0.97
        }
    )

       title = Label(
        text="[b] Level Failed [/b]",
        markup=True,
        font_size="26sp",
        color=(1, 0, 0, 1),
        pos_hint={
            "center_x": 0.5,
            "center_y": 0.86
        }
    )

    # RESULT

       result_lbl = Label(
        markup=True,
        text=
        # f"Wrong Limit : {self.max_wrong}\n\n"
        # f" Correct : {self.score}\n\n"
        # f" Wrong : {wrong}\n\n"
        # f" Score : {self.score}/{total}\n\n"
        # f" Percentage : {percentage:.1f}%",
       
        f"[color=ffff00][b]Wrong Limit : {self.max_wrong}[/b][/color]\n"
        f"[color=00ff00][b]Correct : {self.score}[/b][/color]\n"
        # f"[color=ff0000][b]Wrong : {wrong}[/b][/color]\n"
        f"[color=00aaff][b]Score : {self.score}/{total}[/b][/color]\n"
        f"[color=ff9900][b]Percentage : {percentage:.1f}%[/b][/color]",
 
        font_size="18sp",
        color=(1, 1, 1, 1),
        halign="center",
        pos_hint={
            "center_x": 0.5,
            "center_y": 0.52
        }
    )

    # PLAY AGAIN

       play_again = Button(
        text="Play Again",
        size_hint=(0.35, 0.12),
        color=(0, 0, 0, 1),
        pos_hint={
            "center_x": 0.3,
            "center_y": 0.15
        },
        background_normal="",
        background_color=(0.1, 0.7, 0.3, 1)
    )

    # HOME

       home_btn = Button(
        text="Home",
        size_hint=(0.35, 0.12),
        color=(0, 0, 0, 1),
        pos_hint={
            "center_x": 0.7,
            "center_y": 0.15
        },
        background_normal="",
        background_color=(0.0, 0.8, 0.0, 1)
    )




       layout.add_widget(title1)
       layout.add_widget(title)
       layout.add_widget(result_lbl)
       layout.add_widget(play_again)
       layout.add_widget(home_btn)


    # POPUP

       self.level_popup = Popup(
        title="",
        content=layout,
        size_hint=(0.9, 0.6),
        separator_height=0,
        auto_dismiss=False
    )

    # EVENTS

       play_again.bind(
        on_press=self.restart_game
    )

       play_again.bind(
        on_press=self.level_popup.dismiss
    )

       home_btn.bind(
        on_press=self.go_home
    )

       home_btn.bind(
        on_press=self.level_popup.dismiss
    )


       self.level_popup.open()














    def next_level(self, instance):

        self.level += 1
        self.level_lbl.text = f"Level : {self.level}"

        self.max_questions += 10
        self.max_wrong += 1

        self.wrong_lbl.text = f"Wrong : 0/{self.max_wrong}"

        self.index = 0
        self.score = 0
        self.index = 0
        self.wrong_count = 0

        self.questions = random.sample(
            quiz_data1,
            min(self.max_questions, len(quiz_data1))
        )

        self.level_popup.dismiss()

        self.load_question()    






    def go_home(self, instance):
        self.manager.current = "home"



    def start_game(self):

      self.index = 0
      self.score = 0
      self.total_score = 0
      self.wrong_count = 0

      self.level = 1
      self.level_lbl.text = f"Level : {self.level}"

      self.max_questions = 10
      self.max_wrong = 1
      
      self.wrong_lbl.text = f"Wrong : 0/{self.max_wrong}"
      
      self.wrong_questions = []      

    #   total_questions = min(20, len(quiz_data1))

    #   self.questions = random.sample(
    #     quiz_data1,
    #     total_questions
    # )

      
    #   self.questions = random.sample(
    #       quiz_data1,
    #       min(self.max_questions, len(quiz_data1))
    #   )
     
      quiz_data = self.load_quiz_data()

      self.questions = random.sample(
        quiz_data,
        min(self.max_questions, len(quiz_data))
    )    
  
      self.load_question()





    def restart_game(self, instance):

        self.level_popup.dismiss()

    # Reset scores
        self.score = 0
        self.total_score = 0

        self.wrong_count = 0
        self.wrong_lbl.text = f"Wrong : 0/{self.max_wrong}"

        self.index = 0
        self.result.text = ""

        self.score_lbl.text = f"Score : {self.total_score}"

        quiz_data = self.load_quiz_data()

        self.questions = random.sample(
            quiz_data,
            min(self.max_questions, len(quiz_data))
        )

        for b in self.buttons:
            b.disabled = False

        self.load_question()    









    # def restart_game(self, instance):

    #     self.index = 0
    #     self.score = 0

    #     self.result.text = ""
    #     self.score_lbl.text = " Score : 0"

    #     for b in self.buttons:
    #         b.disabled = False

    #     self.load_question()




    def toggle_popup(self, instance):

        print("BUTTON CLICKED")

      #  if self.popup is None:
       
      
        self.menu_popup = None
        self.game_popup = None
        layout = BoxLayout(
            orientation="vertical",
            spacing=10,
            padding=10
        )

        title = Label(
            text="MENU"
        )

        close_btn = Button(
            text="Close"
        )

        home_btn = Button(
            text="Home"
        )

        layout.add_widget(title)
        layout.add_widget(close_btn)
        layout.add_widget(home_btn)

        self.menu_popup = Popup(
            title="",
            content=layout,
            size_hint=(0.7, 0.4),
            auto_dismiss=True
        )

        close_btn.bind(
            on_press=self.menu_popup.dismiss
        )

        home_btn.bind(
            on_press=self.home_go
        )

        home_btn.bind(
            on_press=self.menu_popup.dismiss
        )

        self.menu_popup.open()




    
    def home_go(self, instance):
        self.manager.current = "home"



    



















class page01(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)




         
        with self.canvas.before:

            self.bg = Rectangle(
                source="ahmed_background.jpeg",
                size=self.size,
                pos=self.pos
            )

            Color(0, 0, 0, 0.20)

            self.overlay = Rectangle(
                size=self.size,
                pos=self.pos
            )

        self.bind(size=self.update_bg, pos=self.update_bg)








        layout = FloatLayout()

        btn01 = GlassButton(
            text="Quiz",
            size_hint=(0.5, 0.08),
            pos_hint={"center_x": 0.5, "center_y": 0.6}
        )

        btn01_back = GlassButton(
            text="Back",
            size_hint=(0.5, 0.08),
            pos_hint={"center_x": 0.5, "center_y": 0.48}
        )



        btn01.bind(on_press=self.open_quiz)
        btn01_back.bind(on_press=self.go_home)

        layout.add_widget(btn01_back)
        layout.add_widget(btn01)
        self.add_widget(layout)

    # ✅ MUST BE OUTSIDE __init__
    def open_quiz(self, instance):
        self.manager.current = "quiz"

    def go_home(self,instance):
        self.manager.current = "home"



    def update_bg(self, *args):

        self.bg.size = self.size
        self.bg.pos = self.pos

        self.overlay.size = self.size
        self.overlay.pos = self.pos



class Setup(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)



        
        with self.canvas.before:

            self.bg = Rectangle(
                source="ahmed_background.jpeg",
                size=self.size,
                pos=self.pos
            )

            Color(0, 0, 0, 0.20)

            self.overlay = Rectangle(
                size=self.size,
                pos=self.pos
            )

        self.bind(size=self.update_bg, pos=self.update_bg)







        # self.count = GlassInput(hint_text="how many question?",
        #                        size_hint=(0.6, 0.08),
        #                        pos_hint={"center_x": 0.5, "center_y": 0.69})

   




        self.count = GlassInput(
    hint_text="how many question?",
    size_hint=(0.6, 0.08),
    pos_hint={"center_x": 0.5, "center_y": 0.69},
    input_filter="int"
)

        self.count.bind(text=self.only_numbers)






        self.duration_spinner = Spinner(
        text="Select time duration",
        values=("8", "10", "12", "14", "16", "18", "20"),
        size_hint=(0.4, 0.08),
        pos_hint={
        "center_x": 0.5,
        "center_y": 0.5
        }
        )


        

        self.add_widget(self.duration_spinner)





        btn = GlassButton(text="NEXT",
                     size_hint=(0.4, 0.06),
                     pos_hint={"center_x": 0.5, "center_y": 0.4})

        btn_back = GlassButton(text="Back",
                     size_hint=(0.4,0.06),
                     pos_hint={"center_x":0.5, "center_y":0.3})

        btn_back.bind(on_press=self.go_home)
        btn.bind(on_press=self.start)
        


        self.add_widget(self.count)
        # self.add_widget(self.duration_spinner)
        self.add_widget(btn)
        self.add_widget(btn_back)

    def go_home(self,instance):
        self.manager.current = "home"


    def update_bg(self, *args):

        self.bg.size = self.size
        self.bg.pos = self.pos

        self.overlay.size = self.size
        self.overlay.pos = self.pos



    def only_numbers(self, instance, value):
        clean = "".join(c for c in value if c.isdigit())

        if value != clean:
            instance.text = clean
            instance.cursor = (len(clean), 0)




    def start(self, instance):

    # =========================
    # COUNT SAFE CHECK
    # =========================

       count_text = self.count.text.strip()

       if count_text == "" or not count_text.isdigit():

        self.count.text = ""
        self.count.hint_text = "⚠ Enter valid number"
        return

       self.total = int(count_text)

    # =========================
    # SPINNER SAFE CHECK
    # =========================

       duration_text = self.duration_spinner.text.strip()
 
       if duration_text == "Select Number":

        self.duration_spinner.text = "⚠ Select time"
        return

    # GLOBAL VIDEO DURATION
       global APP_DURATION

       APP_DURATION = int(duration_text)

    # =========================
    # RESET GAME
    # =========================

       self.index = 0

    # GO NEXT SCREEN
       self.manager.current = "question"








# ================= QUESTION =================
class Question(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)


        self.quiz_data = []
        self.selected_bg = "dark"
        self.selected_frame_style = "clean"
        self.selected_frame_size = "tiktok"


        self.loading_done = False


        
        with self.canvas.before:

            self.bg = Rectangle(
                source="ahmed_background.jpeg",
                size=self.size,
                pos=self.pos
            )

            Color(0, 0, 0, 0.20)

            self.overlay = Rectangle(
                size=self.size,
                pos=self.pos
            )

        self.bind(size=self.update_bg, pos=self.update_bg)





        self.q = GlassInput(hint_text="Question",
                           size_hint=(0.8, 0.08),
                           multiline=True,
                           use_bubble=True,
                           use_handles=True,
                           pos_hint={"center_x": 0.5, "center_y": 0.89})

        self.a = GlassInput(hint_text="A", size_hint=(0.8, 0.08),
                           multiline=True,
                           use_bubble=True,
                           use_handles=True,
                           pos_hint={"center_x": 0.5, "center_y": 0.79})

        self.b = GlassInput(hint_text="B", size_hint=(0.8, 0.08),
                           multiline=True,
                           use_bubble=True,
                           use_handles=True,
                           pos_hint={"center_x": 0.5, "center_y": 0.69})

        self.c = GlassInput(hint_text="C", size_hint=(0.8, 0.08),
                           multiline=True,
                           use_bubble=True,
                           use_handles=True,
                           pos_hint={"center_x": 0.5, "center_y": 0.59})

        self.d = GlassInput(hint_text="D", size_hint=(0.8, 0.08),
                           multiline=True,
                           use_bubble=True,
                           use_handles=True,
                           pos_hint={"center_x": 0.5, "center_y": 0.49})

        # self.correct = GlassInput(hint_text="A/B/C/D",
        #                          size_hint=(0.8, 0.08),
        #                          pos_hint={"center_x": 0.5, "center_y": 0.35})

        self.quiz_data = [
           {"q": "test", "options": ["A","B","C","D"], "correct": "A"}
        ]
        self.correct = Spinner(
           text="Select Correct Option",
           values=("A", "B", "C", "D"),
           size_hint=(0.5, 0.06),
            pos_hint={"center_x": 0.5, "center_y": 0.39}
        )






        btn = GlassButton(text="NEXT",
                     size_hint=(0.4, 0.06),
                     pos_hint={"center_x": 0.5, "center_y": 0.29})
        back_btn1= GlassButton(text="Back",
                    size_hint=(0.4, 0.06),
                    pos_hint={"center_x": 0.5, "center_y": 0.21})
        
        back_btn1.bind(on_press=self.go_home)
        btn.bind(on_press=self.save)

        style_glass_spinner(self.correct)
        self.add_widget(self.correct)
        self.add_widget(self.q)
        self.add_widget(self.a)
        self.add_widget(self.b)
        self.add_widget(self.c)
        self.add_widget(self.d)
        # self.add_widget(self.correct)
        self.add_widget(btn)
        self.add_widget(back_btn1)


    def go_home(self,instance):
        self.manager.current = "home"

   






    def save(self, instance):

        quiz_data.append({
           "q": self.q.text,
           "options": [self.a.text, self.b.text, self.c.text, self.d.text],
           "correct": self.correct.text
        })

        print("CURRENT GLOBAL QUIZ:", quiz_data)   # 🔥 DEBUG

        self.q.text = self.a.text = self.b.text = self.c.text = self.d.text = ""
        self.correct.text = ""

        # if len(self.quiz_data) >= self.manager.get_screen("setup").total:
        if len(quiz_data) >= self.manager.get_screen("setup").total:
            self.manager.current = "generate"

    


















    def update_bg(self, *args):

        self.bg.size = self.size
        self.bg.pos = self.pos

        self.overlay.size = self.size
        self.overlay.pos = self.pos













class Generate(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)


        self.is_generating = False
        self.job_id = None
        self.video_url = None        


        self.quiz_data = []


        self.selected_bg = "dark"
        self.selected_frame_style = "clean"
        self.selected_frame_size = "tiktok"



        self.loading_done = False




         
        with self.canvas.before:

            self.bg = Rectangle(
                source="ahmed_background.jpeg",
                size=self.size,
                pos=self.pos
            )

            Color(0, 0, 0, 0.20)

            self.overlay = Rectangle(
                size=self.size,
                pos=self.pos
            )

        self.bind(size=self.update_bg, pos=self.update_bg)










        layout = FloatLayout()

        # 📊 progress bar
        self.bar = ModernProgressBar(
            max=100,
            size_hint=(0.7, 0.08),
            pos_hint={"center_x": 0.5, "center_y": 0.65}
        )
        Clock.schedule_interval(self.fake_loading, 0.03)


        # # 🧠 loading text (console nahi, screen pe)
        self.label = Label(
            text="Ready",
            font_size=20,
            pos_hint={"center_x": 0.5, "center_y": 0.75}
        )

        # 🎬 generate button
        self.gen_btn = GlassButton(
            text="GENERATE VIDEO",
            size_hint=(0.5, 0.1),
            pos_hint={"center_x": 0.5, "center_y": 0.46}
        )
        
        gen_backbtn = GlassButton(
            text="Back",
            size_hint=(0.5, 0.1),
            pos_hint={"center_x": 0.5, "center_y": 0.34}
        )
       


        # ⬇ download button (hidden until done)
        self.download_btn = GlassButton(
            text="DOWNLOAD",
            size_hint=(0.5, 0.1),
            pos_hint={"center_x": 0.5, "center_y": 0.22},
            opacity=0,
            disabled=True
        )





        

        open_btn = GlassButton(
        text="bg",
        size_hint=(0.3, 0.05),
        pos_hint={"center_x": 0.2, "center_y": 0.95}
    )

        open_btn.bind(
        on_press=lambda x: self.open_bg_window()
    )


        frame_btn = GlassButton(
        text="frame style",
        size_hint=(0.3, 0.05),
        pos_hint={"center_x": 0.5, "center_y": 0.95}
    )

        frame_btn.bind(on_press=lambda x: self.open_frame_style_window())


        size_btn = GlassButton(
        text="frame size",
        size_hint=(0.3, 0.05),
        pos_hint={"center_x": 0.8, "center_y": 0.95}
    )

        size_btn.bind(on_press=lambda x: self.open_size_window())


  











        # self.gen_btn.bind(on_press=lambda x: self.generate_video())
        self.gen_btn.bind(on_press=self.start)
        # self.gen_btn.bind(on_press=self.start)
        gen_backbtn.bind(on_press=self.go_home)
        self.download_btn.bind(on_press=self.download_video)
        
        layout.add_widget(self.bar)
        layout.add_widget(self.label)
        layout.add_widget(self.gen_btn)
        layout.add_widget(gen_backbtn)
        layout.add_widget(self.download_btn)
        layout.add_widget(size_btn)
        layout.add_widget(open_btn)
        layout.add_widget(frame_btn)

        self.add_widget(layout)

        self.video_path = "quiz.mp4"
    #     self.manager.current = "home"
    def go_home(self,instance):
        self.reset_generation()
        self.manager.current = "home"






    def reset_generation(self):

        global quiz_data


        quiz_data = []


        self.job_id = None
        self.video_url = None


        self.label.text = ""


        self.gen_btn.disabled = False
        self.gen_btn.opacity = 1


        self.download_btn.disabled = True
        self.download_btn.opacity = 0


        self.is_generating = False    







    def update_bg(self, *args):

        self.bg.size = self.size
        self.bg.pos = self.pos

        self.overlay.size = self.size
        self.overlay.pos = self.pos


    def fake_loading(self, dt):

    # 🔥 Fake loading 70 tak
      if self.bar.value < 70 and not self.loading_done:

        self.bar.value += 1

    # 🔥 Real loading complete
      elif self.loading_done:

        if self.bar.value < 100:

            self.bar.value += 5

        else:

            print("Loading Complete")

            return False





    # ================= START GENERATION =================
    # def start(self, instance):
    #     self.label.text = "Starting..."
    #     self.bar.value = 0
    #     self.gen_btn.disabled = True

    #     threading.Thread(target=self.generate, daemon=True).start()
            
    def start(self, instance):
       threading.Thread(target=self.generate_video, daemon=True).start()


    # ================= GENERATE =================


   


    # def generate_video(self):

  
    #   url = "https://mental-dealtime-thanksgiving-notifications.trycloudflare.com/generate"


    #   payload = {
    #     # "quiz": quiz_data,
    #     "quiz": self.quiz_data,
    #     "frame_style": self.selected_frame_style,
    #     "bg": self.selected_bg,
    #     "frame_size": self.selected_frame_size,
    #     "duration": APP_DURATION
    #  }
       

    # def generate_video(self):
      
    #   global quiz_data

    #   print("GLOBAL QUIZ DATA =", quiz_data)

    #   url = "https://wine-coordinated-connecticut-low.trycloudflare.com/generate"

    

    #   self.selected_bg = bg_mode

    #   payload = {
    #     "quiz": quiz_data,
    #     "frame_style": self.selected_frame_style,
    #     "bg": self.selected_bg,
    #     "frame_size": self.selected_frame_size,
    #     "duration": APP_DURATION
    #   }





    #   print("PAYLOAD =", payload)
    #   print("QUIZ DATA BEING SENT:")
    #   print(quiz_data)
    #   print("TOTAL:", len(quiz_data))
    #   print("LOCAL QUIZ DATA:", quiz_data)
    #   self.label.text = "Sending to server..."

    #   try:

    #     response = requests.post(url, json=payload, timeout=300)


    #     if response.status_code != 200:
    #         self.label.text = "Server Error ❌"
    #         print("Server Error:", response.text)
    #         return


    #     data = response.json()


    #     self.video_url = data.get("video_url", None)

    #     if not self.video_url:
    #         self.label.text = "No Video URL ❌"
    #         return

  
    #     self.label.text = "Video Ready ✔"
    #     print("VIDEO URL:", self.video_url)
    #     self.download_btn.opacity = 1

    #   except requests.exceptions.RequestException as e:
    #     self.label.text = "Network Error ❌"
    #     print("Network Error:", e)

    #   except Exception as e:
    #     self.label.text = "Error ❌"
    #     print("Error:", e)










    def generate_video(self):

        global quiz_data
        if self.is_generating:
            return


        self.is_generating = True


        # self.gen_btn.disabled = True
        # self.gen_btn.opacity = 0.5
        Clock.schedule_once(
             lambda dt: self.disable_generate_button()
        )


        print("GLOBAL QUIZ DATA =", quiz_data)

        # url = "https://alternatively-buyer-zshops-ant.trycloudflare.com/generate"
        url = f"{SERVER_URL}/generate"
      


        self.selected_bg = bg_mode


        payload = {
            "quiz": quiz_data,
            "frame_style": self.selected_frame_style,
            "bg": self.selected_bg,
            "frame_size": self.selected_frame_size,
            "duration": APP_DURATION
        }


        print("PAYLOAD =", payload)
        print("QUIZ DATA BEING SENT:")
        print(quiz_data)
        print("TOTAL:", len(quiz_data))


        self.label.text = "Generating..."


        try:

            response = requests.post(
                url,
                json=payload,
                timeout=30
            )


            if response.status_code != 200:

                self.label.text = "Server Error ❌"
                print(response.text)
                return



            data = response.json()


            print("SERVER RESPONSE =", data)


            self.job_id = data.get("job_id")


            if not self.job_id:

                self.label.text = "Job ID Missing ❌"
                return



            print("JOB ID =", self.job_id)


            self.label.text = "Generating Video..."


            # start checking status

            Clock.schedule_once(
                lambda dt: self.check_video_status(),
                2
            )



        except requests.exceptions.RequestException as e:

            self.label.text = "Network Error ❌"
            print("Network Error:", e)



        except Exception as e:

            self.label.text = "Error ❌"
            print("Error:", e)    







    def check_video_status(self):

      try:

        # url = f"https://alternatively-buyer-zshops-ant.trycloudflare.com/status/{self.job_id}"
        url = f"{SERVER_URL}/status/{self.job_id}"


        response = requests.get(url)

        data = response.json()


        print("STATUS RESPONSE =", data)



        if data.get("status") == "done":


            self.video_url = data.get("video_url")


            print("VIDEO URL =", self.video_url)


            self.label.text = "Video Ready ✔"


            self.download_btn.opacity = 1
            self.download_btn.disabled = False


            self.generate_btn.disabled = False
            self.generate_btn.opacity = 1


            self.is_generating = False        



        elif data.get("status") == "processing":


            self.label.text = "Generating..."


            Clock.schedule_once(
                lambda dt: self.check_video_status(),
                2
            )



        else:

            Clock.schedule_once(
                 lambda dt: self.video_error_reset()
        )      



      except Exception as e:

        print("STATUS ERROR:", e)






# ================= UI UPDATE =================









    def disable_generate_button(self):

        self.gen_btn.disabled = True
        self.gen_btn.opacity = 0.5




    def video_error_reset(self):

        self.label.text = "Error ❌"

        self.gen_btn.disabled = False
        self.gen_btn.opacity = 1

        self.is_generating = False    







    def update(self, i, total):

        self.label.text = f"Generating {i+1} / {total}"
        self.bar.value = ((i + 1) / total) * 100









# ================= FINISH UI =================

    def finish_ui(self):

       self.label.text = "Video Ready "
       self.bar.value = 100

    # Video ready -> download button show
       self.download_btn.opacity = 1
       self.download_btn.disabled = False

       self.gen_btn.disabled = False




   
    


    # def download_video(self, instance):

    #  try:
    #     if not hasattr(self, "video_url") or not self.video_url:
    #         self.label.text = "No video URL ❌"
    #         return

    #     self.label.text = "Downloading..."

    #     import io
    #     import requests

    #     response = requests.get(self.video_url, stream=True)
    #     response.raise_for_status()

    #     # 🔥 MEMORY BUFFER (no corruption)
    #     video_buffer = io.BytesIO()

    #     for chunk in response.iter_content(chunk_size=1024 * 512):
    #         if chunk:
    #             video_buffer.write(chunk)

    #     video_buffer.seek(0)

    #     # =========================
    #     # SAVE FILE (FINAL STEP)
    #     # =========================
    #     path = os.path.join(
    #         os.path.expanduser("~"),
    #         "QuizVideo.mp4"
    #     )

    #     with open(path, "wb") as f:
    #         f.write(video_buffer.read())

    #     self.label.text = "Downloaded ✔"
    #     print("Saved at:", path)

    #     self.download_btn.opacity = 0
    #     self.download_btn.disabled = True

    #  except Exception as e:
    #     self.label.text = f"Download Failed ❌ {e}"
    #     print("ERROR:", e)


    # def download_video(self, instance):

    #     if not self.video_url:
    #         return

    #     try:

    #         import requests

    #         r = requests.get(self.video_url)

    #         filename = "Quiz_Video.mp4"

    #         if platform == "android":

    #            path = "/storage/emulated/0/Download/" + filename

    #         else:

    #             path = filename


    #         with open(path, "wb") as f:
    #             f.write(r.content)


    #         self.label.text = "Saved ✔"

    #         print("SAVED:", path)


    #     except Exception as e:

    #         print("DOWNLOAD ERROR:", e)
    #         self.label.text = "Download Failed"    


    def download_video(self, instance):

        if not self.video_url:
            return


        try:

            import requests
            print("VIDEO URL =", self.video_url)


            self.label.text = "Downloading..."


            filename = "Quiz_Video.mp4"


            if platform == "android":

                path = "/storage/emulated/0/Download/" + filename

            else:

                path = filename



            with requests.get(
                self.video_url,
                stream=True
            ) as r:


                r.raise_for_status()


                with open(path, "wb") as f:


                    for chunk in r.iter_content(
                        chunk_size=1024*1024
                    ):


                        if chunk:
                            f.write(chunk)



            self.label.text = "Saved ✔"


            print("SAVED:", path)



        # Download ke baad button hide

            self.download_btn.opacity = 0
            self.download_btn.disabled = True



        except Exception as e:

            print("DOWNLOAD ERROR TYPE:", type(e))
            print("DOWNLOAD ERROR:", repr(e))

            self.label.text = "Download Failed"        


        # except Exception as e:


        #     print("DOWNLOAD ERROR:", e)

        #     self.label.text = "Download Failed"    

















    # def download_video(self, instance):

    #   if not self.video_url:
    #     self.label.text = "No video URL ❌"
    #     return

    #   self.label.text = "Downloading..."

    #   try:
    #     import requests
    #     import os

    #     r = requests.get(self.video_url, stream=True, timeout=120)
    #     r.raise_for_status()

    #     path = os.path.join(os.path.expanduser("~"), "QuizVideo.mp4")

    #     with open(path, "wb") as f:
    #         for chunk in r.iter_content(1024 * 512):
    #             if chunk:
    #                 f.write(chunk)

    #     self.label.text = "Downloaded ✔"
    #     print("Saved:", path)

    #   except Exception as e:
    #     self.label.text = f"Download Failed ❌ {e}"









    

    def open_bg_window(self):

    




     layout = BoxLayout(
    orientation="vertical",
    padding=20,
    spacing=10
    )



        
     btn_simple = TickButton(text="Simple")
     btn_galaxy = TickButton(text="Galaxy")
     btn_matrix = TickButton(text="Matrix")
     btn_fire = TickButton(text="Fire")
     btn_neon = TickButton(text="Neon")
     btn_cyber = TickButton(text="Cyber")
   
     
     btn_simple.bind(on_press=lambda x: set_simple())
     btn_galaxy.bind(on_press=lambda x: set_galaxy())
     btn_matrix.bind(on_press=lambda x: set_matrix())
     btn_fire.bind(on_press=lambda x: set_fire())
     btn_neon.bind(on_press=lambda x: set_neon())
     btn_cyber.bind(on_press=lambda x: set_cyberpunk())



    
     layout.add_widget(btn_simple)
     layout.add_widget(btn_galaxy)
     layout.add_widget(btn_matrix)
     layout.add_widget(btn_fire)
     layout.add_widget(btn_neon)
     layout.add_widget(btn_cyber)
   



     self.popup = Popup(
        title="Select Background",
        content=layout,
        size_hint=(0.5, 0.5),   # 👈 choti window
        auto_dismiss=True
    )

     self.popup.open()
     


    def set_bg(self, bg_name, *args):

        self.selected_bg = bg_name

        print("Selected Background:", self.selected_bg)

        if hasattr(self, "popup"):
            self.popup.dismiss()

    # def set_frame_size(self, size_name, *args):
    #      global frame_size
    #      frame_size = size_name
    #      print("Selected Frame:", frame_size)




    def open_size_window(self):


       layout = BoxLayout(orientation="vertical", spacing=10, padding=10)

       btn0 = TickButton(text="video 1:2")
       btn1 = TickButton(text="YouTube 16:9")
       btn2 = TickButton(text="TikTok 9:16")
       btn3 = TickButton(text="Square 1:1")
       btn4 = TickButton(text="Wide 1280x720")

       btn0.bind(on_press=lambda _: self.set_frame_size("video"))
       btn1.bind(on_press=lambda _: self.set_frame_size("youtube_shorts"))
       btn2.bind(on_press=lambda _: self.set_frame_size("tiktok"))
       btn3.bind(on_press=lambda _: self.set_frame_size("square"))
       btn4.bind(on_press=lambda _: self.set_frame_size("wide"))

       layout.add_widget(btn0)
       layout.add_widget(btn1)
       layout.add_widget(btn2)
       layout.add_widget(btn3)
       layout.add_widget(btn4)

       self.popup = Popup(
        title="Select Frame Size",
        content=layout,
        size_hint=(0.6, 0.6)
       )

       self.popup.open()




    def set_frame_size(self, size_name, *args):

        self.selected_frame_size = size_name

        print("Selected Frame:", self.selected_frame_size)

        if hasattr(self, "popup"):
            self.popup.dismiss()



    def open_frame_style_window(self):

        layout = BoxLayout(
            orientation="vertical",
            spacing=10,
            padding=10
        )

    # ======================
    # BUTTONS
    # ======================
        btn0_c = TickButton(text="Clean")
        btn1_t = TickButton(text="TikTok Neon")
        btn2_y = TickButton(text="YouTube Red")
        btn3_g = TickButton(text="Gold Premium")
        btn4_n = TickButton(text="Neon Gaming")
        btn5_r = TickButton(text="Royal Purple")
        btn6_d = TickButton(text="Default White")

    # ======================
    # BINDINGS (IMPORTANT FIXED)
    # ======================

        btn0_c.bind(on_press=lambda _: self.set_frame_style("clean"))
        btn1_t.bind(on_press=lambda _: self.set_frame_style("tiktok"))
        btn2_y.bind(on_press=lambda _: self.set_frame_style("youtube"))
        btn3_g.bind(on_press=lambda _: self.set_frame_style("gold"))
        btn4_n.bind(on_press=lambda _: self.set_frame_style("neon"))
        btn5_r.bind(on_press=lambda _: self.set_frame_style("royal"))
        btn6_d.bind(on_press=lambda _: self.set_frame_style("default"))

    # ======================
    # ADD TO LAYOUT
    # ======================
        layout.add_widget(btn0_c)
        layout.add_widget(btn1_t)
        layout.add_widget(btn2_y)
        layout.add_widget(btn3_g)
        layout.add_widget(btn4_n)
        layout.add_widget(btn5_r)
        layout.add_widget(btn6_d)

    # ======================
    # POPUP
    # ======================
        self.popup = Popup(
            title="Select Frame Style",
            content=layout,
            size_hint=(0.6, 0.7)
        )

        self.popup.open()



    def set_frame_style(self, style):

        self.selected_frame_style = style

        print("Selected Frame Style:", style)

        self.popup.dismiss()























    
       


from kivy.uix.image import Image


# =========================
# QUIZ SCREEN
# =========================

# =========================
# QUIZ SCREEN
# =========================
class Quiz(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.popup = None

        
        import os

        BASE = "/mnt/d/ahtiyat.py"

        # self.correct_sound = SoundLoader.load(os.path.join(BASE, "dragon.mp3"))
        # self.wrong_sound = SoundLoader.load(os.path.join(BASE, "wrong.mp3"))
        # self.click_sound = SoundLoader.load(os.path.join(BASE, "click.mp3"))



        print("BEFORE DRAGON LOAD", flush=True)
        # correct_sound = SoundLoader.load(os.path.join(BASE, "dragon.mp3"))
        correct_sound = None
        print("AFTER DRAGON LOAD:", correct_sound, flush=True)

        print("BEFORE WRONG LOAD", flush=True)
        # wrong_sound = SoundLoader.load(os.path.join(BASE, "wrong.mp3"))
        wrong_sound = None
        print("AFTER WRONG LOAD:", wrong_sound, flush=True)

        print("BEFORE CLICK LOAD", flush=True)
        # click_sound = SoundLoader.load(os.path.join(BASE, "click.mp3"))
        click_sound = None
        print("AFTER CLICK LOAD:", click_sound, flush=True)





    

        self.index = 0
        self.score = 0
        self.wrong_count = 0
        # self.questions = []
        self.correct = ""
        self.questions = self.load_quiz_data()
        # =========================================
        # BUTTON COLORS
        # =========================================

        self.colors = [
            (0.10, 0.60, 1, 0.95),   # BLUE
            (0.90, 0.30, 0.30, 0.95), # RED
            (0.30, 0.80, 0.40, 0.95), # GREEN
            (0.80, 0.50, 1, 0.95)     # PURPLE
        ]

        # =========================================
        # BACKGROUND
        # =========================================

        with self.canvas.before:

            self.bg = Rectangle(
                source="ahmed_background.jpeg",
                size=self.size,
                pos=self.pos
            )

            Color(0, 0, 0, 0.20)

            self.overlay = Rectangle(
                size=self.size,
                pos=self.pos
            )

        self.bind(size=self.update_bg, pos=self.update_bg)

        # =========================================
        # MAIN LAYOUT
        # =========================================

        self.layout = FloatLayout()

        self.add_widget(self.layout)

        # =========================================
        # QUESTION BOX
        # =========================================

        with self.layout.canvas.before:

            # SHADOW
            Color(0, 0, 0, 0.35)

            self.q_shadow = RoundedRectangle(
                pos=(45, 455),
                size=(710, 140),
                radius=[35]
            )

            # MAIN BOX
            Color(0.05, 0.08, 0.18, 0.92)

            self.q_box = RoundedRectangle(
                pos=(20, 680),
                size=(520, 200),
                radius=[35]
            )
            Color(0.05, 0.08, 0.18, 0.92)

            self.score_box = RoundedRectangle(
                pos=(15, 900),
                size=(50, 50),
                radius=[35]
            )

        # =========================================
        # QUESTION LABEL
        # =========================================

        self.q_lbl = Label(
            text="",
            font_size="20sp",
            # bold=True,
            color=(1, 1, 1, 1),

            text_size=(450, None),  # width fix
            halign="center",
            valign="middle",

            pos_hint={
                "center_x": 0.5,
                "center_y": 0.80
            }
        )

        self.layout.add_widget(self.q_lbl)

        # =========================================
        # SCORE LABEL
        # =========================================







        self.menu_btn = AppButton3D(
    text="Result",
    size_hint=(0.24, 0.05),
    pos_hint={
              "center_x": 0.87,
              "center_y": 0.95
            }
)

        self.menu_btn.bind(on_press=self.toggle_popup)
        self.layout.add_widget(self.menu_btn)




        self.score_lbl = Label(
            text="Score : 0",
            font_size="22sp",
            bold=True,
            color=(1, 1, 1, 1),

            pos_hint={
                "center_x": 0.15,
                "center_y": 0.95
            }
        )




        self.wrong_limit_label = Label(
            text="Wrong: 0/5",
            font_size="20sp",
            bold=True,
            color=(1,0,0,1),
            
            pos_hint={
                "center_x": 0.50,
                "center_y": 0.95
            }
        )
         













        # =========================================
        # RESULT LABEL
        # =========================================

        self.result = Label(
            text="",
            font_size="24sp",
            bold=True,

            pos_hint={
                "center_x": 0.5,
                "center_y": 0.08
            }
        )

        self.layout.add_widget(self.result)
        self.layout.add_widget(self.score_lbl)
        self.layout.add_widget(self.wrong_limit_label)

       

        











        self.buttons = []

        positions = [0.60, 0.60, 0.47, 0.47]

        x_positions = [0.24, 0.77, 0.24, 0.77]

        for i in range(4):

            btn = Button(

                text="",

                size_hint=(0.48, 0.10),

                pos_hint={
                    "center_x": x_positions[i],
                    "center_y": positions[i]
                },

                background_normal="",

                background_color=(0, 0, 0, 0),

                color=(1, 1, 1, 1),

                bold=True,

                font_size="15sp",
                
                halign="center",
                
                valign="middle",
                
                text_size=(150, None)


            )




 







            # =====================================
            # BUTTON DESIGN
            # =====================================

            with btn.canvas.before:

                # SHADOW
                Color(0, 0, 0, 0.88)

                btn.shadow = RoundedRectangle(
                    pos=(btn.x - 5, btn.y - 5),
                    size=(btn.width + 10, btn.height + 10),
                    radius=[25]
                )

                # BUTTON COLOR
                btn.bg_color = Color(*self.colors[i])

                # BUTTON SHAPE
                btn.bg = RoundedRectangle(
                    pos=btn.pos,
                    size=btn.size,
                    radius=[25]
                )



        








            # =====================================
            # UPDATE BUTTON GRAPHICS
            # =====================================

            def update_graphics(instance, value):

                instance.bg.pos = instance.pos
                instance.bg.size = instance.size

                instance.shadow.pos = (
                    instance.x - 5,
                    instance.y - 5
                )

                instance.shadow.size = (
                    instance.width + 10,
                    instance.height + 10
                )

            btn.bind(
                pos=update_graphics,
                size=update_graphics
            )

            # =====================================
            # BUTTON ANIMATION
            # =====================================

            def press_effect(instance):

                anim1 = Animation(
                    size_hint=(0.34, 0.09),
                    duration=0.05
                )

                anim2 = Animation(
                    size_hint=(0.47, 0.10),
                    duration=0.05
                )

                (anim1 + anim2).start(instance)

            btn.bind(on_press=press_effect)

            # ANSWER CHECK
            btn.bind(on_press=self.check_answer)

            self.layout.add_widget(btn)
            self.buttons.append(btn)


        from kivy.uix.image import Image


         # THINK IMAGE
        self.show_think1 = Image(
            source="ahmed_think.png",
            size_hint=(0.6, 0.6),
            pos_hint={"center_x": 0.5, "center_y": 0.22},
            opacity=1
        )
        self.layout.add_widget(self.show_think1)


# CORRECT IMAGE
        self.show_correct1 = Image(
            source="ahmed_correct.png",
            size_hint=(0.55, 0.55),
            pos_hint={"center_x": 0.5, "center_y": 0.22},
            opacity=0
        )
        self.layout.add_widget(self.show_correct1)


# WRONG IMAGE
        self.show_wrong1 = Image(
            source="ahmed_wrong.png",
            size_hint=(0.55, 0.55),
            pos_hint={"center_x": 0.5, "center_y": 0.22},
            opacity=0
                )
        self.layout.add_widget(self.show_wrong1)


    def on_enter(self, *args):
        self.show_notes_popup1() 




    
    def show_notes_popup1(self):

        layout = FloatLayout()

        scroll = ScrollView(
            size_hint=(1,0.78),
            pos_hint={"x":0, "top":1},
            do_scroll_x=False,
            do_scroll_y=True
        )

        content = Label(
            text="""Read these conditions carefully before starting the game.

    1. The game will be over as soon as the wrong limit is reached.

    2. You will be given your position in the rank list based on the score you have at the time your wrong limit ends.

    3. Play carefully and try to complete all levels.

    4. Wrong answers will reduce your chances of completing the level.""",

            font_size="18sp",
            color=(1,1,1,1),
            halign="left",
            valign="top",
            size_hint_y=None
        )



        content.bind(
            width=lambda instance, value:
            setattr(instance, "text_size", (value, None))
        )


# ye height ko text ke hisab se barhaye gi
        content.bind(
            texture_size=lambda instance, value:
            setattr(instance, "height", value[1])
        )








        scroll.add_widget(content)

        layout.add_widget(scroll)


        close_btn = Button(
            text="Close",
            size_hint=(0.3,0.12),
            pos_hint={"center_x":0.5,"y":0.03},
            background_color=(0.8,0.1,0.1,1)
        )


        popup = Popup(
            title="Game Rules",
            content=layout,
            size_hint=(0.85,0.75),
            auto_dismiss=False,
            background_color=(0.1,0.02,0.2,1)
        )


        close_btn.bind(
            on_press=popup.dismiss
        )


        layout.add_widget(close_btn)

        popup.open()    




















    # =========================================
    # UPDATE BACKGROUND
    # =========================================

    def update_bg(self, *args):

        self.bg.size = self.size
        self.bg.pos = self.pos

        self.overlay.size = self.size
        self.overlay.pos = self.pos





      
    # def save_result(self, uid, score):

    #    doc_ref = db.collection("users").document(uid)
    #    doc = doc_ref.get()

    #    if doc.exists:
    #        old = doc.to_dict().get("high_score", 0)

    #        if score > old:
    #           doc_ref.update({
    #             "high_score": score
    #         })
    #    else:
    #        doc_ref.set({
    #         "high_score": score
    #     })




    def save_result(self, uid, score):

      try:
        doc = db.child("users").child(uid).get().val()

        # ================= IF USER EXISTS =================
        if doc:

            old = doc.get("high_score", 0)

            if score > old:
                db.child("users").child(uid).update({
                    "high_score": score
                })

        # ================= IF USER NOT EXISTS =================
        else:
            db.child("users").child(uid).set({
                "high_score": score
            })

      except Exception as e:
        print("Firebase error:", e)




    def get_rank(self, my_score):

      try:
        users = db.child("users").get().val()

        if not users:
            return 1

        rank = 1

        for key, data in users.items():

            score = data.get("high_score", 0)

            if score > my_score:
                rank += 1

        return rank

      except Exception as e:
        print("Firebase error:", e)
        return 1














    # def get_rank(self, my_score):

    #    users = db.collection("users").stream()

    #    rank = 1

    #    for u in users:
    #       data = u.to_dict()
    #       score = data.get("high_score", 0)

    #       if score > my_score:
    #         rank += 1

    #    return rank


















    # def load_quiz_data(self):
       

    #     file_path = os.path.join(
    #         os.path.dirname(__file__),
    #         "Quiz_data.json"
    #     )

    #     with open(file_path, "r", encoding="utf-8") as file:
    #         data = json.load(file)

    #     return data["questions"]




    # def load_quiz_data(self):

    #     try:
    #         # Firebase se tamam questions load karo
    #         data = db.child("questions").get().val()

    #         if not data:
    #             print("Firebase mein questions nahi mile")
    #             return []

    #         # Firebase dictionary ko list mein convert karo
    #         if isinstance(data, dict):
    #             questions = []

    #             for key in sorted(data.keys(), key=lambda x: int(x)):
    #                 question = data[key]

    #                 if not isinstance(question, dict):
    #                     continue

    #                 # Required fields check karo
    #                 if not all(k in question for k in
    #                            ("question", "options", "answer")):
    #                     print("Invalid question skipped:", key)
    #                     continue

    #                 questions.append(question)

    #         elif isinstance(data, list):
    #             questions = data

    #         else:
    #             print("Firebase data format ghalat hai")
    #             return []

    #         # Empty questions remove karo
    #         questions = [
    #             q for q in questions
    #             if isinstance(q, dict)
    #             and q.get("question")
    #             and q.get("answer")
    #             and q.get("options")
    #         ]

    #         print("Firebase Questions Loaded:", len(questions))

    #         return questions

    #     except Exception as e:
    #         print("Firebase Questions Error:", e)
    #         return []
    














    def load_quiz_data(self):

        print("QUIZ DATA LOADING STARTED")

        try:
            response = db.child("questions").get()
            data = response.val()

            print("FIREBASE DATA:", data)

            if not data:
                print("NO QUESTIONS FOUND")
                return []

            if isinstance(data, dict):
                questions = list(data.values())
            else:
                questions = data

            print("TOTAL QUESTIONS:", len(questions))

            return questions

        except Exception as e:
            print("FIREBASE ERROR:", repr(e))
            return []    














    # def load_quiz_data(self):

    #     try:
    #         data = db.child("questions").get().val()

    #         if not data:
    #             raise Exception("Firebase mein questions nahi mile")

    #         if isinstance(data, dict):
    #             questions = [
    #                 data[key] for key in sorted(data, key=lambda x: int(x))
    #             ]
    #         else:
    #             questions = data

    #         print("Firebase Questions Loaded:", len(questions))

    #         return questions

    #     except Exception as e:
    #         print("Firebase Questions Error:", e)
    #         return []















    # def load_quiz_data(self):

    #     try:
    #         # Firebase se questions load karo
    #         data = db.child("questions").get().val()

    #         if not data:
    #             raise Exception("Firebase mein questions nahi mile")

    #         # Firebase data ko list mein convert karo
    #         if isinstance(data, dict):
    #             questions = [
    #                 data[key] for key in sorted(data, key=lambda x: int(x))
    #             ]
    #         else:
    #             questions = data

    #         print("Firebase Questions Loaded:", len(questions))
    #         return questions

    #     except Exception as e:
    #         print("Firebase Error:", e)

    #         # Firebase fail ho to local JSON load karo
    #         file_path = os.path.join(
    #             os.path.dirname(__file__),
    #             "Quiz_data.json"
    #         )

    #         with open(file_path, "r", encoding="utf-8") as file:
    #             data = json.load(file)

    #         return data["questions"]    












    def load_question(self):
      print("🔥 LOAD CALLED")
      print("INDEX:", self.index)
      print("TOTAL QUESTIONS:", len(self.questions))

    # wrong image hide
      self.show_wrong1.opacity = 0
      if self.index < 0:
         self.index = 0
    # =========================
    # GAME FINISH CHECK
    # =========================
      if self.index >= len(self.questions):
        print("🏁 FINISH TRIGGERED FROM LOAD")

        for b in self.buttons:
            b.disabled = True

        Clock.schedule_once(lambda dt: self.finish(), 0.3)
        return

    # =========================
    # GET QUESTION
    # =========================
      q = self.questions[self.index]
      self.correct = q["answer"]

    # show think animation
      self.show_think()

    # =========================
    # SHUFFLE OPTIONS
    # =========================
      options = q["options"][:]
      random.shuffle(options)

    # =========================
    # TEXT WRAPPING (IMPORTANT FIX)
    # =========================
      import textwrap

      question_text = q["question"]

    # 370 frame width ke liye safe wrap
      wrapped_question = "\n".join(textwrap.wrap(question_text, width=32))

      self.q_lbl.text = wrapped_question

    # force label inside frame
      self.q_lbl.text_size = (350, None)
      self.q_lbl.halign = "center"
      self.q_lbl.valign = "middle"
      self.q_lbl.texture_update()

    # =========================
    # UPDATE SCORE / RESULT
    # =========================
      self.score_lbl.text = f"🏆 Score : {self.score}"
      self.result.text = ""

    # =========================
    # RESET BUTTONS
    # =========================
      for i, btn in enumerate(self.buttons):

        btn.text = options[i]
        btn.disabled = False
        btn.opacity = 1
        
        r, g, b, a = self.colors[i]

        btn.bg_color.r = r
        btn.bg_color.g = g
        btn.bg_color.b = b
        btn.bg_color.a = a






















    # def load_question(self):
    #     print("🔥 LOAD CALLED")
    #     print("INDEX:", self.index)
    #     print("TOTAL QUESTIONS:", len(self.questions))
    # # =====================================
    # # GAME FINISHED CHECK
    # # =====================================

    #     self.show_wrong1.opacity = 0

    #     if self.index >= len(self.questions):
    #         print("🏁 FINISH TRIGGERED FROM LOAD")
    #         for b in self.buttons:
    #             b.disabled = True

    #         # Clock.schedule_once(lambda dt: self.show_game_over(), 0.3)
    #         Clock.schedule_once(lambda dt: self.finish(), 0.3)
    #         return

    # # =====================================
    # # GET QUESTION
    # # =====================================

    #     q = self.questions[self.index]
    #     self.correct = q["answer"]

    # # THINK IMAGE SHOW (NEW QUESTION)
    #     self.show_think()

    # # =====================================
    # # SHUFFLE OPTIONS
    # # =====================================

    #     options = q["options"][:]
    #     random.shuffle(options)

    # # =====================================
    # # UPDATE UI
    # # =====================================

    #     self.q_lbl.text = q["question"]
    #     self.score_lbl.text = f"🏆 Score : {self.score}"
    #     self.result.text = ""

    # # =====================================
    # # RESET BUTTONS
    # # =====================================

    #     for i, btn in enumerate(self.buttons):

    #         btn.text = options[i]
    #         btn.disabled = False

    #         r, g, b, a = self.colors[i]

    #         btn.bg_color.r = r
    #         btn.bg_color.g = g
    #         btn.bg_color.b = b
    #         btn.bg_color.a = a





    def check_answer(self, instance):
        print("CHECK FUNCTION CALLED")
         # 🔘 CLICK SOUND

        if self.index >= len(self.questions):
           return

        if hasattr(self, "click_sound") and self.click_sound:
           self.click_sound.stop()
           self.click_sound.play()

        for b in self.buttons:
            b.disabled = True

        if instance.text == self.correct:

            self.score += 1
            self.result.text = "✅ Correct!"
            self.result.color = (0, 1, 0, 1)

            self.show_correct()

            if hasattr(self, "correct_sound") and self.correct_sound:
                self.correct_sound.stop()
                self.correct_sound.play()


        else:

            self.result.text = "❌ Wrong!"
            self.result.color = (1, 0, 0, 1)

            self.show_wrong()
            self.wrong_count += 1
            self.wrong_limit_label.text = (
                f"Wrong: {self.wrong_count}/5"
            )            

            if self.wrong_count >= 5:
                self.show_game_over()
                return            

            if hasattr(self, "wrong_sound") and self.wrong_sound:
                self.wrong_sound.stop()
                self.wrong_sound.play()


         

        if self.wrong_count < 5:
            Clock.schedule_once(self.next_q, 1.5)
   




    def show_game_over(self):

        layout = FloatLayout()

    # =========================
    # TITLE
    # =========================
        title = Label(
            text="[b]GAME OVER[/b]",
            markup=True,
            font_size="28sp",
            color=(1, 0, 0, 1),
            pos_hint={
                "center_x": 0.5,
                "center_y": 0.82
            }
        )

    # =========================
    # MESSAGE
    # =========================
        msg = Label(
            text=(
                f"You made 5 wrong answers!\n\n"
                f"Correct : {self.score}\n"
                f"Wrong : {self.wrong_count}\n\n"
                f"Better luck next time!"
            ),
            font_size="20sp",
            color=(1, 1, 1, 1),
            halign="center",
            valign="middle",
            pos_hint={
                "center_x": 0.5,
                "center_y": 0.52
            }
        )

    # =========================
    # PLAY AGAIN BUTTON
    # =========================
        play_again = Button(
            text="Play Again",
            size_hint=(0.35, 0.12),
            pos_hint={
                "center_x": 0.3,
                "center_y": 0.15
            },
            background_normal="",
            background_color=(0.1, 0.7, 0.3, 1)
        )

    # =========================
    # HOME BUTTON
    # =========================
        home_btn = Button(
            text="Home",
            size_hint=(0.35, 0.12),
            pos_hint={
                "center_x": 0.7,
                "center_y": 0.15
            },
            background_normal="",
            background_color=(0.2, 0.5, 1, 1)
        )

    # =========================
    # ADD WIDGETS
    # =========================
        layout.add_widget(title)
        layout.add_widget(msg)
        layout.add_widget(play_again)
        layout.add_widget(home_btn)

    # =========================
    # POPUP
    # =========================
        self.game_over_popup = Popup(
            title="",
            content=layout,
            size_hint=(0.9, 0.6),
            separator_height=0,
            auto_dismiss=False
        )

        home = self.manager.get_screen("home")
        uid = home.user_uuid

        if uid:
            try:
                self.save_result(uid, self.score)
                home.load_ranking()
            except Exception as e:
                print("Game Over Save Error:", e)        



    # =========================
    # BUTTON EVENTS
    # =========================
        play_again.bind(on_press=self.restart_game)
        play_again.bind(on_press=self.game_over_popup.dismiss)

        home_btn.bind(on_press=self.go_home)
        home_btn.bind(on_press=self.game_over_popup.dismiss)

    # =========================
    # OPEN POPUP
    # =========================
        self.game_over_popup.open()

        Clock.unschedule(self.next_q)

    # def restart_game(self, instance):

    #     self.game_over_popup.dismiss()

    #     self.score = 0
    #     self.wrong_count = 0
    #     self.index = 0

    #     self.result.text = ""
    #     self.result.color = (1, 1, 1, 1)

    #     self.load_question()

    def restart_game(self, instance):

    # popup band
        self.game_over_popup.dismiss()

    # STOP old scheduled events
        Clock.unschedule(self.next_q)

    # RESET ALL STATE
        self.score = 0
        self.wrong_count = 0
        self.index = 0
        self.wrong_count = 0
        self.wrong_limit_label.text = "Wrong: 0/5"        

        self.result.text = ""
        self.result.color = (1, 1, 1, 1)

    # ENABLE buttons properly
        for b in self.buttons:
             b.disabled = False
             b.opacity = 1

    # START fresh game
        self.load_question()




    def go_home(self, instance):

        self.manager.current = "home"














    def next_q(self, dt):
        print("NEXT_Q CALLED")
        self.index += 1
        self.load_question()



 



    def show_think(self):

        print("think SHOW")

        self.show_think1.opacity = 1
        self.show_correct1.opacity = 0
        self.show_wrong1.opacity = 0


    def show_correct(self):

        print("CORRECT SHOW")

        self.show_think1.opacity = 0
        self.show_correct1.opacity = 1
        self.show_wrong1.opacity = 0


    def show_wrong(self):

        print("wrong SHOW")

        self.show_think1.opacity = 0
        self.show_correct1.opacity = 0
        self.show_wrong1.opacity = 1






    

    # def show_game_over(self):

    #    layout = BoxLayout(
    #     orientation="vertical",
    #     spacing=10,
    #     padding=10
    # )

    # # TITLE
    #    title = Label(
    #     text="🎉 GAME FINISHED 🎉",
    #     font_size="22sp"
    # )

    # # SCORE
    #    score = Label(
    #     text=f"🏆 Final Score: {self.score}",
    #     font_size="18sp"
    # )

    # # BUTTON BOX
    #    btn_box = BoxLayout(size_hint=(1, 0.4), spacing=10)

    #    play_again = Button(text="🔁 Play Again")
    #    home_btn = Button(text="🏠 Home")

    #    btn_box.add_widget(play_again)
    #    btn_box.add_widget(home_btn)

    #    layout.add_widget(title)
    #    layout.add_widget(score)
    #    layout.add_widget(btn_box)

    # # POPUP
    #    self.popup = Popup(
    #      title="",
    #     content=layout,
    #     size_hint=(0.8, 0.5),
    #     auto_dismiss=False
    # )

    # # EVENTS
    # #    play_again.bind(on_press=self.restart_game)
    # #    play_again.bind(on_press=self.popup.dismiss)




    #    play_again.bind(on_press=self.restart_game)
    #    play_again.bind(on_press=self.popup.dismiss)
      
    #    home_btn.bind(on_press=self.go_home)
    #    home_btn.bind(on_press=self.popup.dismiss)





    #    self.popup.open()





    def home_go(self, instance):

       print("🏠 HOME BUTTON CLICKED")

    # 👤 get user id
       home = self.manager.get_screen("home")
       uid = home.user_uuid

    # ❗ save current score safely (agar quiz me ho)
       if hasattr(self, "score"):
          self.save_result(uid, self.score)
          print("💾 Score saved:", self.score)
       else:
          print("⚠ No score found")

    # 📊 update leaderboard (optional refresh)
       try:
          home.load_ranking()
       except:
          print("⚠ load_ranking not found")

    # 🏠 go home
       self.manager.current = "home"



    




    # def start_game(self):

    #   print("🔥 GAME STARTED")

    #   self.index = 0
    #   self.score = 0

    # # 🧠 shuffle questions
    #   self.questions = random.sample(
    #     Quiz_data,
    #     len(Quiz_data)
    # )

    # # 👤 get user
    #   home = self.manager.get_screen("home")
    #   uid = home.user_uuid

    #   if not uid:
    #     print("No user found")
    #     return

    # # ☁️ PYREBASE: get user data
    #   data = db.child("users").child(uid).get().val()

    #   if data:
    #     old_score = data.get("high_score", 0)
    #     print("📊 Previous Score:", old_score)
    #   else:
    #     old_score = 0
    #     print("📊 No previous score found")

    # # 🧠 start game
    #   self.load_question()




    def start_game(self):

        print("🔥 GAME STARTED")

        self.index = 0
        self.score = 0
        self.wrong_count = 0  
        self.wrong_count = 0
        self.wrong_limit_label.text = "Wrong: 0/5"         

        # self.questions = random.sample(
        #     Quiz_data,
        #     len(Quiz_data)
        # )

        self.questions = random.sample(
            self.load_quiz_data(),
            len(self.load_quiz_data())
        )


        home = self.manager.get_screen("home")
        uid = home.user_uuid

        if not uid:
            print("No user found")
            return

        data = db.child("users").child(uid).get().val()

        if data:
            old_score = data.get("high_score", 0)
            print("📊 Previous Score:", old_score)
        else:
            old_score = 0
            print("📊 No previous score found")

        self.result.text = ""

        for b in self.buttons:
            b.disabled = False

        self.load_question()









    def finish(self):

      home = self.manager.get_screen("home")
      uid = home.user_uuid

      if not uid:
        print("No user found")
        return

      self.save_result(uid, self.score)

      rank = self.get_rank(self.score)

      result = self.manager.get_screen("result")

      result.show(
        self.score,
        "User",
        "PK",
        uid,
        rank
    )

      self.manager.current = "result"



    # def start_game(self):

    #    print("🔥 GAME STARTED")

    #    self.index = 0
    #    self.score = 0

    # # 🧠 shuffle questions
    #    self.questions = random.sample(
    #     Quiz_data,
    #     len(Quiz_data)
    # )

    # # 👤 get user
    #    home = self.manager.get_screen("home")
    #    uid = home.user_uuid

    # # ☁️ check previous score from Firebase
    #    doc = db.collection("users").document(uid).get()

    #    if doc.exists:
    #     data = doc.to_dict()
    #     old_score = data.get("high_score", 0)

    #     print("📊 Previous Score:", old_score)

    #    else:
    #     old_score = 0

    # # 🧠 OPTIONAL: show leaderboard immediately
    #    self.load_question()

  

    
    # def finish(self):

    #     uid = self.manager.get_screen("home").user_uuid

    #     self.save_result(uid, self.score)

    #     rank = self.get_rank(self.score)

    #     result = self.manager.get_screen("result")

    #     result.show(
    #         self.score,
    #         "User",
    #         "PK",
    #         uid,
    #         rank
    #     )

    #     self.manager.current = "result"








    # def restart_game(self, instance):

    #     self.index = 0
    #     self.score = 0

    #     self.result.text = ""
    #     self.score_lbl.text = "🏆 Score : 0"

    #     for b in self.buttons:
    #         b.disabled = False

    #     self.load_question()


    
    def toggle_popup(self, instance):

      print("BUTTON CLICKED")

      if self.popup is None:
      # if self.popup is None:

        layout = BoxLayout(
            orientation="vertical",
            spacing=15,
            padding=20
        )

        # 🎨 Background styling (modern card look)
        with layout.canvas.before:
            Color(0.12, 0.12, 0.15, 1)  # dark background
            self.popup_bg = RoundedRectangle(
                size=layout.size,
                pos=layout.pos,
                radius=[20]
            )

        layout.bind(size=self._update_popup_bg, pos=self._update_popup_bg)

        # 🔥 Title
        title = Label(
            text="⚙ MENU",
            font_size="22sp",
            bold=True,
            color=(1, 1, 1, 1),
            size_hint=(1, 0.3)
        )

        # 🔵 Buttons (modern style)
        close_btn = Button(
            text="Close",
            size_hint=(1, None),
            height=50,
            background_normal="",
            background_color=(0.2, 0.6, 1, 1)  # blue
        )

        home_btn = Button(
            text="Home",
            size_hint=(1, None),
            height=50,
            background_normal="",
            background_color=(1, 0.6, 0.1, 1)  # orange
        )

        # ➕ Add widgets
        layout.add_widget(title)
        layout.add_widget(close_btn)
        layout.add_widget(home_btn)

        # 📦 Popup
        self.popup = Popup(
            title="",
            content=layout,
            size_hint=(0.75, 0.5),
            auto_dismiss=True
        )

        # 🔘 Actions
        close_btn.bind(on_press=self.popup.dismiss)
        # close_btn.bind(on_press=self.menu_popup.dismiss)
        home_btn.bind(on_press=self.home_go)
        home_btn.bind(on_press=self.popup.dismiss)
        # home_btn.bind(on_press=self.menu_popup.dismiss)


      self.popup.open()
        # self.menu_popup.open()



    def home_go(self, instance):

    # 👤 get user id
      home = self.manager.get_screen("home")
      uid = home.user_uuid

      if not uid:
        print("No user found")
        return

    # ☁️ save result (Pyrebase)
      try:
        self.save_result(uid, self.score)
      except Exception as e:
        print("Save error:", e)

    # 🔄 reload leaderboard safely
      try:
        home.load_ranking()
      except Exception as e:
        print("Ranking error:", e)

    # 🏠 go back home
      self.manager.current = "home"










    # def home_go(self, instance):

    #   home = self.manager.get_screen("home")
    #   uid = home.user_uuid

    #   self.save_result(uid, self.score)

    #   try:
    #       home.load_ranking()
    #   except:
    #       pass
  
    #   self.manager.current = "home"

    




    def _update_popup_bg(self, instance, value):
       self.popup_bg.pos = instance.pos
       self.popup_bg.size = instance.size





    def finish(self):

      print("🔥 GAME ENDED / BACK PRESSED")

    # 👤 get user id safely
      home = self.manager.get_screen("home")
      uid = getattr(home, "user_uuid", None)

      if not uid:
        print("No user found")
        self.manager.current = "home"
        return

    # 💾 SAVE SCORE (Pyrebase)
      try:
        self.save_result(uid, self.score)
      except Exception as e:
        print("Save error:", e)

    # 🔄 UPDATE LEADERBOARD
      try:
        home.load_ranking()
      except Exception as e:
        print("Ranking error:", e)

    # 🏠 GO HOME
      self.manager.current = "home"




    def save_result(self, uid, final_score):

      if not uid:
        print("No UID found")
        return

    # ☁️ get user data (Pyrebase)
      data = db.child("users").child(uid).get().val()

      if not data:
        print("User not found")
        return

      old_score = data.get("high_score", 0)

    # 🔥 only best score save
      if final_score > old_score:

        db.child("users").child(uid).update({
            "high_score": final_score
        })

        print("✅ New high score saved:", final_score)













    # def finish(self):

    #    print("🔥 GAME ENDED / BACK PRESSED")
   
    #    home = self.manager.get_screen("home")
    #    uid = home.user_uuid

    # # 💾 SAVE SCORE
    #    self.save_result(uid, self.score)

    # # 🔄 UPDATE LEADERBOARD
    #    try:
    #       home.load_ranking()
    #    except:
    #       print("load_ranking not found")

    # # 🏠 GO HOME
    #    self.manager.current = "home"









    # def save_result(self, uid, final_score):

    #    doc_ref = db.collection("users").document(uid)
    #    doc = doc_ref.get()

    #    if not doc.exists:
    #        return

    #    data = doc.to_dict()
    #    old_score = data.get("high_score", 0)

    # # 🔥 only best score save
    #    if final_score > old_score:
    #       doc_ref.update({
    #           "high_score": final_score
    #       })
  











































































































class MyApp(App):

    def build(self):
        # print("DEBUG: BUILD STARTED", flush=True)
        # print("DEBUG: BEFORE KV", flush=True)
        Builder.load_string(KV)
        # print("DEBUG: AFTER KV", flush=True)
        # Window.set_icon("ahmed_logo13.png")

        # self.title = "AY QuizS"
        # sm = ScreenManager()

        # sm.add_widget(SplashScreen(name="splash"))
        # sm.add_widget(Home(name="home"))

        # # baqi screens
        # sm.add_widget(Setup(name="setup"))
        # sm.add_widget(Question(name="question"))
        # sm.add_widget(Generate(name="generate"))
        # sm.add_widget(QuizScreen(name="quiz"))
        # sm.add_widget(page01(name="page01"))
        # # sm.add_widget(Result(name="result"))
        # sm.add_widget(Quiz(name="Quiz"))
        # sm.add_widget(Quiz00(name="quiz1"))
        




        print("DEBUG: AFTER KV", flush=True)

        print("DEBUG: BEFORE ICON", flush=True)
        Window.set_icon("ahmed_logo13.png")
        print("DEBUG: AFTER ICON", flush=True)

        self.title = "AY QuizS"
        print("DEBUG: BEFORE SCREENMANAGER", flush=True)

        sm = ScreenManager()
        print("DEBUG: AFTER SCREENMANAGER", flush=True)

        print("DEBUG: BEFORE SplashScreen", flush=True)
        sm.add_widget(SplashScreen(name="splash"))
        print("DEBUG: AFTER SplashScreen", flush=True)

        print("DEBUG: BEFORE Home", flush=True)
        sm.add_widget(Home(name="home"))
        print("DEBUG: AFTER Home", flush=True)

        print("DEBUG: BEFORE Setup", flush=True)
        sm.add_widget(Setup(name="setup"))
        print("DEBUG: AFTER Setup", flush=True)

        print("DEBUG: BEFORE Question", flush=True)
        sm.add_widget(Question(name="question"))
        print("DEBUG: AFTER Question", flush=True)

        print("DEBUG: BEFORE Generate", flush=True)
        sm.add_widget(Generate(name="generate"))
        print("DEBUG: AFTER Generate", flush=True)

        print("DEBUG: BEFORE QuizScreen", flush=True)
        sm.add_widget(QuizScreen(name="quiz"))
        print("DEBUG: AFTER QuizScreen", flush=True)

        print("DEBUG: BEFORE page01", flush=True)
        sm.add_widget(page01(name="page01"))
        print("DEBUG: AFTER page01", flush=True)

        print("DEBUG: BEFORE Quiz", flush=True)
        sm.add_widget(Quiz(name="Quiz"))
        print("DEBUG: AFTER Quiz", flush=True)

        print("DEBUG: BEFORE Quiz00", flush=True)
        sm.add_widget(Quiz00(name="quiz1"))
        print("DEBUG: AFTER Quiz00", flush=True)

        print("DEBUG: BEFORE SET CURRENT", flush=True)
        sm.current = "splash"
        print("DEBUG: AFTER SET CURRENT", flush=True)

        print("DEBUG: BUILD COMPLETE", flush=True)
        return sm





        # sm.current = "splash"

        # return sm














if __name__ == "__main__":
    MyApp().run()







