def hangman(word):
    wrong=0
    stages=["",
            "_______       ",
            "|      |       ",
            "|      o       ",
            "|    / | \     ",
            "|     / \      ",
            "|              ",
            "|              ",
            "|______________"]
    
    rletters=list(word)
    board=["_"]*len(word)
    win=False
    print("Welcome to Hangman")


    while 0<len(stages)-wrong:
        print("\n")
        if "_"not in board:
                print("You win!")
                print(" ".join(board))
                win=True
                break
        msg="Guess a letter:"
        char =input(msg)
        if char in rletters:
            cind=rletters.index(char)
            board[cind]=char
            rletters[cind]=char
            rletters[cind]='$'
            print((" ".join(board)))
        else:
            wrong+=1
            print((" ".join(board)))
            e=wrong+1
            print("\n".join(stages[:e]))
            

    if not win:
        print("\n".join(stages))
        print("You lose! It was {}.".format(word))


words=["hello","boy","world"]
import random
a=random.randint(0,4)-1
hangman(words[a])

