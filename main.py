import random 
def rollDice(sides):
  dice = random.randint(1,sides)
  return dice
  
def rollDice_1_to_6_and_1_to_8 ():
  rollDice_6_sided = rollDice(6)
  rollDice_8_sided = rollDice(8)
  return rollDice_6_sided
  return rollDice_8_sided
  health_stats = rollDice_6_sided * rollDice_8_sided
  return health_stats
print("Let's play character stats generator game!")
character = "yes"
while character == "yes":
  name_character = input("What's  the name of your character? " ) 
  health_stats = str(rollDice_1_to_6_and_1_to_8())
  print("Your health stats is", health_stats)
  character = input("Wanna play another character  game?" )
  continue
  
  


 



 

  




