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

# Meerdere trainingronden
# iedere volledige ronde door de dataset heet een epoch.


aantal_epochs = 10 # let op vanaf epoch geen fouten meer bij test data (validatie??)

for epoch in range(aantal_epochs):

    aantal_fouten = 0

    for trainingsvoorbeeld in training_data:

        lichaamslengte = trainingsvoorbeeld[0]
        lichaamsgewicht = trainingsvoorbeeld[1]
        juiste_antwoord = trainingsvoorbeeld[2]

        voorspelling, ml_waarde = voorspel(
            lichaamslengte,
            lichaamsgewicht
        )

        fout = juiste_antwoord - voorspelling

        if fout != 0:

            aantal_fouten = aantal_fouten + 1

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

    print(
        "Epoch:", epoch + 1,
        "- aantal fouten:", aantal_fouten
    )
# Getraind model bekijken 
print()
print("Getraind model:")
print("ML-weight lichaamslengte:", ml_weight_lichaamslengte)
print("ML-weight lichaamsgewicht:", ml_weight_lichaamsgewicht)
print("ML-bias:", ml_bias)


# INFERENCE
# Nieuwe data die niet tijdens het trainen is gebruikt


nieuwe_data = [
    [172, 68],
    [175, 72],
    [178, 76],
    [182, 82],
    [188, 88]
]

for nieuwe_persoon in nieuwe_data:

    lichaamslengte = nieuwe_persoon[0]
    lichaamsgewicht = nieuwe_persoon[1]

    voorspelling, ml_waarde = voorspel(
        lichaamslengte,
        lichaamsgewicht
    )

    print()
    print("Nieuwe persoon:", nieuwe_persoon)
    print("ML-waarde:", ml_waarde)
    print("Voorspelde klasse:", voorspelling)


# VALIDATIE/Test
# Deze data is niet gebruikt tijdens het trainen.
# De juiste antwoorden zijn wel bekend.


validation_data = [
    [173, 69, 0],
    [176, 73, 0],
    [179, 77, 1],
    [183, 83, 1],
    [187, 87, 1]
]

aantal_correct = 0

for validatievoorbeeld in validation_data:

    lichaamslengte = validatievoorbeeld[0]
    lichaamsgewicht = validatievoorbeeld[1]
    juiste_antwoord = validatievoorbeeld[2]

    voorspelling, ml_waarde = voorspel(
        lichaamslengte,
        lichaamsgewicht
    )

    print()
    print("Validatievoorbeeld:", validatievoorbeeld)
    print("ML-waarde:", ml_waarde)
    print("Voorspelling:", voorspelling)
    print("Juiste antwoord:", juiste_antwoord)

    if voorspelling == juiste_antwoord:
        aantal_correct = aantal_correct + 1

print()
print("Aantal correct:", aantal_correct)
print("Totaal aantal validatie/test voorbeelden:", len(validation_data))
accuracy = aantal_correct / len(validation_data) * 100
print("Accuracy:", accuracy, "%")