import json

# Lista dei voti
voti = [2, 4]

# Creiamo la struttura che vogliamo
data = {
    "materia": [{"Voto": voto} for voto in voti]
}

# Salviamo nel file JSON
with open("dati.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)



with open("dati.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# aggiorni il campo 'materia'
voti = [2, 4]
data["materia"] = [{"Voto": voto} for voto in voti]

with open("dati.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)


# Lista dei voti
voti = [2, 4]

# 1️⃣ Leggi il file JSON (se già esiste)
try:
    with open("dati.json", "r", encoding="utf-8") as file:
        data = json.load(file)
except FileNotFoundError:
    data = {}  # se il file non esiste, crea un dizionario vuoto

# 2️⃣ Assicurati che il campo 'studente' esista
if "studente" not in data:
    data["studente"] = {}

# 3️⃣ Inserisci i voti nel campo 'materia'
data["studente"]["materia"] = [{"Voto": voto} for voto in voti]

# 4️⃣ Salva di nuovo il file
with open("dati.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)


voti_nuovi = [6, 8]

# crea la struttura se non esiste
data.setdefault("studente", {}).setdefault("materia", [])

# aggiunge i nuovi voti alla lista esistente
data["studente"]["materia"].extend([{"Voto": voto} for voto in voti_nuovi])

--------------------------

df = pd.read_csv("studenti.csv")


data = {"studenti": {}}

for _, row in df.iterrows():
    nome = row["nome"]
    materia = row["materia"]
    voto = row["voto"]

    # crea struttura se non esiste
    data["studenti"].setdefault(nome, {}).setdefault("materie", [])

    # aggiungi il voto nella lista materie
    data["studenti"][nome]["materie"].append({
        "nome": materia,
        "Voto": voto
    })
