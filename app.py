from team import *
from students import Students

student = Students("Lewis", "E65")

student.talk()    
student.say_favourite_language("Python")  

players = ["Max", "Checo"]

red_bull = Team("Red Bull", players , "Horner")
print(red_bull.players)


print(Team.has_player(red_bull, "Max"))

Team.add_player(red_bull, "Daniel")
print(red_bull.players)

red_bull.play_game(True)
print(red_bull.points)