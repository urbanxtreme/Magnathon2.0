import tkinter as tk
from tkinter import messagebox
import cv2
import mediapipe as mp
import numpy as np
import pickle
import random
import pyttsx3
class HandSignDetectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SigNet")
        icon = tk.PhotoImage(file="icon.png")
        root.iconphoto(True, icon)
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.create_background()
        self.create_header()
        self.create_buttons()
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.hands = self.mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)
        self.labels_dict = {0: 'A', 1: 'B', 2: 'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z',26:'Delete',27:'Space'}
        # Load the model
        self.load_model()
        # Initialize pyttsx3 engine
        self.engine = pyttsx3.init()
        self.prev_predicted_character = None  # Keep track of the previously predicted character
    def create_background(self):
        self.bg = tk.PhotoImage(file="bdb.png")
        self.bg_label = tk.Label(self.root, image=self.bg)
        self.bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)
    def create_header(self):
        header_label = tk.Label(self.root, text="WELCOME TO SigNet", font=("Arial", 24, "bold underline"), fg="black", bg="light cyan")
        header_label.place(relx=0.5, rely=0.1, anchor="center")
    def create_buttons(self):
        button_frame = tk.Frame(self.root, bg="black")
        button_frame.place(relx=0.5, rely=0.5, anchor="center")
        button_styles = {
            "font": ("Arial", 14, "bold"),
            "width": 20,
            "height": 2,
            "bg": "orange",
            "fg": "black",
            "bd": 0,
            "highlightbackground": "black",
            "activebackground": "cyan",
            "activeforeground": "red"
        }
        start_button = tk.Button(button_frame, text="Start Hand Sign Detection", command=self.start_detection, **button_styles)
        start_button.pack(pady=10)
        about_button = tk.Button(button_frame, text="About", command=self.show_about_info, **button_styles)
        about_button.pack(pady=10)
        add_signs_button = tk.Button(button_frame, text="Add Hand Signs", command=self.add_hand_signs, **button_styles)
        add_signs_button.pack(pady=10)
        learn_signs_button = tk.Button(button_frame, text="Learn Hand Signs", command=self.learn_hand_signs, **button_styles)
        learn_signs_button.pack(pady=10)
        translate_button = tk.Button(button_frame, text="Translate", command=self.translate_hand_signs, **button_styles)
        translate_button.pack(pady=10)
    def load_model(self):
        # Load the model from pickle file
        model_dict = pickle.load(open('./model.p', 'rb'))
        self.model = model_dict['model']
    def start_detection(self):
        cap = cv2.VideoCapture(0)
        frame_count = 0
        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    messagebox.showerror("Error", "Failed to read frame from camera.")
                    break
                frame_count += 1
                # Process every 3rd frame to reduce lag
                if frame_count % 3 != 0:
                    continue
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = self.hands.process(frame_rgb)
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        self.mp_drawing.draw_landmarks(
                            frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS,
                            self.mp_drawing_styles.get_default_hand_landmarks_style(),
                            self.mp_drawing_styles.get_default_hand_connections_style())
                    data_aux = []
                    x_ = []
                    y_ = []
                    for hand_landmarks in results.multi_hand_landmarks:
                        for i in range(len(hand_landmarks.landmark)):
                            x = hand_landmarks.landmark[i].x
                            y = hand_landmarks.landmark[i].y
                            x_.append(x)
                            y_.append(y)
                        for i in range(len(hand_landmarks.landmark)):
                            x = hand_landmarks.landmark[i].x
                            y = hand_landmarks.landmark[i].y
                            data_aux.append(x - min(x_))
                            data_aux.append(y - min(y_))
                    H, W, _ = frame.shape
                    x1 = int(min(x_) * W) - 10
                    y1 = int(min(y_) * H) - 10
                    x2 = int(max(x_) * W) - 10
                    y2 = int(max(y_) * H) - 10
                    prediction = self.model.predict([np.asarray(data_aux)])
                    predicted_character = self.labels_dict.get(int(prediction[0]), 'Unknown')
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
                    cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
                                cv2.LINE_AA)
                    # Speak the predicted character only if it's different from the previously predicted one
                    if predicted_character != self.prev_predicted_character:
                        self.speak_character(predicted_character)
                        self.prev_predicted_character = predicted_character
                cv2.imshow('Hand Sign Detection', frame)
                key = cv2.waitKey(1)
                if key == ord('q') or key == 27:
                    break
        except KeyboardInterrupt:
            print("Keyboard interrupt detected. Exiting...")
        finally:
            cap.release()
            cv2.destroyAllWindows()
    def show_about_info(self):
        messagebox.showinfo("About", "This is a hand sign detection application built using Python, OpenCV, and Mediapipe.")
    def add_hand_signs(self):
        # Add functionality for adding hand signs here
        pass
    def learn_hand_signs(self):
        # Add functionality for learning hand signs here
        pass
    def translate_hand_signs(self):
        # Add functionality for translating hand signs here
        pass
    def speak_character(self, character):
        # Speak out the predicted character
        self.engine.say(character)
        self.engine.runAndWait()
if __name__ == "__main__":
    root = tk.Tk()
    app = HandSignDetectorApp(root)
    root.mainloop()






