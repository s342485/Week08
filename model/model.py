class Model:
    def __init__(self):
        pass

    def calcola_anagrammi(self, parola):
        self._anagrammi = []

        # parola = lettere_rimanenti
        # anagramma parziale = ""
        self.ricorsione("", parola)
        return self._anagrammi

    def ricorsione(self, anagramma_parziale , lettere_rimanenti):
        #quando finisco? quando ho lettere rimanenti vuota
        if len(lettere_rimanenti) == 0:
            self._anagrammi.append(anagramma_parziale)
            return

        else:
            for i in range (len(lettere_rimanenti)):
                anagramma_parziale += lettere_rimanenti[i]
                nuove_lettere_rimanenti = lettere_rimanenti[:i] + lettere_rimanenti[i + 1:]
                self.ricorsione(anagramma_parziale, nuove_lettere_rimanenti)
                #BACKTRACKING = Ho finito di esplorare tutti gli anagrammi che iniziano con questa lettera, torno indietro e provo un’altra lettera"
                anagramma_parziale = anagramma_parziale[:-1] #TOLGO LA LETTERA CHE HO ESAMINATO


"""
    dog 
    idea: scelgo una lettera, genero tutti gli anagrammi delle lettere rimanenti
    d -> og | go  --> parole : dog | dgo
    o -> dg | gd  --> parole : odg | ogd
    g -> do | od  --> parole : gdo | god
    
    il numero di anagrammi è 3! (3 fattoriale) e quindi è corretto 3*2*1 = 6 anagrammi 
    di cui solo 2 sono parole con senso per il dizionario inglese
    
    
    OPPURE 
    
    prendo la prima lettera della parola dog 
    [d] di cui lettere rimanenti [og]
    faccio tutti gli anagrammi di d poi
    [do] di cui lettere rimanenti [g]
    [dog] di cui lettere rimanenti []
    """

