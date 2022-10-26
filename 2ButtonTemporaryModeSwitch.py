import gremlin

throttleGuid = "{3BF1AA40-7D19-11EB-8004-444553540000}"
mode2Button = 4
mode3Button = 3

chpt = gremlin.input_devices.JoystickDecorator( # Mode 1 is parent to the other modes. If that is changed decorators for the specific modes might also be needed
    "CH Pro Throttle USB",
    throttleGuid,
     "1"
)

@chpt.button(mode2Button)
def temporaryModeSwitch2(event, vjoy, joy):
    gremlin.util.log("mode2Event")
    j = joy[gremlin.profile.parse_guid(throttleGuid)]
    if event.is_pressed:
        if j.button(mode3Button).is_pressed:
            gremlin.control_action.switch_mode("4")
        else:
            gremlin.control_action.switch_mode("2")
    else:
        if j.button(mode3Button).is_pressed:
            gremlin.control_action.switch_mode("3")
        else:
            gremlin.control_action.switch_mode("1")

@chpt.button(mode3Button)
def temporaryModeSwitch3(event, vjoy, joy):
    gremlin.util.log("mode3Event")
    j = joy[gremlin.profile.parse_guid(throttleGuid)]
    if event.is_pressed:
        if j.button(mode2Button).is_pressed:
            gremlin.control_action.switch_mode("4")
        else:
            gremlin.control_action.switch_mode("3")
    else:
        if j.button(mode2Button).is_pressed:
            gremlin.control_action.switch_mode("2")
        else:
            gremlin.control_action.switch_mode("1")
 