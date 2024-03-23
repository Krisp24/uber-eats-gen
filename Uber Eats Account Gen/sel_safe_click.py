from random import randint

def sel_safe_click(element, sel_actions):
    sel_actions.move_to_element(element)
    sel_actions.pause(randint(1, 10)/20)
    sel_actions.click()
    sel_actions.pause(randint(1, 10)/20)
    sel_actions.perform()
    sel_actions.reset_actions()