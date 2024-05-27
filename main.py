import cv2
from utils import *
import mediapipe as mp
from body_part_angle import BodyPartAngle
from types_of_exercise import TypeOfExercise
from gui import *
import pyttsx3
import datetime
import time


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning sir!")
    elif hour >= 12 and hour < 18:
        speak("good afternoon sir!")
    else:
        speak("good evening Sir!")

    samy = time.strftime("%H:%M:%S")
    speak("the time is" + samy)
    speak("I am your Personal trainer , Get ready for workout.")    

if x==1:
    exercise_type = "walk"
    greet()
    speak("We will perform jogging now")
if x==2:
    exercise_type = "push_up"
    greet()
    speak("We will perform push-up now")
if x==3:
    exercise_type = "sit-up"
    greet()
    speak("We will perform sit-up now")
if x==4:
    exercise_type = "pull-up"
    greet()
    speak("We will perform pull-up now")
if x==5:
    exercise_type = "squat" 
    greet()           
    speak("We will perform squat now")
                

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


cap = cv2.VideoCapture(0)  # webcam

cap.set(3, 800)
cap.set(4, 480)

# setup mediapipe
with mp_pose.Pose(min_detection_confidence=0.5,
                  min_tracking_confidence=0.5) as pose:

    counter = 0  # movement of exercise
    status = True  # state of move
    while cap.isOpened():
        ret, frame = cap.read()
        frame = cv2.resize(frame, (1920, 1080), interpolation=cv2.INTER_AREA)
        # recolor frame to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame.flags.writeable = False
        # make detection
        results = pose.process(frame)
        # recolor back to BGR
        frame.flags.writeable = True
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        try:
            landmarks = results.pose_landmarks.landmark
            counter, status = TypeOfExercise(landmarks).calculate_exercise(exercise_type, counter, status)
        except:
            pass

        frame = score_table(exercise_type, frame, counter, status)

        # render detections (for landmarks)
        mp_drawing.draw_landmarks(
            frame,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(255, 255, 255),
                                   thickness=2,
                                   circle_radius=2),
            mp_drawing.DrawingSpec(color=(174, 139, 45),
                                   thickness=2,
                                   circle_radius=2),
        )

        cv2.imshow('Video', frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
