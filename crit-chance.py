import math
import random
import matplotlib.pyplot as plt


SIMULATIONS = 10000
projectile_damage = 3
projectile_crit_chance = 0.05
expected_damage = {}


for i in range(40):
    sum_crit_chance = i * projectile_crit_chance
    crit_modifier = max(sum_crit_chance, 1)*5
    damage_list = [projectile_damage*crit_modifier if random.random() < min(sum_crit_chance, 1) else projectile_damage for _ in range(SIMULATIONS)]
    average_damage = sum(damage_list) / SIMULATIONS
    damage_variation = math.sqrt(sum((x - average_damage) ** 2 for x in damage_list) / SIMULATIONS)
    expected_damage[sum_crit_chance] = (average_damage, damage_variation)

# Plotting the damage variation and average damage
plt.figure(figsize=(10, 6))
plt.plot(list(expected_damage.keys()), [x[1] for x in expected_damage.values()], marker='o', label='Damage Variation')
plt.plot(list(expected_damage.keys()), [x[0] for x in expected_damage.values()], marker='x', label='Average Damage')
plt.title('Damage Variation and Average Damage vs. Sum Crit Chance')
plt.xlabel('Sum Crit Chance')
plt.ylabel('Damage')
plt.legend()
plt.grid(True)
plt.show()
