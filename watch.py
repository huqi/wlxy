import pyautogui
import time
import cv2
import logging

pyautogui.PAUSE = 5

img_play = cv2.imread(r'play.jpg')
img_yes = cv2.imread(r'yes.jpg')
img_c =  cv2.imread(r'c.jpg')
img_b =  cv2.imread(r'begin.jpg')

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(filename)s : %(levelname)s %(message)s')

def local(img):
    return pyautogui.locateCenterOnScreen(img, confidence=0.6)

while True:
    
    time.sleep(10)
    
    r = local(img_play)
    
    logging.info("找到播放信息，位置:({0})".format(r))
    if r:
        pyautogui.click(r[0], r[1])
        
    logging.info("找到播放信息，位置({0})".format(r))
    pyautogui.click(r[0], r[1])
    r = local(img_c)
    
    if not r:
        r = local(img_b)
    
    if not r:
        r = local(img_yes)   


    logging.info("进入新界面找到播放按钮，位置({0})".format(r))
    pyautogui.click(r[0], r[1])
    
    time.sleep(50*60)
    
    pyautogui.hotkey('ctrl', 'r')
    logging.info("刷新播放页面")
    
    pyautogui.hotkey('ctrl', 'w')
    logging.info("关闭播放页面")
    
    pyautogui.hotkey('ctrl', 'r')
    logging.info("刷新主页面")
    
        
result = pyautogui.locateCenterOnScreen(img, confidence=0.6)
print(result)
# pyautogui.moveTo(result)