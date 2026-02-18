name = input("Wie heist du?")
alter = int(input("Wie alt bist du?"))
wohnort = input("Wo wohnst du?")

if alter < 18:
     print("Du bist noch nicht volljährig - bleib brav")



else:
     print("Willkommen in der Welt der Erwachsenen")


     print("Hallo", name)
     print ("In 10 Jahren bist du",alter+10,"Jahre alt")
     print("Du wohnst also in", wohnort)

input("Drücke Enter zum beenden")