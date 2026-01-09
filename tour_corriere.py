import copy


class Tour_corriere:
    def __init__(self):
        self._soluzioni = []

    def calcola_percorso_migliore(self, N, partenza, zone_fredde):
        self.ricorsione([partenza], N, zone_fredde)


    def ricorsione(self, parziale, N, zone_fredde):
        if len(parziale) == N*N:
            print(parziale)
            self._soluzioni.append(copy.deepcopy(parziale))
            return
        else:
            for row in range(N):
                for col in range(N):
                    parziale.append((row, col))
                    if self.is_ammissibile(parziale, zone_fredde):
                        self.ricorsione(parziale, N, zone_fredde)
                    parziale.pop()



    def is_ammissibile(self, parziale, zone_fredde):
        ultimo = parziale[-1]
        penultimo = parziale[-2]
        for regina in parziale[:len(parziale) - 1]:
            if ultimo[0] == regina[0] and ultimo[1] == regina[1]:
                return False #perche vuol dire che c'è ne un altro uguale, il corriere non può passare dallo stesso punto
            if ultimo in zone_fredde and penultimo in zone_fredde:
                return False # il corriere non può passare in due zone fredde in modo consecutivo

        return True

if __name__ == '__main__':
    tc = Tour_corriere()
    N = 2 #numero grandezza della citta
    zone_fredde = {(0, N-1), (N-1, 0)} #non posso entrare in zone fredde una vicino all'altra
    partenza = (1,1)
    tc.calcola_percorso_migliore(N, partenza, zone_fredde)

