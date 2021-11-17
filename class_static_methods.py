class Player:
    teamName = 'Liverpool' #class variable

    def __init__(self, name):
        self.name = name #creating instance variables

    @classmethod
    def getTeamName(cls):
        return cls.teamName

    @staticmethod
    def demo():
        print("I am a static method.")

print('________________')
print(Player.getTeamName())
p1 = Player('lol')
p1.demo()
Player.demo()