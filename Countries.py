import random
import copy
from random import randint
import pygame
import itertools
from random import shuffle
import networkx as nx
from test_Screen import * 
from colors import *
from battle import *


eraseDice = pygame.image.load('Pictures/Dices/eraseDice.png')


DICE = pygame.image.load('Pictures/Dices/1.png')

MyanmarBonus = 3
SouthIndiaBonus = 4
MaharashtraBonus = 6
BengalBonus = 7
PakistanBonus = 6




	


def getCenter(rectPoints):
    x, y, extendedX, extendedY = rectPoints[0], rectPoints[1], rectPoints[2], rectPoints[3]
    extendedX /= 2
    extendedY /= 2
    return x+extendedX, y+extendedY






class Country(pygame.sprite.Sprite):
    def __init__(self, army, name, clickEffectPath, imagePath):
	pygame.sprite.Sprite.__init__(self)
	self.image = pygame.image.load(imagePath)
	self.bounds = self.image.get_bounding_rect()
        self.army=army
        
        self.clickEffectImage = pygame.image.load(clickEffectPath)
	self.rect = self.image.get_rect()
	self.position = getCenter(self.bounds)

        self.neighbors = None
	self.name = name
	self.button = self.image
	
	self.newbutton = self.image

	self.player = None
	self.colorTriplet = None

	self.background = self.image
	self.borderImage = pygame.image.load(clickEffectPath)
	self.borderBounds = self.borderImage.get_bounding_rect()
	self.color = None

    def belongsToSamePlayer(self, country):
	return self.color == country.color


    #self refers to previousCountry which is the attacker
    def attacks(self, victim):
	
	if battle(self, victim):
	    if victim.player is not None: #this was occupied by some player, that player must reliquish control
		victim.player.relinqishControl(victim)
	    victim.belongsTo(self.player)
            pygame.mixer.music.load('SoundEffects/March.wav')
	    pygame.mixer.music.play(0) 
	    victim.army = self.army
            self.army = 0
	    victim.color_surface()
            victim.updateTroopDisplay()
	    self.updateTroopDisplay()
	else:
	    victim.updateTroopDisplay()
	    self.updateTroopDisplay()



    def belongsTo(self, player):
	self.player = player
	#self.playerName = player.name
	self.colorTriplet = player.colorTriplet
	self.color = player.color
	player.controlOver(self)
	

    def color_surface(self):
	color = self.colorTriplet
        alpha = 255
        for x in range(0,self.bounds.width):
	    for y in range(0,self.bounds.height):
	        if self.button.get_at((self.bounds.x+x, self.bounds.y+y))!=(0,0,0,0):
		    self.button.set_at((self.bounds.x+x, self.bounds.y+y),color)
        self.button.set_alpha(alpha)
	try:
        	screen.blit(self.button, (0, 0))
	        pygame.display.update()
	except NameError:
		print "Name Error for screen has been passed"
		pass
	

    def updateTroopDisplay(self):
	country = self
        troopsBackground = country.position
        right = troopsBackground[0] - 7
        left = troopsBackground[1] - 7
    
        pygame.draw.rect(screen, red, (right, left, 14, 14))
        pygame.display.update()
        msg = str(country.army)

        largeText = pygame.font.Font('freesansbold.ttf', 12)
        TextSurf, TextRect = text_objects(msg, largeText, white)
        TextRect.center = country.position
        screen.blit(TextSurf, TextRect)
        pygame.display.update()

    
Kathiawar = Country(1, "Kathiawar","ClickPictures/KATHIAWAR.png", "SubContinentPictures/KATHIAWAR.png")
Bejapoor = Country(3, "Bejapoor", "ClickPictures/BEJAPOOR.png", "SubContinentPictures/BEJAPOOR.png")
Bustar = Country(2, "Bustar",  "ClickPictures/BUSTAR.png", "SubContinentPictures/BUSTAR.png")

Malabar = Country(4, "Malabar",  "ClickPictures/MALABAR.png", "SubContinentPictures/MALABAR.png")
Nagpur = Country(3, "Nagpur", "ClickPictures/NAGPUR.png", "SubContinentPictures/NAGPUR.png")
CIA = Country(1, "CIA", "ClickPictures/CIA.png", "SubContinentPictures/CIA.png")

Kandeish = Country(2, "Kandeish", "ClickPictures/KANDEISH.png", "SubContinentPictures/KANDEISH.png")
Andaman = Country(5, "Andamans",  "ClickPictures/ANDAMAN.png", "SubContinentPictures/ANDAMAN.png")
Cashmere = Country(3, "Cashmere", "ClickPictures/CASHMERE.png", "SubContinentPictures/CASHMERE.png")
########new are added above 


