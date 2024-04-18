# Magnathon2.0

# Project Name
## SigNet: Hands-On Communication Revolution
Our software represents a groundbreaking advancement in addressing the communication challenges faced by sign language users. By leveraging cutting-edge computer vision and machine learning technologies, our system adeptly captures sign language gestures in real-time with unparalleled precision, seamlessly translating them into easily understandable text and audio formats. Addressing the urgent need for enhanced communication accessibility, our software offers a revolutionary solution that fundamentally transforms how sign language users engage with the world. What truly distinguishes our platform is its exceptional accuracy, versatility, and user-friendliness, facilitated by sophisticated machine learning algorithms meticulously trained on extensive datasets. Beyond its core functionalities, our software boasts an array of features, including support for various sign languages and user-friendly tutorials tailored for beginners, thereby promoting inclusivity and accessibility while democratizing access to sign language proficiency. Furthermore, with support for multiple languages, our software enables users to comprehend sign language gestures in their preferred language, dismantling linguistic barriers and fostering global communication inclusivity. Committed to ongoing research and development, we ensure that our software remains at the forefront of innovation. In essence, our software transcends mere communication facilitation – it empowers individuals, fosters inclusivity, and envisions a world where effortless communication is accessible to all, irrespective of language or ability.

## Team members
- Sreehari S
- Induchoodan VS
- Sofiya B
- Harigovind P Nair

