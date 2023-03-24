import csv
import webbrowser

with open("prefijos.csv", newline="") as table:
    countries = csv.reader(table, quotechar="|")
    country = input(
        "Ingrese el país en español, inglés o francés: "
    ).capitalize()
    for row in countries:
        if country in row[0] or country in row[1] or country in row[2]:
            code = str(row[5])
            break

number = input("Ingrese un número de teléfono: ")
webbrowser.open("https://api.whatsapp.com/send?phone=" + code + number)
