import math
from turtle import * #turtle-Bibliothek

def heart_a(n): #berechnen die x-Koordinate für die Punkte, die das Herz abbilden
    return 15 * math.sin(n) ** 3

def heart_b(n):  #y-koordinate
    return 12 * math.cos(n) -5 *\
        math.cos(2*n) - 2 *\
        math.cos(3*n) - \
        math.cos(4*n)

tracer(2)#Geschwindigkeit 0 - max, 1 langsamer, andere - Zwischenstufen
bgcolor('black')# Hintergrund
for i in range(800):
    goto(heart_a(i)*15, heart_b(i)*15)#Bewegung des Turtles  x-,y-Koordinaten, um das Herz zu zeichnen
    for j in range(1):
        color('pink')#stiftfarbe z.b. red, purple
        hideturtle()#Versteckung des Kursors
        goto(0,0)#Turtle 
done #Ende+Offnung des Fenstens

    
        