Rajpootana = Country(5, "Rajpootana",  "ClickPictures/RAJPOOTANA.png", "SubContinentPictures/RAJPOOTANA.png")#	
Punjab = Country(3, "Punjab",  "ClickPictures/PUNJAB.png", "SubContinentPictures/PUNJAB.png")#
Konkan = Country(3, "Konkan",  "ClickPictures/KONKAN.png", "SubContinentPictures/24.png")#
Nepal = Country(2, "Nepal",  "ClickPictures/NEPAL.png", "SubContinentPictures/31.png")#

Orissa = Country(5, "Orissa",  "ClickPictures/ORISSA.png", "SubContinentPictures/32.png")#
Oude = Country(4, "Oude",  "ClickPictures/OUDE.png", "SubContinentPictures/33.png")#
Pegu = Country(5, "Pegu",  "ClickPictures/PEGU.png", "SubContinentPictures/34.png")#
Raipur = Country(5, "Raipur",  "ClickPictures/RAIPUR.png", "SubContinentPictures/36.png")#

Shan_States = Country(5, "Shan States",  "ClickPictures/SHAN_STATES.png", "SubContinentPictures/37.png")#
Sikkim = Country(3, "Sikkim", "ClickPictures/SIKKIM.png", "SubContinentPictures/38.png")#	
Sindh = Country(5, "Sindh", "ClickPictures/SINDH.png", "SubContinentPictures/39.png")#
Sirhind = Country(5, "Sirhind", "ClickPictures/SIRHIND.png", "SubContinentPictures/40.png")#

Upper_Burma = Country(3, "Upper Burma",  "ClickPictures/UPPER_BURMA.png", "SubContinentPictures/42.png")#
Bhutan = Country(4, "Bhutan", "ClickPictures/BHUTAN.png", "SubContinentPictures/06.png")#
Carnatic = Country(5, "Carnatic", "ClickPictures/CARNATIC.png", "SubContinentPictures/11.png")#
Ceylon = Country(4, "Ceylon", "ClickPictures/CEYLON.png", "SubContinentPictures/12.png")#

Tenaserrim = Country(5, "Tenaserrim",  "ClickPictures/TENASERRIM.png", "SubContinentPictures/41.png")
Kafiristan = Country(2, "Kafiristan", "ClickPictures/KAFIRISTAN.png", "SubContinentPictures/KAFIRISTAN.png")
Multan = Country(2, "Multan", "ClickPictures/MULTAN.png", "SubContinentPictures/MULTAN.png")
Hyderabad = Country(2, "Hyderabad", "ClickPictures/HYDERABAD.png", "SubContinentPictures/HYDERABAD.png")

Mandalay = Country(2, "Mandalay", "ClickPictures/MANDALAY.png", "SubContinentPictures/MANDALAY.png")
Mysore = Country(2, "Mysore", "ClickPictures/MYSORE.png", "SubContinentPictures/MYSORE.png")
Coramandel = Country(4, "Coramandel", "ClickPictures/CORAMANDEL.png", "SubContinentPictures/CORAMANDEL.png")
Arracan = Country(3, "Arracan", "ClickPictures/ARRACAN.png", "SubContinentPictures/ARRACAN.png")


Assam = Country(3, "Assam",  "ClickPictures/ASSAM.png", "SubContinentPictures/ASSAM.png")
West_Bengal = Country(3, "West Bengal",  "ClickPictures/WEST_BENGAL.png", "SubContinentPictures/WEST_BENGAL.png")
Bihar = Country(3, "Bihar",  "ClickPictures/BIHAR.png", "SubContinentPictures/BIHAR.png")
Garhwal = Country(3, "Garhwal",  "ClickPictures/GARHWAL.png", "SubContinentPictures/GARHWAL.png")

Delhi = Country(3, "Delhi", "ClickPictures/DELHI.png", "SubContinentPictures/DELHI.png")
Doab = Country(3, "Doab",  "ClickPictures/DOAB.png", "SubContinentPictures/DOAB.png")
Circas = Country(3, "Circas",  "ClickPictures/CIRCAS.png", "SubContinentPictures/CIRCAS.png")
Malwa = Country(3, "Malwa",  "ClickPictures/MALWA.png", "SubContinentPictures/MALWA.png")

Cutch = Country(3, "Cutch",  "ClickPictures/CUTCH.png", "SubContinentPictures/CUTCH.png")

East_Bengal = Country(5, "East Bengal", "ClickPictures/EAST_BENGAL.png", "SubContinentPictures/EAST_BENGAL.png")
Ahmed = Country(5, "Ahmed", "ClickPictures/AHMED.png", "SubContinentPictures/AHMED.png")


