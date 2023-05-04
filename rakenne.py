# include <iostream>
import random
from json import dumps, load
from time import localtime, sleep
from time import time as tm

from httplib2 import Http


# Define a function that sends message to chat and takes a message as an argument.
def sendMessage(message: str):
    # Get webhook url
    with open("URL.json", "r", encoding="utf-8") as f:
        url = load(f["URL"])

    bot_message = {"text": message}

    message_headers = {"Content-Type": "application/json; charset=UTF8"}

    http_obj = Http()

    response = http_obj.request(
        uri=url, method="POST", headers=message_headers, body=dumps(bot_message)
    )

    print(response)


def main():
    # set seed for choice
    random.seed = tm()

    # Take info from user when class ends.
    time_end = int(input("Enter the ending time in hrs: ")) * 60 + int(
        input("Enter the ending time in mins: ")
    )
    next_msg_at = localtime()[3] * 60 + localtime()[4]
    next_msg_at -= localtime()[4] % 5 - 5

    # Open lauseet.json
    with open("lauseet.json", "r", encoding="utf-8") as f:
        lauseet = load(f)

    msg = list(lauseet["välilauseet"])
    last_msg = list(lauseet["loppulauseet"])

    # Loop sends a message to chat every 5 minutes.
    # Ends at the set time after sending a last message.

    try:
        running = True
        while running:
            # Get the current time in minutes.
            time = localtime()[3] * 60 + localtime()[4]

            if time == time_end:
                if localtime()[6] == 4 and time == 914:
                    sendMessage(
                        "Hyvää yötä, Jeesus myötä, kiitos tästä päivästä\nSE, OLI, KIVA"
                    )
                    running = False
                    print("END!!!")
                    pass
                sendMessage(random.choice(last_msg))
                print("End")
                running = False

            elif time == next_msg_at:
                sendMessage(random.choice(msg).format(time_end - time))
                print(f"Left{time_end - time}")
                next_msg_at += 5

            else:
                # wait half the time until next message and f up the whole thing and don't fix it.
                sleep(next_msg_at - time)
    except KeyboardInterrupt:
        print("Exiting")
        running = False


if __name__ == "__main__":
    print("Running...")
    main()
