

class RogersES:

    noRecall = ["Pregunta", "Fin"]

    answers={}
    keywords={}

    

    #################################################
    # special cases

    # return
    answers["Return"] = ["Return answer"]

    # Pregunta = Question 
    answers["Pregunta"] = ["This is answer <Pregunta>"]

    # Vacío = Empty
    answers["Vacío"] = ["This is answer <Vacio>"]

    #################################################
    # normal cases

    # fin = End
    keywords["Fin"] = ["adios"]
    answers["Fin"] = ["This is answer <Fin>"]

    # Actividad = activity
    keywords["Actividad"] = ["actividad", "escalada", "esquí"]
    answers["Actividad"] = ["Aktivität Antwort 1", "Aktivität Antwort 2", "Aktivität Antwort 3"]

    # Ubicación = Place
    keywords["Ubicación"] = ["ubicación"]
    answers["Ubicación"] = ["Ort Antwort 1", "Ort Antwort 2","Ort Antwort 3"]

     # fecha = date
    keywords["Fecha"] = ["fecha"]
    answers["Fecha"] = ["Datum Antwort 1", "Datum Answers 2", "Datum Answer 3"]

    # Tiempo = Weather
    keywords["Tiempo"] = ["tiempo", "grados"]
    answers["Tiempo"] = ["Wetter Antwort 1", "Wetter Antwort 2", "Wetter Antwort 3"]

