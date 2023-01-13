class Players:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def info(self):
        print(f'Info for player {self.name}')


class SoccerPlayers(Players):
    def __init__(self, name, age, league):
        Players.__init__(self, name, age)
        self.league = league


    def teamNum(self, num1):
        if num1 == 0:
            print('Cannot be this number')
        else:
            print(f'\n{self.name} plays at {num1}')


class ArcadePlayer(SoccerPlayers):
    def __init__(self, name, age, league, city):
        SoccerPlayers.__init__(self, name, age, league)


    def professional(self):
        print('Too good!')


choice = input('Select the number 1 or 2: ')
num = int(input('Enter which number do you play: '))
player1 = ArcadePlayer('Timothy', 55, 'MyLeague', 'Chicago')
player2 = ArcadePlayer('Sally', 20, 'L', 'New York')
player1.info()
player2.info()
play = player1 if (choice == 1) else player2
play.teamNum(num)
