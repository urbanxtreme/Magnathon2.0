import os
import cv2
import mediapipe as mp
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import tkinter as tk
from tkinter import messagebox
import numpy as np
import random
from tkinter.ttk import Progressbar
import pymysql
from tkinter import *
import pyttsx3
import cryptography
#=======================================================================================>
def signin():
    def clear():
        emailentry.delete(0, END)
        usernameentry.delete(0, END)
        passwordentry.delete(0, END)
        confirmpasswordentry.delete(0, END)

    def connect_database():
        if emailentry.get() == "" or usernameentry.get() == "" or passwordentry.get() == "" or confirmpasswordentry.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif passwordentry.get() != confirmpasswordentry.get():
            messagebox.showerror("Error", "Passwords doesn't match")
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="1234")
                mycursor = con.cursor()
            except:
                messagebox.showerror("Error", "Database Connectivity issue, Try Again")
                return
            try:
                query = "create database handsign"
                mycursor.execute(query)
                query = "use handsign"
                mycursor.execute(query)
                query = "create table data(id int auto_increment primary key not null, email varchar(50), username varchar(100), password varchar(20))"
                mycursor.execute(query)
            except:
                mycursor.execute("use handsign")
            query = "select * from data where username=%s"
            mycursor.execute(query, (usernameentry.get()))
            row = mycursor.fetchone()
            query = "select * from data where email=%s"
            mycursor.execute(query, (emailentry.get()))
            column = mycursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "Username Already exists")
            elif column != None:
                messagebox.showerror("Error", "Email already exists")
            else:
                query = "insert into data(email,username,password) values(%s,%s,%s)"
                mycursor.execute(query, (emailentry.get(), usernameentry.get(), passwordentry.get()))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Registration Successful")
                response = messagebox.askyesno("Confirmation", "Do you want aduio output?")
                if response:
                    audiowork()
                else:
                    inference_classifier()
                clear()
                login_window.destroy()

    def hide():
        openeye.config(file="closeye.png")
        passwordentry.config(show="*")
        eyeButton.config(command=show)

    def show():
        openeye.config(file="openeye.png")
        passwordentry.config(show="")
        eyeButton.config(command=hide)

    def hided():
        openeye1.config(file="closeye1.png")
        confirmpasswordentry.config(show="*")
        eyeButton1.config(command=showed)

    def showed():
        openeye1.config(file="openeye1.png")
        confirmpasswordentry.config(show="")
        eyeButton1.config(command=hide)

    def login():
        login_window.destroy()
        import loginpage
        response1 = messagebox.askyesno("Confirmation", "Do you want audio output?")
        if response1:
            audiowork()
        else:
            inference_classifier()

    login_window = Tk()
    icon = PhotoImage(file="icon.png")
    login_window.iconphoto(True, icon)
    login_window.title("Sign In window")
    login_window.geometry("1920x1080+0+2")
    bgImage = PhotoImage(file="bg.png")
    bgLabel = Label(login_window, image=bgImage).place(x=0, y=0, relwidth=1, relheight=1)
    # login frame
    Frame_login = Frame(login_window, bg="lemon chiffon", relief=SOLID)
    Frame_login.place(x=500, y=200, width=500, height=400)
    # Title and subs
    title = Label(Frame_login, text="Sign in", font=("Impact", 25, "bold", "underline"), fg="yellow", bg="black")
    title.place(x=180, y=30)
    # mail
    email = Label(Frame_login, text="E-mail:", font=("Algerian", 15), fg="navy", bg="alice blue")
    email.place(x=0, y=110)
    # entry box
    emailentry = Entry(Frame_login, font=("Times New Roman", 15), bd=0, fg="dark blue", bg="ghost white")
    emailentry.place(x=210, y=110, width=280, height=26)
    # username
    username = Label(Frame_login, text="USERNAME:", font=("Algerian", 15), fg="navy", bg="alice blue")
    username.place(x=0, y=160)
    # entry box
    usernameentry = Entry(Frame_login, font=("Times New Roman", 15), bd=0, fg="dark blue", bg="ghost white")
    usernameentry.place(x=210, y=160, width=280, height=26)
    # password
    password = Label(Frame_login, text="PASSWORD:", font=("Algerian", 15), fg="navy", bg="alice blue")
    password.place(x=0, y=210)
    # entry box
    passwordentry = Entry(Frame_login, font=("Times New Roman", 15), bd=0, fg="dark blue", bg="ghost white")
    passwordentry.place(x=210, y=210, width=280, height=26)
    # confirm password
    confirmpassword = Label(Frame_login, text="CONFIRM PASSWORD:", font=("Algerian", 15), fg="navy", bg="alice blue")
    confirmpassword.place(x=0, y=260)
    # entry box
    confirmpasswordentry = Entry(Frame_login, font=("Times New Roman", 15), bd=0, fg="dark blue", bg="ghost white")
    confirmpasswordentry.place(x=210, y=260, width=280, height=26)
    # login label
    loginlabel = Label(Frame_login, text="Already have an acccount?", font=("Open Sans", 9, "bold"), fg="black",
                       bg="lemon chiffon")
    loginlabel.place(x=150, y=370)
    # buttons
    # sign in
    signinButton = Button(Frame_login, text="Sign In", font=("Open Sans", 15, "bold"), bd=0, cursor="hand2", fg="white",
                          bg="firebrick1", command=connect_database)
    signinButton.place(x=215, y=310)
    # login
    loginbutton = Button(Frame_login, text="Login", font=("Open Sans", 9, "bold underline"), bd=0, command=login,
                         cursor="hand2", fg="blue", bg="lemon chiffon", activebackground="lemon chiffon",
                         activeforeground="hot pink")
    loginbutton.place(x=305, y=370)
    # eye button
    openeye = PhotoImage(file="openeye.png")
    eyeButton = Button(Frame_login, image=openeye, bd=0, bg="ghost white", activebackground="ghost white",
                       activeforeground="ghost white", cursor="hand2", command=hide)
    eyeButton.place(x=460, y=210)
    # eye button2
    openeye1 = PhotoImage(file="openeye1.png")
    eyeButton1 = Button(Frame_login, image=openeye1, bd=0, bg="ghost white", activebackground="ghost white",
                        activeforeground="ghost white", cursor="hand2", command=hided)
    eyeButton1.place(x=460, y=260)
    login_window.mainloop()
