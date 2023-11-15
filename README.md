<h1 align="center">AIMi - AI Aimbot</h1>
<p align="center">
    <a href="https://github.com/McDaived/AIMi">
        <img src="https://github.com/McDaived/AIMi/assets/18085492/56684d14-9573-403e-bb06-6c323d475ebc" alt="Logo" width="500" height="150">
    </a>
<h4 align="center">AIMi its an AI aimbot, it work by real-time object detection with neural networks, and recognizes the patterns similar to human movements and human formation and matching them with game models, it will identify the head as a target to make the mouse crosshair heading to the target, the AIMi is now being train to be better</h4>
<h6 align="center">This isn't considered cheating in the games because it doesn't modify the game files or interfere with the games, it only takes control on behalf of the user.</h6>
  <p align="center">
<img src="https://github.com/McDaived/AIMi/assets/18085492/9e53d002-80ec-472b-9156-5416a061790e" alt="Your Image Description" width="500">
<img src="https://github.com/McDaived/AIMi/assets/18085492/c430ab48-99e4-466b-833f-77879a5a01e9" alt="Your Image Description" width="260">


## ![](https://github.com/McDaived/NoRecoil-CS2/assets/18085492/fdee8c61-c0f7-41a2-80a0-15c1b5f5bb95)Information :
- It's an improved version of a very old version of YOLO, **YOLOv7 will be used in the next release**
- It's the **CPU 80%-GPU 20%** version only by using OpenCV , **in the next release it will be developed to work on the GPU by CUDA to make it fast and work more accurately,** because building OpenCV with CUDA is a complicated process , and i will make it in easy way.
- You don't need RTX to make it work.
- This release is currently optimized for cs2, valorant, fps games, etc..
- Objects detector gui to make you see how it recognizes the model.


## ![](https://github.com/McDaived/AIMi/assets/18085492/fbe9cdc5-b23f-4afb-bb7f-1aa8f807dd90) Issues - Q&A :

<details> 
        <summary>⚠ About Warning ⚠</summary> 
    
``PS: if you get this messege [WARN:0@x.xxx], it's a warning issued by the opencv library
 because it's unable to recognize the CPU because it interferes with CUDA because GPU and CUDA is disabled in this version,
 it's automatically will switch to CPU, It's okay, it's just a warning, ignore this message because it doesnt stop the program from working.``
        
          
</details>         

<details> 
        <summary>⚠ If you run the program and it closes immediately or got error about subprocess, please take the following ⚠</summary> 
    
***Download latest version of python then install it like this pictures..***

![](https://github.com/McDaived/AIMi/assets/18085492/d3217d15-7a18-4782-b8f3-d0cbe6acc41d)
![](https://github.com/McDaived/AIMi/assets/18085492/51b0660c-62f1-475b-8181-df1b9d7bbcdd)
![](https://github.com/McDaived/AIMi/assets/18085492/489a6c20-3729-4e9c-9ad2-e388e39c4284)

          
</details>
<details> 
        <summary>⚠ Slight Vibration Why ?⚠</summary> 
    
``when use AIMi you will see slight vibration in aimbot because its a beta version, everything will be improved in the next releases,
it will be better more accurate in the next releases because it works very well for some people and it works well for me,
 it varies according to the processors that can analyze the neural network , but still work fine .`` 

          
</details>

<details> 
        <summary>⚠ Aiming TO The Ground Why?⚠</summary> 
important: to make it work 


  1. disable raw input in any game you want play.

  2. disable enhance pointer : Mouse Properties->Pointer Options->Enhance Pointer Precision

          
</details>

<details> 
        <summary>⚠ Mouse Input Doesn't Work In Valorant why? ⚠</summary> 
if you use it on valorant it dosent work because you need a driver kernal to bypass it, someone was make it work in valorant by using this.

[Click Here](https://www.unknowncheats.me/forum/3912497-post139.html)

IDK, If this work or not but you need driver kernal to bypass it.

          
</details>

## ![](https://github.com/McDaived/Discord-Profile-Card/assets/18085492/7a4879fd-97a1-4807-98e5-8f62137dee6e)Preview :
https://github.com/McDaived/AIMi/assets/18085492/d9e4e81e-ca92-4dcd-b336-ecffec01ed55


## ![](https://github.com/McDaived/NoRecoil-CS2/assets/18085492/7eab67ab-4b44-40ee-b050-53e48a856fc5)How to use :
1. Download [Python](https://www.python.org/).
2. Download AIMi.
3. Extract it.
4. Disable mouse enhance pointer precision, ``Mouse Properties``->``Pointer Options``->``Enhance Pointer Precision``
5. Disable ${\color{red}RAW}$ ${\color{red}INPUT}$ in any game you want to play, **if available**.

**PS: You do not need to do anything else, just open the program from CMD or double-click, and it will download all the required libraries by it self.**

6. ``Python start.py`` or double-click.

## ![](https://github.com/McDaived/AIMi/assets/18085492/be0dff6f-4ef0-4706-a587-c15ad72ca9ff) Settings :

<details> 
        <summary>Optimazing For cs2</summary> 
    Best Setting for CS2 and make sure use this crosshair or make your own dot crosshair, to make natural network more faster by give some space to analyse model.

1. import this crosshair is game setting ``CSGO-YE93T-V6tTU-Cxa9r-jCf7s-2XJaA ``

2. for best result use this setting

![image](https://github.com/McDaived/AIMi/assets/18085492/5fc8c79b-0dd5-4989-9223-9e93760f84a1)

    


</details>

<details> 
        <summary>For Stretch Screen (Optional)</summary> 
    change line 70 in detect file from lib folder.
    
```py
origbox = (int(Wd/3.1 - ACTIVATION_RANGE/4),#gui box capture
               int(Hd/2.5 - ACTIVATION_RANGE/4),
               int(Wd/4 + ACTIVATION_RANGE/1),
               int(Hd/2 + ACTIVATION_RANGE/2))
```

</details>

<details> 
        <summary>Change Hotkey hold mode (Optional)</summary> 
    line 118 in detect file from lib folder.
    
```py
if button == button.x2: #Change this button.x2 for example : button.left for left click mouse


```

</details>


## ![](https://github.com/McDaived/Discord-Profile-Card/assets/18085492/952742cf-9744-4ccb-9de1-766560ebae12)Features :
- (F1) Aimbot: Always On/Hold Mode
- (Mouse4) Hold Mode: Press/Release
- (0) Exit
- With gui objects detector.

## ![](https://github.com/McDaived/AIMi/assets/18085492/cc9f4ef7-bce7-488a-82dc-e4baa198896a)Change Log :
```diff
Update (Nov 15 2023)
+ improve the neural network a little faster.
+ made aimbot a little smooth.
+ Add sound when active aimbot.
+ Add setting for Stretch Screen in Readme.
+ made Aim a little accurate.
+ Fix aim on head.
```


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


