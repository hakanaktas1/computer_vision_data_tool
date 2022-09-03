import os
import shutil
import sys
from PyQt5.QtCore import QPoint, QRect
import cv2
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QImage, QPainter, QBrush, QColor, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QLabel
import random
import glob

from main_ui import BackGround


class TestRect(QLabel):
    def __init__(self):
        super().__init__()
        self.begin = QPoint()
        self.end = QPoint()
        self.a = {}

    def paintEvent(self, event):
        super().paintEvent(event)
        qp = QPainter(self)
        br = QBrush(QColor(255, 0, 1, 44))
        qp.setBrush(br)
        qp.drawRects(QRect(self.begin, self.end))

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = event.pos()
        self.update()

    def mouseMoveEvent(self, event):

        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        # qp = QPainter(self)
        # self.begin = event.pos()
        self.end = event.pos()
        # self.update()


def show_info_messagebox(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("Information: " + str(text))
    msg.setWindowTitle("Information MessageBox")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


def convert_cv_qt(cv_img):
    rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    h, w, ch = rgb_image.shape
    bytes_per_line = ch * w
    converted = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)

    return QPixmap.fromImage(converted)


def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img


class MainWindow:
    def __init__(self):
        self.response = None
        self.images_list = None
        self.path_name = None
        self.main_win = QMainWindow()
        self.main_win.showMaximized()
        self.main_win.setWindowIcon(QIcon("icons\logo.png"))
        self.ui = BackGround()
        self.ui.setupUi(self.main_win)
        self.ui.home_central_button.clicked.connect(self.home)
        self.ui.resize_central_button.clicked.connect(self.resize)
        self.ui.crop_central_button.clicked.connect(self.crop)
        self.ui.brig_central_button.clicked.connect(self.brig)
        self.ui.rotate_central_button.clicked.connect(self.rotate)
        self.ui.seperate_central_button.clicked.connect(self.seperate)
        self.ui.label_central_button.clicked.connect(self.label)
        self.ui.pushButton_3.clicked.connect(self.home_func)
        self.ui.open_button_resize.clicked.connect(self.get_file_name)
        self.ui.open_button_crop_2.clicked.connect(self.get_file_name)
        self.ui.open_button_rotate_3.clicked.connect(self.get_file_name)
        self.ui.open_button_brig_4.clicked.connect(self.get_file_name)
        self.ui.open_button_ann_5.clicked.connect(self.get_file_name)
        self.ui.pushButton.clicked.connect(self.get_file_name)

        self.count = 0
        self.image = TestRect()
        self.ui.layout_ann_5.addWidget(self.image)
        self.arr_val = []
        self.arr_name = []

        self.ui.run_button_resize.clicked.connect(self.resize_1)
        self.ui.run_button_crop_2.clicked.connect(self.crop_1)
        self.ui.run_button_rotate_3.clicked.connect(self.rotate_1)
        self.ui.run_button_brig_4.clicked.connect(self.brig_1)
        self.ui.pushButton_2.clicked.connect(self.train_test_seperator)
        self.ui.open_button_ann_5.clicked.connect(self.work_1)

        self.ui.preview_button_resize.clicked.connect(self.resize_preview)
        self.ui.preview_button_crop_2.clicked.connect(self.crop_preview)
        self.ui.preview_button_rotate_3.clicked.connect(self.rotate_preview)
        self.ui.preview_button_brig_4.clicked.connect(self.brig_preview)

        self.ui.preview_button_ann_5.clicked.connect(self.work_2)
        self.ui.horizontalSlider.sliderMoved.connect(self.print)
        self.ui.preview_button_ann_6.clicked.connect(self.work_3)
        self.ui.run_button_ann_5.clicked.connect(self.work_4)
        self.ui.run_button_ann_5.clicked.connect(self.work_1)

        self.ui.save_button_brig.clicked.connect(self.save_file_name)
        self.ui.save_button_crop.clicked.connect(self.save_file_name)
        self.ui.save_button_resize.clicked.connect(self.save_file_name)
        self.ui.save_button_rotate.clicked.connect(self.save_file_name)
        self.ui.save_button_split.clicked.connect(self.save_file_name)

    def print(self):
        train, test = int(self.ui.horizontalSlider.value()), 100 - int(self.ui.horizontalSlider.value())
        self.train1, self.test1 = round(train/10)*10, round(test/10)*10
        self.ui.label_21.setText("%{} ".format(self.train1))
        self.ui.label_31.setText("%{} ".format(self.test1))

    def home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_widget)

        self.ui.label_center2.move(222, 157)

    def resize(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.resize_widget)
        self.ui.label_center2.move(218, 265)

    def crop(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.crop_widget)
        self.ui.label_center2.move(218, 365)

    def rotate(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.rotate_widget)
        self.ui.label_center2.move(218, 465)

    def label(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.label_widget)
        self.ui.label_center2.move(218, 665)

    def seperate(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.seperate_widget)
        self.ui.label_center2.move(218, 765)

    def brig(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.brig_widget)
        self.ui.label_center2.move(218, 565)

    def show(self):
        self.main_win.show()

    def get_file_name(self):
        path = os.path.expanduser("~/Desktop")
        self.response = QFileDialog.getExistingDirectory(caption='Choose Directory', directory=path)

    def save_file_name(self):
        path = os.path.expanduser("~/Desktop")
        self.response2 = QFileDialog.getExistingDirectory(caption='Choose Directory', directory=path)

    def home_func(self):
        path = os.path.expanduser("~/Desktop")
        name = self.ui.Home_Project_Name_Line.text()
        name = "/" + name

        img_file_name = r"\images"
        train_file_name = r"\train"
        test_file_name = r"\test"
        self.path_name = path + name
        try:
            os.mkdir(path + name)
            os.mkdir(path + name + img_file_name)
            os.mkdir(path + name + img_file_name + test_file_name)
            os.mkdir(path + name + img_file_name + train_file_name)
            show_info_messagebox("Dosya oluşturuldu")
        except FileExistsError:
            show_info_messagebox("Aynı isimde dosya var!")

    def resize_1(self):
        try:
            count = 0
            images_list = glob.glob(self.response + '/*.jpg')
            images_list2 = glob.glob(self.response + '/*.png')
            images_list.extend(images_list2)
            self.ui.progressBar_resize.setRange(0, len(images_list))
            os.mkdir(self.response2 + "/resized")

            for file in images_list:
                name = file[:-4].split("\\")[-1]
                self.ui.progressBar_resize.setValue(count)
                img = cv2.imread(file)
                img = cv2.resize(img, (int(self.ui.width_resize_text.text()),
                                       int(self.ui.height_resize_text.text())), interpolation=cv2.INTER_NEAREST)
                cv2.imwrite(self.response2 + "/resized/" + name + "_resized" + ".jpg", img)
                count += 1

                if count == len(images_list):
                    self.ui.progressBar_resize.setValue(0)
                    self.ui.info_resize_box.setText("İşlem Tamam " +
                                                    str(len(images_list)) + " Resim Resize Edildi.")
                    show_info_messagebox("İşlem Tamam " + str(len(images_list)) + " Resim Resize Edildi.")

        except ValueError:
            show_info_messagebox("Please write the width and height values")
        except AttributeError:
            show_info_messagebox("Please select file")
        except TypeError:
            show_info_messagebox("Please create project file on home page")
        except FileExistsError:
            show_info_messagebox("Bir önceki dosya üzerine işlem yapılamaz, yeni dosya oluşturabilirsiniz")
        except cv2.error:
            show_info_messagebox("hata")

    def resize_preview(self):
        global image
        try:
            images_list = glob.glob(self.response + '/*.jpg')
            images_list2 = glob.glob(self.response + '/*.png')
            images_list.extend(images_list2)
            rand_image_path = random.choice(images_list)
            image = cv2.imread(rand_image_path)
            image_resized = cv2.resize(image, (int(self.ui.width_resize_text.text()),
                                       int(self.ui.height_resize_text.text())), interpolation=cv2.INTER_NEAREST)
            qt_img = convert_cv_qt(image_resized)
            self.ui.layout_resize.setGeometry(10, 80, image_resized.shape[1], image_resized.shape[0])
            self.ui.layout_resize.setPixmap(qt_img)
            self.ui.info_resize_box.setText("Orginal size; Width:{} and Height:{}\nCropped size; Width:{} and Height:{}"
                                            .format(str(image.shape[1]), str(image.shape[0]),
                                                    str(self.ui.width_resize_text.text()),
                                                    str(self.ui.height_resize_text.text())))
        except ValueError:
            qt_img = convert_cv_qt(image)
            self.ui.layout_resize.setGeometry(10, 80, image.shape[1], image.shape[0])
            self.ui.layout_resize.setPixmap(qt_img)
        except AttributeError:
            show_info_messagebox("Please select file")
        except TypeError:
            show_info_messagebox("Please create project file on home page")
        except FileExistsError:
            show_info_messagebox("Bir önceki dosya üzerine işlem yapılamaz, yeni dosya oluşturabilirsiniz")

    def crop_preview(self):
        global image
        try:
            images_list = glob.glob(self.response + '/*.jpg')
            images_list2 = glob.glob(self.response + '/*.png')
            images_list.extend(images_list2)
            rand_image_path = random.choice(images_list)
            image = cv2.imread(rand_image_path)
            image_crop = image[int(self.ui.ymin_crop_text_2.text()):int(self.ui.ymax_crop_text_3.text()),
                               int(self.ui.xmin_crop_text_2.text()):int(self.ui.xmax_crop_text_3.text())]
            qt_img = convert_cv_qt(image_crop)
            self.ui.layout_crop.setGeometry(10, 80, image_crop.shape[1], image_crop.shape[0])
            self.ui.layout_crop.setPixmap(qt_img)
            self.ui.info_crop_box_2.setText("Orginal size; Width:{} and Height:{}\nCropped size; Width:{} and Height:{}"
                                            .format(str(image.shape[1]), str(image.shape[0]),
                                                    str(int(self.ui.xmax_crop_text_3.text())
                                                        - int(self.ui.xmin_crop_text_2.text())),
                                                    str(int(self.ui.ymax_crop_text_3.text())
                                                        - int(self.ui.ymin_crop_text_2.text()))))
        except ValueError:
            qt_img = convert_cv_qt(image)
            self.ui.layout_crop.setGeometry(10, 80, image.shape[1], image.shape[0])
            self.ui.layout_crop.setPixmap(qt_img)
        except AttributeError:
            show_info_messagebox("Please select file")
        except TypeError:
            show_info_messagebox("Please create project file on home page")
        except FileExistsError:
            show_info_messagebox("Bir önceki dosya üzerine işlem yapılamaz, yeni dosya oluşturabilirsiniz")
        except IndexError:
            show_info_messagebox("ERROR")

    def crop_1(self):
        try:
            count = 0
            images_list = glob.glob(self.response + '/*.jpg')
            images_list2 = glob.glob(self.response + '/*.png')
            images_list.extend(images_list2)
            self.ui.progressBar_crop_2.setRange(0, len(images_list))
            os.mkdir(self.response2 + "/cropped")

            for file in images_list:
                name = file[:-4].split("\\")[-1]
                self.ui.progressBar_crop_2.setValue(count)
                image = cv2.imread(file)
                image_crop = image[int(self.ui.ymin_crop_text_2.text()):int(self.ui.ymax_crop_text_3.text()),
                                   int(self.ui.xmin_crop_text_2.text()):int(self.ui.xmax_crop_text_3.text())]
                cv2.imwrite(self.response2 + "/cropped/" + name + "_cropped" + ".jpg", image_crop)
                count += 1

            if count == len(images_list):
                self.ui.progressBar_crop_2.setValue(0)
                self.ui.info_resize_box.setText("İşlem Tamam " +
                                                str(len(images_list)) + " Resim Crop Edildi.")
                show_info_messagebox("İşlem Tamam " + str(len(images_list)) + " Resim Crop Edildi.")
        except ValueError:
            show_info_messagebox("Please write the width and height values")
        except AttributeError:
            show_info_messagebox("Please select file")
        except TypeError:
            show_info_messagebox("Please create project file on home page")
        except FileExistsError:
            show_info_messagebox("Bir önceki dosya üzerine işlem yapılamaz, yeni dosya oluşturabilirsiniz")
        except cv2.error:
            show_info_messagebox("hata")
        except IndexError:
            show_info_messagebox("ERROR")

    def rotate_1(self):
        try:
            count = 0
            images_list = glob.glob(self.response + '/*.jpg')
            images_list2 = glob.glob(self.response + '/*.png')
            images_list.extend(images_list2)
            self.ui.progressBar_rotate_3.setRange(0, len(images_list))
            os.mkdir(self.response2 + "/rotated")

            for file in images_list:
                name = file[:-4].split("\\")[-1]
                self.ui.progressBar_rotate_3.setValue(count)
                image = cv2.imread(file)
                (h, w) = image.shape[:2]
                (cX, cY) = (w // 2, h // 2)
                m = cv2.getRotationMatrix2D((cX, cY), int(self.ui.angle_rotate_text_3.text()), 1.0)
                rotated = cv2.warpAffine(image, m, (w, h))
                cv2.imwrite(self.response2 + "/rotated/" + name + "_rotated" + ".jpg", rotated)
                count += 1

                if count == len(images_list):
                    self.ui.progressBar_rotate_3.setValue(0)
                    self.ui.info_rotate_box_3.setText("İşlem Tamam " + str(len(images_list)) + " Resim Rotate Edildi.")
                    show_info_messagebox("İşlem Tamam " + str(len(images_list)) + " Resim Rotate Edildi.")
        except ValueError:
            show_info_messagebox("Please write the width and height values")
        except AttributeError:
            show_info_messagebox("Please select file")
        except TypeError:
            show_info_messagebox("Please create project file on home page")
        except FileExistsError:
            show_info_messagebox("Bir önceki dosya üzerine işlem yapılamaz, yeni dosya oluşturabilirsiniz")
        except cv2.error:
            show_info_messagebox("hata")
        except IndexError:
            show_info_messagebox("ERROR")

    def rotate_preview(self):
        global image, cX, cY, w, h
        try:
            images_list = glob.glob(self.response + '/*.jpg')
            images_list2 = glob.glob(self.response + '/*.png')
            images_list.extend(images_list2)
            rand_image_path = random.choice(images_list)
            image = cv2.imread(rand_image_path)
            (h, w) = image.shape[:2]
            (cX, cY) = (w // 2, h // 2)
            m = cv2.getRotationMatrix2D((cX, cY), int(self.ui.angle_rotate_text_3.text()), 1.0)
            rotated = cv2.warpAffine(image, m, (w, h))
            qt_img = convert_cv_qt(rotated)
            self.ui.layout_rotate.setGeometry(10, 80, rotated.shape[1], rotated.shape[0])
            self.ui.layout_rotate.setPixmap(qt_img)

        except ValueError:
            m = cv2.getRotationMatrix2D((cX, cY), 0, 1.0)
            rotated = cv2.warpAffine(image, m, (w, h))
            qt_img = convert_cv_qt(rotated)
            self.ui.layout_rotate.setGeometry(10, 80, rotated.shape[1], rotated.shape[0])
            self.ui.layout_rotate.setPixmap(qt_img)
        except AttributeError:
            show_info_messagebox("Please select file")
        except TypeError:
            show_info_messagebox("Please create project file on home page")
        except FileExistsError:
            show_info_messagebox("Bir önceki dosya üzerine işlem yapılamaz, yeni dosya oluşturabilirsiniz")
        except IndexError:
            show_info_messagebox("ERROR")

    def brig_preview(self):
        global image
        try:
            images_list = glob.glob(self.response + '/*.jpg')
            images_list2 = glob.glob(self.response + '/*.png')
            images_list.extend(images_list2)
            rand_image_path = random.choice(images_list)
            image = cv2.imread(rand_image_path)
            brig = increase_brightness(image, int(self.ui.brig_brig_text_4.text()))

            qt_img = convert_cv_qt(brig)
            self.ui.layout_brig.setGeometry(10, 80, brig.shape[1], brig.shape[0])
            self.ui.layout_brig.setPixmap(qt_img)
        except ValueError:
            brig = increase_brightness(image, 0)
            qt_img = convert_cv_qt(brig)
            self.ui.layout_brig.setGeometry(10, 80, brig.shape[1], brig.shape[0])
            self.ui.layout_brig.setPixmap(qt_img)

        except AttributeError:
            show_info_messagebox("Please select file")
        except TypeError:
            show_info_messagebox("Lürfen resim dosyası seçiniz")
        except FileExistsError:
            show_info_messagebox("Bir önceki dosya üzerine işlem yapılamaz, yeni dosya oluşturabilirsiniz")
        except IndexError:
            show_info_messagebox("ERROR")

    def brig_1(self):
        try:
            count = 0
            images_list = glob.glob(self.response + '/*.jpg')
            images_list2 = glob.glob(self.response + '/*.png')
            images_list.extend(images_list2)
            self.ui.progressBar_brig_4.setRange(0, len(images_list))
            os.mkdir(self.response2 + "/brighted")

            for file in images_list:
                name = file[:-4].split("\\")[-1]
                self.ui.progressBar_brig_4.setValue(count)
                image = cv2.imread(file)
                brig = increase_brightness(image, int(self.ui.brig_brig_text_4.text()))
                cv2.imwrite(self.response2 + "/brighted/" + name + "_brighted" + ".jpg", brig)
                count += 1

                if count == len(images_list):
                    self.ui.progressBar_brig_4.setValue(0)
                    self.ui.info_brig_box_4.setText("İşlem Tamam " + str(len(images_list)) + " Resim Rotate Edildi.")
                    show_info_messagebox("İşlem Tamam " + str(len(images_list)) + " Resim Brighted Edildi.")
        except ValueError:
            show_info_messagebox("Please write the width and height values")
        except AttributeError:
            show_info_messagebox("Please select file")
        except TypeError:
            show_info_messagebox("Please create project file on home page")
        except FileExistsError:
            show_info_messagebox("Bir önceki dosya üzerine işlem yapılamaz, yeni dosya oluşturabilirsiniz")
        except cv2.error:
            show_info_messagebox("hata")
        except IndexError:
            show_info_messagebox("ERROR")

    def train_test_seperator(self):
        try:
            images_list = glob.glob(self.response + '/*.jpg')
            images_list2 = glob.glob(self.response + '/*.png')
            images_list.extend(images_list2)

            img_list = []

            os.mkdir(self.response2 + "/train_app")
            os.mkdir(self.response2 + "/test_app")

            for filename in images_list:
                img_list.append(filename)
            print(self.path_name)
            train_dir = str(self.response2) + "/train_app"
            test_dir = str(self.response2) + "/test_app"

            print(" % i images found" % len(img_list))
            train_num = round(len(img_list) * self.train1/100)

            for i in range(train_num):
                file_number = random.randint(0, len(img_list) - 1)

                shutil.copy(img_list[file_number], train_dir)

                xml_file = img_list[file_number][:-4] + ".xml"
                txt_file = img_list[file_number][:-4] + ".txt"

                if os.path.isfile(xml_file):
                    shutil.copy(xml_file, train_dir)
                elif os.path.isfile(txt_file):
                    shutil.copy(txt_file, train_dir)

                img_list.remove(img_list[file_number])

            for i in range(len(img_list)):

                file_number = random.randint(0, len(img_list) - 1)

                shutil.copy(img_list[file_number], test_dir)

                xml_file = img_list[file_number][:-4] + ".xml"
                txt_file = img_list[file_number][:-4] + ".txt"
                if os.path.isfile(xml_file):
                    shutil.copy(xml_file, test_dir)
                elif os.path.isfile(txt_file):
                    shutil.copy(txt_file, test_dir)

                img_list.remove(img_list[file_number])

            show_info_messagebox("Process Completed")

        except ValueError:
            show_info_messagebox("ERROR")
        except AttributeError:
            show_info_messagebox("Please select file or value of train test")
        except TypeError:
            show_info_messagebox("Please select file or value of train test")
        except FileExistsError:
            show_info_messagebox("Exist file error please clear train_app and test_app file ")
        except IndexError:
            show_info_messagebox("ERROR")
        except cv2.error:
            show_info_messagebox("ERROR")

    def work_1(self):
        try:
            images_list = glob.glob(self.response + '/*.jpg')
            self.path = images_list[self.count]
            self.uploaded = cv2.imread(self.path)
            self.ui.verticalLayoutWidget_5.setGeometry(10, 80, self.uploaded.shape[1], self.uploaded.shape[0])

            qt_img = convert_cv_qt(self.uploaded)
            self.image.setPixmap(QPixmap(qt_img))
        except ValueError:
            show_info_messagebox("ERROR")
        except AttributeError:
            show_info_messagebox("ERROR")
        except TypeError:
            show_info_messagebox("ERROR")
        except FileExistsError:
            show_info_messagebox("ERROR")
        except cv2.error:
            show_info_messagebox("ERROR")
        except IndexError:
            show_info_messagebox("ERROR")

    def work_2(self):
        try:
            a = self.ui.ann_ann_text_5.text()
            val = (self.image.begin.x(), self.image.begin.y()), (self.image.end.x(), self.image.end.y())
            self.arr_val.append(val)
            self.arr_name.append(a)
            self.uploaded = cv2.imread(self.path)

            for i in range(len(self.arr_val)):

                self.ui.info_ann_box_13.setText(str(self.arr_name[i]))
                self.ui.info_ann_box_14.setText(str(self.arr_val[i][0])+str(self.arr_val[i][1]))

                self.ui.info_ann_box_15.setText(str(len(self.arr_val)))
                self.uploaded2 = cv2.rectangle(
                    img=self.uploaded,
                    pt1=self.arr_val[i][0],
                    pt2=self.arr_val[i][1],
                    color=(0, 0, 0),
                    thickness=1,
                    lineType=cv2.LINE_AA
                )

                self.uploaded2 = cv2.putText(
                    img=self.uploaded,
                    text=self.arr_name[i],
                    org=self.arr_val[i][0],
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.5,
                    color=(123, 0, 0),
                    thickness=1,
                    lineType=cv2.LINE_AA
                )

            qt_img = convert_cv_qt(self.uploaded2)
            self.image.setPixmap(QPixmap(qt_img))
        except ValueError:
            show_info_messagebox("ERROR")
        except AttributeError:
            show_info_messagebox("ERROR")
        except TypeError:
            show_info_messagebox("ERROR")
        except FileExistsError:
            show_info_messagebox("ERROR")
        except cv2.error:
            show_info_messagebox("ERROR")

    def work_3(self):
        try:
            self.arr_name.clear()
            self.arr_val.clear()
            self.image.setPixmap(QPixmap(self.path))
            self.ui.info_ann_box_13.setText(" ")
            self.ui.info_ann_box_14.setText(" ")
            self.ui.info_ann_box_15.setText(" ")
        except ValueError:
            show_info_messagebox("ERROR")
        except AttributeError:
            show_info_messagebox("ERROR")
        except TypeError:
            show_info_messagebox("ERROR")
        except FileExistsError:
            show_info_messagebox("ERROR")
        except cv2.error:
            show_info_messagebox("ERROR")

    def work_4(self):

        try:
            file = self.path[:-4] + ".xml"

            with open(file, 'w') as f:
                f.write('<annotation>\n')
                f.write('\t<folder>'+str(self.response)+'</folder>\n')
                f.write('\t<filename>' + self.path[:-4].split("\\")[-1] + '</filename>\n')
                f.write('\t<path>' + self.path + '</path>\n')
                f.write('\t<source>\n')
                f.write('\t\t<database>Unknown</database>\n')
                f.write('\t</source>\n')
                f.write('\t<size>\n')
                f.write('\t\t<width>' + str(self.uploaded.shape[0]) + '</width>\n')
                f.write('\t\t<height>' + str(self.uploaded.shape[1]) + '</height>\n')
                f.write('\t\t<depth>3</depth>\n')
                f.write('\t</size>\n')
                f.write('\t<segmented>0</segmented>\n')
                for i in range(len(self.arr_name)):
                    f.write('\t<object>\n')
                    f.write('\t\t<name>' + str(self.arr_name[i]) + '</name>\n')
                    f.write('\t\t<pose>Unspecified</pose>\n')
                    f.write('\t\t<truncated>0</truncated>\n')
                    f.write('\t\t<difficult>0</difficult>\n')
                    f.write('\t\t<bndbox>\n')
                    f.write('\t\t\t<xmin>' + str(self.arr_val[i][0][0]) + '</xmin>\n')
                    f.write('\t\t\t<ymin>' + str(self.arr_val[i][0][1]) + '</ymin>\n')
                    f.write('\t\t\t<xmax>' + str(self.arr_val[i][1][0]) + '</xmax>\n')
                    f.write('\t\t\t<ymax>' + str(self.arr_val[i][1][1]) + '</ymax>\n')
                    f.write('\t\t</bndbox>\n')
                    f.write('\t</object>\n')
                f.write('</annotation>\n')
                f.close()

            self.count = self.count + 1
            self.arr_name.clear()
            self.arr_val.clear()

        except ValueError:
            show_info_messagebox("ERROR")
        except AttributeError:
            show_info_messagebox("ERROR")
        except TypeError:
            show_info_messagebox("ERROR")
        except FileExistsError:
            show_info_messagebox("ERROR")
        except cv2.error:
            show_info_messagebox("ERROR")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
