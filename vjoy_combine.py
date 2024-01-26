"""User plugin to combine two physical axes into one virtual axis via intermediate vJoy axes

To use, each physical axis should first be remapped to separate intermediate vJoy axes. 
Asign any relative scaling, sign inversion, or deadzones at each input device axis 
via the usual Response Curve mapper. Then, in the plugin settings select each physical
axis and corresponding intermediate vJoy axis. Finally, select the vJoy axis to output
the combined signal to.

This allows the user to more easily mainpulate response curves and deadzones at the input
device, rather than through relatively inflexible additions to this plugin script.

Optional axis multipliers are allowed. This allows for on-the-fly adjustments to relative
axes weighting without adjusting a pre-set response curve. Axis inversion can be applied 
with the checkboxes provided.

"""

"""
Many thanks for WhiteMagic for his many example scripts and for creating Joystick
Gremlin in the first place.
    
Copyright 2021 Edward Barber

Permission is hereby granted, free of charge, to any person obtaining a copy of this 
software and associated documentation files (the "Software"), to deal in the Software 
without restriction, including without limitation the rights to use, copy, modify, merge, 
publish, distribute, sublicense, and/or sell copies of the Software, and to permit 
persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or 
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR 
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE 
FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
DEALINGS IN THE SOFTWARE.
"""

import threading
import time
import gremlin
from gremlin.user_plugin import *

# variables to be selected by the user during configuration creation
mode = ModeVariable("Mode", "The mode in which to use this mapping")

input_1 = PhysicalInputVariable(
    "Input physical axis 1",
    "Physical axis mapped intermediate virtual axis 1",
    [gremlin.common.InputType.JoystickAxis]
)

weight_1 = FloatVariable(
    "Axis 1 multiplier",
    "Multiply axis 1 value before combining",
    1,
    -10.0,
    10.0
)

invert_1 = BoolVariable(
    "Invert axis 1?",
    "Bodge to allow negative weights while GUI widget is broken",
    False
) 

input_2 = PhysicalInputVariable(
    "Input physical axis 2",
    "Physical axis mapped to intermediate virtual axis 2",
    [gremlin.common.InputType.JoystickAxis]
)

weight_2 = FloatVariable(
    "Axis 2 multiplier",
    "Multiply axis 2 value before combining",
    1,
    -10.0,
    10.0
)

invert_2 = BoolVariable(
    "Invert axis 2?",
    "Bodge to allow negative weights while GUI widget is broken",
    False
) 

output = VirtualInputVariable(
    "Output virtual axis",
    "Axis to use the sum of intermediate axes 1 and 2",
    [gremlin.common.InputType.JoystickAxis]
)

# invert weights if requested
if invert_1.value:
    weight_1.value = -weight_1.value
if invert_2.value:
    weight_2.value = -weight_2.value

# update both axes simultaneously if either changes
def update_axis(vjoy, joy):
    axis_1_value = weight_1.value * joy[input_1.device_guid].axis(input_1.input_id).value
    axis_2_value = weight_2.value * joy[input_2.device_guid].axis(input_2.input_id).value
    value = gremlin.util.clamp((axis_1_value -0.05 + axis_2_value),-1.0,1.0)
    vjoy[output.vjoy_id].axis(output.input_id).value = value
    
# input axes decorators
dec_1 = input_1.create_decorator(mode.value)
dec_2 = input_2.create_decorator(mode.value)


@dec_1.axis(input_1.input_id)
def axis1(event, vjoy, joy):
    update_axis(vjoy, joy)

@dec_2.axis(input_2.input_id)
def axis2(event, vjoy, joy):
    update_axis(vjoy, joy)