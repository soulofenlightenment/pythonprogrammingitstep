class FootballTeam:

    def __init__(self,team_name,coach):
        self.team_name = team_name
        self.coach = coach
        self.players = []
    
    @staticmethod
    def player_validation(name,position,number,age,nationality):
        role = (
            'gk','cb','lb','rb','lwb','rwb',
            'dm','cm','am','lm','rm',
            'cf','st','ss','rw','lw'
        )
        if type(name) != str:
            raise ValueError(f'{name} can\'t be a name')
        if position not in role or type(position) != str:
            raise ValueError(f'that kind of {position} not exists')
        if number not in range(1,100) or type(number) != int:
            raise ValueError(f'this number: {number} is not playable')
        if age not in range(16, 74) or type(age) != int:
            raise ValueError('incorrect age')
        if type(nationality) != str:
            raise ValueError('inccorect nation')

    def player(self,number):
        for person in self.players:
            if person['number'] == number:
                return person

    def player_add(self,name,position,number,age,nationality):
        self.player_validation(name,position,number,age,nationality)
        player = {
            'name': name,
            'position': position,
            'number': number,
            'age': age,
            'nationality': nationality
        }
        self.players.append(player)

    def player_remove(self, number):
        count = 0
        for player in self.players:
            if number == player['number']:
                self.players.pop(count)
            count+=1
    
    def player_update(self,number,**kwargs):
        for person in self.players:
            if person['number'] == number:
                person.update(kwargs)
    
    def team(self):
        return self.team_name
    def Coach(self):
        return self.coach

real_madrid = FootballTeam('real madrid','ancelotti')
real_madrid.player_add('mbappe','cf',10,26,'france')
real_madrid.player_add('courtois','gk',1,33,'belgium')
real_madrid.player_add('bellingham','cm',5,22,'england')
real_madrid.player_add('ronaldo','st',7,40,'portugal')
print(real_madrid.player(7))
real_madrid.player_remove(7)
print(real_madrid.players)
real_madrid.player_update(1, goal = 2, height = 2.0)
print(real_madrid.player(1))
print(real_madrid.team(),real_madrid.Coach())
