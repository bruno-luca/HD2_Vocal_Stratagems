stratagems = {
    # MISC
    "rinforzo": "udrlu",
    "rifornimento": "ddur",
    "hell bomb": "duldurdu",
    "ricarica eagle": "uulur",
    "artiglieria della fast" : "ruud",

    # CENTRO AMMINISTRATIVO PATRIOTTICO
    "mitragliatrice": "",
    "fucile antimateria": "dlrud",
    "vigoroso": "dlduul",
    "anticarro consumabile": "",
    "fucile senza rinculo": "",
    "lanciafiamme": "",
    "cannone automatico": "",
    "mitragliatrice pesante": "",
    "lanciarazzi ad esplosione aerea": "",
    "cannone a rotaia": "drdulr",
    "lancia": "ddudd",

    # CANNONI ORBITALI
    "sbarramento orbitale gatling": "rdluu",
    "attacco orbitale con esplosione aerea": "rrr",
    "sbarramento orbitale da 120": "rrdlrd",
    "sbarramento orbitale da 380": "rduuldd",
    "sbarramento orbitale mobile": "rdrdrd",
    "laser orbitale": "rdurd",
    "cannone a rotaia orbitale": "ruddr",

    # HANGAR
    "mitragliamento a tappeto eagle": "urr",
    "attacco aereo eagle": "urdr",
    "bomba a grappolo eagle": "urddr",
    "attacco aereo con napalm eagle": "urdu",
    "jetpack": "duudu",
    "attacco fumogeno eagle": "urud",
    "missili eagle da 110": "urul",
    "bomba eagle da 500": "urddd",

    # PONTE
    "attacco orbitale di precisione": "rru",
    "attacco orbitale gas": "rrdr",
    "attacco orbitale elettromagnetico": "rrld",
    "barriera fumogena": "rrdu",
    "postazione per mitragliatrice pesante": "dulrrl",
    "relay generatore di scudi": "ddlrlr",
    "torre tesla": "durulr",

    # OFFICINA DI INGEGNERIA
    "campo mine antiuomo": "",
    "pacco rifornimenti": "",
    "lanciagranate": "",
    "cannone laser": "",
    "mine incendiarie": "",
    "rover cane da guardia": "",
    "zaino scudo antiproiettile": "",
    "fulminatore": "",
    "cannone quasar": "",
    "pacchetto generatore di scudi": "",

    # LAB DI ROBOTICA
    "sentinella mitragliatrice": "",
    "sentinella gatling": "",
    "sentinella con mortaio": "",
    "cane da guardia": "",
    "sentinella con cannone automatico": "",
    "sentinella con razzo": "",
    "sentinella con mortaio elettromagnetico": "",
    "esoscheletro patriota": ""
}

key_map = {
    "u": "u",
    "d": "d",
    "r": "r",
    "l": "l"
}

def call_stratagem(s):
    command = stratagems.get(s)
    print(f"Calling stratagem [{s.upper()}]: {command}")