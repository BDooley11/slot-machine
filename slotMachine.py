import emoji,random
from random import choice

#purse class manages original balance and winning/losing bets
class Purse():

    def __init__(self,balance):
            self.balance = balance
        
    def debit(self,bet):
        self.bet = bet
        self.balance -= self.bet
        return self.balance
    
    def credit(self,bet):
        self.bet = bet
        self.balance += self.bet
        return self.balance
        
    def get_balance(self):
        return self.balance

# slot class handles the taking of the bed and the spinning of the column
class Slot():

    def __init__(self,column1,column2,column3):
        self.column1 = column1
        self.column2 = column2
        self.column3 = column3
 
    def pull_handle(self): 
        self.column1 = Column.change_face()
        self.column2 = Column.change_face()
        self.column3 = Column.change_face()
        self.result = [self.column1, self.column2, self.column3]
        return self.result
        
    def show_slot(self,result):
        print(result[0],result[1],result[2])

    def take_bet(self, balance):
        user = input("How much do you bet: ")
        while True:
            try:
                bet = int(user)
                if bet >= 2 and bet <= balance:
                    return bet
                else:
                    user = input("How much do you bet: ")
            except ValueError:
                if user == "N":
                    return "N"
                else:
                    user = input("How much do you bet: ")

    def score_slot(self,result):
        if result[0] == result[1] and result[1] ==result[2]:
            return "Full House"
        elif result[0] != result[1] and result[0] != result[2] and result[1] != result[2]:
            return "Losing Bet"
        else:
            return "Half House"	

#column class handles the emoji image that's generated when slot spun
class Column():
    
    def change_face():
        faces = [emoji . emojize( ':red_apple:' ), emoji . emojize( ':pear:' ), emoji . emojize( ':tangerine:' )]
        result = random.choices(faces)
        return result

# handles game mechanics
def run_slot_machine():
    Purse1 = Purse(10)
    Slot1 = Slot(1,2,3)
    
    print("==========  Slot Machine ==========")
    print("Minimum bet is 2. Type 'N' to exit.")
    print("You have",Purse1.get_balance())
    print("")
    while Purse1.get_balance() >=2:
        bet = Slot1.take_bet(Purse1.get_balance())
        if bet == "N":
            print("Thank you for playing.")
            print("You are leaving with",Purse1.get_balance())
            break
        else:
            result = Slot1.pull_handle()
            Slot1.show_slot(result)
            spin = Slot1.score_slot(result)
            if spin == "Full House":
                Purse1.credit(bet)
                print("You score",(bet+bet),"- You have",Purse1.get_balance())
                print("")
            elif spin == "Half House":
                Purse1.credit(bet/2)
                print("You score",(bet+bet/2),"- You have",Purse1.get_balance())
                print("")
            else:
                Purse1.debit(bet)
                if Purse1.get_balance() >=2:
                    print("You score 0 - You have",Purse1.get_balance())
                    print("")
                else:
                    print("You score 0 - Thank you for playing.")
                    print("You are leaving with",Purse1.get_balance())
                                   
    print("")


run_slot_machine()
