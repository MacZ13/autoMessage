import config
import requests
import time
import keyboard
from datetime import datetime

class Finish(Exception):
    pass

def send_message(channel_id, token, message):
    payload = {
        'content': message
    }
    header = {
        'authorization': token
    }
    response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=header)
    return response

def main():
    channel_id = 1026909109745877052  # the channel id u wanna send the msg to
    delay = 120  # the delay between every msg its going to send IN SECONDS
    message = "!!work"  # put the msg u wanna say here
    token = config.TOKEN  # put ur token here

    current_time = datetime.now().strftime("%H:%M:%S")
    print("Starting...")
    print('Successfully started at', current_time)
    print('Hold CTRL then press X to stop the script.')

    try:
        i = 0
        while True:
            print("Sending msg", i, "...")
            response = send_message(channel_id, token, message)
            if response.status_code == 200:
                print("Message sent successfully")
            else:
                print("Failed to send message")

            for a in range(delay):
                time.sleep(1)
                if keyboard.is_pressed('ctrl+x'):
                    raise Finish
            i += 1
        print("Sent all msgs")
    except Finish:
        print("Stopped loop")

if __name__ == '__main__':
    main()
