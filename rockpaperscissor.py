from random import randint


class RockPaperScissor:
    choice = {1: "rock", 2: "paper", 3: "scissor"}
    winSitutation = [["paper", "rock"], ["rock", "scissor"], ["scissor", "paper"]]
    player_score = 0
    comp_score = 0

    def switch(self,r):
        ch=str(r)
        if ch == '1':
            return self.choice.get(1)
        elif ch == '2':
            return  self.choice.get(2)
        elif ch == '3':
            return self.choice.get(3)
        elif ch == '4':
            print("\n----------")
            print(" Final Score\nPlayer = ", self.player_score, " Computer = ", self.comp_score)
            print("\n----------")
            exit(0)
        else:
            print("Invalid choice")
            return False

    def checkWinner(self,p,c):
        p_win = [p,c]
        c_win =[c,p]
        if p == c:
            print("DRAW")
        else:
            for w in self.winSitutation:
                if p_win == w:
                    print("\nPlayer wins")
                    self.player_score += 1
                if c_win == w:
                    print("\nComputer wins")
                    self.comp_score +=1

        print("Player = ", self.player_score," Computer = ", self.comp_score)
        print("\n----------")


rsp =RockPaperScissor()
while True:
    player_choice = input("1)Rock\n2)Paper\n3)Scissor\n4)Exit Enter your choice(1,2,3,4): ")
    player = rsp.switch(player_choice)
    if player:
        computer = rsp.switch(randint(1, 3))
        print("player selected ", player)
        print("Computer selected ", computer)
        print("-------", player, " vs ", computer, "-------")
        rsp.checkWinner(player, computer)

