""" #RULES :


# THIS SCRIPT HAS BEEN MADE FOR EDUCATION PURPOSE ONLY

# USE AT YOUR OWN RISK THIS SCRIPT, IT'S A SELFBOT AND IT'S BANNABLE BY DISCORD IF U REALLY WANNA USE IT, I RECOMMEND YOU USING IT ON A ALT ACCOUNT. 
# IT'S AGAISNT DISCORD TOS AND YOU CAN GET BANNED OR YOUR ACCOUNT CAN GET TERMINATED. 
# IF YOU RUN THE SCRIPT, YOU ASSUME THAT YOU READ THIS MESSAGES AND ACCEPT THAT __I'M NOT 
# RESPONSABLE IN ANY CASE FOR ANY DAMAGE CAUSED TO YOUR DISCORD ACCOUNT!__
# USE IT AT YOUR OWN RISK PLEASE. AND DON'T DM ME IF ANYTHING HAPPEND TO YOUR DISCORD ACCOUNT!!


# INFOS :

# IF YOU NEED ANY HELP, MAKE SURE TO JOIN THE DISCORD : https://discord.gg/hFFnWYjYE3

import config

# SETTINGS :

inf = 999999999999999

inf = {
    "inf" : inf
}

channel_id = 1103759996468080752 # the channel id u wanna send the msg to
delay = 120 # the delay between every msg its going to send IN SECONDS ( for example : if u put 120, it will send a msg to the channel id u selected every 120s)
message = "!!work" # put the msg u wanna say here
token = config.TOKEN # put ur token here
number = inf # remove 1 and put the number of msgs u wanna send here, put 9999999 or something like that if you wanna send infinite messages
inf = 999999999999999

# SCRIPT DONT TOUCH :


# imports
from asyncio import sleep
import requests
import time, keyboard
class Finish(Exception): pass
from datetime import datetime
currentDateAndTime = datetime.now()
currentTime = currentDateAndTime.strftime("%H:%M:%S")






#script

payload = {
    'content': 
    f"{message}"
}
header = {
    'authorization': f'{token}'
}

#print and send msg to api
print("Starting...")
print('Succesfully started at', currentTime)
print('Hold CTRL then press X to stop the script.')
try:
    for i in range(0,number):
        print("Sending msg", i,"...")
        r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=header)  
#to end the script with esc or when the numbers of msgs are sent
        for a in range(delay*10): 
            time.sleep(0.1)
            if keyboard.is_pressed('ctrl+x'):
                raise Finish 
    print("Sent all msgs")
except Finish:
    print("Stopped loop") """