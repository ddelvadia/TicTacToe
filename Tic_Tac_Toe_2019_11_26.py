# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def board(t):
  
  print('\n\n')
  print(t[0]+" | "+t[1]+" | " + t[2])
  print("-"+" - "+"-"+" - "+"-")
  print(t[3]+" | "+t[4]+" | " + t[5])
  print("-"+" - "+"-"+" - "+"-")
  print(t[6]+" | "+t[7]+" | " + t[8])

  

def greating(t, start):
  loc=int(input('\n\nPlease enter the number where you wish to enter {}\n'.format(start)))

  #print('\n\n')
  #print(t[0]+" | "+t[1]+" | " + t[2])
  #print("-"+" - "+"-"+" - "+"-")
  #print(t[3]+" | "+t[4]+" | " + t[5])
  #print("-"+" - "+"-"+" - "+"-")
  #print(t[6]+" | "+t[7]+" | " + t[8])


  return loc

def turns(current):
  if current=='X':
    nxt='O'
    return nxt
  else:
    nxt='X'
    return nxt

def win(t):
  if t[0] == t[1]==t[2]:
    print('winner!')
    return True
  elif t[3] == t[4]==t[5]:
    print('winner!')
    return True
  elif t[6] == t[7]==t[8]:
    print('winner!')
    return True
  elif t[0] == t[3]==t[6]:
    print('winner!')
    return True  
  elif t[1] == t[4]==t[7]:
    print('winner!')
    return True  
  elif t[2] == t[5]==t[8]:
    print('winner!')
    return True 
  elif t[0] == t[4]==t[8]:
    print('winner!')
    return True 
  elif t[2] == t[4]==t[6]:
    print('winner!')
    return True 
  else:
    return False


def main():
  w=1
  t=["1","2","3","4","5","6","7","8","9"]
  turn='X'
  winner=win(t)
  board(t)
  while winner==False:
    loc=greating(t, turn)
    t[loc-1]=turn
    board(t)
    turn=turns(turn)
    winner=win(t)
    if w > 8:
        print("It's a draw")
        break
    w+=1    
  
  #print("It's a draw!")
  
main()