CountryList = [Kathiawar, Bejapoor, Bustar, Malabar, Nagpur, CIA, Kandeish, Andaman, Cashmere, Rajpootana, Punjab, Konkan, Nepal, Orissa, Oude, Pegu, Raipur, Shan_States, Sikkim, Sindh, Sirhind, Upper_Burma, Bhutan, Carnatic, Ceylon, Tenaserrim, Kafiristan, Multan, Hyderabad, Mandalay, Mysore, Coramandel, Arracan, Assam, West_Bengal, Bihar, Garhwal, Delhi, Doab, Circas, Malwa, Cutch, East_Bengal, Ahmed]

South_India = [Ceylon, Carnatic, Coramandel, Mysore, Malabar, Konkan, Bejapoor, Hyderabad, Circas, Bustar, Nagpur, Raipur, Orissa, CIA, Kandeish]

Indus_Valley_India = [Ahmed, Kathiawar, Cutch, Sindh, Rajpootana, Multan, Punjab, Sirhind, Delhi, Garhwal, Kafiristan, Cashmere]

Bengo_Myanmar = [West_Bengal, East_Bengal, Bihar, Sikkim, Bhutan, Assam, Upper_Burma, Shan_States, Mandalay, Arracan, Pegu, Tenaserrim, Andaman]



#making the graphs...             ****************************************************************
#**************************************************************************************************
#For the graph
SouthIndiaGraph = nx.Graph()

NorthWestIndiaGraph = nx.Graph()

SouthEastAsiaGraph = nx.Graph()

CombinedGraph = nx.Graph()


#To make the color triplets unique:
colorToCountry = {}



#Graph.add_edge(Mysore, Malabar, weight=3)

SouthIndiaNeighbors = [(Mysore, Malabar), (Mysore, Carnatic), (Mysore, Coramandel), (Mysore, Bejapoor), (Ceylon, Carnatic), (Carnatic, Coramandel), (Carnatic, Malabar), (Coramandel, Circas), (Malabar, Konkan), (Konkan, Kandeish), (Bejapoor, Hyderabad), (Bejapoor, Kandeish), (Hyderabad, Kandeish), (Hyderabad, Bustar), (Hyderabad, Nagpur), (Kandeish, Nagpur), (Circas, Orissa), (Circas, Bustar), (Bustar, Nagpur), (Bustar, Raipur), (Bustar, Orissa), (Nagpur, Raipur), (Nagpur, CIA), (Raipur, Orissa), (Raipur, Orissa), (Orissa, CIA)]

NorthWestIndiaNeighbors = [(Kafiristan, Cashmere), (Kafiristan, Punjab), (Punjab, Sirhind), (Punjab, Garhwal), (Punjab, Multan), (Punjab, Rajpootana), (Garhwal, Sirhind), (Multan, Sindh), (Sindh, Cutch), (Sindh, Rajpootana), (Rajpootana, Ahmed), (Rajpootana, Ahmed), (Rajpootana, Malwa), (Rajpootana, Doab), (Delhi, Rajpootana), (Rajpootana, Sirhind), (Ahmed, Kathiawar), (Malwa, Doab), (Doab, Oude), (Doab, Delhi), (Doab, Malwa), (Garhwal, Oude)]

SouthEastAsiaNeighbors = [(Pegu, Andaman), (Andaman, Tenaserrim), (Tenaserrim, Mandalay), (Pegu, Tenaserrim), (Pegu, Arracan), (Pegu, Mandalay), (Arracan, Mandalay), (Arracan, East_Bengal), (Mandalay, Upper_Burma), (Mandalay, Shan_States), (Shan_States, Upper_Burma), (Upper_Burma, East_Bengal), (Upper_Burma, Assam), (Assam, East_Bengal), (Assam, Bihar), (Assam, Bhutan), (East_Bengal, West_Bengal), (East_Bengal, Bihar), (Bhutan, Sikkim), (Sikkim, Bihar)]
#for South India



for link in SouthIndiaNeighbors:
    SouthIndiaGraph.add_edge(link[0], link[1], weight=3)

for link in NorthWestIndiaNeighbors:
    NorthWestIndiaGraph.add_edge(link[0], link[1], weight=3)

for link in SouthEastAsiaNeighbors:
    SouthEastAsiaGraph.add_edge(link[0], link[1], weight=3)

MyanmarConstituentParts = [(Upper_Burma, Shan_States), (Upper_Burma, Mandalay), (Shan_States, Mandalay), (Mandalay, Arracan), (Mandalay, Pegu), (Mandalay, Tenaserrim), (Arracan, Pegu), (Pegu, Tenaserrim), (Pegu, Andaman)]

MyanmarGraph = nx.Graph()

