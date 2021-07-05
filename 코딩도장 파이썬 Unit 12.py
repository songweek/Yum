lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
print(lux)

x = {100: 'hundred', False: 0, 3.5: [3.5, 3.5]}
print(x)

c = dict()
print(c)

lux1 = dict(health = 490, mana = 334, melee = 550, armor = 18.72)
print(lux1)

lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72]))
print(lux2)

lux3 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
print(lux3)

lux4 = dict({'helath': 490, 'mana': 334, 'melee': 550, 'armor': 18.72})
print(lux4)

print(lux['health'])
print(lux['armor'])

lux['health'] = 2037
lux['mana'] = 1184
print(lux)

lux['mana_regen']=3.28
print(lux)

print('health' in lux)
print('attack_speed' in lux)
print('attack_speed' not in lux)
print('health' not in lux)

print(len(lux))

camille = {
    'health': 575.6,
    'health_regen': 1.7,
    'mana': 338.8,
    'mana_regen': 1.63,
    'melee': 125,
    'attack_damage': 60,
    'attack_speed': 0.625,
    'armor': 26,
    'magic_resistance': 32.1,
    'movement_speed': 340
}

print(camille['health'])
print(camille['movement_speed'])