import tkinter as tk
import time
import random

SIRINA = 9 # sirina mreze aplikacije
ISKANE_BESEDE=["samokolnica","avtomobil","konjušnica","samozadostnost",
               "obdarovanje","čebela","vrhunec","monopol","aktovka"]
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
prikazan_text = inicializacija_prikaza(len(trenutna_beseda))
stevilo_poskusov = 0 #možnih poskusov je 10
crke=["A","B","C","Č","D","E","F","G","H","I","J","K","L","M","N","O","P","R",
          "S","Š","T","U","V","Z","Ž"]

podnaslov=tk.Label(okno,text= "Izberi črko:").grid(row = dobi_vrstico(),columnspan = SIRINA)

# dodam gumbe za crke
zacetek_gumbov = dobi_vrstico()
for x in range(len(crke)):
    gumb = tk.Button(okno,text = crke[x]).grid(row = x // SIRINA + zacetek_gumbov,column = x % SIRINA)
row_count = zacetek_gumbov + len(crke)//SIRINA + 1 # nastavim da row_count kaze na pravilno vrstico

tk.Label(okno, text = "Iskana beseda:").grid(row = dobi_vrstico(),columnspan = SIRINA)

izpis_lab = tk.Label(okno, text = v_lep_izpis(prikazan_text),font = 2000).grid(row = dobi_vrstico(),
                                                                               columnspan = SIRINA)

