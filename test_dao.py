from database.DAO import DAO
from model.model import Model

dao = DAO()
model = Model()

risultati = dao.get_anagrammi_corretti()

for r in risultati:
    print(r)