import turtle as t #Turtle-Grafikbibliothek
t.speed(0)# maximale Gescwindichkeit
t.bgcolor('black')#Farbe vom Hintergrund
t.color('aqua')#Farbe von Kreisen
t.hideturtle()#Versteckung des Cursors
for i in range(160):
    t.circle(i-5)#Zeichen eines Kreises mit einem sich ändernden Radius (jedes mal i - 5)
    t.left(5)#Dreht den Turtle um 5 Grad nach links, 5, 15,100
t.done# Ende+oddnet Fenster

