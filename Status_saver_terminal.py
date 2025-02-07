#!/data/data/com.termux/files/usr/bin/python
from glob import glob
from Status import Status
from time import sleep
import datetime
from tqdm import tqdm
import os
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

def main():
    os.system("clear")
    print(banner)
    print("Choose What Statuses to save:")
    print("1. Pictures")
    print("2. Videos")
    print("3. Both")
    print("4. Exit")
    global choice 
    n = 1
    while n:
        choice = input('Enter choice: ')
        if choice == '1':
            print('Saving Pics')
            for i in tqdm(glob('/sdcard/Android/media/com.whatsapp/WhatsApp/Media/.Statuses/*jpg')):
                Status('pics', i)     
            n = 0
        elif choice == '2':
            print('Saving videos')
            Status().save_video()
            n = 0
        elif choice == '3':
            print('Saving all')
            Status().save_both()
            n = 0
        elif choice == '4':
            exit('Thank you for using Status saver')
        else:
            print("Invalid Input!!")
            continue
    else:
        print('Thank you for Using status saver')
        if input('Save sth else? y/n > ').lower() == 'y':
            main()

if __name__ == "__main__":
    main()
