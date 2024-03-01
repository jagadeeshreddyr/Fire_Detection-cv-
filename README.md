# Fire Detection

![Fire Detection](fire.jpeg)

## Overview

This project focuses on detecting fires through image processing techniques, particularly leveraging OpenCV (cv2). The objective is to showcase the efficiency and speed of image processing in fire detection, which can be up to 10 times faster compared to real-time sensors.

## Features

- Utilizes a pre-trained model based on the Haar Cascade algorithm for fire detection (model path: `xml/fire_detection.xml`).
- Integrates with the Blynk IoT platform to provide real-time alerts upon fire detection. The system seamlessly connects to Wi-Fi for communication.
- Conducts a hardware comparison by integrating smoke and fire sensors with an ESP32 microcontroller. This comparison highlights the disparities between traditional sensors and image processing.
- The project is easily executable by installing the provided Conda environment using the YAML file.
- To test the system, simply position a lit matchstick in front of the camera to initiate the fire detection process.

## Getting Started

To start with this project, follow these steps:

1. Clone this repository to your local machine.

2. Install the Conda environment using the provided YAML file:

   ```bash
   conda env create -f environment.yml

## About the Haar Cascade Algorithm

The Haar Cascade algorithm is a machine learning-based approach used for object detection in images. It involves training a cascade of classifiers based on the Haar-like features of images. In the context of fire detection, the algorithm is trained to recognize patterns and characteristics associated with flames, enabling accurate identification in images or video frames.
