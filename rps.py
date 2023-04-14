import numpy as np
import matplotlib.pyplot as plt

Rock=1
paper=2
scissors=3
allPoints1=[]
allPoints2=[]
for i in range(3):
    player1=int(input("choose: "+"1=Rock, 2=paper or 3=scissors: "))
    player2=int(input("choose: "+"1=Rock, 2=paper or 3=scissors: "))
    PointsP1=[0]
    PointsP2=[0]



    for x in range(1):

        step1=PointsP1[-1]
        step2=PointsP2[-1]

        if(player1==1 and player2==1):
            step1=step1+5
            step2=step2+5
            print("TIE")
        elif(player1==1 and player2==2):
            step2=step2+1
            print("player2 wins")
        elif(player1==2 and player2==2):
            step1=step1+5
            step2=step2+5
            print("TIE")
        elif(player1==2 and player2==1):
            step1=step1+1
            print("player1 wins")
        elif(player1==1 and player2==3):
            step1=step1+1
            print("player1 wins")
        elif(player1==3 and player2==1):
            step2=step2+1
            print("player2 wins")
        elif(player1==3 and player2==3):
            step1=step1+5
            step2=step2+5
            print("TIE")
        elif(player1==3 and player2==2):
            step1=step1+1
            print("player1 wins")
        elif(player1==2 and player2==3):
            step2=step2+1
            print("player2 wins")
        else:
            print("Let's roll to Next round")

        PointsP1.append(step1)
        PointsP2.append(step2)
    allPoints1.append(PointsP1)
    allPoints2.append(PointsP2)
Total1=np.array(allPoints1)
Total2=np.array(allPoints2)
p1=Total1.sum()
p2=Total2.sum()
print("Total for Player1: "+ str(p1))
print("Total for player2: "+ str(p2))


if p1>p2:
    print("PLAYER1 IS THE WINNER CONGRATS!!")
elif p1==p2:
    print("BOTH ARE THE WINNERS CONGRATS!!")
else:
    print("PLAYER2 IS THE  WINNER CONGRATS!!")


end1=np.transpose(Total1)
end2=np.transpose(Total2)
r1=end1[-1,:]
r2=end2[-1,:]
print(r1)
print(r2)
plt.plot(r1, color="red", label="player 1")
plt.plot(r2, color="green", label="player 2")

plt.legend()
plt.show()




