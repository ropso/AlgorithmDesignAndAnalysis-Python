class Goat(object):
    def __init__(self,tail):
        super().__init__(self)
        self._tail=tail
    def milk(self):
        pass
    def jump(self):
        pass
    
class Pig(object):
    def __init__(self,nose):
        super().__init__(self)
        self._nose=nose

class Horse(object):
    def __init__(self,height,color):
        super().__init__(self)
        self._height=height
        self._color=color

    def jump(self):
        pass

    def run(self):
        pass


class Racer(Horse):
    def __init__(self,height,color,isracer):
        super().__init__(self,height,color)
        self._isracer=isracer
    def race(self):
        print("racer horse like like a pro bono champion")
    __slots__='_isracer'
    
