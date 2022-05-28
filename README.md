## Putting AI into a Drone 

### Objective
- The aim of this project was to program a tello drone to perform basic computer vision tasks such as object detection, face detection, etc.
- Programming was done using the OpenCV library and Python API called `djitellopy` which provides an easy interface over the official Tello SDK and Tello EDU SDK.
- The project contains many smaller modules and computer vision tasks implemented to control the DJI Tello.
- It is an ongoing project of mine, more modules coming soon integerating more computer vision and deep learning in the drone.
- References and inspiration were taken from the lecture series by [Murtaza's Workshop - Robotics and AI](https://www.youtube.com/c/MurtazasWorkshopRoboticsandAI)

### Projects 

#### Face Tracking: 
In this module, the aim was to program the drone to:
- Take live input from its surrounding
- Extract out frames from it.
- Detect face using opencv’s state of the art face detector and return a score for the face depending on the size of it visible in the scene and its orientation
- Based on the above scores, decide weather to move away or towards the face and decide the rotation movement based on orientation of the face.
-Performed reasonably well and was able to track a given subject.

#### Mapping:
In this module, the aim was to program the drone to:
- Given a particular path, trace the path, detect the path and follow along the path.
- The path can be really complex consisting of complicated curves and angles.
- Motion is with a controlled angular and linear velocity which is also programmed.
- Motion is delayed to have grater control and smoother mapping.

#### Surveilance:
In this module, the aim was to program the drone to:
- Move around in the scene, keep capturing live input obtained from the  scene and store the feed.
- The drone can perform movement in 12DOF at a particular speed which can be controlled.

#### Helper Modules:
- Basic Movements: The drone can be controlled to perform various basic movements at different directions and DOFs.
- Image capture : The drone can capture images at various orientations, extract and store the inputs for further processing.
- Keyboard control: The drone can be controlled using the system keyboard instead of an RC(incase RC is not available) to control its movement, flight, landing etc.


#### References:
- https://github.com/damiafuentes/DJITelloPy
- https://youtu.be/LmEcyQnfpDA
