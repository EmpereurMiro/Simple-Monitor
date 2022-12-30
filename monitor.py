import requests
import hashlib
import time
import os
from pystyle import Write, Colors, Colorate, Center

banner = """



                                     ███╗   ███╗ ██████╗ ███╗   ██╗██╗████████╗ ██████╗ ██████╗ 
                                     ████╗ ████║██╔═══██╗████╗  ██║██║╚══██╔══╝██╔═══██╗██╔══██╗
                                     ██╔████╔██║██║   ██║██╔██╗ ██║██║   ██║   ██║   ██║██████╔╝
                                     ██║╚██╔╝██║██║   ██║██║╚██╗██║██║   ██║   ██║   ██║██╔══██╗
                                     ██║ ╚═╝ ██║╚██████╔╝██║ ╚████║██║   ██║   ╚██████╔╝██║  ██║
                                     ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                         
                                                          by t.me/EmpereurMiro



"""

# Start of program


os.system("mode 130,40")
os.system("title Simple Monitor / t.me/EmpereurMiro")
os.system("cls")

print(Center.XCenter(Colorate.Vertical(Colors.green_to_yellow, banner, 1)))

url = Write.Input("[?] Target URL >>> ", Colors.green_to_yellow, interval=0.0025)
webhook_url = "Webhook Link" 
time.sleep(1.2)
os.system("cls")
    


def check_website_update(url, webhook_url):
    response = requests.get(url)
    html = response.text

    # Calculates the hash of the HTML content
    hash = hashlib.sha256(html.encode('utf-8')).hexdigest()

    # Stores the hash in a variable
    previous_hash = hash

    while True:
        # Retrieves the HTML content of the site again
        response = requests.get(url)
        html = response.text

        # Recalculates the hash of the HTML content
        hash = hashlib.sha256(html.encode('utf-8')).hexdigest()

        # If the hash has changed, it means that the site has been modified
        if hash != previous_hash:
            # Send a notification to the Discord webhook
            data = {
                "content": "Le site {} a été modifié !".format(url)
            }
            requests.post(webhook_url, json=data)
            # Sends a message to your terminal
            print("[!] Site modifié")

            # Updates the value of the previous_hash variable
            previous_hash = hash

        # Wait 30 seconds before checking the site again
        time.sleep(30)

check_website_update(url, webhook_url)
