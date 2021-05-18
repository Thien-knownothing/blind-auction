from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
should_cont = True
auction_list = {}
while should_cont :
  auctor = input("Please type in your name: ")
  bet_value = int(input("Place your auction amount: "))
  auction_list[auctor] = bet_value
  cont = input(" Is there any others auctor: Yes/No ")
  if cont[0].lower() == "y":
    should_cont = True
    clear()
  elif cont[0].lower() == "n":
    should_cont = False

win_value = max(auction_list.values())
print(win_value)
def win_cond(auction):
  for key, val in auction.items():
    if win_value == val:
      return key
winner = win_cond(auction_list)
print(f'Winner is {winner}')