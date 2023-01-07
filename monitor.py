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

    hash = hashlib.sha256(html.encode('utf-8')).hexdigest()
    previous_hash = hash

    while True:
        response = requests.get(url)
        html = response.text

        hash = hashlib.sha256(html.encode('utf-8')).hexdigest()
        if hash != previous_hash:
            data = {
                "content": "Le site {} a été modifié !".format(url)
            }
            requests.post(webhook_url, json=data)
            print("[!] Site modifié")

            previous_hash = hash

        time.sleep(30)

check_website_update(url, webhook_url)
