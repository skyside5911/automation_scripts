from wath_package import WhatsApp
import time
import os

if __name__ == "__main__":

    Script_path = os.getcwd()
    ###################### number file path #######################
    PathSlash = "\\"
    Number_file = Script_path + PathSlash + "numbers.csv"

    messenger = WhatsApp()
    ##################### read file ########################
    N_file = open(Number_file,'r')
    N_read = N_file.readlines()

    for number in N_read:
        find_num = number.replace("\n",'')
        if len(find_num) == 10:
            messenger.find_user(find_num)
            messenger.send_message("hello vicky bhai kaise ho tum")
            # messenger.send_file('path-to-file') # send file with this function
            # messenger.send_picture('path-to-file') # send file with this function 
            time.sleep(5)
            print("send message successfuly to ",find_num) 
        else:
            print("Number is worng = ",find_num)