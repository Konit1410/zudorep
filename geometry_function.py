class SpecialFunction:

    #Calculation of the center of a line on the coordinate system
    def middle_section(a, b):

     x = (a[0] + b[0])//2
     y = (a[1] + b[1])//2
     return f"Middle X: {x} Y: {y}"


    #Checks for collisions between rectangles on the coordinate system
    def collision_between_rectangles(a, b):
        if (a[0] <= b[0] <= a[2]) and (a[1] <= b[1] <= a[3]):
            return "Collision"

        elif (b[0] <= a[0] <= b[2]) and (b[1] <= a[1] <= b[3]):
            return "Collision"

        else:
            return "There is no collision"
