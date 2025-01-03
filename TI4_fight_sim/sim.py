import copy
from combatants import *

attackers = [Infantry(), Infantry()]
defenders = [Infantry()]

attacker_bonus = 1
defender_bonus = 0

def run_sim(attackers, defenders, attacker_bonus, defender_bonus):
    INIT_ATTACKERS = copy.deepcopy(attackers)
    INIT_DEFENDERS = copy.deepcopy(defenders)
    start_of_combat = True

    while attackers and defenders:
        perform_combat_round(start_of_combat, attackers, defenders, attacker_bonus, defender_bonus)
        start_of_combat = False

    return len(attackers), len(defenders)

def perform_combat_round(start_of_combat, attackers, defenders, attacker_bonus, defender_bonus):
    if start_of_combat:
        # Anti-fighter barrage phase
        attacker_hits = perform_anti_fighter_barrage(attackers)
        defender_hits = perform_anti_fighter_barrage(defenders)

        # Assign anti-fighter barrage hits
        assign_hits_to_fighters(defenders, attacker_hits)
        assign_hits_to_fighters(attackers, defender_hits)

        start_of_combat = False

    attacker_hits = 0
    defender_hits = 0

    # Attackers' turn to roll dice
    for attacker in attackers:
        for combatant_attack in attacker.attack:
            if roll_dice(combatant_attack, attacker_bonus):
                attacker_hits += 1

    # Defenders' turn to roll dice
    for defender in defenders:
        for combatant_attack in defender.attack:
            if roll_dice(combatant_attack, defender_bonus):
                defender_hits += 1

    # Assign hits to defenders
    assign_hits(defenders, attacker_hits)

    # Assign hits to attackers
    assign_hits(attackers, defender_hits)

def perform_anti_fighter_barrage(combatants):
    hits = 0
    for combatant in combatants:
        for barrage_roll in combatant.anti_fighter_barrage:
            if roll_dice(barrage_roll, 0):  # No bonus applied
                hits += 1
    return hits

def assign_hits_to_fighters(combatants, hits):
    fighters = [c for c in combatants if isinstance(c, Fighter)]
    while hits > 0 and fighters:
        fighter = fighters.pop(0)
        combatants.remove(fighter)
        hits -= 1

def assign_hits(combatants, hits):
    while hits > 0 and combatants:
        # Try to find a combatant with sustain_damage that is not yet damaged
        target = next((c for c in combatants if c.sustain_damage and not c.damaged), None)
        
        if target:
            target.damaged = True
        else:
            # If no such combatant, remove the one with the lowest cost
            target = min(combatants, key=lambda c: c.cost)
            combatants.remove(target)
        
        hits -= 1

def roll_dice(combatant_attack, bonus):
    import random
    roll = random.randint(1, 10)
    return roll + bonus >= combatant_attack

if __name__ == "__main__":
    attacker_wins = 0
    defender_wins = 0
    ties = 0
    total_attackers_remaining = 0
    total_defenders_remaining = 0

    for _ in range(10000):
        attackers_copy = copy.deepcopy(attackers)
        defenders_copy = copy.deepcopy(defenders)
        attackers_remaining, defenders_remaining = run_sim(attackers_copy, defenders_copy, attacker_bonus, defender_bonus)
        
        if attackers_remaining > 0 and defenders_remaining == 0:
            attacker_wins += 1
            total_attackers_remaining += attackers_remaining
        elif defenders_remaining > 0 and attackers_remaining == 0:
            defender_wins += 1
            total_defenders_remaining += defenders_remaining
        else:
            ties += 1

    print("Attackers won:", attacker_wins, "times with an average of", (total_attackers_remaining / attacker_wins if attacker_wins > 0 else 0), "attackers remaining.")
    print("Defenders won:", defender_wins, "times with an average of", (total_defenders_remaining / defender_wins if defender_wins > 0 else 0), "defenders remaining.")
    print("Ties:", ties, "times.")