for link in MyanmarConstituentParts:
    MyanmarGraph.add_edge(link[0], link[1], weight = 3)


CombinedGraph = nx.compose(SouthIndiaGraph,NorthWestIndiaGraph)

CombinedGraph = nx.compose(CombinedGraph, SouthEastAsiaGraph)


#making the graphs...             ****************************************************************
#**************************************************************************************************





### For players
class Player():
    
    
    def __init__(self, name, colorTriplet):
	self.name = name
	self.capital = None
	self.colorTriplet = colorTriplet
        self.color = sum(colorTriplet)
	self.territoryList = []
	self.OccupiedTerritoryGraph = nx.Graph()


    def controlOver(self, country):
	self.OccupiedTerritoryGraph.add_node(country)
	self.territoryList.append(country)

    def relinqishControl(self, country):
	self.OccupiedTerritoryGraph.remove_node(country)
	self.territoryList.remove(country)
	

Human_Player = Player("Sikh Empire", green)

Red_Player = Player("Portuguese Empire", red)

Blue_Player = Player("Maratha Empire", blue)

Players = [Human_Player, Red_Player, Blue_Player]


num_of_players = 3


listOfOccupiedCountries = [Pegu, Assam, Shan_States, Cashmere, Multan, Ahmed, Ceylon, Bejapoor, Orissa]

PlayersDistribution = [Human_Player, Red_Player, Blue_Player]*3

def makeCountryIntoButton(country, alpha):
    for x in range(0,country.bounds.width):
	for y in range(0,country.bounds.height):
	    if country.button.get_at((country.bounds.x+x, country.bounds.y+y))!=(0,0,0,0):
		colorToCountry.update({(country.bounds.x+x, country.bounds.y+y):country})  #Creating dictiorany to make buttons



#initialize all countries with grey
for country in CountryList:
    country.colorTriplet = grey
    country.color = sum(grey)
    country.army = randint(2, 5)
    country.color_surface()
    makeCountryIntoButton(country, 255)

#initialize the occupied parts of the map

#keeping a record of which players owns which countryies
for country, player in zip(listOfOccupiedCountries, PlayersDistribution):
    player.controlOver(country)
    country.player = player


#colorize all the countries belonging to players
for country in listOfOccupiedCountries:
    country.colorTriplet = country.player.colorTriplet
    country.color = sum(country.colorTriplet)
    country.army = randint(5, 8)
    country.color_surface()

attackableCountriesFromRed = []
def printNames(ObjectList):
    for country in ObjectList:
	print country.name
	attackableCountriesFromRed.append(country)

def printNamesOfCountryObject(ObjectList):
    for country in ObjectList:
	print country.name
	


print "Hello"
printNames(Red_Player.OccupiedTerritoryGraph.nodes()) 
RedCountries = list(Red_Player.OccupiedTerritoryGraph.nodes())
    
for myCountry in RedCountries:
    myCountryNeighbors = CombinedGraph.neighbors(myCountry)
    print("The neighbors of {0}".format(myCountry.name))
    print "are:..."
    printNames(myCountryNeighbors)
    print "\n"

printNamesOfCountryObject(attackableCountriesFromRed)
niceToAttack = sorted(attackableCountriesFromRed, key=lambda x: x.army, reverse=False)
niceToAttack = [country for country in niceToAttack if country.player != Red_Player]
print "The countries that are suitable to be attacked are:"
printNamesOfCountryObject(niceToAttack)

def neighborsOf(ObjectList):
    niceToAttack = []
    for country in ObjectList:
	print country.name
	niceToAttack.append(country)
    return niceToAttack

def AIAttack(country):
    if country.army == 0:
	return
    currentPlayerColor = country.color
    niceToAttack = list(CombinedGraph.neighbors(country))
    for attackableCountry in niceToAttack:
        if attackableCountry.color == currentPlayerColor:
	    return
    	country.attacks(attackableCountry)
    	if  attackableCountry.color == country.color:
	    AIAttack(attackableCountry)

def AITurn(Player):
    troops = 7
    fairShare = troops/len(Player.territoryList)#watch out for zerodivision error
    remaining = troops%len(Player.territoryList)

    for country in Player.territoryList:
	country.army = country.army + fairShare
	country.updateTroopDisplay()
    Player.territoryList[0].army = Player.territoryList[0].army + remaining

    for country in Player.territoryList:
	AIAttack(country)
    #printNames()
    
    """
    if any player has occupied a bonus spot:
	attackCost = Djistra(PlaterWhoGotBonus)
	if closestCountry_to_LaunchAttack.army + troops > attackCost:
		Attack(PlayerWhoGotBonus)
    """

if __name__ == '__main__': 
    print "Hello"
    #AITurn(Red_Player)





