import cv2
import mediapipe as mp

mpDraw = mp.solutions.drawing_utils 
mpPose = mp.solutions.pose
pose = mpPose.Pose()

cam = cv2.VideoCapture(0)

while True:
    success , img = cam.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)

    cv2.imshow("IMAGE",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break