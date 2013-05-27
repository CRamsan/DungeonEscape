import util

class Unit():
    
    def __init__(self, type):
        self.id = util.id_generator()
        self.condition = 'Normal'
        self.x = None
        self.y = None
    