import cv2
import time
import os
import csv
from datetime import datetime

# Create a directory to save photos if not exists
if not os.path.exists('student_photos'):
    os.makedirs('student_photos')

# Create or open attendance file to log records
attendance_file = 'attendance.csv'
if not os.path.isfile(attendance_file):
    with open(attendance_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['101', 'khan', 'Date', 'Time', 'Status'])

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
webcam = cv2.VideoCapture(0)

attendance_given = False
start_time = time.time()

while True:
    success, frame = webcam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # If face is detected
    if len(faces) > 0:
        attendance_given = True
        cv2.putText(frame, "Face Detected - Present ✅", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Prompt to input student Roll Number and Name
        cv2.putText(frame, "Press 's' to mark attendance", (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Attendance Check", frame)

        # Capture Roll Number and Name when 's' is pressed
        if cv2.waitKey(1) & 0xFF == ord('s'):
            roll_number = input("Enter Roll Number: ")
            student_name = input("Enter Student Name: ")

            # Capture student photo
            photo_path = f"student_photos/{roll_number}_{student_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.jpg"
            cv2.imwrite(photo_path, frame)

            # Record attendance with date and time
            attendance_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            with open(attendance_file, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([roll_number, student_name, datetime.now().strftime('%Y-%m-%d'), attendance_time, 'Present'])

            print(f"Attendance marked for {student_name} (Roll No: {roll_number}) at {attendance_time}")
            break

    else:
        cv2.putText(frame, "No Face Detected ❌", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow("Attendance Check", frame)

    # Auto-close after 10 seconds
    if time.time() - start_time > 10:
        break

    # Quit the program if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam and close window
webcam.release()
cv2.destroyAllWindows()
