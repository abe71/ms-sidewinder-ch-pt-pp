# ms-sidewinder-ch-pro-throttle-ch-pro-pedals
A joystick gremlin map for vjoy, microsoft-sidewinder2 joystick, ch-pro throttle and ch pro pedals

## setup

### vJoy
configure vjoy 1 to 8 with at least the 4 first axises, 4 POVs (continous) and 32 buttons. The number of axises or buttons must differ for joystick gremlin to work, so I use 33 buttons for vjoy 2, 34 buttons for vjoy3 etc. The map itself ignores these extraneous buttons, they are there just for joystick gremlin to recognize them as different devices.

### HidHide
I use hidHide:
https://github.com/nefarius/HidHide/releases
to hide the physical inputs from IL2 which can not handle more than 8 controllers in total.

Make sure joystick gremlin is whitelisted before hiding your devices. I also whitelist the CH control manager to be able to calibrate the throttle and pedals.

### joystick gremlin
I use joustick gremlin Release 13.3

http://whitemagic.github.io/JoystickGremlin 

Make sure to install vjoy devices as described above before loading the map into joystick gremlin.

### IL2
Put abe.action in data\input\custom in you il2 installation folder. Also rename the devices.txt to devices.txt.backup in the data\input folder, otherwise if you have used other controllers the game might get confused. devices.txt will be regenerated at game startup with the correct controller mapping, so make sure hidHide is activated before starting IL2. You can always circle back and delete the devices.txt and restart the game if you forgot.


## Description of the map
The amount of virtual buttons might feel overwhelming at first, but it makes it possible to organize the mappings logically so it is actually easier to remember there everything is. You will have access to 256 virtual buttons plus 4 mouse buttons and 32 virtual hats + 8 axises. The ministick on the CH pro throttle is configuered as a mouse, but it would be easy to remap the stick as axis x and y on vjoy 3 instead if wanted.

### Modes
Buttons 5-8 on the sidewinder is used for "sticky mode". Button 3 and 4 on the CH pro throttle controls mode 1-4 just like a shift/control key combination would. 

* Mode 1: button 3 and 4 on the throttle released, 
* Mode 2: button 4 on the throttle
* Mode 3 button 3 on the throttle
* Mode 4: both button 3 and 4 on the pro throttle

This pattern repeats for the higher modes. Pushing button 5 - 8 controls the "sticky mode" on the sidewinder. So pushing button 6 on the sidewinder gives mode 5 if button 3 and 4 on the throttle are released, mode 6 if throttle button 4 is pressed and so on. All in all there are 16 modes, four shift/control modes for each of the four sticky modes.

## Button mapping
All buttons are mapped to joystick buttons different on all modes, making use of all buttons on all 8 vjoy devices. There are a few exceptions:

* Button 1, the fire button on the sidewinder is mapped to the same button in all modes
* Button 1, the ministick on the pro throttle is mapped to mouse buttons and is the same for all sticky modes: 
  - mode 1, 5, 9 and 13: left mouse button
  - mode 2, 6, 10, 14: right mouse button
  - mode 3, 7, 11, 15: middle mouse button
  - mode 4, 8, 12, 16: forward mouse button
* Button 3 and 4 on the pro throttle are shift mode buttons in all modes
* button 5-8 on the sidewinder are buttons for the sticky modes and have the same functionality in all modes

## Pro throttle Ministick
The PT ministick is mapped as mouse
