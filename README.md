### <p align="center"> Simple Monitor </p>
  
-----
<p align="center"><img src="https://i.imgur.com/CUGFuQU.jpg"></p>

-----

<center> 
  
<br><br>
  * The program uses the `requests` module to retrieve the HTML content <br>of a website and the `hashlib` module's hashing function to calculate a hash <br>of the HTML content.
* It uses an infinite loop that executes the check every `30 seconds` <br>(you can adjust this value to your needs) and compares the current hash of the <br>HTML content with the previously recorded hash.
* If the hash has changed, it means the website has been modified <br>and the program sends a `Discord notification` using the requests module <br>and the URL of a Discord webhook. If the hash is identical, <br>the program waits 60 seconds before checking the website again.
  
<br>
Source code of the file avaiable
<br><br><br>
<img src="https://i.imgur.com/jR26XzQ.png" width="80%">
</center>
<br>

-----

### <p align="center">📁 Dependencies 📁</p><br>

<p align="center"><strong><i>In order for the program to work, you have to install these ressources:</i></strong</p>

<br><br>
* <a href="https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe">Python3</a>
* run setup.bat in the folder
<br><br>

-----

### <p align="center">🔌 Utilisation 🔌</p><br>
  
* Edit the `monitor.py` file to change the line 34 to put your webhook in the `webhook_url="link"`
* Launch the file with the cmd `python monitor.py`
<br>
  
-----

### <p align="center">📌 Disclaimer 📌</p><br>

<br><br>
* ***Please use this program only for educational purposes.***
* ***It is not meant to be used in any malicious way, and I decline any responsibility for what you do with it.***
<br><br>

-----

  ### <p align="center">Empereur Miro</p> <br>

  ###### <p align="center">thank to `billythegoat356` for pystyle & the README.md</p>
