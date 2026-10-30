# features + labels (data + answer)
training_data = [
    [160, 55, 0],
    [165, 60, 0],
    [170, 65, 0],
    [180, 80, 1],
    [185, 85, 1],
    [190, 90, 1]
]

# modelstructuur: nog niet getraind
ml_weight_lichaamslengte = 0.0
ml_weight_lichaamsgewicht = 0.0
ml_bias = 0.0

# learning rate = grootte van één aanpassing
learning_rate = 0.001


def voorspel(lichaamslengte, lichaamsgewicht):
    ml_waarde = (
        lichaamslengte * ml_weight_lichaamslengte
        + lichaamsgewicht * ml_weight_lichaamsgewicht
        + ml_bias
    )

    if ml_waarde >= 0:
        voorspelling = 1
    else:
        voorspelling = 0

    return voorspelling, ml_waarde



# EEN VOLLEDIGE TRAININGSRONDE (epoch)
# ik loop een keer door alle trainingsvoorbeelden.


for trainingsvoorbeeld in training_data:

    lichaamslengte = trainingsvoorbeeld[0]
    lichaamsgewicht = trainingsvoorbeeld[1]
    juiste_antwoord = trainingsvoorbeeld[2]

    # Voorspelling maken met het huidige model
    voorspelling, ml_waarde = voorspel(
        lichaamslengte,
        lichaamsgewicht
    )

    # Fout berekenen
    fout = juiste_antwoord - voorspelling

    print()
    print("Trainingsvoorbeeld:", trainingsvoorbeeld)
    print("ML-waarde:", ml_waarde)
    print("Voorspelling:", voorspelling)
    print("Juiste antwoord:", juiste_antwoord)
    print("Fout:", fout)

    # Alleen aanpassen als de voorspelling fout is
    if fout != 0:

        ml_weight_lichaamslengte = (
            ml_weight_lichaamslengte
            + fout * lichaamslengte * learning_rate
        )

        ml_weight_lichaamsgewicht = (
            ml_weight_lichaamsgewicht
            + fout * lichaamsgewicht * learning_rate
        )

        ml_bias = (
            ml_bias
            + fout * learning_rate
        )

        print("Model aangepast")

print()
print("Model na één volledige trainingsronde:")
print("ML-weight lichaamslengte:", ml_weight_lichaamslengte)
print("ML-weight lichaamsgewicht:", ml_weight_lichaamsgewicht)
print("ML-bias:", ml_bias)

"""
voorbeeld 1
→ voorspellen
→ fout
→ parameters aanpassen

voorbeeld 2
→ gebruikt de aangepaste parameters van voorbeeld 1
→ fout
→ parameters opnieuw aanpassen

voorbeeld 3
→ gebruikt weer het nieuwste model

enzovoort...
"""


# Controle na één epoch
# ik test alle trainingsvoorbeelden met het huidige model.


print()
print("Controle van het getrainde model na epoch 1:")

for trainingsvoorbeeld in training_data:

    lichaamslengte = trainingsvoorbeeld[0]
    lichaamsgewicht = trainingsvoorbeeld[1]
    juiste_antwoord = trainingsvoorbeeld[2]

    voorspelling, ml_waarde = voorspel(
        lichaamslengte,
        lichaamsgewicht
    )

    print()
    print("Trainingsvoorbeeld:", trainingsvoorbeeld)
    print("ML-waarde:", ml_waarde)
    print("Voorspelling:", voorspelling)
    print("Juiste antwoord:", juiste_antwoord)