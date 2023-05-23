add = 0

def on_button_pressed_a():
    global add
    add = 5 + 10
    basic.show_number(add)
input.on_button_pressed(Button.A, on_button_pressed_a)
