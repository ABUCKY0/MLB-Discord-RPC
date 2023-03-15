import pypresence
from pypresence import Presence
import time
import vars
from funcs import checkValidity


client_id = '1036051053440925819'  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

print("This code does not get live scores yet. ")

print("""ARI - Arizona Diamondbacks
ATL - Atlanta Braves
BAL - Baltimore Orioles
BOS - Boston Red Sox
CHC - Chicago Cubs
CWS - Chicago White Sox
CIN - Cincinnati Reds
CLE - Cleveland Guardians
COL - Colorado Rockies
DET - Detroit Tigers
HOU - Houston Astros
KCR - Kansas City Royals
LAD - Los Angeles Dodgers
LAA - Los Angeles Angels
MIA - Miami Marlins
MIL - Milwaukee Brewers
MIN - Minnesota Twins
NYY - New York Yankees
NYM - New York Mets
OAK - Oakland Athletics
PHI - Philadelphia Phillies
PIT - Pittsburgh Pirates
SDG - San Diego Padres
SEA - Seattle Mariners
SFG - San Francisco Giants
STL - St. Louis Cardinals
TBR - Tampa Bay Rays
TEX - Texas Rangers
TOR - Toronto Blue Jays
WAS - Washington Nationals""")


first = str(input("Pick the First team to display on your Discord profile: (Input the three letter abbreviation for the team)")).upper()
checkValidity(first)
second = str(input("Pick the Second team to display on your Discord profile: (Input the three letter abbreviation for the team)")).upper()
checkValidity(second)
homeOrAway = str(input("Are you home or away? (Input H or A)")).upper()


if homeOrAway == "H":
    homeOrAway = "VS"
elif homeOrAway == "A":
    homeOrAway = "@"
else:
    print("Invalid Home Or Away input. Please restart the program and enter a valid input.")
    exit()

print(RPC.update(state="Lookie Lookie", details="A test of qwertyquerty's Python Discord RPC wrapper, pypresence!"))  # Set the presence

while True:  # The presence will stay on as long as the program is running
    time.sleep(15) # Can only update rich presence every 15 seconds

    