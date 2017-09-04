import tkinter as tk
import time
import random

SIRINA = 9 # sirina mreze aplikacije
ISKANE_BESEDE=["SAMOKOLNICA","AVTOMOBIL","KONJUŠNICA","SAMOZADOSTNOST",
               "OBDAROVANJE","ČEBELA","VRHUNEC","MONOPOL","AKOTVKA"]
row_count = 0 # v kateri vrstici bodo novi gumbi
def dobi_vrstico():
    global row_count
    row_count += 1
    return row_count - 1
HANGMAN = (

"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
""")

def inicializacija_prikaza(dolzina_besede):
    beseda = []
    for x in range(dolzina_besede):
        beseda.append('_')
    return beseda

def v_lep_izpis(beseda_seznam):
    izpis = beseda_seznam[0]
    for x in range(1,len(beseda_seznam)):
        izpis += " " + beseda_seznam[x]
    return izpis

okno=tk.Tk()
okno.title("Vislice")
naslov=tk.Label(okno,text= "ČAS JE ZA VISLICE!!!", fg="blue").grid(row = dobi_vrstico(),columnspan = SIRINA)
naslov1 = tk.Label(okno, text = "Pozdravljeni v igrici Zabavne vislice.\n"
                   +"Na voljo za vsako besedo imate 10 poskusov, po tem pa ste obešeni...\n"+
                   "Ste pripravljeni?", fg = "red").grid(row = dobi_vrstico(),columnspan = SIRINA)

izrecene_crke =''
trenutna_beseda = ISKANE_BESEDE[0] #prototip
array_beseda = inicializacija_prikaza(len(trenutna_beseda))
stevilo_poskusov = 0 #možnih poskusov je 10
crke=["A","B","C","Č","D","E","F","G","H","I","J","K","L","M","N","O","P","R",
          "S","Š","T","U","V","Z","Ž"]

podnaslov=tk.Label(okno,text= "Izberi črko:").grid(row = dobi_vrstico(),columnspan = SIRINA)

# dodam gumbe za crke
zacetek_gumbov = dobi_vrstico()
for x in range(len(crke)):
    tk.Button(okno,text = crke[x], command = lambda crka=crke[x]: preveri_crko(crka)).grid(row = x // SIRINA
                        + zacetek_gumbov,column = x % SIRINA) # problemi z lambda
row_count = zacetek_gumbov + len(crke)//SIRINA + 1 # nastavim da row_count kaze na pravilno vrstico

tk.Label(okno, text = "Iskana beseda:").grid(row = dobi_vrstico(),columnspan = SIRINA)

izpis = tk.StringVar()
izpis.set(v_lep_izpis(array_beseda))
izpis_lab = tk.Label(okno, textvariable = izpis,font = 2000).grid(row = dobi_vrstico(),
                                                                         columnspan = SIRINA)
visl_text = [tk.StringVar(),0]
visl_text[0].set(HANGMAN[0])
vislica = tk.Message(okno, textvariable = visl_text[0],font = 2000).grid(row = dobi_vrstico(),
                                                                         columnspan = SIRINA)
def preveri_crko(crka):
    global izrecene_crke
    global trenutna_beseda
    global array_beseda
    global visl_text

    if crka in izrecene_crke:
        return
    izrecene_crke += crka
    if crka not in trenutna_beseda:
        visl_text[1] += 1
        visl_text[0].set(HANGMAN[visl_text[1]])
        return
    
    for x in range(len(trenutna_beseda)):
        if(crka == trenutna_beseda[x]):
            array_beseda[x] = crka
    izpis.set(v_lep_izpis(array_beseda))


