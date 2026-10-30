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



# Mijn eerste training voorbeeld. handmatig alleen voor een test.


lichaamslengte = 160
lichaamsgewicht = 55
juiste_antwoord = 0

voorspelling, ml_waarde = voorspel(
    lichaamslengte,
    lichaamsgewicht
)

fout = juiste_antwoord - voorspelling

print("Voor training:")
print("ML-waarde:", ml_waarde)
print("Voorspelling:", voorspelling)
print("Juiste antwoord:", juiste_antwoord)
print("Fout:", fout)

# Alle drie de parameters aanpassen
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

print()
print("Model na training:")
print("ML-weight lichaamslengte:", ml_weight_lichaamslengte)
print("ML-weight lichaamsgewicht:", ml_weight_lichaamsgewicht)
print("ML-bias:", ml_bias)

# Controle: hetzelfde voorbeeld opnieuw voorspellen
nieuwe_voorspelling, nieuwe_ml_waarde = voorspel(
    lichaamslengte,
    lichaamsgewicht
)

print()
print("Controle na training:")
print("Nieuwe ML-waarde:", nieuwe_ml_waarde)
print("Nieuwe voorspelling:", nieuwe_voorspelling)
print("Juiste antwoord:", juiste_antwoord)