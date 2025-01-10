import tkinter as tk
from random import randint

Campo_minato = tk.Tk()
Campo_minato.title("Campo Minato")

colonne = 20
righe = 13
prima = True
BOMBE = 50

# Inizializzazione griglia
griglia = [[0 for x in range(colonne)] for j in range(righe)]
for a in griglia:
    print(a)

def cerca_bombe():
    global griglia
    for i in range(righe):
        for j in range(colonne):
            if griglia[i][j] != -1:
                c=0
                if i > 0 and griglia[i-1][j-1] == -1:
                    c+=1
                if i > 0 and griglia[i-1][j] == -1:
                    c+=1
                if i > 0 and j < colonne-1 and griglia[i-1][j+1] == -1:
                    c+=1
                if j > 0 and griglia[i][j-1] == -1:
                    c+=1
                if j < colonne-1 and griglia[i][j+1] == -1:
                    c+=1
                if i < righe-1 and j>0 and griglia[i+1][j-1] == -1:
                    c+=1
                if i < righe-1 and griglia[i+1][j] == -1:
                    c+=1
                if i < righe-1 and j < colonne - 1 and griglia[i+1][j+1] == -1:
                    c+=1
                griglia[i][j] = c

    for a in griglia:
        print(a)
    

def bandiera(evento):
    cella = evento.widget
    for x in range(righe):
        for j in range(colonne):
            if pulsanti[x][j] == cella:
                riga = x
                colonna = j
    pulsanti[riga][colonna].config(text="🚩")

def zero(riga,colonna):

    for i in range(-1, 2):
        if i+riga<0:
            continue
        if i+riga>righe-1:
            break
        for k in range(-1, 2):
            if k+colonna<0:
                continue
            if k+colonna>colonne-1:
                break
            if pulsanti[i+riga][k+colonna].cget("text") == "" and griglia[i+riga][k+colonna]!=-1:
                if (i+riga+k+colonna)%2 == 0:
                    colore = "gray72"
                else: 
                    colore = "gray64"
                pulsanti[i+riga][k+colonna].config(bg=colore, text=griglia[i+riga][k+colonna])
                if griglia[i+riga][k+colonna]==0:
                    zero(i+riga,k+colonna)
                                            

def scopri(evento):
    global griglia, pulsanti, prima
    cella = evento.widget
    for x in range(righe):
        for j in range(colonne):
            if pulsanti[x][j] == cella:
                riga = x
                colonna = j
    if prima:
        prima = False
        crea_bombe(riga, colonna)
        cerca_bombe()
        for x in range(righe):
            for j in range(colonne):
                if pulsanti[x][j]==pulsanti[riga][colonna]:
                    if (j + x) % 2 == 0:
                        colore = "gray72"
                    else:
                        colore = "gray64"
                    pulsanti[riga][colonna].config(bg=colore, text=griglia[riga][colonna])
                    if griglia[riga][colonna]==0:
                        zero(riga,colonna)
                    
    if griglia[riga][colonna] != -1:
        for x in range(righe):
            for j in range(colonne):
                if pulsanti[x][j]==pulsanti[riga][colonna]:
                    if (j + x) % 2 == 0:
                        pulsanti[riga][colonna].config(bg="gray72", text=griglia[riga][colonna])
                        if griglia[riga][colonna]==0:
                            zero(riga,colonna)
                    else:
                        pulsanti[riga][colonna].config(bg="gray64", text=griglia[riga][colonna])
                        if griglia[riga][colonna]==0:
                            zero(riga,colonna)
    else:
        for i in range(righe):
            for j in range(colonne):
                if griglia[i][j]==-1:
                    pulsanti[i][j].config(text="💣")

def crea_bombe(r1, c1):
    global griglia
    for _ in range(BOMBE):
        r, c = r1, c1
        while r == r1 and c == c1 or griglia[r][c] == -1:
            r = randint(0, righe - 1)
            c = randint(0, colonne - 1)
        griglia[r][c] = -1

pulsanti = [[None for x in range(colonne)] for j in range(righe)]
for x in range(righe):
    for j in range(colonne):
        cella = tk.Button(Campo_minato, height=2, width=4)
        cella.bind("<Button-1>", scopri)
        cella.bind("<Button-3>", bandiera)
        if (j + x) % 2 == 0:
            cella.config(bg="green3")
        else:
            cella.config(bg="green2")
        cella.grid(row=x, column=j)
        pulsanti[x][j] = cella

Campo_minato.mainloop()