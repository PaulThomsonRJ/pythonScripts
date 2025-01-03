class Combatant:
    def __init__(self, attack: list, sustain_damage: bool = False, damaged: bool = False, anti_fighter_barrage: list = [], cost: float = 0.0):
        self.attack = attack
        self.sustain_damage = sustain_damage
        self.damaged = damaged
        self.anti_fighter_barrage = anti_fighter_barrage
        self.cost = cost

class Cruiser(Combatant):
    def __init__(self):
        super().__init__(attack=[7], cost=2)
    
class Carrier(Combatant):
    def __init__(self):
        super().__init__(attack=[9], cost=3)

class Fighter(Combatant):
    def __init__(self):
        super().__init__(attack=[9], cost=0.5)
    
class Destroyer(Combatant):
    def __init__(self):
        super().__init__(attack=[9], anti_fighter_barrage=[9, 9], cost=1)
    
class Infantry(Combatant):
    def __init__(self):
        super().__init__(attack=[8], cost=0.5)
