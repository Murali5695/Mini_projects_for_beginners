import random
def play():
    user=input("'r' for rock and 'p' for paper and 's' for scissor ")
    computer=random.choice(['s','p','r'])
    if user == computer:
        return 'it\'s is a  tie'
    if won(user,computer):
        return "you Won"
    return "you lose"
def won(player,opponent):
    #r>s$s>p$p>r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p' ) or (player == 'p' and opponent == 'r'):
        return True
print(play())

