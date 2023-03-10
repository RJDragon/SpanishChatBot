

class SwearES:

    noRecall = ["Pregunta", "Fin"]

    # answer when there was a question
    answers={}
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
    keywords["Palabrotas"] = ["puta", "Puta", "putero", "Putero", "mierda", "Mierda", "joder", "Joder", "culo", "Culo", "Gilipollas", "gilipollas",
    "Pollas", "pollas", "folle", "Folle", "Que te den", "que te den", "Coño", "coño", "cago", "Cago", "Pinche", "pinche", "Pendejo", "pendejo",
    "chúpamela", "los cojones", "hostia", "Anal", "anal", "Arschloch", "arschloch", "Besserwisser", "Biatch", "bitch", "Bitch", "Blödkopf", "Bock", "bock", "dildo", "Dildo", "Dirne",
    "Doofkopf", "Dreckshure", "dumm", "Dummkopf", "Eichel", "Fehlfick", "Fettfotze", "ficken", "Ficken", "fick", "Fickehler", "fotze", "Fotze", "Hafennutte", "idiot", "Idiot",
    "Inzucht", "kacke", "Kacke", "kagge", "kot", "Kot", "Lauch", "Missgeburt", "Nutte", "nutte", "Opfer", "opfer", "penis", "Penis", "pimmel", "Pimmel", "scheide", "Scheide", "scheiße",
    "Scheiße", "Schließmuskel", "sperma", "Sperma", "Taschenmuschi", "titten", "tittenfick", "Titten", "Vollidiot", "vollidiot", "wichser", "wixxer", "Wichser", "Wixxer", "ziegenficker",
    "Ziegenficker"]
    answers["Palabrotas"] = ["Por favor, usa lengua adecuada"]
    remarks["Palabrotas"] = ["Por favor, usa lengua adecuada"]
