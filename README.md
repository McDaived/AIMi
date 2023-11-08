<h1 align="center">AIMi - AI Aimbot</h1>
<p align="center">
    <a href="https://github.com/McDaived/AIMi">
        <img src="https://github.com/McDaived/AIMi/assets/18085492/56684d14-9573-403e-bb06-6c323d475ebc" alt="Logo" width="500" height="150">
    </a>
<h4 align="center">AIMi its an AI aimbot, it work by real-time object detection with neural networks, and recognizes the patterns similar to human movements and human formation and matching them with game models, it will identify the head as a target to make the mouse crosshair heading to the target, the AIMi is now being trained to make it pretty good</h4>
<h6 align="center">This isn't considered cheating in the games because it doesn't modify the game files or interfere with the games, it only takes control on behalf of the user.</h6>
  <p align="center">
<img src="https://github.com/McDaived/AIMi/assets/18085492/9e53d002-80ec-472b-9156-5416a061790e" alt="Your Image Description" width="500">
<img src="https://github.com/McDaived/AIMi/assets/18085492/c430ab48-99e4-466b-833f-77879a5a01e9" alt="Your Image Description" width="260">


## ![](https://github.com/McDaived/NoRecoil-CS2/assets/18085492/fdee8c61-c0f7-41a2-80a0-15c1b5f5bb95)Information :
- It's an improved version of a very old version of YOLOv3, **YOLOv7 will be used in the next release**
- It's the **CPU 80%-GPU 20%** version only by using OpenCV , **in the next release it will be developed to work on the GPU by CUDA to make it fast and work more accurately,** because building OpenCV with CUDA is a complicated process , and i will make it in easy way.
- You don't need RTX to make it work.
- This release is currently optimized for cs2, valorant, fps games, etc..
- Objects detector gui to make you see how it recognizes the model.

``PS: if you get this messege [WARN:0@2.310], its a warning issued by the opencv library
because its unable to recognize the CPU because it interferes with CUDA cuz GPU is disabled in this version,
Its okay, its just a warning, ignore this message because it doesnt stop the program from working, just a warning
I will solve this bug in the next release.``



## ![](https://github.com/McDaived/Discord-Profile-Card/assets/18085492/7a4879fd-97a1-4807-98e5-8f62137dee6e)Preview :
https://github.com/McDaived/AIMi/assets/18085492/d9e4e81e-ca92-4dcd-b336-ecffec01ed55


## ![](https://github.com/McDaived/NoRecoil-CS2/assets/18085492/7eab67ab-4b44-40ee-b050-53e48a856fc5)How to use :
1. Download [Python](https://www.python.org/).
2. Download AIMi.
3. Extract it.
4. Disable mouse enhance pointer precision, ``Mouse Properties``->``Pointer Options``->``Enhance Pointer Precision``

**PS: You do not need to do anything else, just open the program from CMD or double-click, and it will download all the required libraries by it self.**

5. ``Python start.py`` or double-click.

## ![](https://github.com/McDaived/Discord-Profile-Card/assets/18085492/952742cf-9744-4ccb-9de1-766560ebae12)Features :
- (F1) Aimbot: Always On/Hold Mode
- (Mouse4) Hold Mode: Press/Release
- (0) Exit
- With gui objects detector.

## ![](https://github.com/McDaived/AIMi/assets/18085492/575d27e7-105d-4861-ba99-79e3ac2432dc)About :

### Neural network :
Neural network aimbots are great for a lot of reasons... Probably most importantly, it never access the memory of the game, so it's practically invisible to "Anti-Cheat" sofware, additionally, they can abstract it capabilities to many different games without code modifications.
![](https://github.com/McDaived/AIMi/assets/18085492/a861b711-21e4-4d42-bd87-44d35be9b8b2)

### YOLOvX :
The detection network is trained on a combination of video game images and the **COCO** dataset, it is optimized to recognize human-like objects as quickly as possible, the detection engine can be abstracted to many FPS games.

To know more about [yolov3](https://github.com/ultralytics/yolov3)

![](https://github.com/McDaived/AIMi/assets/18085492/50e29940-26f7-4eb7-a136-818ef8b22348)

### OpenCV :
it provide an abstraction layer for working with the screen capture data, but it it also allows us to harness the power of GPU hardware by interfacing CUDA and OpenCL, it uses OpenCV to process that image into a form that is recognizable to the object-detection engine.

![](https://github.com/McDaived/AIMi/assets/18085492/57f36a86-c149-44ac-a140-6fc05a0bad99)

