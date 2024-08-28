import random

def get_user_choice():
  """
  be karbar mige ke bein sang,kaghaz va gheichi yeki entekhab kon

  Returns:
    int: The user's choice (1 for sang, 2 for kaghaz, 3 for gheichi).
  """
  global items
  items= {1: "Sang", 2: "Kaghaz", 3: "Gheychi"}
  while True:
    try:
      user_choice = int(input("entekhab khodeto be sorat adad vard kon:\n1) Sang,\n2) Kaghaz,\n3) Gheychi\n"))
      if user_choice in range(1, 4):
        return user_choice
      else:
        print("dadash bein 1 ta 3 yek adad vared kon")
    except ValueError:
      print("faghad adad vared kon")

def get_computer_choice():
  """
 yek entekhab random baraye computer 

  Returns:
    int: The computer's choice (1 for sang, 2 for kaghaz, 3 for gheichi).
  """
  computer_choice = random.randint(1, 3)
  print("Computer chose:", items[computer_choice])
  return computer_choice

def determine_winner(user_choice, computer_choice):
  """
 in function barande bazi ra moshakhas mikonad

  Args:
    user_choice: int (1 for sang, 2 for kaghaz, 3 for gheichi).
    computer_choice: int (1 for sang, 2 for kaghaz, 3 for gheichi).

  Returns:
    str: barande taeen shode.
  """
  if user_choice == computer_choice:
    return "Mosavi!"
  elif user_choice == 1:
    if computer_choice == 2:
      return "bakhti"
    else:
      return "bordi"
  elif user_choice == 2:
    if computer_choice == 1:
      return "bordi"
    else:
      return "bakhti"
  elif user_choice == 3:
    if computer_choice == 1:
      return "bordi"
    else:
      return "bakhti"

def play_game(final_score):
  """
  ta residan be emtiaz taeen shode edame midahand va emtiaz jam mikonan

  Args:
    winning_score: int (The score required to win the game).
  """
  user_score = 0
  computer_score = 0

  while user_score < final_score and computer_score < final_score:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    if result == "bordi":
      user_score += 1
    elif result =="bakhti":
      computer_score += 1

    print(f"player: {user_score}, \nComputer: {computer_score}")
    print(result)

  if user_score == final_score:
    print("barikalla bordi.")
  else:
    print("ishalla seri badi")

print("be bazie sang kaghaz gheici khoshamadid")
input("Esmeto vared kon:\n ")
final_score = int(input("chand emtiazi bazi mikoni?\n")) #taeen mikonim chand emtiazi bazi konim

play_game(final_score) #bazi shoro mishe

print("merci ke hasti")
