# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 12:19:09 2019

@author: Prajwal
"""
import time
def printer(a):
    count_row=1
    for i in a:
            count_col=1
            for j in i:
                if(count_col==3):
                    if(j==0):
                        print(" ", end=" ")
                    else:
                        print(j, end=" ")
                else:
                    if(j==0):
                        print(" ", end=" | ")
                    else:
                        print(j, end=" | ")
                    count_col+=1
            if(count_row==3):
                print("\n")
            else:
                print("\n----------")
                count_row+=1
        
        
def check(position, a):
    r1=set(a[0])
    r2=set(a[1])
    r3=set(a[2])
    c1={a[0][0], a[1][0], a[2][0]}
    c2={a[0][1], a[1][1], a[2][1]}
    c3={a[0][2], a[1][2], a[2][2]}
    d1={a[0][0], a[1][1], a[2][2]}
    d2={a[2][0], a[1][1], a[0][2]}
    if(position==1):
        if(len(r1)==1 or len(c1)==1 or len(d1)==1):
            return True
        else: 
            return False
    elif(position==2):
        if(len(r1)==1 or len(c2)==1):
            return True
        else:
            return False
    elif(position==3):
        if(len(r1)==1 or len(c3)==1 or len(d2)==1):
            return True
        else:
            return False
    elif(position==4):
        if(len(r2)==1 or len(c1)==1):
            return True
        else:
            return False
    elif(position==5):
        if(len(r2)==1 or len(c2)==1 or len(d1)==1 or len(d2)==1):
            return True
        else:
            return False
    elif(position==6):
        if(len(r2)==1 or len(c3)==1):
            return True
        else:
            return False
    elif(position==7):
        if(len(r3)==1 or len(c1)==1 or len(d2)==1):
            return True
        else:
            return False
    elif(position==8):
        if(len(r3)==1 or len(c2)==1):
            return True
        else:
            return False
    elif(position==9):
        if(len(r3)==1 or len(c3)==1 or len(d1)==1):
            return True
        else:
            return False
    
        
def available(a, position, positions):
    availability=False
    if (position>=1 and position<=9):
         availability=True
    else:
        availability=False
        return
    if((a[positions[position][0]][positions[position][1]])!=0):
        availability=False
    else:
        availability=True
    return availability
    
           
    




def play(a, p1, p2, positions):
    play_count=0
    while(play_count<8):
        if play_count%2==0:    
            check2=0
            while(check2==0):
                pos=int(input("\nPlayer 1, enter your position "))
                if(available(a, pos, positions)):
                    check2=1
                else:
                    print("This position is already filled or you have not entered a number within 9. Pease enter number again")
                    check2=0
            a[positions[pos][0]][positions[pos][1]]=p1
            printer(a)
            result=check(pos, a)
            if(result):
                print("\nPlayer 1 wins")
                return 
            else:
                play_count+=1
        else:
            check2=0
            while(check2==0):
                pos=int(input("\nPlayer 2, enter your position "))
                if(available(a, pos, positions)):
                    check2=1
                else:
                    print("This position is already filled or you have not entered a number within 9. Please enter number again")
                    check2=0
            a[positions[pos][0]][positions[pos][1]]=p2
            printer(a)
            result=check(pos, a)
            if(result):
                print("\nPlayer 2 wins")
                return
            else:
                play_count+=1
        if(play_count==8):
            check3=0
            while(check3==0):
                pos=int(input("\nPlayer 1, enter your position "))
                if(available(a, pos, positions)):
                    check3=1
                else:
                    print("This position is already filled or you have not entered a number within 9. Please enter number again")
                    check3=0
            a[positions[pos][0]][positions[pos][1]]=p1
            printer(a)
            result=check(pos, a)
            if(result):
                print("\nPlayer 1 wins")
                return 
            else:
                print("\nGame is drawn")
    

def main():
    a=[[0,0,0], [0,0,0], [0,0,0]]
    positions={1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}
    choices={'X', 'O'}
    pc1=0
    while(pc1==0):
        p1=input("Player 1, enter your choice, X or O ?").upper()
        if(p1 in choices):
            pc1=1
        else:
            print("\n\nEnter either X or O. Other options are invalid")
            pc1=0
    
    if(p1=='X'):
        p2='O'
        print("\nPlayer 1 chose X and player 2 chose O");
    elif(p1=='O') :
        p2='X'
        print("\nPlayer 1 chose O and player 2 chose X");
     
    print("\nLoading...")
    time.sleep(5)   
    print("\nGame Begins !")
    play(a, p1, p2, positions)

main()





            
    
    

    
    
    

        




