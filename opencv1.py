from pyautogui import *
import os
import pyautogui
import time
import win32api, win32con
import random
import win32con

global state

def file_path(file_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = dir_path+'/'+str(file_name)+'.png'
    return file

def randomizer(int):
    return int + random.randrange(-25,25) * 0.01


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(randomizer(1)*0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


def if_fishing():
    global state, bobber_location, bobber_center
    confidencev = 0.7
    while state == 'idle':
        conf = str(confidencev * 100)
        print('searching for bobber!',conf[:5])
        bobber = pyautogui.locateOnScreen(file_path('bobbersmall'), confidence=confidencev, region = (0,0,3480,2160))
        if bobber:
            bobber_center = pyautogui.center(bobber)
            print('bobber found at',bobber_center)
            win32api.SetCursorPos(bobber_center)
            bobber_location = bobber
            state = 'fishing'
            return True
        else:
            print('not fishing!')
            time.sleep(randomizer(1)*0.1)
            confidencev -= 0.0005
3130
1580
3108 -122
1500 -80
def if_bite():
    global state, bobber_location, bobber_center
    time.sleep(randomizer(2))
    print('fishing start')
    confidence_start = 0.86
    bobber_center_offset = (bobber_center[0]+300,bobber_center[1])
    win32api.SetCursorPos(bobber_center_offset)
    count = 0
    while state == 'fishing':
        conf = str(confidence_start * 100)
        print('waiting for bite!',conf[:5],count)
        bl0 = bobber_location[0]
        bl1 = bobber_location[1]
        bl2 = bobber_location[2]
        bl3 = bobber_location[3]
        bl0 -= 180
        bl1 -= 180
        bl2 += 360
        bl3 += 360
        bobber_search = (bl0,bl1,bl2,bl3)
        if count == 0:
            bobber = pyautogui.locateOnScreen(file_path('bobber0'), region=bobber_search, confidence=confidence_start, grayscale = False)
            count += 1
        elif count == 1:
            bobber = pyautogui.locateOnScreen(file_path('bobber1'), region=bobber_search, confidence=confidence_start, grayscale = False)
            count += 1
        elif count == 2:
            bobber = pyautogui.locateOnScreen(file_path('bobber2'), region=bobber_search, confidence=confidence_start, grayscale = False)
            count += 1
        elif count == 3:
            bobber = pyautogui.locateOnScreen(file_path('bobber3'), region=bobber_search, confidence=confidence_start, grayscale = False)
            count += 1
        elif count == 4:
            bobber = pyautogui.locateOnScreen(file_path('bobber4'), region=bobber_search, confidence=confidence_start, grayscale = False)
            count += 1
        elif count == 5:
            bobber = pyautogui.locateOnScreen(file_path('bobber5'), region=bobber_search, confidence=confidence_start, grayscale = False)
            count = 0
        if bobber:
            win32api.SetCursorPos(bobber_center)
            click(bobber_center[0],bobber_center[1])
            state = 'reeling'
            print('fish on!')
            return True
        else:
            confidence_start -= 0.0001

def if_reeling():
    print('starting reel!')
    global state,bobber_center
    # print('clicking')
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    # time.sleep(8)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    # print('unclicked')
    bobber_center_offset = (bobber_center[0]+300,bobber_center[1])
    barscount = 0
    time.sleep(randomizer(2)*0.1)
    bars_bool = False
    mouse_down = False
    print(state)
    check = 0
    while state == 'reeling':
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        print('clicked down! 1')
        mouse_down_2 = True
        if not bars_bool:
            boar = (1600, 950, 1000, 500)
            print('checking for bars!')
            bars = pyautogui.locateOnScreen(file_path('bars'),region=boar,confidence=0.8)
            print('bars checked!')
        barscount += 1
        if bars or bars_bool:
            if mouse_down_2:
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                print('clicked up!')
                mouse_down_2 = False
            bars_bool = True
            print('bars found!')
            boar_part_2 = (boar[0],boar[1]+50,boar[2],boar[3])
            bob = pyautogui.locateOnScreen(file_path('bobbermg'),region=boar_part_2,confidence=0.8,grayscale=True)
            if bob:
                check += 1
                bars = pyautogui.locateOnScreen(file_path('bars'),region=boar,confidence=0.8)
                if not bars and check > 5:
                    barscount = 6
                    bars_bool = False
                print(bob[2])
                bar_center = pyautogui.center(bars)
                bob_center = pyautogui.center(bob)
                if bob_center[0] < bar_center[0]:
                    while bob_center[0] < bar_center[0]:
                        print('clicked down! 2')
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                        bob = pyautogui.locateOnScreen(file_path('bobbermg'),region=boar_part_2,confidence=0.8,grayscale=True)
                        if bob:
                            print(bob_center[0],bar_center[0])
                            bob_center = pyautogui.center(bob)
                            mouse_down = True
                        if mouse_down and bob_center[0] >= bar_center[0]:
                            print('clicked up!')
                            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
            bars = pyautogui.locateOnScreen(file_path('bars'),region=boar,confidence=0.8)
            if bars_bool == True:
                if not bars:
                    state = 'idle'
                    return True
        if barscount > 5 and not bars_bool:
            if mouse_down_2:
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                print('clicked up!')
                mouse_down_2 = False
            state = 'idle'
            print('false positive!')
            index = 0
            while index < 7:
                win32api.SetCursorPos(bobber_center_offset)
                print('checking for bobber!')
                index_lol = 0
                while index_lol < 10:
                    bobber = pyautogui.locateOnScreen(file_path('bobbernew'), confidence=0.7, region=bobber_location, grayscale = False)
                    index_lol += 1
                    if bobber:
                        break
                index += 1
                if not bobber:
                    print('not found!')
                    win32api.SetCursorPos(bobber_center)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                    time.sleep(randomizer(5)*00.1)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                    time.sleep(randomizer(2))
                else:
                    print('found!',index)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                    break
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def if_bite_2():
    global state, bobber_location, bobber_center
    bobber_center_offset = (bobber_center[0]+300,bobber_center[1])
    win32api.SetCursorPos(bobber_center_offset)
    bobber_pix = (int(bobber_center[0]-20),int(bobber_center[1]-80))
    # print(bobber_pix)
    # return
    last_10 = []
    while state == 'fishing':
        pix = pyautogui.pixel(bobber_pix[0],bobber_pix[1])
        print('bobber_pix',pix[0])
        if pix[0] < 200:
            last_10.append(True)
        else:
            last_10.append(False)
        while len(last_10) >= 10:
            last_10.pop(0)
        total = 0
        for entry in last_10:
            if entry == True:
                total += 1
        if total > 7:
            print('fish on!')
            state = 'reeling'
            return True

def if_reeling_2():
    global state, bobber_location, bobber_center
    iteration = False
    bars = None
    bar_searches = 0
    sc = 0
    while state == 'reeling':
        if not iteration:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            md = True
            iteration = True
        if not bars:
            bars = pyautogui.locateOnScreen(file_path('bars'),region=(1600, 950, 1000, 500),confidence=0.8)
            print(bar_searches)
            bar_searches += 1
        if bars == None and bar_searches > 20:
            state = 'idle'
            return True
        while bars:
            bars_center = pyautogui.center(bars)
            bar_pix = (int(bars_center[0]+220),int(bars_center[1]+34))
            pix = pyautogui.pixel(bar_pix[0],bar_pix[1])
            while pix[0] > 230 or pix[1] > 160:
                if md == True:
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                os.chdir(str(os.path.dirname(os.path.realpath(__file__)))+'/bobbermghelp')
                pyautogui.screenshot(str(sc)+'.png',region=(1600, 900, 1000, 500))
                bob = pyautogui.locateOnScreen(file_path('bobbermg'),region=(1600, 900, 1000, 500),confidence=0.8,grayscale=True)
                sc += 1
                if bob:
                    bob_center = pyautogui.center(bob)
                    while bob_center[0] < bars_center[0]:
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                        bob = pyautogui.locateOnScreen(file_path('bobbermg'),region=(1600, 900, 1000, 500),confidence=0.6,grayscale=True)
                        if bob:
                            bob_center = pyautogui.center(bob)
                        if not bob:
                            break
                        print(bob_center[0],bob_center[1])
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                bar_pix = (int(bars_center[0]+220),int(bars_center[1]+34))
                pix = pyautogui.pixel(bar_pix[0],bar_pix[1])
            state == 'idle'
            return True

def recast():
    global state, bobber_center, bobber_center
    bobber_center_offset = (bobber_center[0]+300,bobber_center[1])
    bobber_pix = (int(bobber_center[0]-122),int(bobber_center[1]-80))
    last_10 = []
    win32api.SetCursorPos(bobber_center_offset)
    while True:
        pix = pyautogui.pixel(bobber_pix[0],bobber_pix[1])
        print(pix[0])
        if pix[0] > 100:
            last_10.append(True)
        else:
            last_10.append(False)
        while len(last_10) >= 10:
            last_10.pop(0)
        total = 0
        for entry in last_10:
            if entry == True:
                total += 1
        if total < 7:
            win32api.SetCursorPos(bobber_center)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            time.sleep(randomizer(1)*0.1)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
            break


              
        
        


def main():
    global state,bobber_center
    state = 'idle'
    while True:
        if state == 'idle':
            if if_fishing():
                recast()
                if if_bite_2():
                    recast()
                    if if_reeling_2():
                        recast()
                        
if __name__ == '__main__':
    main()