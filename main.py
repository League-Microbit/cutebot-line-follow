basic.show_icon(IconNames.GHOST)

def on_forever():
    if cuteBot.tracking(cuteBot.TrackingState.L_R_UNLINE):
        cuteBot.motors(15, 15)
    elif cuteBot.tracking(cuteBot.TrackingState.L_UNLINE_R_LINE):
        cuteBot.motors(20, 10)
    elif cuteBot.tracking(cuteBot.TrackingState.L_LINE_R_UNLINE):
        cuteBot.motors(10, 20)
    else:
        cuteBot.motors(-15, -15)
        basic.pause(500)
        cuteBot.motors(20, -20)
        basic.pause(200)
basic.forever(on_forever)
