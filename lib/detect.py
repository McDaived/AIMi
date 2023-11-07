import sys
import time
import timeit
from termcolor import colored
from utils.grab import screen
import cv2
import imutils
import mss
import _thread
import ctypes
import os
import signal
import numpy as np
import pynput
import keyboard
from pynput.mouse import Listener
sct = mss.mss()
Wd, Hd = sct.monitors[1]["width"], sct.monitors[1]["height"]
SendInput = ctypes.windll.user32.SendInput

def position(x, y):
    x = 1 + int(x * 65536./Wd)
    y = 1 + int(y * 65536./Hd)
    extra = ctypes.c_ulong(0)
    ii_ = pynput._util.win32.INPUT_union()
    ii_.mi = pynput._util.win32.MOUSEINPUT(x, y, 0, (0x0001 | 0x8000), 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    command=pynput._util.win32.INPUT(ctypes.c_ulong(0), ii_)
    SendInput(1, ctypes.pointer(command), ctypes.sizeof(command))


def aimbot(ENABLE_AIMBOT):
     
    YOLO_DIRECTORY = "models" #yolo model path
    
    CONFIDENCE = 0.36
    
    THRESHOLD = 0.22
    
    aimbot_paused = True #make aimbot off on startup
    
    GREEN = '\033[92m'#dont touch it 
    
    RED = '\033[91m'#dont touch it 
    
    RESET = '\033[0m'#dont touch it 
    
    ACTIVATION_RANGE = 250 #box in the center of your screen, lower value of pixel makes the capture faster, for example 250 mean 250x250 pixel box.

    labelsPath = os.path.sep.join([YOLO_DIRECTORY, "coco-dataset.labels"])
    LABELS = open(labelsPath).read().strip().split("\n")
    np.random.seed(42)
    COLORS = np.random.randint(0, 255, size=(len(LABELS), 3),
                               dtype="uint8")

    weightsPath = os.path.sep.join([YOLO_DIRECTORY, "yolov3-tiny.weights"])#yolo path weights
    configPath = os.path.sep.join([YOLO_DIRECTORY, "yolov3-tiny.cfg"])#yolo path models
    time.sleep(0.4)
    
    print("\033[1;36m[Status] loading objects detector..")
    net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)#load objects detector
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_DEFAULT)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_OPENCL)
    ln = net.getLayerNames()
    ln = [ln[i - 1] for i in net.getUnconnectedOutLayers()]

    
    print("\033[1;36m[Status] Define screen capture area..")
    W, H = None, None
    origbox = (int(Wd/2 - ACTIVATION_RANGE/2),#gui box capture
               int(Hd/2 - ACTIVATION_RANGE/2),
               int(Wd/2 + ACTIVATION_RANGE/2),
               int(Hd/2 + ACTIVATION_RANGE/2))

    if not ENABLE_AIMBOT:
        print(colored("[Status] aimbot disabled, only objects detector works...", "red"))
    else:
        print(colored("[AI] Aimbot enabled..", "green"))

    def signal_handler(sig, frame):
        print("\n[Exit] cleaning up...")
        sct.close()#quit and clear terminal
        cv2.destroyAllWindows()
        sys.exit(0)
    signal.signal(signal.SIGINT, signal_handler)

    build_info = str("".join(cv2.getBuildInformation().split()))#check if cpu and gpu cuda is working or disable.
    if cv2.ocl.haveOpenCL():
        cv2.ocl.setUseOpenCL(True)
        cv2.ocl.useOpenCL()
        print(colored("[CPU] OpenCL is enabled..", "green"))
    else:
        print(
            colored("[WARNING-CPU] OpenCL is disabled..", "yellow"))
    if "CUDA:YES" in build_info:
        print(colored("[GPU] CUDA is enabled..", "green"))
    else:
        print(
            colored("[WARNING-GPU] CUDA is disabled..", "yellow"))

    print()
    
    def toggle_aimbot():
        nonlocal aimbot_paused
        aimbot_paused = not aimbot_paused
        status = "hold mode" if aimbot_paused else "always on"
        color = RED if aimbot_paused else GREEN
        print("\nAimbot : " + color + status + RESET)
    keyboard.add_hotkey('F1', toggle_aimbot)
    
    
    def on_click(x, y, button, pressed):
       
       if button == button.x2:
        nonlocal aimbot_paused
        aimbot_paused = not aimbot_paused
        if pressed:
            print("")
        else:
            print("")
    with Listener(on_click=on_click) as listener:
     
     while True:
        if aimbot_paused:
            time.sleep(0.1)
            continue
        start_time = timeit.default_timer()
        frame = np.array(screen(region=origbox))
        frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)
        if W is None or H is None:
            (H, W) = frame.shape[: 2]

        frame = cv2.UMat(frame)
        blob = cv2.dnn.blobFromImage(frame, 1 / 260, (150, 150),
                                     swapRB=False, crop=False)
        net.setInput(blob)
        layerOutputs = net.forward(ln)
        boxes = []
        confidences = []
        classIDs = []
        for output in layerOutputs:
            for detection in output:
                scores = detection[5:]
                # classID = np.argmax(scores)
                # confidence = scores[classID]
                classID = 0  # person = 0
                confidence = scores[classID]
                if confidence > CONFIDENCE:
                    box = detection[0: 4] * np.array([W, H, W, H])
                    (centerX, centerY, width, height) = box.astype("int")
                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))
                    boxes.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))
                    classIDs.append(classID)
        idxs = cv2.dnn.NMSBoxes(boxes, confidences, CONFIDENCE, THRESHOLD)
        
        if len(idxs) > 0:
        
            bestMatch = confidences[np.argmax(confidences)]

            for i in idxs.flatten():
                (x, y) = (boxes[i][0], boxes[i][1])
                (w, h) = (boxes[i][2], boxes[i][3])
                cv2.circle(frame, (int(x + w / 2), int(y + h / 5)), 5, (0, 0, 255), -1) #draw target dot
                # color = [int(c) for c in COLORS[classIDs[i]]]
                cv2.rectangle(frame, (x, y), #draw a box rectangle
                 (x + w, y + h), (0, 255, 0), 2)
                text = "Target {}%".format(int(confidences[i] * 100))
                cv2.putText(frame, text, (x, y - 8),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                if ENABLE_AIMBOT and bestMatch == confidences[i]:
                    mouseX = origbox[0] + (x + w/1.5)
                    mouseY = origbox[1] + (y + h/5)
                    position(mouseX, mouseY)

        cv2.imshow("Gui Objects Detector", frame)
        elapsed = timeit.default_timer() - start_time
        sys.stdout.write(
            "\033[1;33m\rFPS:{1} MS:{0}\t".format(int(elapsed*1000), int(1/elapsed)))
        sys.stdout.flush()
        if cv2.waitKey(1) & 0xFF == ord('0'):
            break

    signal_handler(0, 0)
    listener.join()