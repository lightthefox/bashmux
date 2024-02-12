from getpass import getpass as hideinp
from os import system as sys
from time import sleep

def dotDotDot(time:int):
	td = time/3
	for i in range(3):
		sleep(td)
		print(".", end="", flush=True)
	sleep(td)

print("Select Yes on the following Prompt!")
sys("termux-setup-storage")
hideinp("Press the Enter Key to continue...")
sys("clear")


#Main Setup
print("IMPORTANT! WHEN YOU GET PROMPTED TO SELECT AN OPTION, ALWAYS SELECT YES!!!")
print("Type Understood (case-insensitive) to continue")
while input().lower() != "understood":
	sys("clear")
	print("IMPORTANT! WHEN YOU GET PROMPTED TO SELECT AN OPTION, ALWAYS SELECT YES!!!")
	print("Type Understood (case-insensitive) to continue")

print("Updating Packages...")
sys("pkg upgrade -y && pkg update -y && pkg upgrade -y")
dotDotDot(3)
sys("clear")
print("Installing Packages...")
sys("pkg install tmux openssl git neofetch cmatrix clang figlet")
sys("cp ./newbashrc ~/../usr/etc/bash.bashrc")

sys("clear")
print("To Setup Fonts, go to .termux and run fonts.sh")
