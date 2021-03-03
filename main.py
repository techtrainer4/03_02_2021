import random
def dumb_game():
  money = int(input("How much you want to start with?"))
  wins = 0
  losses = 0
  amt = [money]
  while money > 0:
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    s = d1 + d2
    if s == 7:
      print("{}! You win!".format(s))
      money += 5 
      amt.append(money)
      wins += 1
      print("You have ${} left.".format(money))
    else:
      print("{}! You lost!".format(s))
      money -= 1
      amt.append(money)
      losses += 1
      print("You have ${} left.".format(money))

  print("Wins: ",wins,"Losses: ",losses, "Max You Had: ",max(amt))

#dumb_game()


nums = [] 
for i in range(10000):
  d1 = random.randint(1,6)
  d2 = random.randint(1,6)
  s = d1 + d2 
  nums.append(s)

#print(nums)
print(nums.count(7))


  

  








