import numpy as np
import cv2
from keras.models import load_model
from mss import mss
import os
import time
import pyautogui
import matplotlib.pyplot as plt

screen_height = 280
screen_width = 580
screen_top_padding = 150
screen_left_padding = 60

Image_height = 78
Image_width = 224

sct = mss()
monitor = {'top': screen_top_padding, 'left': screen_left_padding, 'width': screen_width, 'height': screen_height}

class AutoPilot:
    def __init__(self, path='', delay=0, record_trip=False):
        self.model_path = os.path.join(path, 'image_classifier.model')
        try:
            self.pilot_model = load_model(self.model_path)
            print('Model was found and loaded successfully.')
        except:
            print('Model not found. Untrained model was loaded.')

        self.loop_delay = delay
        self.record_trip = record_trip
        self.trip = []

    def grab_screen(self):
        screen = np.array(sct.grab(monitor))
        screen = cv2.resize(screen, (Image_width, Image_height))
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
        return screen

    def drive(self, duration=10):
        start = time.time()
        end = start

        while end - start < duration:
            frame = self.grab_screen()
            frame = np.expand_dims(frame, axis=0)  # Expanding dims to match model's input shape

            if self.record_trip:
                self.trip.append(frame)

            prediction = self.pilot_model.predict(frame)
            output = np.argmax(prediction)

            actions = ['w', 's', 'a', 'd']  # forward, break, left, right
            action = actions[output]
            pyautogui.press(action)  # Simulate key press
            print(action)

            time.sleep(self.loop_delay)
            end = time.time()

    def show_trip(self):
        for frame in self.trip:
            plt.imshow(np.squeeze(frame))
            plt.show()
            time.sleep(self.loop_delay)

        print('Done')


autopilot = AutoPilot(path='.', delay=0.1, record_trip=True)
time.sleep(5)
autopilot.drive(duration=10)
