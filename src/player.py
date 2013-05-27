import util

class Player():
    
    def __init__(self, name):
        self.id = util.id_generator()
        self.state = 'Not Started'
        self.name = name
        self.units = []
        self.token = util.id_generator(12)
    
    def validate_token(self, token):
        return self.token == token
    
    def get_unit(self, unitid):
        for unit in self.units :
            if unit.id == unitid:
                return unit