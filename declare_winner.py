"""
Create a function that returns the name of the winner in a fight between two fighters.

Each fighter takes turns attacking the other and whoever kills the other first is victorious. Death is defined as having health <= 0.

Each fighter will be a Fighter object/instance. See the Fighter class below in your chosen language.

Both health and damagePerAttack (damage_per_attack for python) will be integers larger than 0. You can mutate the Fighter objects.
"""


def declare_winner(fighter1, fighter2, first_attacker):
    # Code your solution here
    move = first_attacker
    winner = ""
    while fighter1.health > 0 and fighter2.health > 0:
        if fighter1.name == move:
            fighter2.health -= fighter1.damage_per_attack
            move = fighter2.name
        else:
            fighter1.health -= fighter2.damage_per_attack
            move = fighter1.name
    if fighter1.health > fighter2.health:
        winner = fighter1.name
    else:
            winner = fighter2.name
    return winner

"""
test.describe("Example test cases")

test.assert_equals(declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Lew"), "Lew")

test.assert_equals(declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Harry"),"Harry")

test.assert_equals(declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harry"),"Harald")

test.assert_equals(declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harald"),"Harald")

test.assert_equals(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Jerry"), "Harald")
    
test.assert_equals(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Harald"),"Harald")
"""