#=======================================================================================>
def collect_imgs():
    DATA_DIR = './data'
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    number_of_classes = 1
    dataset_size = 100
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()
    for j in range(number_of_classes):
        class_dir = os.path.join(DATA_DIR, str(j))
        if not os.path.exists(class_dir):
            os.makedirs(class_dir)
        print('Collecting data for class {}'.format(j))
        input("Press Enter when ready...")
        counter = 0
        while counter < dataset_size:
            ret, frame = cap.read()
            if not ret:
                print("Error: Failed to capture image.")
                break
            if frame.shape[0] > 0 and frame.shape[1] > 0:
                cv2.imshow('frame', frame)
                cv2.waitKey(25)
                cv2.imwrite(os.path.join(class_dir, '{}.jpg'.format(counter)), frame)
                counter += 1
            else:
                print("Error: Invalid frame dimensions.")
                break
    cap.release()
    cv2.destroyAllWindows()
#================================================================================>
def create_dataset():
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)
    DATA_DIR = './data'
    data = []
    labels = []
    for dir_ in os.listdir(DATA_DIR):
        for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):
            data_aux = []
            x_ = []
            y_ = []
            img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = hands.process(img_rgb)
            if results.multi_hand_landmarks:
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
                data.append(data_aux)
                labels.append(dir_)
    f = open('data.pickle', 'wb')
    pickle.dump({'data': data, 'labels': labels}, f)
    f.close()
#======================================================================================>
def train_classifier():
    data_dict = pickle.load(open('./data.pickle', 'rb'))
    data = np.asarray(data_dict['data'])
    labels = np.asarray(data_dict['labels'])
    x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)
    model = RandomForestClassifier()
    model.fit(x_train, y_train)
    y_predict = model.predict(x_test)
    score = accuracy_score(y_predict, y_test)
    print('{}% of samples were classified correctly !'.format(score * 100))
    f = open('model.p', 'wb')
    pickle.dump({'model': model}, f)
    f.close()
