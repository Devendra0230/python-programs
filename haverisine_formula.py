from math import asin, cos, radians, sin, sqrt


class haversine():
    def __init__(self):
        slat = float(input("Enter starting latitude value: "))
        slong = float(input("Enter starting longitude value"))
        elat = float(input("Enter ending latitude value"))
        elong = float(input("Enter ending longitude value"))

        slat = radians(slat)
        elat = radians(elat)
        slong = radians(slong)
        elong = radians(elong)

        #Haversine formula
        dlon = elong - slong
        dlat = elat - slat

        a = sin(dlat/2)**2 + cos(slat) * cos(elat) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))
        r = 6371

        print(c*r)
        
show = haversine()

