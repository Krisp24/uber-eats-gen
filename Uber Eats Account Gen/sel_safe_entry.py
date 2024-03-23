from random import randint

def sel_safe_entry(element, sel_actions, input_var):
    sel_actions.move_to_element(element)
    sel_actions.click(element)
    sel_actions.pause(randint(1, 10)/20)
    for letter in input_var:
        sel_actions.send_keys(letter)
        sel_actions.pause(randint(1, 10)/20)
    sel_actions.perform()
    sel_actions.reset_actions()
