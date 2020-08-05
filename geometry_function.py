class SpecialFunction:

    #Calculating the middle of the line
    def middle_section(a, b):

     x = (a[0] + b[0])//2
     y = (a[1] + b[1])//2
     return f"Środek odcinka ma współrzędne X: {x} Y: {y}"


    #Check for collisions between two rectangles - zakładając, że użytkownik posiada wszystkie dane na temat
    #współrzędnych prostokątów
    def collision_between_rectangles(a, b):
        if (a[0] <= b[0] <= a[2]) and (a[1] <= b[1] <= a[3]):
            return "Kolizja wystepuje"

        elif (b[0] <= a[0] <= b[2]) and (b[1] <= a[1] <= b[3]):
            return "Kolizja wystepuje"

        else:
            return "Kolizja nie występuje"

#dane testowe do metody middle_section Przykład: c = (x, y) punktu na układzie współrzędnym
c = (-25, 2)
d = (17, 12)

#dane testowe do metody collision_between_rectangles Przykład: e = (Ax1, Ay1, Bx2, By2) dwa pierwsze argumenty to są
#współrzędne pierwszego wierchołka boku AB, kolejne dwa argumty to są współdzędne drugiego wierzchołka boku AB
e = (1,2,4,2)
f = (2,2,5,2)
k = SpecialFunction
print(k.middle_section(c,d))
print(k.collision_between_rectangles(f,e))