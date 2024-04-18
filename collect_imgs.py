import os
import cv2
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
