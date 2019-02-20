from screen import*
import random
"""
Defender 0 army = 1 dice                         Attacker 1 army = 1 dice
	 1 army = 2 dice			 	  2 army = 2 dice
	 2 army = 2 dice				  3 army = 3 dice
	 3 army = 3 dice,.....and so on..                 4 army = 4 dice,...and so and so forth.....
"""
eraseDice = pygame.image.load('Pictures/Dices/eraseDice.png')


DICE = pygame.image.load('Pictures/Dices/1.png')

armyToDiceDefender = {0:1, 1:2}

def numDefenderDice(army):
	if armyToDiceDefender.get(army, False) is False:
		return 2
	else:
		return armyToDiceDefender.get(army, False)

armyToDiceAttacker = {1:1, 2:2, 3:3}

def numAttackerDice(army):
	if armyToDiceAttacker.get(army, False) is False:
		return 3
	else:
		return armyToDiceAttacker.get(army, False)


def battle (attacking, defending):
    '''Decides the outcome of an attack based on dice rolls
    
    Returns: the outcome of the attack (True if the terriroy is 
             captured, otherwise False)
    Params: attacking - the id of the territory performing the attack
            defending - the id of the territory receiving the attack

	**Currently it works till "the last man standing" **
    '''
    while attacking.army > 0 and defending.army > 0: 
    	attack_dice = list()
    	defend_dice = list()
        
    	print "\n\n New Iteration....\n"
	screen.blit(eraseDice , (0, 0))
	pygame.display.update()

	#initializing dice images 
	DICE_MOVE_RIGHT = 32 #for red/attacking/human player
	DICE_X_AXIS = 474

	dice_x_axis_for_computer_player = 474
	dice_move_right = 32 #for blus/defending/AI player

    	# Attacking Dice
    	num_dice = numAttackerDice(attacking.army)
    	for i in range(num_dice): # Dice rolls
		diceRollResult = random.randint(1,6)
        	attack_dice.append(diceRollResult)
		path = "Pictures/Dices/PlayerDice" + str(diceRollResult) + ".png"
		DICE1 = pygame.image.load(path)
		screen.blit(DICE1 ,(DICE_X_AXIS,532))
		pygame.display.update()
		DICE_X_AXIS = DICE_X_AXIS + DICE_MOVE_RIGHT

    	attack_rolls = len(attack_dice)
    
    	# Defending Dice
    	num_dice = numDefenderDice(defending.army)
    	for i in range(num_dice): # Dice rolls
		diceRollResult = random.randint(1,6)
        	defend_dice.append(diceRollResult)
		path = "Pictures/Dices/" + str(diceRollResult) + ".png"
		DICE1 = pygame.image.load(path)
		screen.blit(DICE1 ,(dice_x_axis_for_computer_player,595))
		pygame.display.update()
		dice_x_axis_for_computer_player = dice_x_axis_for_computer_player + dice_move_right


    	defend_rolls = len(defend_dice)
    
    	attack_dice.sort()
    	defend_dice.sort()

    	text1 = "Attacker rolled: "
    	for i in range(attack_rolls):
        	text1 += str(attack_dice[i]) + " "
	
    	text1 += "\nDefender rolled: " 
    	for i in range(defend_rolls):
        	text1 += str(defend_dice[i]) + " "
    	print(text1)
    
    	for i in range(min(attack_rolls, defend_rolls)):
		print("This is the {0}th roll".format(i+1))
        	if max(attack_dice) > max(defend_dice):
            		print "Defender lost 1 army!" # Print message
			defending.army = defending.army - 1
    	
        	else: # defender wins
            		print "Attacker lost 1 army!" # Print message
			attacking.army = attacking.army - 1
        	attack_dice.remove(max(attack_dice))
        	defend_dice.remove(max(defend_dice))

    return attacking.army > 0 # if we did not capture the territory
