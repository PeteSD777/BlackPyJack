# -*- coding: utf-8 -*-



cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

import random
dealer=0
you=0


while True:
 
  

  if dealer==0 and you==0:
    for i in range(2):
      you+=cards[random.randrange(0, len(cards))]
      dealer+=cards[random.randrange(0,len(cards))]
      
    print(f"you start with: {you}")
  start = input("Press y to continue, press n to end game, press q to exit ")


  if start=="Q".lower():
    break

 
  if start=="Y".lower():

    
    
    

    hit=input("Hit it with an h")
    if hit=="H".lower():
      if cards[random.randrange(1,len(cards))]==11 and you>10:
        you+=1
      you+=cards[random.randrange(1,len(cards))]
      if cards[random.randrange(1,len(cards))]==1 and dealer>10:
        dealer+=1
      dealer+=cards[random.randrange(1,len(cards))]
      print(you)
      if you>21:
        print(f"you {you}, dealer {dealer},you lose")
        dealer=0
        you=0
        continue
      elif dealer>21:
        print(f"you {you}, dealer {dealer},you win")
        dealer=0
        you=0
        continue
     

     
      if you>21 and dealer>21:
        if you>dealer and you>21:
          print(f"you {you} lose")
        elif dealer>you and dealer>21:
          print(f"you {you}, dealer {dealer}, you won")
        you=0
        dealer=0
        continue
   




  def check(start):
    global dealer
    global you
    if start=="N".lower():
      
          if dealer>you and dealer<=21:
            print(f"you{you}, dealer{dealer}, you lose")
          elif dealer<you and you<=21:
            print(f"you{you}, dealer{dealer},you win")
          elif you==dealer:
            print(f"you{you}, dealer{dealer}, draw")
          
          dealer=0
          you=0

         
  check(start)
  continue



