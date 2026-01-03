import copy

class NRegine:
    def __init__(self):
        self._num_soluzioni = 0
        self._num_iterazioni = 0
        self._soluzioni = []

    def _risolvi_n_regine(self, N):
        self._num_soluzioni = 0
        self._num_iterazioni = 0
        self._soluzioni = []

        self._ricorsione([],N)


    def _ricorsione(self, parziale, N):
        self._num_iterazioni += 1

        #caso terminale
        if len(parziale) == N:
            if self._soluzione_nuova(parziale):
                self._num_soluzioni += 1
                self._soluzioni.append(copy.deepcopy(parziale))

        #caso ricorsivo
        else:
            for row in range(N):
                for col in range(N):
                    parziale.append((row, col))  #appendo una tupla (riga, colonna)
                    if self._nuova_regina_ammissibile(parziale):
                        self._ricorsione(parziale, N)
                    parziale.pop() # backtracking, rimuove l'ultima regina aggiunta

    def _nuova_regina_ammissibile(self, parziale):
        # True se è ammissibile, False altrimenti
        ultima_regina = parziale[-1]
        for regina in parziale[:len(parziale)-1]: #tutte le regine prima dell'ultima
            #controllare riga (ricordiamo che ogni regina è una tupla (0, 1) dove 0 è la riga, 1 è la colonna
            if ultima_regina[0] == regina[0]:
                return False
            #controllare colonna
            if ultima_regina[1] == regina[1]:
                return False
            #controllare diagonale \
            if (ultima_regina[0] - ultima_regina[1]) == (regina[0] - regina[1]):
                return False
            #controllare diagonale /
            if (ultima_regina[0] + ultima_regina[1]) == (regina[0] + regina[1]):
                return False

        return True

    def _soluzione_nuova(self, soluzione_nuova):
        for soluzione in self._soluzioni:
            for regina in soluzione_nuova:
                if regina in soluzione:
                    return False

        return True

    #OSS: SOLUZIONI SALVA TUTTE LE N POSIZIONI DI N REGINE, SE QUESTA SOLUZIONE E' GIA' STATA SCRITTA VIENE SCARTATA







if __name__ == '__main__':
    nr = NRegine()
    nr._risolvi_n_regine(4)
    print(f"Trovate {nr._num_soluzioni} soluzioni")
    print(f"Trovate {nr._num_iterazioni} iterazioni")
    print(nr._soluzioni)


