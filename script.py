import keyboard
import pyautogui
import time
from twitter_profiles import profiles_to_follow

def detectorDeCoordenadas():
    while True:
        currentMouseX, currentMouseY = pyautogui.position()
        print(currentMouseX, currentMouseY)

        if keyboard.read_key() == "esc":
            print("Progam finish")
            break

def createNewTab():
    with pyautogui.hold('ctrl'):
        pyautogui.press('t')

def typeOnSearchBar(link):
    pyautogui.write(link)

def clickFollowButton():
    pyautogui.click(599, 351)

def followRoutine(link):
    createNewTab()
    typeOnSearchBar(link)
    pyautogui.press('enter')
    time.sleep(3)
    clickFollowButton()

def main():
    if keyboard.read_key() == "enter":
        for profile_link in profiles_to_follow:
            followRoutine(profile_link)
            print('We are now following: ' + profile_link.rsplit('/', 1)[-1], "!")

main()