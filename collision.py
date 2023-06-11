def mouseCollision(Ax, Ay, Bx, By, Bwidth, Bheight):
    return (Ax >= Bx and Ax <= Bx + Bwidth) and (Ay >= By and Ay <= Ay <= By + Bheight)
    
def rectCollision(Ax, Ay, Awidth, Aheight, Bx, By, Bwidth, Bheight):
    return (Ax + Awidth > Bx) and (Ax < Bx + Bwidth) and (Ay + Aheight > By) and (Ay < By + Bheight)

def lineCollision(Alines, Bx, By, Bwidth, Bheight):
    for line in Alines:
        if rectCollision(line[0], line[1], line[2], line[3], Bx, By, Bwidth, Bheight):
            return line[4]

