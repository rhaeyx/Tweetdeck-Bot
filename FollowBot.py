class FollowBot:
    def follow(self, num): # num is how many accs to follow 300 right 290 below
        lines = 15
        counter = 1
        pyautogui.moveTo(575,630, duration=1) # First follow when scrolled up.
        y = -350
        try:
            for line in range(lines)):
                x = 300
                if counter % 2 == 0:
                    x = -300

                pyautogui.click()
                pyautogui.moveRel(x,0, duration=1) # Move to next acc to follow.
                pyautogui.click()
                pyautogui.moveRel(x,0, duration=1) # Move to next acc to follow.
                pyautogui.click()
                time.sleep(1)
                pyautogui.scroll(y)
                time.sleep(1)

                counter += 1
            print('Done')
        except:
            print('Interrupted.')
