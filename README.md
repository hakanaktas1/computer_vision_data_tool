# Data Preparation Tool Kit for Computer Vision / AI 


###### Pyqt5, Opencv

<img height="75" src="icons\opencv.png" width="60" title="opencv"/><img height="150" src="icons\logo2.png" width="150" title="logoo"/><img height="75" src="icons\pyqt5.png" width="75" title="logoo"/>


A set of special tools to assist the data generation process for the AI model. A number of operations performed during the preparation of the data were collected in a single application. These operations are:
* Resize
* Crop
* Increase brightness
* Rotate
* **Label**
* Split as train and test randomly

#### Dependencies
opencv-python version(4.6.0)

PyQt5     version(5.15.7)

#### Installing
`pip install -r requeriments.txt`

### Overview to app
![](https://github.com/hakanaktas1/computer_vision_data_tool/blob/main/gifs/firstgif.gif)


## Labeling Page
Mouse events of the Pyqt5 library are used

When the "save" button is clicked after the labeling process is completed,

It creates a label file in ".xml" format with the same file path as the images and the same name as the image.

!["adasd"]()


## Home Page
To create a new AI project file on the desktop, write the project name and click the "create" button.


"images/train" and "images/train" paths are automatically created in the file.

![](https://github.com/hakanaktas1/computer_vision_data_tool/blob/main/gifs/home.gif)


## Resize Page

All images in the dataset are resized according to the entered values

!["adasd"](https://media.giphy.com/media/7kb6EwRwnHICxbtpoI/giphy.mp4)


## Crop Page

All images in the dataset are cropped according to the entered values

!["adasd"](C:\Users\Hakan\Desktop\hakanka\project3_exe\gifs\crop.gif)


## Rotate Page

All images in the dataset are increased brightness according to the entered values

!["adasd"](C:\Users\Hakan\Desktop\hakanka\project3_exe\gifs\rotate.gif)


## Brightness Page

All images in the dataset are increased brightness according to the entered values

!["adasd"](C:\Users\Hakan\Desktop\hakanka\project3_exe\gifs\brig.gif)

## Brightness Page

All data labeled with the entered rate value are randomly distributed in the train and test folders.

Thanks to randomly distributed data, your model training will be more efficient.

!["adasd"](C:\Users\Hakan\Desktop\hakanka\project3_exe\gifs\split.gif)
