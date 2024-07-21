Overview
This project focuses on developing a robust Python-based system for precise license plate detection and optical character recognition (OCR). Utilizing OpenCV for image preprocessing and Tesseract for OCR, the system aims to enhance the accuracy of identifying vehicle license plates.

Features
Accurate License Plate Detection: Utilizes OpenCV for image preprocessing tasks such as grayscale conversion, noise reduction, and edge detection.
Optical Character Recognition (OCR): Integrates Tesseract to extract alphanumeric characters from detected license plates, ensuring high precision in identifying vehicle registration information.
Technology Stack
Python: The core programming language used for developing the system.
OpenCV: Employed for image preprocessing, including grayscale conversion, noise reduction using bilateral filtering, and edge detection using the Canny algorithm.
Tesseract: Utilized for OCR to accurately extract characters from the license plates.
Installation
To run this project, follow these steps:

Clone the repository:
git clone https://github.com/yaaaashvii/license-plate-detection.git
Navigate to the project directory:
cd license-plate-detection
Install the required dependencies:
pip install -r requirements.txt

How It Works
Image Preprocessing:

Convert the input image to grayscale.
Apply bilateral filtering to reduce noise.
Use the Canny algorithm to detect edges.

License Plate Detection:

Identify potential license plate regions using contour detection.
Filter and select the most probable license plate region.

Optical Character Recognition (OCR):

Extract the license plate region and pass it to Tesseract.
Recognize and extract alphanumeric characters from the license plate.

Results
The system achieves high precision in detecting and recognizing vehicle license plates, making it suitable for various applications such as automated toll systems, parking management, and law enforcement.
