import requests
import hashlib
import time

# Replace the site URL and the webhook URL with your own
url = "Taget link"
webhook_url = "Webhook link" 

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
                "content": "Le site {} a été modifié ! <@260491691163779072>".format(url)
            }
            requests.post(webhook_url, json=data)
            # Sends a message to your terminal
            print("Site modifié !")

            # Updates the value of the previous_hash variable
            previous_hash = hash

        # Wait 30 seconds before checking the site again
        time.sleep(30)

check_website_update(url, webhook_url)
