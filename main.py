import os  # accessing the os functions
import check_camera
import Capture_Image
import Train_Image
import Recognize


# creating the title bar function

def title_bar():
    os.system('cls')  # for windows

    # title of the program

    print("\t**********************************************")
    print("\t***** He Thong Diem Danh Khuon Mat *****")
    print("\t**********************************************")


# creating the user main menu function

def mainMenu():
    title_bar()
    print()
    print(10 * "*", "XIN CHAO CAC BAN", 10 * "*")
    print("[1] Kiem tra camera")
    print("[2] Chup anh khuon mat")
    print("[3] Train Mo Hinh")
    print("[4] Nhan Dien Va Diem Danh")
    # print("[5] Auto Mail")
    print("[6] Thoat")

    while True:
        try:
            choice = int(input("Nhap vao lua chon cua ban: "))

            if choice == 1:
                checkCamera()
                break
            elif choice == 2:
                CaptureFaces()
                break
            elif choice == 3:
                Trainimages()
                break
            elif choice == 4:
                RecognizeFaces()
                break
            # elif choice == 5:
            #     os.system("py automail.py")
            #     break
            #     mainMenu()
            elif choice == 6:
                print("Thank You")
                break
            else:
                print("Nhap sai hay nhap tu 1-4")
                mainMenu()
        except ValueError:
            print("Nhap sai  Enter 1-4\n thu lai")
    exit


# ---------------------------------------------------------
# calling the camera test function from check camera.py file

def checkCamera():
    check_camera.camer()
    key = input("Nhap phim bat ky de tro lai main menu")
    mainMenu()


# --------------------------------------------------------------
# calling the take image function form capture image.py file

def CaptureFaces():
    Capture_Image.takeImages()
    key = input("Nhap phim bat ky de tro lai main menu")
    mainMenu()


# -----------------------------------------------------------------
# calling the train images from train_images.py file

def Trainimages():
    Train_Image.TrainImages()
    key = input("Nhap phim bat ky de tro lai main menu")
    mainMenu()


# --------------------------------------------------------------------
# calling the recognize_attendance from recognize.py file

def RecognizeFaces():
    Recognize.recognize_attendence()
    key = input("Nhap phim bat ky de tro lai main menu")
    mainMenu()


# ---------------main driver ------------------
mainMenu()
