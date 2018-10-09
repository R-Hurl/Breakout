from graphics import Circle, Rectangle, Point

def circleRectIntersect(circle,rectangle):
    ### Python algorithm for intersection of a circle and rectangle created as
    ### a hybrid of several postings show on the following webpage at StackOverflow
    ### http://stackoverflow.com/questions/401847/circle-rectangle-collision-detection-intersection

    ccx = circle.getCenter().getX()
    ccy = circle.getCenter().getY()
    cr = circle.getRadius()

    if rectangle.getP1().getX() < rectangle.getP2().getX():
        rlx = rectangle.getP1().getX()
        rrx = rectangle.getP2().getX()
    else:
        rlx = rectangle.getP2().getX()
        rrx = rectangle.getP1().getX()

    if rectangle.getP1().getY() < rectangle.getP2().getY():
        rty = rectangle.getP1().getY()
        rby = rectangle.getP2().getY()
    else:
        rty = rectangle.getP2().getY()
        rby = rectangle.getP1().getY()

    #determine if center point is left, right or within the width range of the rectangle
    if ccx < rlx:
        #closest to left
        closestX = rlx
        side = "left"
    elif ccx > rrx:
        #closest to right
        closestX = rrx
        side = "right"
    else:
        #circle center is in width range of the rectangle
        closestX = ccx
        side = "inrange"

    #determine if center point is above, below or within the height range of the rectangle
    if ccy < rty:
        #closest to top
        closestY = rty
        tb = "top"
    elif ccy > rby:
        #closest to bottom
        closestY = rby
        tb = "bottom"
    else:
        #circle center is in height range of the rectangle
        closestY = ccy
        tb = "inrange"
    
    # Calculate the distance between the circle's center and the closest points in rectangle
    dx = closestX - ccx
    dy = closestY - ccy
    
    # If the distance is less than the circle's radius, an intersection occurs
    if (dx * dx + dy * dy) <= cr * cr:
        #intersection happened, now determine which side we hit
        if side == "inrange":
            return tb
        else: return side
    else:
        #no intersection
        return "no"
