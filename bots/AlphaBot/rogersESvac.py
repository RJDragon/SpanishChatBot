

class RogersESvac:

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
    # normal cases

    # ### small talk ####
    # # saludo = greeting
    # keywords["Saludo"] = ['Hola', 'Buenos días', 'Buenas tardes', 'Buenas noches', "Saludos", "Saludo", 'Hola,', 
    # 'Buenos días,', 'Buenas tardes,', 'Buenas noches,', "Saludos,", "Saludo,"]
    # answers["Saludo"] = ["Hola. Muy bien, y tu?"]
    # remarks["Saludo"] = ["Hola", "Saludos"]

    # # como estas = how are you
    # keywords["Como estas"] = ["que tal", "que tal?", "Que tal", "Qué tal", "Qué tal?", "¿Qué tal?", "qué tal", "qué tal?", "Cómo estás?", "¿Cómo estás?", "Cómo estás", "cómo estás?", "cómo estás", "como estas",
    # "como estas?", "Como estas", "Como estas?", "Cómo te va?", "¿Cómo te va?", "Cómo te va", "cómo te va?", "como te va?", "cómo te va", "como te va", "Cómo te sientes?", "Cómo te sientes?",
    # "como te sientes", "como te sientes?", "¿Cómo está usted?", ]
    # answers["Como estas"] = ["Muy bien, y tu?", "Bien, gracias. ¿Y tú?", "Bien, aunque un poco cansado. Y tu?"]
    # remarks["Como estas"] = ["Muy bien, y tu?", "Bien, gracias. ¿Y tú?", "Bien, aunque un poco cansado. Y tu?"]

    # # nombre = name
    # keywords["Nombre"] = ["¿Cómo te llamas?", "Cómo te llamas?", "¿Como te llamas?", "Como te llamas?", "Como te llamas", "Cómo te llamas", "llamas",
    # "Hola! Me llamo", "Hola, me llamo"]
    # answers["Nombre"] = ["Me llamo Laura", "Me llamo Pascal", "Me llamo Roberto"]
    # remarks["Nombre"] = ["Me llamo Laura", "Me llamo Pascal", "Me llamo Roberto"]

    # # Residencia = Residence
    # keywords["Residencia"] = ["De dónde eres", "eres?", "vives?", "donde vives"]
    # answers["Residencia"] = ["Yo soy de Madrid. Es un buen lugar para ir de vacaciones. Qué hiciste las vacaciones pasadas?", 
    # "Soy de Barcelona. Es un buen lugar para ir de vacaciones. Qué hiciste las vacaciones pasadas?",
    # "Yo soy de Valencia. Es un buen lugar para ir de vacaciones. Qué hiciste las vacaciones pasadas?"]
    # remarks["Residencia"] = ["Yo soy de Madrid. Es un buen lugar para ir de vacaciones. Qué hiciste las vacaciones pasadas?", 
    # "Soy de Barcelona. Es un buen lugar para ir de vacaciones. Qué hiciste las vacaciones pasadas?",
    # "Yo soy de Valencia. Es un buen lugar para ir de vacaciones. Qué hiciste las vacaciones pasadas?"]
    # ### end of small talk ###

    ### talking about the vacation ###
    
    # Entrada en las vacaciones = entering the vacations(-topic) after being asked about it!# rule in bot.py to be able to speak about it more often, maybe following questions include the word "vacaciones"
    # keywords["Vacaciones"] = ["vacaciones", "vacaciones?", "pasadas", "pasadas?"]
    # answers["Vacaciones"] = ["Iv been in Spain, y tu?", "I was in Poland", "I went surfing"]
    # remarks["Vacaciones"] = ["Iv been in Spain, y tu?", "I was in Poland", "I went surfing"]

    # Ubicación = Place ## RULE ABOUT NOT ALREADY TALKED BOUT VACACIONES IN GENERAL BECAUSE WE ALREADY MENTION OUR DESTINATION
    keywords["Ubicación"] = ["vacaciones?", "vacaciones", "Afganistán", "Albania", "Alemania", "Andorra", "Angola", "Antigua y Barbuda",
    "Arabia Saudita", "Argelia", "Argentina", "Armenia", "Australia", "Austria",
    "Azerbaiyán", "Bahamas", "Bangladés", "Barbados", "Baréin", "Bélgica",
    "Belice", "Benín", "Bielorrusia", "Birmania", "Bolivia", "Bosnia y Herzegovina",
    "Botsuana", "Brasil", "Brunéi", "Bulgaria", "Burkina Faso", "Burundi", "Bután",
    "Cabo Verde", "Camboya", "Camerún", "Canadá", "Catar", "Chad", "Chile", "China",
    "Chipre", "Colombia", "Comoras", "Corea del Norte", "Corea del Sur", "Costa de Marfil",
    "Costa Rica", "Croacia", "Cuba", "Dinamarca", "Dominica", "Ecuador", "Egipto",
    "El Salvador", "Emiratos Árabes Unidos", "Eritrea", "Eslovaquia", "Eslovenia",
    "España", "Estados Unidos", "Estonia", "Etiopía", "Filipinas", "Finlandia", "Fiyi",
    "Francia", "Gabón", "Gambia", "Georgia", "Ghana", "Granada", "Grecia", "Guatemala",
    "Guinea", "Guinea ecuatorial", "Guinea-Bisáu", "Guyana", "Haití", "Honduras",
    "Hungría", "India", "Indonesia", "Irak", "Irán", "Irlanda", "Islandia", "Islas Marshall",
    "Islas Salomón", "Israel", "Italia", "Jamaica", "Japón", "Jordania", "Kazajistán",
    "Kenia", "Kirguistán", "Kiribati", "Kuwait", "Laos", "Lesoto", "Letonia", "Líbano",
    "Liberia", "Libia", "Liechtenstein", "Lituania", "Luxemburgo", "Macedonia del Norte",
    "Madagascar", "Malasia", "Malaui", "Maldivas", "Malí", "Malta", "Marruecos", "Mauricio",
    "Mauritania", "México", "Micronesia", "Moldavia", "Mónaco", "Mongolia", "Montenegro",
    "Mozambique", "Namibia", "Nauru", "Nepal", "Nicaragua", "Níger", "Nigeria", "Noruega",
    "Nueva Zelanda", "Omán", "Países Bajos", "Pakistán", "Palaos", "Panamá", "Papúa Nueva Guinea", "Paraguay", "Perú", "Polonia", "Portugal", "Reino Unido",
    "República Centroafricana", "República Checa", "República del Congo", "República Democrática del Congo",
    "República Dominicana", "Ruanda", "Rumania", "Rusia", "Samoa", "San Cristóbal y Nieves",
    "San Marino", "San Vicente y las Granadinas", "Santa Lucía", "Santo Tomé y Príncipe", "Senegal",
    "Serbia", "Seychelles", "Sierra Leona", "Singapur", "Siria", "Somalia", "Sri Lanka", "Suazilandia",
    "Sudáfrica", "Sudán", "Sudán del Sur", "Suecia", "Suiza", "Surinam", "Tailandia", "Tanzania",
    "Tayikistán", "Timor Oriental", "Togo", "Tonga", "Trinidad y Tobago", "Túnez", "Turkmenistán",
    "Turquía", "Tuvalu", "Ucrania", "Uganda", "Uruguay", "Uzbekistán", "Vanuatu", "Vaticano",
    "Venezuela", "Vietnam", "Yemen", "Yibuti", "Zambia", "Zimbabue",
    "Afganistán.", "Albania.", "Alemania.", "Andorra.", "Angola.", "Antigua y Barbuda.",
    "Arabia Saudita.", "Argelia.", "Argentina.", "Armenia.", "Australia.", "Austria.",
    "Azerbaiyán.", "Bahamas.", "Bangladés.", "Barbados.", "Baréin.", "Bélgica.",
    "Belice.", "Benín.", "Bielorrusia.", "Birmania.", "Bolivia.", "Bosnia y Herzegovina.",
    "Botsuana.", "Brasil.", "Brunéi.", "Bulgaria.", "Burkina Faso.", "Burundi.", "Bután.",
    "Cabo Verde.", "Camboya.", "Camerún.", "Canadá.", "Catar.", "Chad.", "Chile.", "China.",
    "Chipre.", "Colombia.", "Comoras.", "Corea del Norte.", "Corea del Sur.", "Costa de Marfil.",
    "Costa Rica.", "Croacia.", "Cuba.", "Dinamarca.", "Dominica.", "Ecuador.", "Egipto.",
    "El Salvador.", "Emiratos Árabes Unidos.", "Eritrea.", "Eslovaquia.", "Eslovenia.",
    "España.", "Estados Unidos.", "Estonia.", "Etiopía.", "Filipinas.", "Finlandia.", "Fiyi.",
    "Francia.", "Gabón.", "Gambia.", "Georgia.", "Ghana.", "Granada.", "Grecia.", "Guatemala.",
    "Guinea.", "Guinea ecuatorial.", "Guinea-Bisáu.", "Guyana.", "Haití.", "Honduras.",
    "Hungría.", "India.", "Indonesia.", "Irak.", "Irán.", "Irlanda.", "Islandia.", "Islas Marshall.",
    "Islas Salomón.", "Israel.", "Italia.", "Jamaica.", "Japón.", "Jordania.", "Kazajistán.",
    "Kenia.", "Kirguistán.", "Kiribati.", "Kuwait.", "Laos.", "Lesoto.", "Letonia.", "Líbano.",
    "Liberia.", "Libia.", "Liechtenstein.", "Lituania.", "Luxemburgo.", "Macedonia del Norte.",
    "Madagascar.", "Malasia.", "Malaui.", "Maldivas.", "Malí.", "Malta.", "Marruecos.", "Mauricio.",
    "Mauritania.", "México.", "Micronesia.", "Moldavia.", "Mónaco.", "Mongolia.", "Montenegro.",
    "Mozambique.", "Namibia.", "Nauru.", "Nepal.", "Nicaragua.", "Níger.", "Nigeria.", "Noruega.",
    "Nueva Zelanda.", "Omán.", "Países Bajos.", "Pakistán.", "Palaos.", "Panamá.", "Papúa Nueva Guinea.", "Paraguay.", "Perú.", "Polonia.", "Portugal.", "Reino Unido.",
    "República Centroafricana.", "República Checa.", "República del Congo.", "República Democrática del Congo.",
    "República Dominicana.", "Ruanda.", "Rumania.", "Rusia.", "Samoa.", "San Cristóbal y Nieves.",
    "San Marino.", "San Vicente y las Granadinas.", "Santa Lucía.", "Santo Tomé y Príncipe.", "Senegal.",
    "Serbia.", "Seychelles.", "Sierra Leona.", "Singapur.", "Siria.", "Somalia.", "Sri Lanka.", "Suazilandia.",
    "Sudáfrica.", "Sudán.", "Sudán del Sur.", "Suecia.", "Suiza.", "Surinam.", "Tailandia.", "Tanzania.",
    "Tayikistán.", "Timor Oriental.", "Togo.", "Tonga.", "Trinidad y Tobago.", "Túnez.", "Turkmenistán.",
    "Turquía.", "Tuvalu.", "Ucrania.", "Uganda.", "Uruguay.", "Uzbekistán.", "Vanuatu.", "Vaticano.",
    "Venezuela.", "Vietnam.", "Yemen.", "Yibuti.", "Zambia.", "Zimbabue.",
    "Afganistán!", "Albania!", "Alemania!", "Andorra!", "Angola!", "Antigua y Barbuda!",
    "Arabia Saudita!", "Argelia!", "Argentina!", "Armenia!", "Australia!", "Austria!",
    "Azerbaiyán!", "Bahamas!", "Bangladés!", "Barbados!", "Baréin!", "Bélgica!",
    "Belice!", "Benín!", "Bielorrusia!", "Birmania!", "Bolivia!", "Bosnia y Herzegovina!",
    "Botsuana!", "Brasil!", "Brunéi!", "Bulgaria!", "Burkina Faso!", "Burundi!", "Bután!",
    "Cabo Verde!", "Camboya!", "Camerún!", "Canadá!", "Catar!", "Chad!", "Chile!", "China!",
    "Chipre!", "Colombia!", "Comoras!", "Corea del Norte!", "Corea del Sur!", "Costa de Marfil!",
    "Costa Rica!", "Croacia!", "Cuba!", "Dinamarca!", "Dominica!", "Ecuador!", "Egipto!",
    "El Salvador!", "Emiratos Árabes Unidos!", "Eritrea!", "Eslovaquia!", "Eslovenia!",
    "España!", "Estados Unidos!", "Estonia!", "Etiopía!", "Filipinas!", "Finlandia!", "Fiyi!",
    "Francia!", "Gabón!", "Gambia!", "Georgia!", "Ghana!", "Granada!", "Grecia!", "Guatemala!",
    "Guinea!", "Guinea ecuatorial!", "Guinea-Bisáu!", "Guyana!", "Haití!", "Honduras!",
    "Hungría!", "India!", "Indonesia!", "Irak!", "Irán!", "Irlanda!", "Islandia!", "Islas Marshall!",
    "Islas Salomón!", "Israel!", "Italia!", "Jamaica!", "Japón!", "Jordania!", "Kazajistán!",
    "Kenia!", "Kirguistán!", "Kiribati!", "Kuwait!", "Laos!", "Lesoto!", "Letonia!", "Líbano!",
    "Liberia!", "Libia!", "Liechtenstein!", "Lituania!", "Luxemburgo!", "Macedonia del Norte!",
    "Madagascar!", "Malasia!", "Malaui!", "Maldivas!", "Malí!", "Malta!", "Marruecos!", "Mauricio!",
    "Mauritania!", "México!", "Micronesia!", "Moldavia!", "Mónaco!", "Mongolia!", "Montenegro!",
    "Mozambique!", "Namibia!", "Nauru!", "Nepal!", "Nicaragua!", "Níger!", "Nigeria!", "Noruega!",
    "Nueva Zelanda!", "Omán!", "Países Bajos!", "Pakistán!", "Palaos!", "Panamá!", "Papúa Nueva Guinea!", "Paraguay!", "Perú!", "Polonia!", "Portugal!", "Reino Unido!",
    "República Centroafricana!", "República Checa!", "República del Congo!", "República Democrática del Congo!",
    "República Dominicana!", "Ruanda!", "Rumania!", "Rusia!", "Samoa!", "San Cristóbal y Nieves!",
    "San Marino!", "San Vicente y las Granadinas!", "Santa Lucía!", "Santo Tomé y Príncipe!", "Senegal!",
    "Serbia!", "Seychelles!", "Sierra Leona!", "Singapur!", "Siria!", "Somalia!", "Sri Lanka!", "Suazilandia!",
    "Sudáfrica!", "Sudán!", "Sudán del Sur!", "Suecia!", "Suiza!", "Surinam!", "Tailandia!", "Tanzania!",
    "Tayikistán!", "Timor Oriental!", "Togo!", "Tonga!", "Trinidad y Tobago!", "Túnez!", "Turkmenistán!",
    "Turquía!", "Tuvalu!", "Ucrania!", "Uganda!", "Uruguay!", "Uzbekistán!", "Vanuatu!", "Vaticano!",
    "Venezuela!", "Vietnam!", "Yemen!", "Yibuti!", "Zambia!", "Zimbabue!",
    "Afganistán,", "Albania,", "Alemania,", "Andorra,", "Angola,", "Antigua y Barbuda,",
    "Arabia Saudita,", "Argelia,", "Argentina,", "Armenia,", "Australia,", "Austria,",
    "Azerbaiyán,", "Bahamas,", "Bangladés,", "Barbados,", "Baréin,", "Bélgica,",
    "Belice,", "Benín,", "Bielorrusia,", "Birmania,", "Bolivia,", "Bosnia y Herzegovina,",
    "Botsuana,", "Brasil,", "Brunéi,", "Bulgaria,", "Burkina Faso,", "Burundi,", "Bután,",
    "Cabo Verde,", "Camboya,", "Camerún,", "Canadá,", "Catar,", "Chad,", "Chile,", "China,",
    "Chipre,", "Colombia,", "Comoras,", "Corea del Norte,", "Corea del Sur,", "Costa de Marfil,",
    "Costa Rica,", "Croacia,", "Cuba,", "Dinamarca,", "Dominica,", "Ecuador,", "Egipto,",
    "El Salvador,", "Emiratos Árabes Unidos,", "Eritrea,", "Eslovaquia,", "Eslovenia,",
    "España,", "Estados Unidos,", "Estonia,", "Etiopía,", "Filipinas,", "Finlandia,", "Fiyi,",
    "Francia,", "Gabón,", "Gambia,", "Georgia,", "Ghana,", "Granada,", "Grecia,", "Guatemala,",
    "Guinea,", "Guinea ecuatorial,", "Guinea-Bisáu,", "Guyana,", "Haití,", "Honduras,",
    "Hungría,", "India,", "Indonesia,", "Irak,", "Irán,", "Irlanda,", "Islandia,", "Islas Marshall,",
    "Islas Salomón,", "Israel,", "Italia,", "Jamaica,", "Japón,", "Jordania,", "Kazajistán,",
    "Kenia,", "Kirguistán,", "Kiribati,", "Kuwait,", "Laos,", "Lesoto,", "Letonia,", "Líbano,",
    "Liberia,", "Libia,", "Liechtenstein,", "Lituania,", "Luxemburgo,", "Macedonia del Norte,",
    "Madagascar,", "Malasia,", "Malaui,", "Maldivas,", "Malí,", "Malta,", "Marruecos,", "Mauricio,",
    "Mauritania,", "México,", "Micronesia,", "Moldavia,", "Mónaco,", "Mongolia,", "Montenegro,",
    "Mozambique,", "Namibia,", "Nauru,", "Nepal,", "Nicaragua,", "Níger,", "Nigeria,", "Noruega,",
    "Nueva Zelanda,", "Omán,", "Países Bajos,", "Pakistán,", "Palaos,", "Panamá,", "Papúa Nueva Guinea,", "Paraguay,", "Perú,", "Polonia,", "Portugal,", "Reino Unido,",
    "República Centroafricana,", "República Checa,", "República del Congo,", "República Democrática del Congo,",
    "República Dominicana,", "Ruanda,", "Rumania,", "Rusia,", "Samoa,", "San Cristóbal y Nieves,",
    "San Marino,", "San Vicente y las Granadinas,", "Santa Lucía,", "Santo Tomé y Príncipe,", "Senegal,",
    "Serbia,", "Seychelles,", "Sierra Leona,", "Singapur,", "Siria,", "Somalia,", "Sri Lanka,", "Suazilandia,",
    "Sudáfrica,", "Sudán,", "Sudán del Sur,", "Suecia,", "Suiza,", "Surinam,", "Tailandia,", "Tanzania,",
    "Tayikistán,", "Timor Oriental,", "Togo,", "Tonga,", "Trinidad y Tobago,", "Túnez,", "Turkmenistán,",
    "Turquía,", "Tuvalu,", "Ucrania,", "Uganda,", "Uruguay,", "Uzbekistán,", "Vanuatu,", "Vaticano,",
    "Venezuela,", "Vietnam,", "Yemen,", "Yibuti,", "Zambia,", "Zimbabue,",
    "¿En qué país pasaste tus últimas vacaciones?", "pais", "En qué país", "pais?", "país?"]
    answers["Ubicación"] = ["He estado en Francia, es un país precioso. ¿Has volado o cómo has llegado hasta allí?",
    "Esta vez estaba en Italia. ¡Hay tanto que ver allí! ¿Fuiste en coche o cómo llegaste?",
    "Estuve en Portugal. ¡Nunca he estado allí! ¿Cómo has llegado hasta allí?", "He estado en Francia, es un país precioso.",
    "Esta vez estaba en Italia. ¡Hay tanto que ver allí!", "Estuve en Portugal. ¡Nunca he estado allí!"]
    answers2["Ubicación"] = ["He estado en Francia, es un país precioso."]
    remarks["Ubicación"] = ["¡Qué guay! ¿Cómo has llegado hasta allí?", "¡Qué guay! ¿Has volado o cómo has llegado hasta allí?",
    "¡Qué guay! ¿Fuiste en coche o cómo llegaste?"]

    # WIE HINGEKOMMEN
    keywords["Transporte"] = ["avión", "Volé", "volé", "vole", "volí","Vole", "Volí", "Volamos", "Fuimos en avión", "Fui en avión", "fui en avión", "fuimos en avión", "avion",
    "avión", "Avión", "Avion", "Fuimos en tren", "fuimos en tren", "tren", "Tren", "trén", "Trén", "Tomamos el tren", "Tomemos el tren", "tomamos el tren",
    "Fui en tren", "fui en tren", "coche", "Coche", "auto", "Auto", "bicicleta", "Bicicleta", "Bici", "bici", "bus", "Bus", "Autobus", "autobus", "autobús", "Autobús", "barco", "Barco",
    "¿Cómo has llegado hasta allí?"]
    answers["Transporte"] = ["He viajado en coche. ¿En qué mes fuiste de vacaciones por última vez?", "Viajé en tren. ¿En qué temporada fuiste de vacaciones?", "He viajado en coche.",
    "Viajé en tren."]
    answers2["Transporte"] = ["Viajé en tren."]
    remarks["Transporte"] = ["Ah, ya veo. ¿En qué mes fuiste de vacaciones por última vez?", "Vale, vale, lo entiendo. ¿En qué temporada fuiste de vacaciones?", "Ah, ya veo."]
    

    # fecha = date
    keywords["Fecha"] = ["fecha", "En junio", "En julio", "En agosto", "En septiembre", "En octubre", "En noviembre", "En deciembre" , "En enero", "En febrero",
    "En marzo", "En abril", "En mayo", "en junio", "en julio", "en agosto", "en septiembre", "en octubre", "en noviembre", "en deciembre", "diciembre" , "en enero",
    "en febrero", "en marzo", "en abril", "en mayo", "En verano", "En invierno", "En primavera", "En otoño", "en las vacaciones" , "En las vacaciones", "en mis vacaciones",
    "en navidad", "En navidad", "En las vacaciones de navidad", "en las vacaciones de navidad", "En la semana santa", "en la semana santa", "En la Semana Santa"]
    answers["Fecha"] = ["Estuve de vacaciones en primavera. El momento perfecto para viajar. ¿Te fuiste de vacaciones con tu familia o con otras personas?",
    "Estuve de vacaciones en noviembre. El momento perfecto para viajar. ¿Te fuiste de vacaciones con amigos o familiares?",
    "Estuve de vacaciones en Navidad. ¡Totalmente hermoso! ¿Con quién te fuiste de vacaciones?", "Estuve de vacaciones en primavera. El momento perfecto para viajar.",
    "Estuve de vacaciones en noviembre. El momento perfecto para viajar.", "Estuve de vacaciones en Navidad. ¡Totalmente hermoso!"]
    answers2["Fecha"] = ["Estuve de vacaciones en Navidad. ¡Totalmente hermoso!"]
    remarks["Fecha"] = ["Eso suena bien. ¿Te fuiste de vacaciones con tu familia o con otras personas?", "Eso suena bien. ¿Te fuiste de vacaciones con amigos o familiares?", "¿Con quién te fuiste de vacaciones?",
    "Eso suena bien."]

    # Compañía = company
    keywords["Compañía"] = ["familia","personas", "con tu", "amigos", "amigo", "relatives and common names", "familiares", "Prima", "prima", "quién", "con mis Padres", "Con mis padres", "Con mis Padres", "madre", "Madre",
    "padres", "Padres", "abuela", "Abuela", "abuelo", "Abuelo", "tío", "tio", "Tío", "Tio", "Primo", "primo", "familia", "Familia", 
    "compañero de fiestas", "compañera de fiestas", "amigo del alma", "amiga del alma", "amigo del corazón", "amiga del corazón", "amigo incondicional",
    "amiga incondicional", "compañero de aventuras", "compañera de aventuras", "amigo leal", "amiga leal", "amigo íntimo", "amiga íntima", "amigo de confianza", "amiga de confianza",
    "compañero de viaje", "compañera de viaje", "amigo del barrio", "amiga del barrio", "amigo del trabajo", "amiga del trabajo"]
    answers["Compañía"] = ["Me fui de vacaciones con mi abuela. Fue un poco agotador, ¡pero lo pagó casi todo!", "Me fui de vacaciones con mi hermana. ¡Funcionó muy bien!",
    "Me fui de vacaciones con mis padres, como todos los años.",
    "Me fui de vacaciones con mi abuela. Fue un poco agotador, ¡pero lo pagó casi todo! ¿Qué tiempo hizo en tus vacaciones?",
    "Me fui de vacaciones con mi hermana. ¡Funcionó muy bien! ¿Hizo buen o mal tiempo durante tus vacaciones?",
    "Me fui de vacaciones con mis padres, como todos los años. ¿Hacía frío o calor en tu destino de vacaciones?"]
    answers2["Compañía"] = ["Me fui de vacaciones con mis padres, como todos los años."]
    remarks["Compañía"] = ["Qué bien. ¿Qué tiempo hizo en tus vacaciones?", "Qué bien. ¿Hizo buen o mal tiempo durante tus vacaciones?", "¿Hacía frío o calor en tu destino de vacaciones?", "Qué bien."]

    
    # Tiempo = Weather
    keywords["Tiempo"] = ["tiempo", "grados","frío", "cálido", "fresco", "nublado", "buen tiempo", "calor", "Calor", "lluvia", "lluvia", "Lluvia", "Lluvia", "nieve", "neva",
    "nevó", "nevaba", "estaba nevando", "mucho calor", "Mucho calor", "viento", "mal tiempo", "El tiempo estaba mal", "Hizo buen tiempo", "hizo buen tiempo", "hizo mal tiempo",
    "Hacía mal tiempo", "hacía mal tiempo", "Hizo calor", "hizo calor", "había mucho sol", "Había mucho sol", "sol"]
    answers["Tiempo"] = ["El tiempo era increíblemente hermoso. Mucho sol y nada de lluvia. ¿Qué actividades realizaste durante sus vacaciones?",
    "El tiempo no era muy bueno. Estaba muy nublado y hacía frío. ¿Qué hiciste en tus vacaciones?",
    "El tiempo podría haber sido mejor. Había niebla todo el tiempo.", "El tiempo era fantástico. El sol brillaba todo el tiempo y hacía muchísimo calor."]
    answers2["Tiempo"] = ["El tiempo podría haber sido mejor. Había niebla todo el tiempo."]
    remarks["Tiempo"] = ["¿Qué actividades realizaste durante sus vacaciones?", "¿Qué hiciste en tus vacaciones?"]
    
    # Actividad = activity 
    keywords["Actividad"] = ["actividad", "escalada", "esquí", "museos", "visitar", "visité", "visitamos",
    "visitado", "Visitar", "senderismo", "Nadar en el mar", "nadar en el mar",
    "nadé", "nadamos", "nadado", "fui", "fuimos", "ido", "tomé", "tomamos", "tomado", "practiqué",
    "practicamos", "practicado", "asistí", "asistimos", "asistido", "Tener un picnic",
    "Hacer una degustación de vinos", "Ir de compras", "Tomar el sol en la playa", "Practicar deportes acuáticos",
    "Visitar un parque temático", "Asistir a conciertos o eventos culturales", "actividad", "escalada", "esquí",
    "museos", "visitar", "visité", "visitamos", "visitado", "Visitar", "senderismo", "Nadar en el mar", "nadar en el mar",
    "nadar", "nadé", "nadamos", "nadado", "fui", "fuimos", "ido", "tomé", "tomamos", "tomado", "practiqué", "practicamos",
    "practicado", "asistí", "asistimos", "asistido", "Tener un picnic", "degustación", "compras", "Tomar", "sol en la playa",
    "Practicar", "deportes", "acuáticos", "visitar", "parque", "asistir", "conciertos", "eventos", "culturales"]
    answers["Actividad"] = ["Hicimos surf, escalada y nadamos mucho en el mar.",
    "Hicimos mucho senderismo por las montañas, visitamos lugares de interés e hicimos un curso de cocina.",
    "Vimos muchos lugares de interés, fuimos a la playa todos los días y a menudo a la sauna.",
    "Hicimos surf, escalada y nadamos mucho en el mar. ¿Has aprendido algo nuevo en tus vacaciones?",
    "Hicimos mucho senderismo por las montañas, visitamos lugares de interés e hicimos un curso de cocina. ¿Has aprendido algo nuevo en tus vacaciones?",
    "Vimos muchos lugares de interés, fuimos a la playa todos los días y a menudo a la sauna. ¿Has aprendido algo nuevo en tus vacaciones?"]
    answers2["Actividad"] = ["Vimos muchos lugares de interés, fuimos a la playa todos los días y a menudo a la sauna."]
    remarks["Actividad"] = ["Casi me da envidia. ¿Has aprendido algo nuevo en tus vacaciones?", "Eso suena bien." ]
    # answers["Actividad"] = ["Visité el zoológico y tuve un picnic en el parque", "Fuimos de compras al centro comercial y tomé un helado",
    # "Practiqué mi deporte favorito, el tenis, en la cancha del hotel"]
    # remarks["Actividad"] = ["Esto suena interesante. Visité el zoológico y tuve un picnic en el parque",
    # "Esto parece interesante. Fuimos de compras al centro comercial y tomé un helado", "Esto parece divertido. Practiqué mi deporte favorito, el tenis, en la cancha del hotel"]

    # experiencias = experiences
    keywords["Experiencias"] = ["cultura", "nuevo", "nueva", "experiencia", "experiencias", "Experiencias", "idioma", "diferente", "Diferente"]
    answers["Experiencias"] = ["Aprendí muchísimo sobre la cultura del país. Es increíblemente interesante.",
    "Conocí a nuevas personas en mis vacaciones. Quiero encontrarme con ellos aquí.",
    "Conocí a nuevos chicos en mis vacaciones. El próximo año les visitaré.",
    "Aprendí muchísimo sobre la cultura del país. Es increíblemente interesante. ¿Qué es lo que más te ha gustado de tus vacaciones?",
    "Conocí a nuevas personas en mis vacaciones. Quiero encontrarme con ellos aquí. ¿Qué es lo que más te ha gustado de tus vacaciones?",
    "Conocí a nuevos chicos en mis vacaciones. El próximo año les visitaré. ¿Qué es lo que más te ha gustado de tus vacaciones?"]
    answers2["Experiencias"] = ["Conocí a nuevas personas en mis vacaciones. Quiero encontrarme con ellos aquí."]
    remarks["Experiencias"] = ["¡Es impresionante! :P ¿Qué es lo que más te ha gustado de tus vacaciones?"]

 
    # hermoso día = nicest day ### NEU BESONDERS GUT GEFALLEN
    keywords["Especial"] = ["especial"]
    answers["Especial"] = ["Me gustaron especialmente la cultura y la lengua del país.", "La gente de allí me pareció la mejor de todas las vacaciones.",
    "Me gustaron especialmente la cultura y la lengua del país.", "La gente de allí me pareció la mejor de todas las vacaciones."]
    answers2["Especial"] = ["Me gustaron especialmente la cultura y la lengua del país."]
    remarks["Especial"] = ["¡Qué guay! Parece una gran experiencia. ¡Espero volver a hablar contigo pronto!",
    "¡Qué bonito! Parece una gran experiencia. ¡Espero volver a hablar contigo pronto!",
    "Casi me da envidia. Parece una gran experiencia. ¡Espero volver a hablar contigo pronto!"]

    # # peor día = worst day
    # keywords["Peor día"] = ["peor día"]
    # answers["Peor día"] = ["general example like on the last day I saw I failed an exam"]
    # remarks["Peor día"] = ["dammmmnnnn"]

    # Atmósfera = atmosphere
    # keywords["Atmósfera"] = ["nice, loud, beautiful?"]
    # answers["Atmósfera"] = ["nice, loud, beautiful / +new question"]
    # remarks["Atmósfera"] = ["Oh Isee....question to next topic"]

    # fin = End
    keywords["Fin"] = ["adios", "Adios", "Adiós", "adiós", "Hasta luego", "hasta luego", "Nos vemos",
    "Chau", "chau", "nos vemos", "Bye", "bye", "adios!", "Adiós!", "adiós!", "Hasta luego!", "hasta luego!", "Nos vemos!",
    "Chau!", "chau!", "nos vemos!", "Bye!", "bye!"]
    answers["Fin"] = ["Todo esto me da mucha envidia. Encantado de haber charlado contigo. ¡Espero que podamos repetirlo pronto!",
    "¡Qué vacaciones más bonitas has pasado! Espero que volvamos a charlar pronto, me ha gustado mucho la conversación."]
    remarks["Fin"] = ["Todo esto me da mucha envidia. Encantado de haber charlado contigo. ¡Espero que podamos repetirlo pronto!",
    "¡Qué vacaciones más bonitas has pasado! Espero que volvamos a charlar pronto, me ha gustado mucho la conversación."]