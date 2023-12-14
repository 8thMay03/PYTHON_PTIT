cnt = {}
Teams = []
Participants = []

class Team:
    def __init__(self, teamID, teamName, uniName):
        self.teamID = "Team{:02d}".format(teamID)
        self.teamName = teamName
        self.uniName = uniName
    
class Participant:
    def __init__(self, id, name, teamID):
        self.id = "C{:03d}".format(id)
        self.name = name
        self.teamID = teamID
        self.team = cnt[teamID]
    
    def __str__(self):
        return ("{} {} {} {}").format(self.id, self.name, self.team.teamName, self.team.uniName)

for i in range(1, int(input()) + 1):
    A = Team(i, input(), input())
    Teams.append(A)
    cnt[A.teamID] = A

for i in range(1, int(input()) + 1):
    Participants.append(Participant(i, input(), input()))

Participants.sort(key=lambda x: x.name)

for Participant in Participants:
    print(Participant.__str__())