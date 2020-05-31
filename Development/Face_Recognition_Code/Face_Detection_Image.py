#!/usr/bin/env python3

# Project:      Robotic Greeter - McMaster University - CareGo Tek
# Program Name: Capture_Picture_Main.py
# Author:       Somak Mukherjee
# Date:         Friday 24 April, 2020
# Version:      1
# Description:  Capture_Picture_Main.py program is a testing program of Face_Detection_Camera.py; this process is use
#           	to detect the faces from an image. First, you need to load the image into the following line present
#          	 	in code: image_path = 'Sample_Images/image1.jpg'.
#
#           	example_image is the directory you need to put your sample image and then need to run the
#           	program. This process will also detect the image coordinate and check if it is present in
#           	encoding.pickle file (~/Face_Recognition_Code/encoding.pickle). If the same coordinate picture
#           	details are current in the archive, then this program will show the known person's name on the video
#           	frame. If not, then it will show as Unknown.
#
# NOTE:       	This program can be run separately or as a stand-alone program as follow:
#           	>> python3 Face_Detection_Image.py

import cv2
import pickle
import face_recognition
from datetime import date, datetime


def face_detection_image():
	encoding_file = 'encodings.pickle'
	image_path = 'Sample_Images/image1.jpg'
	detect_model = 'cnn'

	args = {'encodings': encoding_file, 'image': image_path, 'detection_method': detect_model}

	data = pickle.loads(open(args["encodings"], "rb").read())
	image = cv2.imread(args["image"])
	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	boxes = face_recognition.face_locations(rgb, model=args["detection_method"])
	encodings = face_recognition.face_encodings(rgb, boxes)
	names = []

	for encoding in encodings:

		matches = face_recognition.compare_faces(data["encodings"],	encoding)
		name = "Unknown"
		if True in matches:
			matched_id = [i for (i, b) in enumerate(matches) if b]
			counts = {}
			for i in matched_id:
				name = data["names"][i]
				counts[name] = counts.get(name, 0) + 1
			name = max(counts, key=counts.get)

		names.append(name)

	for ((top, right, bottom, left), name) in zip(boxes, names):

		cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
		y = top - 15 if top - 15 > 15 else top + 15
		cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

	cv2.imshow("Image", image)
	cv2.waitKey(0)


def main():
	today = date.today()
	current_date = today.strftime("%d/%m/%Y")
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	print('Starting program : Face_Detection_Image.py - at : ' + current_time + ' on : ' + current_date)

	face_detection_image()

	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	print('Ending program : Face_Detection_Image.py - at : ' + current_time + ' on : ' + current_date)


if __name__ == "__main__":
	main()
