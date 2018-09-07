# Hang man

def hangman():# word = correct word
# Step.0 Random wordlist
    my_wordlist = ["cat", "dog", "banana", "Jason", "michel"]

    import random

    num = random.randint(0,4)
    word = my_wordlist[num]
    
# Step.1 Introduction
    wrong = 0 # Wrong number of times
    stages = ["", # 9 contents
              "__________          ",
              "|                   ",
              "|         |         ",
              "|         0         ",
              "|        /|\        ",
              "|        / \        ",
              "|                   ",
              ]

    rletters = list(word) # abcde => ["a", "b",..., "e"]
    board = ["_"] * len(word) # if word is "cat", board is gonna be ["_","_","_"]
    win = False
    print("Welcome to Hang Man!")
    
# Step.2 loop
    while wrong < len(stages) - 1: # loop until the number of wrong exceed that of stages 
        print("\n") # new line
        msg = "Guess a word:"
        char = input(msg) # player put a single word
        
        if char in rletters: # if the word player chose is included in the list "rletters"
            cind = rletters.index(char) # return index number of char in rletters
            board[cind] = char # if char = 'a' then, board will go to ["_","a","_"]
            rletters[cind] = "$" # rletters => ["c","$","t"]
            #print(rletters) # Delete this later
            #print(board) # Delete this later

        else:
            wrong += 1
            
        print(" ".join(board)) # display like " _ a _ "
        #e = wrong + 1 # if there is no add in wrong, e is gonna be 0 and it won't change
        print("\n".join(stages[0:wrong+1]))
        
        if "_" not in board: # remember? board = ["_","_","_"]
            print("You win!")
            print(" ".join(board)) # it gonna be like "a p p l e"
            win = True
            break
        
# Step.3 If not win        
    if not win: # if not win = True(win = False), This statement will start working
        print("\n".join(stages[0:wrong+1]))
        print("You lose! The answer is {}.".format(word))

hangman()



        
