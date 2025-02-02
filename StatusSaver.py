#!/data/data/com.termux/files/usr/bin/python
from glob import glob
import os
from time import sleep
import datetime
from tqdm import tqdm

class Status:
    banner = '''
        ░██████╗ ████████╗ ░█████╗░ ████████╗ ██╗░░░██╗ ░██████╗
        ██╔════╝ ╚══██╔══╝ ██╔══██╗ ╚══██╔══╝ ██║░░░██║ ██╔════╝
        ╚█████╗░ ░░░██║░░░ ███████║ ░░░██║░░░ ██║░░░██║ ╚█████╗░
        ░╚═══██╗ ░░░██║░░░ ██╔══██║ ░░░██║░░░ ██║░░░██║ ░╚═══██╗
        ██████╔╝ ░░░██║░░░ ██║░░██║ ░░░██║░░░ ╚██████╔╝ ██████╔╝
        ╚═════╝░ ░░░╚═╝░░░ ╚═╝░░╚═╝ ░░░╚═╝░░░ ░╚═════╝░ ╚═════╝░ 

        ░██████╗ ░█████╗░ ██╗░░░██╗ ███████╗ ██████╗░
        ██╔════╝ ██╔══██╗ ██║░░░██║ ██╔════╝ ██╔══██╗
        ╚█████╗░ ███████║ ╚██╗░██╔╝ █████╗░░ ██████╔╝
        ░╚═══██╗ ██╔══██║ ░╚████╔╝░ ██╔══╝░░ ██╔══██╗
        ██████╔╝ ██║░░██║ ░░╚██╔╝░░ ███████╗ ██║░░██║
        ╚═════╝░ ╚═╝░░╚═╝ ░░░╚═╝░░░ ╚══════╝ ╚═╝░░╚═╝
        '''

    def __init__(self):
        self.ANDROID = glob("/storage/emulated/0/*")
        self.PICS = "/storage/emulated/0/Statuses/Pics"
        self.VIDS = "/storage/emulated/0/Statuses/Videos"
        self.videos = glob('/storage/emulated/0/Android/media/com.whatsapp/Whatsapp/Media/.Statuses/*.mp4')
        self.pics = glob('/storage/emulated/0/Android/media/com.whatsapp/Whatsapp/Media/.Statuses/*.jpg')
    
    def check_folders(self):
        self.__init__()
        if "/storage/emulated/0/Statuses" in self.ANDROID:
            print("Statuses folder Exists")
        else:
            print("Making Statuses Folder")
            os.makedirs("/sdcard/Statuses")
            os.makedirs("/sdcard/Statuses/Pics")
            os.makedirs("/sdcard/Statuses/Videos")
    def save_pics(self):
	    for i in tqdm(self.pics):
	    	date_made = datetime.datetime.fromtimestamp(os.path.getmtime(i))
	    	extension = os.path.splitext(i)[1]
	    	new_name = f"{date_made.strftime("%Y-%m-%d %H:%M:%S")}{extension}"
	    	new_file_path = os.path.join(self.PICS, new_name)
	    	with open(i, 'rb') as f:
	    		picture = f.read()
	    	with open(new_file_path, "wb") as f:
	    		f.write(picture)
    def save_video(self):
        for i in tqdm(self.videos):
            date_made = datetime.datetime.fromtimestamp(os.path.getmtime(i))
            extension = os.path.splitext(i)[1]
            new_name = f"{date_made.strftime("%Y-%m-%d %H:%M:%S")}{extension}"
            new_file_path = os.path.join(self.VIDS, new_name)
            with open(i, 'rb') as f:
            	video = f.read()
            with open(new_file_path, "wb") as f:
            	f.write(video)

    def save_both(self):
        all_ = tqdm(self.videos + self.pics)
        for i in all_:
        	date_made = datetime.datetime.fromtimestamp(os.path.getmtime(i))
        	extension = os.path.splitext(i)[1]
        	new_name = f"{date_made.strftime("%Y-%m-%d %H:%M:%S")}{extension}"
        	if extension == ".mp4":
        		new_file_path = os.path.join(self.VIDS, new_name)
        	elif extension == ".jpg":
        		new_file_path = os.path.join(self.PICS, new_name)
        	with open(i, 'rb') as f:
        		file = f.read()
        	with open(new_file_path, "wb") as f:
        		f.write(file)
    def delete_old(self):
		pass
		# TODO: implement this method
	    # _old = 7
	    # for i in tqdm(self.videos + self.pics):
		#     if datetime.datetime.now().strftime("%Y-%m-%d") - datetime.datetime.fromtimestamp(os.path.getmtime(i)).strftime("%Y-%m-%d") >= _old:
		# 	    print("Old")


def main():
    os.system("clear")
    print(Status.banner)
    print("Choose What Statuses to save:")
    print("1. Pictures")
    print("2. Videos")
    print("3. Both")
    print("4. Exit")
    global choice 
    Status().check_folders()
    choice = input('Enter choice: ')
    while True:
        if choice == '1':
            Status().save_pics()
            break
        elif choice == '2':
            Status().save_video()
            break
        elif choice == '3':
            Status().save_both()
            break
        elif choice == '4':
            exit("Thank you for using Status Saver!")
        else:
            print("Invalid Input!!")



if __name__ == "__main__":
    main()