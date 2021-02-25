import os

os.system("clear")
os.system("apt-get figlet")
os.system("figlet PORT SCAN")

print("""

WELCOME TO PORT SCAN 

1)Port Scan




	""")

islemno = raw_input("Enter Number")

if(islemno==1)
        hedefip = raw_input("Enter Target IP")
        os.system("nmap" + hedefip)