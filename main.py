def on_button_pressed_a():
    basic.pause(2000)
    Drones.Basic_action(Drones.Basicoptions.TAKEOFF)
    Drones.hovering(10)
    Drones.Basic_action(Drones.Basicoptions.LANDING)
input.on_button_pressed(Button.A, on_button_pressed_a)


def on_received_string(receivedString):
    if receivedString == "stop":
        basic.show_icon(IconNames.SAD)
        Drones.Basic_action(Drones.Basicoptions.LANDING)
        basic.show_icon(IconNames.SWORD)
        control.reset()
radio.on_received_string(on_received_string)

radio.set_group(33)
Drones.init_module(Drones.Runmodes.MASTER)