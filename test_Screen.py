import pygame
import numpy
from Countries import * #namespace of the two files are like as if it the same file(no need for Countries.Rajpootana)
from colors import *
import time 
from timeit import default_timer as timer




running = 1




CommunicationScreen = (4, 390, 188, 250) #combined screen

statusDispayScreen = (8, 396, 180, 60)   #1

textScreen = (4, 485, 188, 76)           #2

isNeighbor = (4, 573, 188, 67)           #3

attackButtonScreen = (30, 654, 120, 50)  #4
attackButtonScreenLimits = (30, 654, 150, 704)



"""starting top      |    |
   left position     |    |
                     amount of width ==>
                          |
                          V
                         amount of pixels height from starting pos
"""

SCR_SIZE = (840, 723)  #(width, height)
screen=pygame.display.set_mode(SCR_SIZE)

mainmap = pygame.image.load('SubContinentPictures/mapWithNoColors.png')

#DICE = pygame.image.load('Pictures/Dices/1.png')

def loadImages():
    screen.blit(mainmap, (0, 0))
    pygame.draw.rect(screen, white, CommunicationScreen)
    pygame.display.update()
    pygame.draw.rect(screen, yellow, attackButtonScreen) #for the attack button
    display_message("Finished Attacks", 4, red)
    
    initialColoringMap(CountryList)
    displayArmies(CountryList)

def displayArmies(CountryList):
    for country in CountryList:
	updateTroopDisplay(country)
    

    
def initialColoringMap(Region):
    for country in Region:	
	screen.blit(country.button, (0, 0))
        pygame.display.update()
	




def color_surface(country, alpha):
    color = country.colorTriplet
    for x in range(0,country.bounds.width):
	for y in range(0,country.bounds.height):
	    if country.button.get_at((country.bounds.x+x, country.bounds.y+y))!=(0,0,0,0):
		country.button.set_at((country.bounds.x+x, country.bounds.y+y),color)
    country.button.set_alpha(alpha)#needs to be set only once for an image
    screen.blit(country.button, (0, 0))
    pygame.display.update()

def clickEffect(presentCountry, previousCountry):
    if previousCountry == presentCountry:
	return
    
    removeClickEffect(previousCountry)
    screen.blit(presentCountry.clickEffectImage, (0, 0))
    pygame.display.update()

def clickEffectAfterAttack(country):
    screen.blit(country.clickEffectImage, (0, 0))
    pygame.display.update()


def removeClickEffect(country):
    for x in range(0,country.borderBounds.width):
	for y in range(0,country.borderBounds.height):
	    if country.borderImage.get_at((country.borderBounds.x+x, country.borderBounds.y+y)) != (0,0,0,0):
		country.borderImage.set_at((country.borderBounds.x+x, country.borderBounds.y+y),light_grey)#update this latter to country.color
    country.borderImage.set_alpha(255)	
    screen.blit(country.borderImage, (0, 0))
    

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def getCenter(rectPoints):
    x, y, extendedX, extendedY = rectPoints[0], rectPoints[1], rectPoints[2], rectPoints[3]
    extendedX /= 2
    extendedY /= 2
    return x+extendedX, y+extendedY

#different parts of the screen are specified in levels: level 0, 1, 2


def display_message(msg, level, color):
    #pygame.draw.rect(screen, white, textScreen)
    largeText = pygame.font.Font('freesansbold.ttf', 14)
    TextSurf, TextRect = text_objects(msg, largeText, color)
    if level == 1:
	pygame.draw.rect(screen, reddish_white, statusDispayScreen)
	TextRect.center = (getCenter(statusDispayScreen))
    elif level == 2:
	pygame.draw.rect(screen, greenish_white, textScreen)
	TextRect.center = (getCenter(textScreen))
    elif level == 3:
	pygame.draw.rect(screen, reddish_white, isNeighbor)
 	TextRect.center = (getCenter(isNeighbor))
    else:
	
	TextRect.center = (getCenter(attackButtonScreen))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()



