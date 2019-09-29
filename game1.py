import random


class Player(object):
    """Class of the players"""

    def __init__(self, hp, name):
        self.initial_hp = hp
        self.hp = hp
        self.name = name

    def hit(self, opponent):

        """Giving damage in range 18-25 points"""

        damage = random.randint(18, 25)
        opponent.hp -= damage
        print(f'Player {self.name} caused {damage} damage to {opponent.name}')

    def strong_hit(self, opponent):

        """Giving more damage in range 10-35 points"""

        damage = random.randint(10, 35)
        opponent.hp -= damage
        print(f'Player {self.name} caused critical {damage} damage to {opponent.name}!')

    def heal(self):

        """Restore points in range 18-25"""

        heal = random.randint(18, 25)
        self.hp += heal
        print(f'Player {self.name} got cured {heal} points')

    def turn(self, opponent):

        """Choice of used ability"""

        if self.name == 'PC' and self.hp < (self.initial_hp * 0.35):
            random.choice([self.hit(opponent), self.strong_hit(opponent), self.heal(), self.heal()])
        else:
            random.choice([self.hit(opponent), self.strong_hit(opponent), self.heal()])


class Game(object):
    """This class initialises the game and running process"""

    def __init__(self):

        self.user = Player(100, name='User')
        self.pc = Player(100, name='PC')

    def run(self):
            while True:
                random.choice([self.pc.turn(opponent=self.user), self.user.turn(opponent=self.pc)])
                if self.pc.hp <= 0:
                    print('User won this game!')
                    break
                elif self.user.hp <= 0:
                    print('PC won this game!')
                    break


game = Game()
game.run()



