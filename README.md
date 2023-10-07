# Raspberry Pi Hand Geture Control

## Overview

The Hand Gesture Control Project is a Raspberry Pi-based project that allows users to control both hardware and software applications using hand gestures. The project uses computer vision and gesture recognition to detect hand movements and perform specific actions based on the detected gestures.

## Getting Started

To get started with the project, follow these steps:

1. **Prerequisites:**
   - Raspberry Pi with a camera module.
   - Python installed on your Raspberry Pi.
   If you haven't set up the camera module on your Raspberry Pi yet, you can follow this [article on setting up the camera module] (https://www.digikey.in/en/maker/blogs/2021/how-to-connect-a-camera-to-a-raspberry-pi) to get started.

2.  **Installation:**
    Clone the repository to your Raspberry Pi.
    ```
      git clone https://github.com/AM-5006/Rpi-Hand-Gesture.git
      cd Rpi-Hand-Gesture
    ```
    Install the required dependencies by running the following command: ```pip3 install -r requirements.txt```

3. **Usage:**
   Run the main program using the following command: ```python main.py```
     - After running main.py, a graphical user interface (GUI) will appear on your screen.
     - The GUI provides two options: "Control Hardware" and "Control Software."
     - Select one of the options by clicking the corresponding button.
     - To exit the application, simply close the GUI window. The application will stop, and any hardware or software control actions will cease.

## Contributing
  Contributions to the Raspberry Pi Hand Geture Control project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
