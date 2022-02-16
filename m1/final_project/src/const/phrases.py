
def phrase_for_start_first_greeting(data):
    return "Hello, " + data["user_name"] + "!"

def phrase_for_start_regular_greeting(data):
    return "Hello again, " + data["user_name"] + "! It's good to see ya back!"

def phrase_for_answer_to_main_menu_buttons(data):
    return "You pressed " + data["button_title"]
