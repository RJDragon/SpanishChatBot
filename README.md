
# Chatbot Framework for Cognitive Science Seminar "Schreiben im Fremdsprachenunterricht Französisch und Spanisch"

Universität Osnabrück, Wintersemester 2022/2023

## Installation

The framework uses Python >= 3.8 and Django.


## Licence

The Code is distributed under a GPL V3 licence.

It contains code from others:
- the french Eliza chatbot in the bots/freliza folder is derived from https://elizia.net/cerveau/ (GPL V3)
- the french lexicon in he data folder is also taken from https://elizia.net/cerveau/ (GPL V3)
- 


## Chatbot
Chatbot Schreiben im Fremdsprachenunterricht Französisch/Spanisch (WiSe 2022/23)

Here are the steps for installing and running the server for the first time (for detailed instructions, see below) :
- Download the Python interpreter from https://python.org
- Open the downloaded file to install it. On Windows, make sure that "Add Python to PATH" is checked.
- Download Visual Studio Code from https://code.visualstudio.com/Download
- Install it by opening the downloaded file
- Start Visual Studio Code and click on the "source control" icon in the left icon bar and click on "Clone Repository"
- Enter https://github.com/tthelen/chatbot_sem22.git and press enter
- Select a folder on your computer where the ipaca code will be stored.
- Click on "Open" to open the cloned repository.
- Open a terminal from the "Terminal" menu.
- Enter python -m venv venv (exactly like this! Spaces are important and the commands are case sensitive) in the terminal to create a virtual python environment.
- On Windows, enter venv\scripts\activate in the terminal to activate the environment (MacOS/Linux: source venv/bin/activate)
- Install additional Python libraries with the command pip install -r requirements.txt
- Create the database by entering python manage.py migrate
- Create example lessons with python manage.py createsuperuser
- Start the server with python manage.py runserver
- Open a browser and enter the address http://127.0.0.1:8000 or Ctrl-Click on the address in the terminal
- To stop the server, follow the instructions in the terminal or close Visual Studio Code

- To update and run the chatbot code afterward, perform these steps every time after starting Visual Studio Code:
- To update the code, click on the source control icon on the three-dot menu and choose "Pull".
- Open the terminal and activate the virtural Python environment (Windows: venv\scripts\activate and MacOS/Linux: source venv/bin/activate)
- Start the server with python manage.py runserver
- Open a browser and enter the address http://127.0.0.1:8000 or Ctrl-Click on the address in the terminal
- To stop the server, follow the instructions in the terminal or close Visual Studio Code