class Combatant:
    def __init__(self, attack: list, sustain_damage: bool = False, damaged: bool = False, anti_fighter_barrage: list = [], cost: float = 0.0):
        self.attack = attack
        self.sustain_damage = sustain_damage
        self.damaged = damaged
        self.anti_fighter_barrage = anti_fighter_barrage
        self.cost = cost

    def __repr__(self):
        return f"Combatant(attack={self.attack}, sustain_damage={self.sustain_damage}, damaged={self.damaged}, anti_fighter_barrage={self.anti_fighter_barrage}, cost={self.cost})"


class Cruiser(Combatant):
    def __init__(self):
        super().__init__(attack=[7], cost=2)

    def __repr__(self):
        return f"Cruiser(attack={self.attack}, sustain_damage={self.sustain_damage}, damaged={self.damaged}, cost={self.cost})"
    
class Carrier(Combatant):
    def __init__(self):
        super().__init__(attack=[9], cost=3)

    def __repr__(self):
        return f"Carrier(attack={self.attack}, sustain_damage={self.sustain_damage}, damaged={self.damaged}, cost={self.cost})"

class Fighter(Combatant):
    def __init__(self):
        super().__init__(attack=[9], cost=0.5)

    def __repr__(self):
        return f"Fighter(attack={self.attack}, sustain_damage={self.sustain_damage}, damaged={self.damaged}, cost={self.cost})"
    
class Destroyer(Combatant):
    def __init__(self):
        super().__init__(attack=[9], anti_fighter_barrage=[9, 9], cost=1)

    def __repr__(self):
        return f"Destroyer(attack={self.attack}, sustain_damage={self.sustain_damage}, damaged={self.damaged}, anti_fighter_barrage={self.anti_fighter_barrage}, cost={self.cost})"
    
class Infantry(Combatant):
    def __init__(self):
        super().__init__(attack=[8], cost=0.5)

    def __repr__(self):
        return f"Infantry(attack={self.attack}, sustain_damage={self.sustain_damage}, damaged={self.damaged}, cost={self.cost})"
