class Flower:
    '''class name:Flower, make a Flower name
    constructors:
        a.parametrised counstructor:
            Flower(name,no_of_petals,Price)->3args
            args type(str,int,float)
    datamembers:
    1.name
    2.nopetals
    3.price
    memberfunction:
    1. get_flower_name
    2. get_no_of_petal
    3. get_price
    4. set_name
    5. set_no_of_petals
    6. set_price
     '''
    def __init__(self,name,nopetals,price):
        if type(nopetals) != int or type(price)not in (float,int):
            raise ValueError("please provide aapropriate arguments")

        self._name=name
        self._nopetals=nopetals
        self._price=price

    def get_details(self):
        return ("the name of flower is "+str(self._name)+" the no of petalns\n"+str(self._nopetals)+"\nFlower price"+str(self._price))



if __name__=="__main__":
    Flower1=Flower("jasmin",190,300)
    print(Flower1.get_details())
    # test 1
    Flowerr2=Flower("Rose",23,45.90)
    print(Flowerr2.get_details())
