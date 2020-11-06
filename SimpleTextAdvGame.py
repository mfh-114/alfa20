#!/usr/bin/env python3

import os
import json
import time


# ===================
# Util function start
# ===================

# ===========================
# Read game book JSON message
# ===========================
def readGameBook():
    file = open("gamebook.json", "r")
    gamebook = file.read()
    # print(gamebook)

    gbJsonObj = json.loads(gamebook)
    # print(jsonObj["title"])

    return gbJsonObj


# ============================
# Clear the screen based on OS
# ============================
def clear():

    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


def displayPlayerHealth(healthCount):
    healthCount += healthCount
    txtout('Player health: %d' % healthCount)


def displayTitle():
    txtout("**********************************************")
    txtout("***      Welcome to world of Arckine       ***")
    txtout("**********************************************")


def txtout(text):
    # column = os.get_terminal_size().columns
    # print(text.center(column))
    print(text)


def tick():
    time.sleep(2)


# =================
# Util function end
# =================


# ================
# Game scene logic
# ================
def simpleScene(sceneObj):
    try:
        gameTextList = sceneObj["game_play_texts"]
    
        for gText in gameTextList:
            txtout(gText)
    
        choiceList = sceneObj["choices"]
        for choice in choiceList:
            txtout(choice)
    
        txtout("Hints: "+sceneObj["hint"])
    
        choice = input(">")
    
        nextScenes = sceneObj["next_scenes"]
        nextScene = nextScenes["choice_"+choice]
        name = nextScene["name"]

        return name
       
    except Exception as err:
        raise Exception(err)


def complexScene(sceneObj):
    txtout("It is complex scene")
    try:
        sceneDescList = sceneObj["scene_desc"]
    
        for gText in sceneDescList:
            txtout(gText)
    
        gamePlayList = sceneObj["game_plays"]

        for gamePlay in gamePlayList:

            
        for choice in choiceList:
            txtout(choice)
    
        txtout("Hints: "+sceneObj["hint"])
    
        choice = input(">")
    
        nextScenes = sceneObj["next_scenes"]
        nextScene = nextScenes["choice_"+choice]
        name = nextScene["name"]

        return name
       
    except Exception as err:
        raise Exception(err)

# =========
# Game loop
# =========
def gameLoop(gbJsonObj):
    sceneName = "splash"
    cmd = ""
    while cmd != 'quit':

        player = gbJsonObj["player1"]

        displayTitle()
        displayPlayerHealth(player["health"])

        txtout("")

        # game scene logic

        # scene   
        try:
            sceneObj = gbJsonObj[sceneName+"_scene"]
            sceneType = sceneObj["scene_type"]
            if sceneType == "simple":
                sceneName = simpleScene(sceneObj)
            elif sceneType == "complex":
                sceneName = complexScene(sceneObj)
            else:
                txtout("Exit")
                quit()
        except Exception as err:
            print(err)
            clear()
            continue

        tick()
        # clear screen old output/input
        clear()


# =============
# Main function
# =============
def main():

    # Before starting game clear the screen.
    clear()

    gbJsonObj = readGameBook()
    gameLoop(gbJsonObj)


if __name__ == "__main__":
    main()
