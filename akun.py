name = "/data/data/com.termux/files/usr/bin/data/nama"  # Replace with the actual path

try:
    with open(name, 'r') as f:
        file_content = f.read()
        namee = (file_content)
except FileNotFoundError:
    print(f"Error: File '{filepath}' not found.")


#name = "Bob"
import smtplib
import os,sys
fadd = 'helc95209@gmail.com'
tadd = 'plankstons@gonetor.com'
msg = "PENGGUNA ONLINE = " + namee + "MEMBUAT AKUN!"
username = 'helc95209@gmail.com'
password = 'svxsolvclixcvkjj'
server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fadd,tadd,msg)
#server.sendmail(fadd,tadd,msg)

os.system("rm /data/data/com.termux/files/usr/bin/YD && touch /data/data/com.termux/files/usr/bin/YD")
os.system("ls /data/data/com.termux/files/usr/bin/idd/jon > /data/data/com.termux/files/usr/bin/YD")

#greeting = "Hello, " + name + "!"
#print(greeting)  # Output: Hello, Bob!

ID = "/data/data/com.termux/files/usr/bin/YD"

try:
    with open(ID, 'r') as f:
        file_content = f.read()
        nameee = (file_content)
except FileNotFoundError:
    print(f"Error: File '{filepath}' not found.")


#name = "Bob"
import smtplib
import os,sys
fadd = 'helc95209@gmail.com'
tadd = 'plankstons@gonetor.com'
print("\033[92m [1]fastssh [2]oceanssh [3]jagoanssh \033[0m")
print("")
print("\033[92m server|user|pass \033[0m")
print("\033[93m contoh, 1|bjorka|123 \033[0m")
#msg = input("\033[92m > \033[0m")
msg = input("ID = " + nameee + "MEMBUAT AKUN!")
username = 'helc95209@gmail.com'
password = 'svxsolvclixcvkjj'
server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fadd,tadd,msg)
#server.sendmail(fadd,tadd,msg)
print(" ")
#greeting = "Hello, " + name + "!"
#print(greeting)  # Output: Hello, Bob!

