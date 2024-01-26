
import gremlin


from gremlin.user_plugin import *

_PLUGIN_NAME = "Continous Fire"
_VERSION = '1.0'

_DEBUG = False  # extra log messages

mode = ModeVariable("Mode", "The mode to use for this mapping")

btn_input = PhysicalInputVariable(
    "Input Button",
    "Button which will be mapped by this plugin.",
    [gremlin.common.InputType.JoystickButton],
)

vjoy_btn = VirtualInputVariable(
    "Output Button",
    "vJoy button to use as the output.",
    [gremlin.common.InputType.JoystickButton],
)


def output_button(pressed_state, vjoy):
    if _DEBUG:
        gremlin.util.log(f"{_PLUGIN_NAME}: Setting output state to {pressed_state}")
    vjoy[target_vjoy_id].button(target_input_id).is_pressed = pressed_state


gremlin.util.log(f"{_PLUGIN_NAME}: Activating...")
gremlin.util.log(f"{_PLUGIN_NAME}: Input is {btn_input.value}")
gremlin.util.log(f"{_PLUGIN_NAME}: Mode is {mode.value}")

target_vjoy_id = vjoy_btn.vjoy_id
target_input_id = vjoy_btn.input_id

if not btn_input.value:
    gremlin.util.log(f"{_PLUGIN_NAME}: Invalid input, cannot activate plugin")

input_decorator = btn_input.create_decorator(mode.value)

@input_decorator.button(btn_input.input_id)
def input_button(event, joy, vjoy):
    if _DEBUG:
        gremlin.util.log(f"{_PLUGIN_NAME}: Input button state: {event.is_pressed}")
    global input_button_start_time, hold_timer
    if event.is_pressed:
        if _DEBUG:
            gremlin.util.log(f"{_PLUGIN_NAME}: Processing press...")
        # send 'pressed' to target
        if vjoy[target_vjoy_id].button(target_input_id).is_pressed:
            output_button(False, vjoy)
        else:
            output_button(True, vjoy)