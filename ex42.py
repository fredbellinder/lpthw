class Vehicle(object):
    def __init__(self, type, regnr):
        self.type = type
        self.regnr = regnr

    def getRegNr(self):
        return self.regnr

    def getType(self):
        return self.type


class Motorcycle(Vehicle):
    def __init__(self, type, regnr, brand):
        self.brand = brand
        Vehicle.__init__(self, type, regnr)

    def getBrand(self):
        return self.brand


class Onroad(Motorcycle):
    def __init__(self, type, regnr, brand, colour, cc, style, model, sold):
        Motorcycle.__init__(self, type, regnr, brand)
        self.colour = colour
        self.cc = cc
        self.style = style
        self.model = model
        self.sold = sold


versys = Onroad('MC', 'HMB016', 'Kawasaki',
                'green', '650', 'Touring', 'Versys', False)
xsr700 = Onroad('MC', 'MAY395', 'Yamaha',
                'british racing green', '700', 'UJM', 'XSR700', True)

# print(versys.style)
# print(xsr700.getRegNr(), xsr700.__hash__())


class Person(object):
    def __init__(self, persnr):
        self.persnr = persnr


class Joker(object):
    def tellJoke(self):
        return "two chickens crossed the road, yada yada yada..."


class BikeOwner(Person, Joker):
    def __init__(self, persnr, fname, lname, gender):
        self.fname = fname
        self._lname = lname
        self.gender = gender
        self.bike = None


fred = BikeOwner("Fred", "Bellinder", "Man", "19860829-4818")

fred.bike = versys
onny = fred.bike.__hash__()
twoey = versys.__hash__()
print(onny == twoey)
print(fred.bike.__hash__() == (fred.bike.__hash__()))

print(dir(fred))
print(fred.bike.type)

del fred.bike
print(dir(fred))


print(fred.tellJoke())
