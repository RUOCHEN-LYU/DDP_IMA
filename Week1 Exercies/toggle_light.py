def toggle_light(light_on):
    if light_on == True:
        light_on = False
        print("Light turned off.")
    else:
        light_on = True
        print("Light turned off.")
    return light_on

toggle_light(False)
#toggle_light(True)
#toggle_light(0)
#toggle_light(1)