def updateTroopDisplay(country):
    troopsBackground = country.position
    right = troopsBackground[0] - 7
    left = troopsBackground[1] - 7
    
    pygame.draw.rect(screen, red, (right, left, 14, 14))
    msg = str(country.army)

    largeText = pygame.font.Font('freesansbold.ttf', 12)
    TextSurf, TextRect = text_objects(msg, largeText, white)
    TextRect.center = country.position
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    

if __name__ == "__main__":
    pygame.init() #keep it here itself
    pygame.mixer.music.load('SoundEffects/game_start.ogg')
    pygame.mixer.music.play(0)  
    running = True
      
    loadImages()

    troopsToBePlaced = 7
    attacksDone = False
    previousCountry = Mandalay
    screen.blit(previousCountry.clickEffectImage, (0, 0))
    pygame.display.update()

    display_message("Please place 7 troops...", 1, red)

    #TurnSummaryInfo
    TurnMoves = []
    
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
	mouse = pygame.mouse.get_pos()
        color = sum(screen.get_at(mouse))-255   # op of screen.get_at() is in the form (r, g, b, 255)	
	
        clicked = pygame.mouse.get_pressed()
        country = colorToCountry.get(mouse, False) # a dictionary that indicates the country the pointer is on by giving the color
        
	#print "Pos ", mouse, "|color(r+g+b): ", color, "|clicked?", clicked[0]
	
        if clicked[0]:
	    if country:  
                display_message(country.name + " has " + str(country.army) + " troops", 2, red)
		pygame.time.wait(160) #keep this at 200 itself
		clickEffect(country, previousCountry)
		if troopsToBePlaced and country.color == Human_Player.color:
		    country.army = country.army + 1
		    updateTroopDisplay(country)
		    troopsToBePlaced = troopsToBePlaced - 1
		    if not troopsToBePlaced:
			display_message("Finished placing troops:", 1, red)

	        if country.color != Human_Player.color and not troopsToBePlaced and CombinedGraph.has_edge(country, previousCountry) and previousCountry.color == Human_Player.color and not attacksDone and previousCountry.army != 0:
		    """The last condition is for the case when there are no armies to attack with and we need to bypass the below code """
		    pygame.mixer.music.load('SoundEffects/Dice.wav')
    		    pygame.mixer.music.play(0) 
		    pygame.time.wait(300)
	  	    victimCountry = country
		    attackingCountry = previousCountry
		    display_message("This is a neighbor", 3, red)
		    
		    attackingCountry.attacks(victimCountry)
		    
		    clickEffectAfterAttack(victimCountry)

		elif country.color == Human_Player.color == previousCountry.color and attacksDone and CombinedGraph.has_edge(country, previousCountry):
		    """ If prevCountry and currCountry belongs to Human_Player, and attacks are over, it has an edge with previous country,then 			allow reinforcements to move"""
		    pygame.time.wait(300)
	  	    victimCountry = country
		    attackingCountry = previousCountry
		    display_message("This is a neighbor", 3, red)
		    
		    attackingCountry.attacks(victimCountry)
		    clickEffectAfterAttack(victimCountry)

		elif not attacksDone and country != previousCountry and not CombinedGraph.has_edge(country, previousCountry) and country.color != Human_Player.color:
		    display_message("NOT a neighbor!", 3, red)
		    pygame.mixer.music.load('SoundEffects/InvalidMove.wav')
    		    pygame.mixer.music.play(0) 

		
 
	        previousCountry = country

	    elif color == 510:  
		attacksDone = True
		pygame.draw.rect(screen, orange, attackButtonScreen)
		display_message("Place reinforcements", 4, red)		    
		pygame.time.wait(200)
		print "clicked!!!!!!!!!!!!!!!!!!!!!!!!!!"
	    elif color == 420:
		pygame.draw.rect(screen, orange, attackButtonScreen)
		pygame.display.update()
		display_message("Turn ended!", 4, red)
		pygame.mixer.music.load('SoundEffects/Alert.wav')
    		pygame.mixer.music.play(0)
		pygame.time.wait(200)
		#insert the call to make computer play
		AITurn(Red_Player)
		AITurn(Blue_Player)
		attacksDone = False
		#redAIPlays()
		pass
    pygame.quit()
    
