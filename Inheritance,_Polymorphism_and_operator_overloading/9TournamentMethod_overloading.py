def CalculateScore(*args):
    if len(args) == 3 and all(isinstance(x,int)for x in args):
        sixers, fours, singles=args
        return (sixers*6)+(fours*4)+singles

    elif len(args) == 3 and isinstance(args[2],str):
        white, black, redPocket=args
        score=(white*2)+(black*1)
        if redPocket == "yes":
            score+=5
        return score

    elif len(args) == 2:
        goals, fouls=args
        return goals-fouls

#~~~Main~~~
sixers=int(input("CRICKET:\nEnter number of sixers:"))
fours=int(input("Enter number of fours:"))
singles=int(input("Enter number of singles:"))
print("CALCULATED SCORE: ", CalculateScore(sixers, fours, singles) )

white=int(input("CARROM:\nEnter number of white coins pocket:"))
black=int(input("Enter number of black coins pocket:"))
redPocket=input("Red Pockets(yes/no):")
print("CALCULATED SCORE: ",CalculateScore(white, black, redPocket))

goals=int(input("BASKETBALL:\nEnter number of goals:"))
fouls=int(input("Enter number of fouls:"))
print("CALCULATED SCORE: ",CalculateScore(goals, fouls))
