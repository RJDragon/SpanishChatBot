from .rogersES import RogersES
from .rogersESvac import RogersESvac
from .swearWords import SwearES

from translate import Translator


#from googletrans import Translator

import random

# who am I kidding nltk doesnt like me
# # nltk take 2; translating
# from nltk.translate import AlignedSent, Alignment, IBMModel1
# # downloading necessary data
# nltk.download('comtrans')
# from nltk.corpus import comtrans



# globals
# ytu = False
# attribute class for handling values 
class Attribute:
    def __init__(self):
        self.state = 0
        self.value = ""

# vacation class fitting all data of the person
class Vacation:
    def __init__(self):
        # small talk
        self.hello = Attribute()
        self.hru = Attribute()
        self.name = Attribute()
        self.residence = Attribute()
        # vacation talk
        self.vacation = Attribute()
        self.activity = Attribute()
        self.place = Attribute()
        self.date = Attribute()
        self.weather = Attribute()
        self.transporte = Attribute()
        self.exp = Attribute()
        self.special = Attribute()
        self.company = Attribute()
        # fin
        self.end = Attribute()
        self.sorry = Attribute()

# preprocess_input checken. Der macht die Wörter zum Teil kaputt. Sätze noch nicht getetest

class Bot:

    name = 'SpanishBot'
    avatar = 'avatar/SpanishFlag.png'

    studentVacation = Vacation()

    def __init__(self):
        self.rogersES = RogersES()
        self.rogersESvac = RogersESvac()
        self.swearWords = SwearES()
        

        self.smallCase = "" # found small talk keyword
        self.vacationCase = "" # found vacation keyword 
        self.swearCase = ""
        self.question = False
        self.initializing = True
        self.studentInput = "???" # input from student
        self.secondAnswer = False

        self.ytu = False
        self.talkingVac = False
        self.justHola = False

        #self.sorry = 0
        self.session = None # copied from Eliza doesnt hurt even if I dont use sessions lateR?


    # needs work. there is no name yet, also random choice doenst really makes sense considering time of day
    def welcome(self):
        greetings = ["Hola :)", "Buenos días ^^"]
        return random.choice(greetings) + ' ¿Cómo estás?'

    # TO DO find list in text with keys? ### I dont quite get it, comes from eliza
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
       
       
        inputNotPrep = self.studentInput
        # inputProper = self.preprocess_input(last_user_message)
        #return inputProper
        inputSplit = inputNotPrep.split()
        #inputSplit = inputProper.split()
        #return inputSplit

        #2 vocabulary work
        if "¿Cómo se llama" in inputNotPrep:
            inputSplit.remove("¿Cómo")
            inputSplit.remove("se")
            inputSplit.remove("llama")
            inputSplit.remove("en")
            inputSplit.remove("Español?")
            inputSplit = " ".join(inputSplit)
            translator= Translator(to_lang="es", from_lang="de")
            return "En Español se dice <<" + translator.translate(inputSplit) + ">>"

            
            #return inputSplit

        # 3. check if input is a question:
        if self.studentInput[-1] == "?":
            self.question = True
        if self.studentInput[0] == "¿":
            self.question = True
        ## this means later on I have two cases? question and answer/remarks?

        # swear word detection
        # detect_swear_words(self, inputNotPrep)
        for name in self.swearWords.keywords.keys():
            if self.foundKeys(self.swearWords.keywords[name], inputNotPrep, inputSplit):
                self.swearCase = name

        # 4.1 search for SMALL TLAK keywords in input/split words
        for name in self.rogersES.keywords.keys():
            if self.foundKeys(self.rogersES.keywords[name], inputNotPrep, inputSplit):
                self.smallCase = name
            #return self.rogersES.keywords.keys()
            # same thing aBOVE BUT TRIED WITH PREPOCESSING
            # if self.foundKeys(self.rogersES.keywords[name], inputProper, inputSplit):
            #     self.case = name
        #4.2 search for VACATION keywords in input
        for name in self.rogersESvac.keywords.keys():
            if self.foundKeys(self.rogersESvac.keywords[name], inputNotPrep, inputSplit):
                self.vacationCase = name
        # 5. after everything end this function with the response function

       

        # checking if Vacaniones was used to initialize the topic or just mentioned in other context
        if self.vacationCase == "Ubicación":
            if "vacaciones" in inputSplit:
                inputSplit.remove("vacaciones")
                self.vacationCase = "Initializing"
                for name in self.rogersESvac.keywords.keys():
                    if self.foundKeys(self.rogersESvac.keywords[name], inputNotPrep, inputSplit):
                        self.vacationCase = name
                if self.vacationCase == "Initializing":
                    self.vacationCase = "Ubicación"
        
        
        # ytu

        # gpt ytu lösung:
        if any(substring in inputNotPrep for substring in ["y tu", "y tù", "y tù?", "y tu?"]):
            self.ytu = True
            self.question = True
        # if "y tu" in inputNotPrep: #or "y tù" in inputNotPrep or "y tù?" in inputNotPrep or "y tu?":
        #     self.ytu = True
        #     self.question = True
        # only hola
        if "hola" in inputSplit or "Hola" in inputSplit or "hola!" in inputSplit or "Hola!" in inputSplit:
            self.justHola = True
        # gpt hola lösung
        # if any(substring in inputSplit.lower() for substring in ["hola", "hola!"]):
        #     self.justHola = True
        # if "Hola" or "hola" or "Hola," or "hola," or "holaa" or "Holaa" or "hola!" or "Hola!" or "¡Hola!" or "¡hola!" in inputSplit:
        #     self.smallCase = "Hola"
        # else:
        #     self.smallCase = ""

        #print(self.smallCase)
        return self.response()

    # response
    def response(self):

        response = ""

        # if self.case == "Question":
        #     self.question = True
        #     # return "This was a question!"
        
        # small talk
        # if self.smallCase == "Saludo":
        #     if self.studentVacation.hello.state == 1:
        #         return "Hola de nuevo"
        #     if self.studentVacation.hello.state == 0:
        #         self.studentVacation.hello.state = 1 
        
        if self.smallCase == "Como estas":
            if self.studentVacation.hru.state == 1:
                return "Todavía bien"
            if self.studentVacation.hru.state == 0:
                self.studentVacation.hru.state = 1 

        if self.smallCase == "Nombre":
            if self.studentVacation.name.state == 1:
                return "Ya te dije mi nombre"
            if self.studentVacation.name.state == 0:
                self.studentVacation.name.state = 1
                #self.talkingVac = True

        if self.smallCase == "Residencia":
            
            if self.studentVacation.residence.state == 1:
                self.talkingVac = True
                return "Creo que mencioné donde vivo"
            if self.studentVacation.residence.state == 0:
                self.studentVacation.residence.state = 1 

        # vacation talk
        if self.vacationCase == "Vacaciones":
            self.talkingVac = True
            if self.studentVacation.vacation.state == 1:
                return "¿De nuevo?"   
            if self.studentVacation.vacation.state == 0:
                self.studentVacation.vacation.state = 1  

        if self.vacationCase == "Ubicación":
            self.talkingVac = True
            if self.studentVacation.place.state == 2:
                return "Ya hemos hablado de su destino de vacaciones. Hablemos de otros temas relacionados con sus vacaciones"
            if self.studentVacation.place.state == 1:
                self.secondAnswer = True
                self.studentVacation.place.state = 2
            if self.studentVacation.place.state == 0:
                self.studentVacation.place.state = 1
        
        if self.vacationCase == "Transporte":
            self.talkingVac = True
            if self.studentVacation.transporte.state == 2:
                return "Hablamos de su transporte"
            if self.studentVacation.transporte.state == 1:
                self.secondAnswer = True
                self.studentVacation.transporte.state = 2
            if self.studentVacation.transporte.state == 0:
                self.studentVacation.transporte.state = 1

        if self.vacationCase == "Fecha":
            self.talkingVac = True
            if self.studentVacation.date.state == 2:
                return "El período ya se conoce"
            if self.studentVacation.date.state == 1:
                self.secondAnswer = True
                self.studentVacation.date.state = 2
            if self.studentVacation.date.state == 0:
                self.studentVacation.date.state = 1
        
        if self.vacationCase == "Compañía":
            self.talkingVac = True
            if self.studentVacation.company.state == 2:
                return "Hablemos de otra cosa además del acompañamiento"
            if self.studentVacation.company.state == 1:
                self.secondAnswer = True
                self.studentVacation.company.state = 2
            if self.studentVacation.company.state == 0:
                self.studentVacation.company.state == 1

        if self.vacationCase == "Tiempo":
            self.talkingVac = True
            if self.studentVacation.weather.state == 2:
                return "El tiempo ya se conoce"
            if self.studentVacation.weather.state == 1:
                self.secondAnswer = True
                self.studentVacation.weather.state = 2
            if self.studentVacation.weather.state == 0:
                self.studentVacation.weather.state = 1

        if self.vacationCase == "Actividad":
            self.talkingVac = True
            if self.studentVacation.activity.state == 2:
                return "Hablamos de su actividad"
            if self.studentVacation.activity.state == 1:
                self.secondAnswer = True
                self.studentVacation.activity.state = 2
            if self.studentVacation.activity.state == 0:
                self.studentVacation.activity.state = 1    

        if self.vacationCase == "Experiencias":
            self.talkingVac = True
            if self.studentVacation.exp.state == 2:
                return "No tengo que hablar más de experiencias"
            if self.studentVacation.exp.state == 1:
                self.secondAnswer = True
                self.studentVacation.exp.state = 2
            if self.studentVacation.exp.state == 0:
                self.studentVacation.exp.state = 1
        
        if self.vacationCase == "Especial":
            self.talkingVac = True
            if self.studentVacation.special.state == 2:
                return "No puedo hablar de nada más especial"
            if self.studentVacation.special.state == 1:
                self.secondAnswer = True
                self.studentVacation.special.state = 2
            if self.studentVacation.special.state == 0:
                self.studentVacation.special.state = 1
        
        if self.vacationCase == "Fin":
            self.talkingVac = True
            if self.studentVacation.end.state == 2:
                return "Ya nos hemos despedido, ¿no?"
            if self.studentVacation.end.state == 1:
                self.secondAnswer = True
                self.studentVacation.end.state = 2
            if self.studentVacation.end.state == 0:
                self.studentVacation.end.state = 1

       

        # return self.case

        #small talk and vacation talk? smth like Hola(!) how were your vacations(!)
        # its just small talk
        if self.swearCase != "":
            response = self.chooseSwearResponse(self.swearCase, 0)

        elif self.smallCase != "" and self.vacationCase == "" and self.talkingVac == False:
            response = self.chooseSmallResponse(self.smallCase, 0)
            #self.talkingVac = True

        elif self.smallCase != "" and self.vacationCase == "" and self.talkingVac == True:
            response = "Háblame de tus últimas vacaciones. ¿En qué país pasaste tus últimas vacaciones?"

        elif self.smallCase == "" and self.vacationCase != "":
            response = self.chooseVacationResponse(self.vacationCase, 0)
        
        elif self.smallCase != "" and self.vacationCase != "":
            response = self.chooseSmallResponse(self.smallCase, 0) + " " + self.chooseVacationResponse(self.vacationCase, 0)

        # ytu-asnwers for the vacation talk, needs to be ahead of small talk so no random como estas answer in vaction topics

        # umgekehrte Reihenfolge (einfach) oder immer an den Anfang springen
        # elif self.

       
        
        elif self.studentVacation.exp.state == 1: # and self.ytu == True:
            self.ytu = False
            self.vacationCase = "Especial"
            self.studentVacation.special.state = 1
            response = self.chooseVacationResponse(self.vacationCase, 0)
        
        elif self.studentVacation.activity.state == 1: # and self.ytu == True:
            self.ytu = False
            self.vacationCase = "Experiencias"
            self.studentVacation.exp.state = 1
            response = self.chooseVacationResponse(self.vacationCase, 0)

        elif self.studentVacation.weather.state == 1: #and self.ytu == True:
            self.ytu = False
            self.vacationCase = "Actividad"
            self.studentVacation.activity.state = 1
            response = self.chooseVacationResponse(self.vacationCase, 0)

        elif self.studentVacation.company.state == 1: #and self.ytu == True:
            self.ytu = False
            self.vacationCase = "Tiempo"
            self.studentVacation.weather.state = 1
            response = self.chooseVacationResponse(self.vacationCase, 0)
        
        elif self.studentVacation.date.state == 1: #and self.ytu == True:
            self.ytu = False
            self.vacationCase = "Compañía"
            self.studentVacation.company.state = 1
            response = self.chooseVacationResponse(self.vacationCase, 0)
        
        elif self.studentVacation.transporte == 1: #and self.ytu == True:
            self.ytu = False
            self.vacationCase = "Fecha"
            self.studentVacation.date.state = 1
            response = self.chooseVacationResponse(self.vacationCase, 0)

        elif self.studentVacation.place == 1: #and self.ytu == True:
            self.ytu = False
            self.vacationCase = "Transporte"
            self.studentVacation.transporte = 1
            response = self.chooseVacationResponse(self.vacationCase,0)
        
        elif self.studentVacation.residence == 1: #and self.ytu == True:
            self.ytu = False
            self.vacationCase = "Ubicación"
            self.studentVacation.place = 1
            self.talkingVac = True
            response = self.chooseVacationResponse(self.vacationCase, 0)

        # if self.studentVacation.place.state == 1:
        # if self.studentVacation.transporte.state == 1:
        # if self.studentVacation.date.state == 0:
        # if self.studentVacation.weather.state == 0:
        # if self.studentVacation.activity.state == 0:
        # if self.studentVacation.weather.state == 1:
        # if self.studentVacation.exp.state == 1:
        # if self.studentVacation.special.state == 0:
        

        # small talk ytu answers
        # later forcing topics in order if not asked directly
        elif self.studentVacation.name.state == 1 and self.ytu == True:
            self.ytu = False
            self.smallCase = "Residencia"
            self.studentVacation.residence.state = 1
            response = self.chooseSmallResponse(self.smallCase, 0)
        
        elif self.studentVacation.hru.state == 1 and self.ytu == True:
            self.ytu = False
            self.smallCase = "Nombre"
            self.studentVacation.name.state = 1
            response = self.chooseSmallResponse(self.smallCase, 0)

        elif self.studentVacation.hru.state == 0 and self.ytu == True:
            self.ytu = False
            self.smallCase = "Como estas"
            self.studentVacation.hru.state = 1
            response = self.chooseSmallResponse(self.smallCase, 0)
        
       

        # there is a word we cannot process, maybe just an answer like a name, without reasking.
        # we are still in small talk phase, which means we can pick up another small talk topic
        # needs work...
        # elif self.talkingVac == False: #and self.smallCase != "Residencia":

            
        #     if self.studentVacation.residence.state == 1:
        #         response = "Háblame de tus últimas vacaciones"
        #         self.talkingVac = True
                

        #     elif self.studentVacation.name.state == 1:
                
        #         self.smallCase = "Residencia"
        #         self.studentVacation.residence.state = 1
        #         self.talkingVac = True
        #         response = self.chooseSmallResponse(self.smallCase, 0)
        #         #response = ""

        #     elif self.studentVacation.hru.state == 1:
                
        #         self.smallCase = "Nombre"
        #         self.studentVacation.name.state = 1
        #         self.talkingVac = True
        #         response = self.chooseSmallResponse(self.smallCase, 0)


        #     elif self.justHola == True:
        #         self.smallCase = "Hola"
        #         response = self.chooseSmallResponse(self.smallCase, 0)

        #     elif self.studentVacation.hru.state == 0:
                
        #         # if self.justHola == True:
        #         #     response = "Hola de nuevo"
                
        #         self.smallCase = "Como estas"
        #         self.studentVacation.hru.state = 1
        #         response = self.chooseSmallResponse(self.smallCase, 0)
            
            

        elif self.studentVacation.special.state == 1:
                self.vacationCase = "Fin"
                self.studentVacation.end.state = 1
                response = self.chooseVacationResponse(self.vacationCase, 0)

            
        elif self.studentVacation.sorry.state == 0:
            self.studentVacation.sorry.state = 1
            response = "Lo siento. ¿Podrías reescribir esto o preguntarme algo nuevo? No estoy seguro si te entendí"
            

        elif self.studentVacation.sorry.state == 1:
            if self.talkingVac == False: #and self.smallCase != "Residencia":

            
                if self.studentVacation.residence.state == 1:
                    response = "Háblame de tus últimas vacaciones"
                    self.talkingVac = True
                

                elif self.studentVacation.name.state == 1:
                
                    self.smallCase = "Residencia"
                    self.studentVacation.residence.state = 1
                    self.talkingVac = True
                    response = self.chooseSmallResponse(self.smallCase, 0)
                    #response = ""

                elif self.studentVacation.hru.state == 1:
                
                    self.smallCase = "Nombre"
                    self.studentVacation.name.state = 1
                    self.talkingVac = True
                    response = self.chooseSmallResponse(self.smallCase, 0)


                elif self.justHola == True:
                    self.smallCase = "Hola"
                    response = self.chooseSmallResponse(self.smallCase, 0)

                elif self.studentVacation.hru.state == 0:
                
                    # if self.justHola == True:
                    #     response = "Hola de nuevo"
                
                    self.smallCase = "Como estas"
                    self.studentVacation.hru.state = 1
                    response = self.chooseSmallResponse(self.smallCase, 0)
            
        else:
            response = "Lo siento. ¿Podrías reescribir esto o preguntarme algo nuevo? No estoy seguro si te entendí"

        # its just vacation talk
        return response


