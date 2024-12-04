def on_logo_pressed():
    basic.show_arrow(randint(0, 8))
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)
