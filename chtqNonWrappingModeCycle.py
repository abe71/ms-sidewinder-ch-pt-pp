import gremlin

tqGuid = "{B6C2C240-7D1E-11EB-8006-444553540000}"         
modeCycleUpButton = 1
modeCycleDownButton = 2
cycleUp = {'1' : '2', '2' : '3', '3' : '4', '4' : '4'} # '4' : '4' makes the mode cycle up stop at mode 4
cycleDown = {'4' : '3', '3' : '2', '2' : '1', '1' : '1'}

chtq = gremlin.input_devices.JoystickDecorator( # Mode 1 is parent to the other modes. If that is changed decorators for the specific modes might also be needed
    "CH Throttle Quadrant USB",
    tqGuid,
     "1"
)

@chtq.button(modeCycleUpButton)
def modeCycle(event, vjoy, joy):
    if event.is_pressed:
        gremlin.control_action.switch_mode(cycleUp[gremlin.event_handler.EventHandler().active_mode])

@chtq.button(modeCycleDownButton)
def modeCycle(event, vjoy, joy):
    if event.is_pressed:        
        gremlin.control_action.switch_mode(cycleDown[gremlin.event_handler.EventHandler().active_mode])