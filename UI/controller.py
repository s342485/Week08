import flet as ft
from database.DAO import DAO

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self.anagrammi_corretti = []
        self.anagrammi_errati = []

    def calcola_anagrammi(self, e):
        parola = self._view.txt_word.value
        if parola == "":
            self._view.create_alert("Inserisci una parola")
        else:
            anagrammi = self._model.calcola_anagrammi(parola)
            self.anagrammi_corretti, self.anagrammi_errati = self.calcolo_anagrammi_corretti(anagrammi)

            for anagramma in self.anagrammi_corretti:
                self._view.lst_correct.controls.append(ft.Text(anagramma))

            for anagramma in self.anagrammi_errati:
                self._view.lst_wrong.controls.append(ft.Text(anagramma))

            self._view.update_page()


    def reset(self, e):
        self._view.lst_correct.controls.clear()
        self._view.lst_wrong.controls.clear()
        self._view.txt_word.value = ""
        self._view.update_page()

    @staticmethod
    def calcolo_anagrammi_corretti(anagrammi):
        dao = DAO()
        anagrammi_db  = dao.get_anagrammi_corretti()
        anagrammi_corretti = []
        anagrammi_errati = []

        for anagramma in anagrammi:
            if anagramma not in anagrammi_db:
                anagrammi_errati.append(anagramma)
            else:
                anagrammi_corretti.append(anagramma)


        return anagrammi_corretti, anagrammi_errati

