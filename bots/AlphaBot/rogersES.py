

class RogersES:

    noRecall = ["Pregunta", "Fin"]

    # answer when there was a question
    answers={}
    answers2={}
    keywords={}
    # answer when there was no question
    remarks={}

    

    #################################################
    # special cases

    # return
    answers["Return"] = ["Return answer"]

    # Pregunta = Question 
    answers["Pregunta"] = ["This is answer <Pregunta>"]

    # Vacío = Empty
    answers["Vacío"] = ["This is answer <Vacio>"]

    #################################################

    #################################################
    # swear word detection
    # palabrotas = swear words
    # keywords["Palabrotas"] = ["puta", "Puta", "putero", "Putero", "mierda", "Mierda", "joder", "Joder", "culo", "Culo", "Gilipollas", "gilipollas",
    # "Pollas", "pollas", "folle", "Folle", "Que te den", "que te den", "Coño", "coño", "cago", "Cago", "Pinche", "pinche", "Pendejo", "pendejo",
    # "chúpamela", "los cojones", "hostia"]
    # answers["Palabrotas"] = ["swear word detection"]
    # remarks["Palabrotas"] = ["swear word detection"]


    #################################################
    # normal cases

    ### small talk ####
    # saludo = greeting
    # keywords["Saludo"] = ["Hola", "hola", "Buenos días", "buenos días", "Buenas tardes", "buenas tardes", "Buenas noches", "buenas noches", "Saludos",
    # "saludos", "Saludo", "saludo"]
    # answers["Saludo"] = ["Hola. Muy bien, y tu?"]
    # remarks["Saludo"] = ["Hola", "Saludos"]

    answers["Hola"] = ["Hola de nuevo"]
    remarks["Hola"] = ["Hola de nuevo"]

    # como estas = how are you
    keywords["Como estas"] = ["que tal", "que tal?", "Que tal", "Qué tal", "Qué tal?", "¿Qué tal?", "qué tal", "qué tal?", "Cómo estás?", "¿Cómo estás?", "Cómo estás", "cómo estás?", "cómo estás", "como estas",
    "como estas?", "Como estas", "Como estas?", "Cómo te va?", "¿Cómo te va?", "Cómo te va", "cómo te va?", "como te va?", "cómo te va", "como te va", "Cómo te sientes?", "Cómo te sientes?",
    "como te sientes", "como te sientes?", "¿Cómo está usted?", ]
    answers["Como estas"] = ["Muy bien, gracias. ¿Cómo te llamas?", "Bien, gracias. ¿Cómo te llamas?", "Bien, aunque un poco cansado. ¿Cómo te llamas?"]
    remarks["Como estas"] = ["Muy bien. ¿Cómo te llamas?", "Bien. ¿Cómo te llamas?", "¿Unque un poco cansado? ¿Cómo te llamas?"]

    # nombre = name
    keywords["Nombre"] = ["¿Cómo te llamas?", "Cómo te llamas?", "¿Como te llamas?", "Como te llamas?", "Como te llamas", "Cómo te llamas", "llamas",
    "Hola! Me llamo", "Hola, me llamo"]
    answers["Nombre"] = ["Me llamo Laura. ¿En qué ciudad vives?", "Me llamo Pascal. ¿En qué ciudad vives?", "Me llamo Roberto. ¿En qué ciudad vives?"]
    remarks["Nombre"] = ["Me llamo Laura. ¿En qué ciudad vives?", "Me llamo Pascal. ¿En qué ciudad vives?", "Me llamo Roberto. ¿En qué ciudad vives?"]

    # Residencia = Residence
    keywords["Residencia"] = ["De dónde eres", "eres?", "vives?", "donde vives", "¿En qué ciudad vives?", "En qué ciudad vives"]
    answers["Residencia"] = ["Yo soy de Madrid, la capital de España. Es un buen lugar para ir de vacaciones. ¿En qué país pasaste tus últimas vacaciones?", 
    "Yo soy de Barcelona, una ciudad linda en España. Es un buen lugar para ir de vacaciones. ¿En qué país pasaste tus últimas vacaciones?",
    "Yo soy de Guadalajara, una ciudad grande en México. Es un buen lugar para ir de vacaciones. ¿En qué país pasaste tus últimas vacaciones?",
    "Yo soy de Bilbao, una ciudad en el norte de España. Es un buen lugar para ir de vacaciones. ¿En qué país pasaste tus últimas vacaciones?",
    "Yo soy de Villa del Mar, una ciudad en la playa en Chila. Es un buen lugar para ir de vacaciones. ¿En qué país pasaste tus últimas vacaciones?"]
    remarks["Residencia"] = ["Yo soy de Madrid, la capital de España. Es un buen lugar para ir de vacaciones. ¿En qué país pasaste tus últimas vacaciones?", 
    "Yo soy de Barcelona, una ciudad linda en España. Es un buen lugar para ir de vacaciones. ¿En qué país pasaste tus últimas vacaciones?",
    "Yo soy de Guadalajara, una ciudad grande en México. Es un buen lugar para ir de vacaciones. ¿En qué país pasaste tus últimas vacaciones?",
    "Yo soy de Bilbao, una ciudad en el norte de España. Es un buen lugar para ir de vacaciones. ¿En qué país pasaste tus últimas vacaciones?",
    "Yo soy de Villa del Mar, una ciudad en la playa en Chila. Es un buen lugar para ir de vacaciones. ¿En qué país pasaste tus últimas vacaciones?"]
    ### end of small talk ###

    ### talking about the vacation ###
    # fin = End
    # keywords["Fin"] = ["adios"]
    # answers["Fin"] = ["This is answer <Fin>"]
    # remarks["Fin"] = ["This is answer <Fin>"]

    # # Actividad = activity
    # keywords["Actividad"] = ["actividad", "escalada", "esquí"]
    # answers["Actividad"] = ["Aktivität Antwort 1", "Aktivität Antwort 2", "Aktivität Antwort 3"]
    # remarks["Actividad"] = ["Aktivität Antwort 1", "Aktivität Antwort 2", "Aktivität Antwort 3"]

    # # Ubicación = Place
    # keywords["Ubicación"] = ["ubicación"]
    # answers["Ubicación"] = ["Ort Antwort 1", "Ort Antwort 2","Ort Antwort 3"]
    # remarks["Ubicación"] = ["Ort Antwort 1", "Ort Antwort 2","Ort Antwort 3"]

    #  # fecha = date
    # keywords["Fecha"] = ["fecha"]
    # answers["Fecha"] = ["Datum Antwort 1", "Datum Answers 2", "Datum Answer 3"]
    # remarks["Fecha"] = ["Datum Antwort 1", "Datum Answers 2", "Datum Answer 3"]

    # # Tiempo = Weather
    # keywords["Tiempo"] = ["tiempo", "grados"]
    # answers["Tiempo"] = ["Wetter Antwort 1", "Wetter Antwort 2", "Wetter Antwort 3"]
    # remarks["Tiempo"] = ["Wetter Antwort 1", "Wetter Antwort 2", "Wetter Antwort 3"]
