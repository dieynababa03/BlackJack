import random
# Function that generates random cards
def randomNum(cardsList):
  for index in range(1):
    cardsListIndex = random.randint(0, len(cardsList)- 1)
    cardsNumber = cardsList[cardsListIndex]
  return cardsNumber
# Calculates the total
def scoreTotal(cardsList):
  totalSum = sum(cardsList)
  # if total is 21 return 0 meaning they
  # won
  if totalSum == 21:
    return 0
  # for when user/computer wants to keep adding cards
  if totalSum > 21 and 11 in cardsList:
    cardsList.remove(11)
    cardsList.append(1)
  return totalSum

blackJack = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user = []
computer = []
# generating starting deck
for index in range(2):
  user.append(randomNum(cards))
  computer.append(randomNum(cards))

# loop that keeps game running until winner
while blackJack:
  # printing computer and users deck
  print(f"Your deck {user}")
  print(f"Computers first card {computer[0]}")
  # calculating total
  userTotal = scoreTotal(user)
  computerTotal = scoreTotal(computer)
  # calculating whether or not score is 0
  # which determines who has blackjack
  if userTotal == 0:
    print(f"You Win with the deck {user}!")
    blackJack = False
  if computerTotal == 0:
    print(f"Computer Wins with the deck {computer}!")
    blackJack = False

  if userTotal > 21:
    if 11 in user:
      if 1 in user:
        if userTotal > 21:
          print("You lose!")
          blackJack = False
    # if the users total is greater than 21
    # and there is no ace
    else:
      print("You lose!")
      blackJack = False
  # asking user if they'd like another card
  if blackJack == True:
    anotherCard = input("Would you like another card?:(y/n) ")
    print("\n")
  if anotherCard == "y":
    user.append(randomNum(cards))
  else:
    # adding cards to the computer until winner is
    # found
    while blackJack:
      if computerTotal < 17:
        computer.append(randomNum(cards))
        computerTotal = scoreTotal(computer)
      if computerTotal > 21:
        print(f"Computer wins with the deck {computer}!")
        blackJack = False
      else:
        # if computer is still not over
        # 21 calculate a winner
        if computerTotal > userTotal:
          print(f"Computer Wins with the deck {computer}!")
          blackJack = False
        elif userTotal > computerTotal:
          print(f"You Win with the deck {user}!")
          blackJack = False
        else:
          print("It's a draw!")
          blackJack = False
  






