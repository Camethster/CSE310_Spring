from random import randint

def display_monsters(battle):
    for combatant in battle.intiative:
        print(combatant[0].name)


class action():
    def __init__(self):
        self.x

class ablility():
    def __init__(self):
        self.x


class lair_action():
    def __init__(self):
        self.x

class monster():
    def __init__(self,battle):
        self.name = ""
        self.hit_points = 0
        self.speed = 0
        self.AC = 0
        self.str = 0
        self.dex = 0
        self.con = 0
        self.int = 0
        self.wis = 0
        self.cha = 0 
        self.save_throw = {}
        self.skills = []
        self.resist = []
        self.immune = []
        self.c_immune = []
        self.senses = []
        self.language = []
        self.CR = 0
        self.ability = []
        self.action = []
        self.action = 1
        self.b_Action = 1
        self.movement =  1
        self.intiative = 0
        self.battle = battle 

    def create(self):
        good_input = False
        while(not(good_input)):
            try: 
                self.name = input("Monster Name: ")
                self.hit_points = int(input(self.name + " HP:"))
                self.speed = int(input(self.name  + " Speed:"))
                good_input = True
            except:
                print("Please input a valid value")

        return 
    
    def turn(self):
        good_input = False
        while(not(good_input)):
            turn_opt = input(self.name + " Turn options: \n1.action\n2.bonus action\n3.movement\n4.end turn")
            if turn_opt == "1" or turn_opt.lower() == "action":
                if self.action == 0:
                    display_monsters(self.battle)
                    self.attack(input("Which Combatant: "))
                    
                    pass
                self.action = 0
            elif turn_opt == "2" or turn_opt.lower() == "bonus action":
                if self.bonus_action == 0:
                    print("Used")
                   
                self.bonus_action = 0
            elif turn_opt == "3" or turn_opt.lower() == "movement":
                if self.movement == 0:
                    print("Used")
                self.movement = 0
            elif turn_opt == "4" or turn_opt.lower() == "end turn":
                good_input = True
            else:
                continue

class player(monster):
    def create(self):
        good_input = False
        while(not(good_input)):
            try: 
                self.name = input("Player Name: ")
                self.hit_points = int(input(self.name + " HP: "))
                good_input = True
            except:
                print("Please input a number")
        return 


class Battle():
    def __init__(self):
        self.monsters = []
        self.players = []
        self.lair_action = []
        self.intiative = []


    def intiate(self):
        num_play = int(input("How many Players: "))
        for x in range(num_play):
            new_player = player(self)
            new_player.create()
            self.players.append(new_player)
            #try:
            self.intiative.append((int(input(new_player.name + " Intiative: ")),  new_player))
            #except:    
                #print("Invalid Value")
        
        new_monster = monster(self)
        more = True
        while(more):
            print("Monsters:")
            new_monster.create()
            modifier = int(input(new_monster.name + " Modifier: "))
            name = new_monster.name
            for x in range(int(input("How many of this monster: "))):
                new_monster.name = name + " " + str(x+1)
                self.intiative.append((randint(1,20) + modifier, new_monster))
            if input("More Monsters? (y/n)").lower() == "n":
                more = False
        return
        

    def run(self):
        
        #print(self.intiative)
        #self.intiative = self.intiative.sort(key = lambda x: x[0])
        #print(self.intiative)
        for combatant in self.intiative:
            print(combatant[0])
            combatant[1].turn()