##### lets try without prepocessing for now
    # def preprocess_input(self, input_str):
    #     # Convert the input string to lowercase
    #     input_str = input_str.lower()

    #     # Remove any leading or trailing white space
    #     input_str = input_str.strip()

    #     # Remove any punctuation
    #     input_str = re.sub(r'[^\w\s]', '', input_str)

    #     # Tokenize the input string
    #     tokens = nltk.word_tokenize(input_str)

    #     # Remove any stop words
    #     spanish_stop_words = stopwords.words('spanish')
    #     tokens = [token for token in tokens if token not in spanish_stop_words]

    #     # Perform stemming
    #     stemmer = SnowballStemmer("spanish")
    #     tokens = [stemmer.stem(token) for token in tokens]

    #     # Rejoin the tokens into a single string
    #     input_str = " ".join(tokens)

    #     return input_str

    # theoretisch eine Funktion zur Random Auswahl an Antwortmöglichkeiten zu einem spezifischen case
    # in Elize werden allerdings alte Antworten aussortiert, damit Antworten sich nicht wiederholen
    # erstmal nicht implementiert
    
    # function swear words
    def chooseSwearResponse(self, currentcase, currentmemory):
        listLocalResponse = self.swearWords.answers[currentcase][:]
        listLocalRemarks = self.swearWords.remarks[currentcase][:]
        if self.ytu == True:
            response = random.choice(listLocalResponse)
            self.question = False
        elif self.question == True:
            response = random.choice(listLocalResponse) # choose randomly an answer
            self.question = False
        else:
            response = random.choice(listLocalRemarks)
        return response


    # function for chosing SMALL TALK RESPONSE
    def chooseSmallResponse(self, currentcase, currentmemory):
        listLocalResponse = self.rogersES.answers[currentcase][:]
        listLocalRemarks = self.rogersES.remarks[currentcase][:]
        if self.ytu == True:
            response = random.choice(listLocalResponse)
            self.question = False
        elif self.question == True:
            response = random.choice(listLocalResponse) # choose randomly an answer
            self.question = False
        else:
            response = random.choice(listLocalRemarks)
        return response

    # function for chosing VACATION RESPONSE
    def chooseVacationResponse(self, currentcase, currentmemory):
        listLocalResponse = self.rogersESvac.answers[currentcase][:]
        listLocalRemarks = self.rogersESvac.remarks[currentcase][:]
        listLocalSecond = self.rogersESvac.answers2[currentcase][:]
        if self.question == True and self.secondAnswer == True:
            response = random.choice(listLocalSecond)
            self.question = False
            self.secondAnswer = False
        elif self.question == True:
            response = random.choice(listLocalResponse) # choose randomly an answer
            self.question = False
        elif self.vacationCase == "Fin" and self.secondAnswer == True:
            response = random.choice(listLocalSecond)
        else:
            response = random.choice(listLocalRemarks) 
        return response
    
    # def detect_swear_words(self, text):
    # # Spanish swear words
    # swear_words = ["puta", "puto", "cabron", "cabrón", "mierda", "coño", "culo", "pinga", "pendejo", "pinche", "Puta", "putero",
    # "Putero", "mierda", "Mierda", "joder", "Joder", "culo", "Culo", "Gilipollas", "gilipollas", "Pollas", "pollas", "folle",
    # "Folle", "Que te den", "que te den", "Coño", "cago", "Cago", "Pinche", "pinche", "Pendejo", "chúpamela", "los cojones", "hostia"]

    # swear_words_found = [word for word in swear_words if word in text.lower()]

    # return swear_words_found