#=========================================================================================>
def inference_classifier():
    class HandSignDetectorApp:
        def __init__(self, root):
            self.root = root
            self.root.title("SigNet")
            icon = tk.PhotoImage(file="icon.png")
            root.iconphoto(True, icon)
            self.root.geometry("800x600+400+100")
            self.root.resizable(False, False)
            self.create_background()
            self.create_header()
            self.create_buttons()
            self.mp_hands = mp.solutions.hands
            self.mp_drawing = mp.solutions.drawing_utils
            self.mp_drawing_styles = mp.solutions.drawing_styles
            self.hands = self.mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)
            self.labels_dict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K',11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z', 26: 'Delete', 27: 'Space'}
            self.load_model()
        def create_background(self):
            self.bg = tk.PhotoImage(file="bdb.png")
            self.bg_label = tk.Label(self.root, image=self.bg)
            self.bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)
        def create_header(self):
            header_label = tk.Label(self.root, text="WELCOME TO SigNet", font=("Arial", 24, "bold underline"),fg="black", bg="light cyan")
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
            start_button = tk.Button(button_frame, text="Start Hand Sign Detection", command=self.start_detection,**button_styles)
            start_button.pack(pady=10)
            about_button = tk.Button(button_frame, text="About", command=self.show_about_info, **button_styles)
            about_button.pack(pady=10)
            add_signs_button = tk.Button(button_frame, text="Add Hand Signs", command=self.add_hand_signs,**button_styles)
            add_signs_button.pack(pady=10)
            learn_signs_button = tk.Button(button_frame, text="Learn Hand Signs", command=self.learn_hand_signs,**button_styles)
            learn_signs_button.pack(pady=10)
            translate_button = tk.Button(button_frame, text="Translate", command=self.translate_hand_signs,**button_styles)
            translate_button.pack(pady=10)
        def introcolor(self, colors):
            fg = random.choice(colors)
            self.header_label.config(fg=fg)
            self.header_label.after(200, self.introcolor, colors)
        def welcome(self, ss):
            if self.count >= len(ss):
                self.count = 0
                self.text = ""
                self.header_label.config(text=self.text)
            else:
                self.text = self.text + ss[self.count]
                self.header_label.config(text=self.text)
                self.count += 1
            self.header_label.after(200, self.welcome, ss)
        def load_model(self):
            # Load the model from pickle file
            model_dict = pickle.load(open('./model.p', 'rb'))
            self.model = model_dict['model']
        def start_detection(self):
            cap = cv2.VideoCapture(0)
            try:
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        messagebox.showerror("Error", "Failed to read frame from camera.")
                        break
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
                        cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0),
                                    3,
                                    cv2.LINE_AA)
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
            messagebox.showinfo("About","This is a hand sign detection application built using Python, OpenCV, and Mediapipe.")
        def add_hand_signs(self):
            import newsigns
        def learn_hand_signs(self):
            pass
        def translate_hand_signs(self):
            pass
    if __name__ == "__main__":
        root = tk.Tk()
        app = HandSignDetectorApp(root)
        root.mainloop()
#===========================================================================================>
def newsigns():
    def import_file():
        messagebox.showinfo("Sign", "Press ok to go forward and input your own hand sign.")
        import collect_imgs
        progress_window = tk.Toplevel()
        progress_window.title("Importing Files")
        progress_window.geometry("300x100")
        progress_label = tk.Label(progress_window, text="Importing files, please wait...")
        progress_label.pack(pady=10)
        progress_bar = Progressbar(progress_window, orient="horizontal", mode="indeterminate", length=200)
        progress_bar.pack(pady=5)
        import create_dataset
        import train_classifier
        import inference_classifier
        progress_bar.start(10)  # Start the progress bar animation
        progress_window.after(50000, progress_window.destroy)  # Close the progress window after 5 seconds
    def confirm_action():
        response = messagebox.askyesno("Confirm?", "Are you sure you want to register this hand sign?")
        if response:
            messagebox.showinfo("Confirmed", "Hand sign registration confirmed!")
    def check_action():
        messagebox.showinfo("Check", "Checking hand sign...")
        import inference_classifier
    window = tk.Tk()
    window.title("Hand Sign Detection")
    window.geometry("600x600+450+150")
    window.config(bg="gold2")
    import_button = tk.Button(window, text="Import Hand Sign", font=("Arial", 14), bg="red", fg="white",command=import_file)
    import_button.place(relx=0.5, rely=0.3, anchor="center", width=200, height=50)
    confirm_button = tk.Button(window, text="Confirm", font=("Arial", 14), bg="green", fg="white",command=confirm_action)
    confirm_button.place(relx=0.5, rely=0.5, anchor="center", width=200, height=50)
    check_button = tk.Button(window, text="Check", font=("Arial", 14), bg="blue", fg="white", command=check_action)
    check_button.place(relx=0.5, rely=0.7, anchor="center", width=200, height=50)
    window.mainloop()
#======================================================================================>
def audiowork():
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
            self.labels_dict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K',
                                11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
                                20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z', 26: 'Delete', 27: 'Space'}
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
            header_label = tk.Label(self.root, text="WELCOME TO SigNet", font=("Arial", 24, "bold underline"),
                                    fg="black", bg="light cyan")
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
            start_button = tk.Button(button_frame, text="Start Hand Sign Detection", command=self.start_detection,
                                     **button_styles)
            start_button.pack(pady=10)
            about_button = tk.Button(button_frame, text="About", command=self.show_about_info, **button_styles)
            about_button.pack(pady=10)
            add_signs_button = tk.Button(button_frame, text="Add Hand Signs", command=self.add_hand_signs,
                                         **button_styles)
            add_signs_button.pack(pady=10)
            learn_signs_button = tk.Button(button_frame, text="Learn Hand Signs", command=self.learn_hand_signs,
                                           **button_styles)
            learn_signs_button.pack(pady=10)
            translate_button = tk.Button(button_frame, text="Translate", command=self.translate_hand_signs,
                                         **button_styles)
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
                        cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0),
                                    3,
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
            messagebox.showinfo("About",
                                "This is a hand sign detection application built using Python, OpenCV, and Mediapipe.")

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

signin()
#collect_imgs()          #Used for training
#create_dataset()        #Used for training
#train_classifier()      #Used for training