## Link to product walkthrough
[SIGNET presentation.pdf](https://github.com/urbanxtreme/Magnathon2.0/files/15020632/SIGNET.presentation.pdf)

## OUTPUTS
## SIGN IN PAGE
![Screenshot 2024-04-18 081945](https://github.com/urbanxtreme/Magnathon2.0/assets/152000292/d0a7c5dc-7c52-43c1-89be-443f93e24958)
## POPS UP NECESSARY ERRORS WHEN REQUIRED
![Screenshot 2024-04-18 082149](https://github.com/urbanxtreme/Magnathon2.0/assets/152000292/0273b3dd-bf93-48e3-8c71-ed2160c429f0)
![Screenshot 2024-04-18 082204](https://github.com/urbanxtreme/Magnathon2.0/assets/152000292/87c7a59b-d224-41aa-ab10-0923a90ac331)
## LOGIN MENU FOR ALREADY SIGNED IN USERS
![Screenshot 2024-04-18 082340](https://github.com/urbanxtreme/Magnathon2.0/assets/152000292/36603774-be35-49a8-b5e0-dd9975dbd7e2)
## SigNET MENU PAGE
![Screenshot 2024-04-18 082459](https://github.com/urbanxtreme/Magnathon2.0/assets/152000292/d864a8e0-0d59-4f1f-9907-5415d776d11a)
## ABOUT OPTION
![Screenshot 2024-04-18 085942](https://github.com/urbanxtreme/Magnathon2.0/assets/152000292/a19de8a7-c458-40d2-a18a-6aed3f5d2d1d)
## HAND SIGN DETECTION ('A' IS BEING SHOWN)
![Screenshot 2024-04-18 090107](https://github.com/urbanxtreme/Magnathon2.0/assets/152000292/ea66bec5-ff8e-4798-afbc-fb30e1386a12)
## HAND SIGN DETECTION ('L' IS BEING SHOWN)
![Screenshot 2024-04-18 090141](https://github.com/urbanxtreme/Magnathon2.0/assets/152000292/7813bee0-0edc-4742-961f-9634dcdf5780)
## HAND SIGN DETECTION ('Y' IS BEING SHOWN)
![Screenshot 2024-04-18 090227](https://github.com/urbanxtreme/Magnathon2.0/assets/152000292/28c6effb-c68d-470b-98b7-c3a5d106e33c)
## ADD HAND SIGNS MENU
![Screenshot 2024-04-18 093300](https://github.com/urbanxtreme/Magnathon2.0/assets/152000292/052b3144-802e-4489-88da-9d0536613a8b)
## CONFIRMING WHETHER THEY SURELY WANT TO MOVE FORWARD
![Screenshot 2024-04-18 090425](https://github.com/urbanxtreme/Magnathon2.0/assets/152000292/8b406002-8711-4546-b4da-07a1fbfc9841)
## ASKING THEM IF THEY ARE SURE ABOUT THE HAND SIGN AND TO ADD IT
![Screenshot 2024-04-18 090500](https://github.com/urbanxtreme/Magnathon2.0/assets/152000292/65b03734-709e-4f64-a802-6c74df4c058b)

## How it Works ?
This code is a Python program that aims to detect and recognize hand signs using computer vision and machine learning techniques.

1. **Importing Libraries**: The code starts by importing necessary libraries such as OpenCV (`cv2`), MediaPipe (`mediapipe`), NumPy (`numpy`), Tkinter (`tkinter`), and others. These libraries provide functionalities for image processing, machine learning, graphical user interface (GUI) creation, etc.
2. **Sign-in Window (GUI)**: The `signin()` function defines a graphical user interface (GUI) for user registration. It uses Tkinter to create a window with input fields for email, username, password, and confirm password. Users can register by entering their information, and upon successful registration, the data is stored in a MySQL database.
3. **Data Collection**: The `collect_imgs()` function collects hand sign images from the user. It captures images from the webcam, saves them in a directory (`./data`), and organizes them into folders corresponding to different hand signs.
4. **Dataset Creation**: The `create_dataset()` function processes the collected images to create a dataset for training the machine learning model. It uses MediaPipe to extract hand landmarks from the images and stores the extracted features along with corresponding labels (hand signs) in a pickle file (`data.pickle`).
5. **Model Training**: The `train_classifier()` function trains a machine learning model (Random Forest Classifier) using the dataset created in the previous step. It splits the dataset into training and testing sets, trains the model on the training data, and evaluates its performance using the testing data. The trained model is saved in a pickle file (`model.p`).
6. **Inference (Detection)**: The `inference_classifier()` and 'audiowork()' functions implement real-time hand sign detection using the trained model. It creates a GUI application using Tkinter where users can start the detection process. The application accesses the webcam, captures frames, detects hand signs in the frames, and predicts the corresponding hand sign using the trained model. Detected hand signs are displayed on the screen along with the webcam feed.
7. **Additional Functionality**: The `newsigns()` function provides options for users to import hand sign images, confirm hand sign registration, and check detected hand signs. It interacts with other modules (`collect_imgs.py`, `create_dataset.py`, `train_classifier.py`, `inference_classifier.py`) to perform these tasks.

Overall, this code demonstrates a complete pipeline for hand sign detection and recognition, from data collection to model training and real-time inference using a graphical user interface.

## Libraries used
1. openCV: 4.9.0.80
2. mediaPipe: 0.10.11
3. pickle: 0.3.0
4. scikit-learn: 1.4.2
5. tkinter: 0.1
6. numPy: 1.26.4
7. random: 1.0.0
8. pyMySQL: 1.1.0
9. cryptography: 42.0.5
10. pyttsx3: 2.90

## How to configure
Certainly! Here's how you can explain the configuration process as if you've already done it:

1. **Setting up the Environment**:
   - I started by ensuring that Python is installed on my computer. If not, I downloaded and installed Python from the official website.
2. **Library Installation**:
   - Next, I used pip, Python's package manager, to install the required libraries listed in the program. This command installs all the necessary libraries so that the program can run smoothly.
   - pip install opencv-python mediapipe scikit-learn pillow pymysql cryptography
3. **Database Configuration**:
   - Since the program interacts with a MySQL database, I made sure to have MySQL installed and running on my system. Then, I configured the program to connect to my MySQL database by providing the hostname, username, and password in the code.
4. **File Paths**:
   - I checked that all the image files and resources such as (icon.png, bg.png, openeye.png, closeye.png, etc.) referenced in the program exist in the specified locations. If needed, I adjusted the file paths in the code to match my project's directory structure.
5. **GUI Configuration**:
   - The program uses Tkinter for the graphical user interface. I reviewed the code to understand how the GUI elements are structured and customized them according to my preferences. This involved adjusting the layout, styling, and functionality of the GUI.
6. **Testing and Debugging**:
   - After configuring the program, I thoroughly tested it to ensure that all components work as expected. This included testing user interactions, database operations, and any other functionalities. If I encountered any errors during testing, I debugged them and made necessary corrections.
7. **Running the Program**:
   - Once everything was configured and tested successfully, I ran the program by executing the main Python file. This launched the program, and I was able to interact with it using the graphical user interface.
8. **Additional Customization**:
   - Depending on my specific requirements, I made additional customizations to the program. This could include adding new features, modifying existing functionalities, or integrating with other systems or services.

By following these steps, I successfully configured the program to meet my needs and have it ready for use. It was a comprehensive process, but it ensured that the program worked seamlessly and met all my requirements.

## How to Run
To run this program:
1. Ensure you have all the necessary dependencies installed. You can install them using pip if you haven't already:
   pip install opencv-python mediapipe scikit-learn pymysql pyttsx3 cryptography
2. Place all your image data for training in the `data` directory.
3. Uncomment the lines `#collect_imgs()`, `#create_dataset()`, and `#train_classifier()` if you need to collect new images, create a dataset, and train the classifier respectively. These steps are optional if you already have a trained model and dataset.
4. Ensure you have the required image files (`icon.png`, `bg.png`, `bdb.png`, `openeye.png`, `closeye.png`, `openeye1.png`, `closeye1.png`) in the same directory as your Python script.
5. Run the Python script. This will open a GUI window where you can sign in or register. Once signed in, you can start hand sign detection and explore other functionalities like adding, learning, and translating hand signs. Depending on the options selected during registration or sign-in, you may also get audio output for detected hand signs.

Remember to handle the database setup separately according to your environment. Also, make sure to adjust any file paths or configurations as needed for your specific setup.
