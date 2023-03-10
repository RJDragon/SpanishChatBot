import re
import nltk
nltk.download_package('stopwords')
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from .rogersES import RogersES

import random

# attribute class for handling values 
# class Attribute:
#     def __init__(self):
#         self.state = 0
#         self.value = ""

# # vacation class fitting all data of the person
# class Vacation:
#     def __init__(self):
#         self.activity = Attribute()
#         self.place = Attribute()
#         self.date = Attribute()
#         self.weather = Attribute()

class Bot:

    name = 'Spanish Bot'
    avatar = 'avatar/SpanishFlag.png'

    studentVacation = Vacation()

    def __init__(self):
        self.rogersES = RogersES()

        self.case = "Return" # found keyword
        self.studentInput = "???" # input from student

    def welcome(self):
        greetings = ['Hola,', 'Buenos días,', 'Buenas tardes,', 'Buenas noches,']
        return random.choice(greetings) + ' ' + self.name + '! ¿Cómo estás?'

    # TO DO find list in text with keys?
    def foundKeys(self, keys, text, list):
        """
        searches for a list keys in a text (string) and in the corresponding list of words
        two cases: key is a word: it must appear surrounded by blanks
        or key contains spaces: it doesn't matter, as long as it appears
        """
        for c in keys :
            if " " in c and c in text:
                return True
            elif c in list:
                return True
        return False

    # chat - all work is done here
    def chat(self, last_user_message, session):
        # to do list

        # 1. preprocessing (done)
        # preprocessing of student input
        self.studentInput = last_user_message.strip()
        inputProper = self.preprocess_input(last_user_message)
        #return inputProper
        inputSplit = inputProper.split()
        #return inputSplit

        # 2. check for input from user and if empty start timer for new question
        if len(inputSplit) == 0:
           self.case = "Vacío"

        # 3. check if input is a question:
        elif self.studentInput[-1] == "?":
            self.case = "Question"

        # 4. search for keywords in input/split words
        for name in self.rogersES.keywords.keys():
            #return self.rogersES.keywords.keys()
            if self.foundKeys(self.rogersES.keywords[name], inputProper, inputSplit):
                self.case = name 

        # 5. after everything end this function with the response function

        return self.response()

    # response
    def response(self):

        if self.case == "Question":
            return "This was a question!"

        if self.case == "Actividad":
            if self.studentVacation.activity.state == 1:
                return "Hablamos de su actividad"
            if self.studentVacation.activity.state == 0:
                self.studentVacation.activity.state = 1    

        if self.case == "Ubicación":
            if self.studentVacation.place.state == 1:
                return "Ya hemos hablado de su destino de vacaciones. Hablemos de otros temas relacionados con sus vacaciones"
            if self.studentVacation.place.state == 0:
                self.studentVacation.place.state = 1

        if self.case == "Fecha":
            if self.studentVacation.date.state == 1:
                return "El período ya se conoce"
            if self.studentVacation.date.state == 0:
                self.studentVacation.date.state = 1

        if self.case == "Tiempo":
            if self.studentVacation.weather.state == 1:
                return "El tiempo ya se conoce"
            if self.studentVacation.weather.state == 0:
                self.studentVacation.weather.state = 1

        #return self.case
        response = self.chooseResponse(self.case, 0)
        return response

    def preprocess_input(self, input_str):
        # Convert the input string to lowercase
        input_str = input_str.lower()

        # Remove any leading or trailing white space
        input_str = input_str.strip()

        # Remove any punctuation
        input_str = re.sub(r'[^\w\s]', '', input_str)

        # Tokenize the input string
        tokens = nltk.word_tokenize(input_str)

        # Remove any stop words
        spanish_stop_words = stopwords.words('spanish')
        tokens = [token for token in tokens if token not in spanish_stop_words]

        # Perform stemming
        stemmer = SnowballStemmer("spanish")
        tokens = [stemmer.stem(token) for token in tokens]

        # Rejoin the tokens into a single string
        input_str = " ".join(tokens)

        return input_str

    # theoretisch eine Funktion zur Random Auswahl an Antwortmöglichkeiten zu einem spezifischen case
    # in Elize werden allerdings alte Antworten aussortiert, damit Antworten sich nicht wiederholen
    # erstmal nicht implementiert
    def chooseResponse(self, currentcase, currentmemory):
        listLocalResponse = self.rogersES.answers[currentcase][:]
        response = random.choice(listLocalResponse) # choose randomly an answer
        return response