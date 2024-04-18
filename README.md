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
[link to video](Link-here)
Add your ppt to your repository  
## OUTPUTS
![Screenshot 2024-04-18 082149](https://github.com/urbanxtreme/Magnathon2.0/assets/152000292/0273b3dd-bf93-48e3-8c71-ed2160c429f0)



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
1. OpenCV
2. MediaPipe
3. Pickle
4. Scikit-learn
5. Tkinter
6. NumPy
7. Random
8. PyMySQL
9. Cryptography

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
Instructions for running
