import pypresence
from pypresence import Presence
import time
import vars
from funcs import checkValidity
import statsapi
import time
import datetime
from datetime import datetime
import pytz

print("Discord MLB Game Status, by @NotJohnnyTamale#6389")
#discord client
client_id = '1036051053440925819'  
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop


t = time.localtime()
current_time = time.strftime("%Y-%m-%d", t)
sched = statsapi.schedule(start_date=str(current_time))
print("Today's games: ")

for i in range(len(sched)):
    print(str(i) + ": " + sched[i].get('away_name') + " @ " + sched[i].get('home_name'))
print("")
gameNumber = int(input("Input the number of the game to display on your Discord profile: "))

try:
    game = sched[gameNumber]
except:
    print("Invalid game number. Please restart the program and enter a valid input.")
    exit()

gamePk = game.get('game_id')
print("Note that if inning says 1 of 1, it's because the game has not started yet.")
def convertTime(time):
    time = datetime.strptime(time, '%Y-%m-%dT%H:%M:%SZ', ) #formatting gamedate
    time = pytz.utc.localize(time) #localizing gamedate to UTC
    time = time.timestamp() #converting gamedate to unix
    return time

def setup():
    global home, away, gametype, game_datetime, FINAL_gameStartTime, details, FINAL_gametype, times, inning, max
    home = game.get('home_name') # Home Team
    away = game.get('away_name') # Away Team
    gametype = game.get('game_type') # Game Type
    game_datetime = game.get('game_datetime') # Game Date
    #convert gamedate to unix
    FINAL_gameStartTime = convertTime(game_datetime)


    details = away + "(" + str(game.get("away_score")) + ")" + " @ " + home + "(" + str(game.get("home_score")) + ")"
    # Game Type
    if gametype == "S":
        FINAL_gametype = "Spring Training"
    elif gametype == "R":
        FINAL_gametype = "Regular Season"
    elif gametype == "F":
        FINAL_gametype = "Wild Card Game"
    elif gametype == "D":
        FINAL_gametype = "Division Series"
    elif gametype == "L":
        FINAL_gametype = "League Championship Series"
    elif gametype == "W":
        FINAL_gametype = "World Series"
    elif gametype == "C": 
        FINAL_gametype = "Championship Series"
    elif gametype == "N":
        FINAL_gametype = "Nineteenth Century Series"
    elif gametype == "P":
        FINAL_gametype = "Playoffs"
    elif gametype == "I":
        FINAL_gametype = "Intersquad"
    elif gametype == "E":
        FINAL_gametype = "Exhibition"
    else:
        FINAL_gametype = "Unknown"
    current_time_two = time.strptime(str(current_time), '%Y-%m-%d')
    #current_time_two = current_time_two.
    # Game Time Check positiviity
    times = FINAL_gameStartTime
    '''if (FINAL_gameStartTime - convertTime(str(current_time_two))) > 0:
        times = t
    else:
        times = FINAL_gameStartTime'''
    
    

setup()

print("")
print ("Press Ctrl+C to stop the program.")
print ("Discord RPC should be working now! If it's not, please restart the program.")
while True:
    RPC.update(state=FINAL_gametype, details=game.get("summary"), start=FINAL_gameStartTime, large_image="mlb", large_text="Major League Baseball", small_text="Major League Baseball")  # Set the presence
    time.sleep(15)  # Refresh time because discord only allows 15 seconds between updates
    sched = statsapi.schedule(start_date=str(current_time))
    setup()