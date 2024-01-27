# ms-sidewinder-ch-pro-throttle-ch-pro-pedals
A joystick gremlin map for vjoy, microsoft-sidewinder2 joystick, ch-pro throttle and ch pro pedals

## vJoy
configure vjoy 1 and 2 with at least the 4 first axises, 2 POVs and 32 buttons. The number of axises or buttons must differ for joystick gremlin to work, so I use 33 buttons for vjoy 2 otherwise as the default.

## HidHide
I use hidHide:
https://github.com/nefarius/HidHide/releases
To hide the physical inputs from the elite, it simplifies the key/axis mapping  a lot.

Make sure joystick gremlin is whitelisted before hiding your devices. I also whitelist the CH control manager to be able to calibrate the throttle and pedals.

## joystick gremlin
I use joustick gremlin Release 13.3

http://whitemagic.github.io/JoystickGremlin 

Make sure to install vjoy devices as described above before loading the map into joystick gremlin.


## Modes
Buttons 5-8 on the sidewinder is used for "sticky mode". Button 3 and 4 controls mode 1-4 just like a shift/control key combination would. 

* Mode 1: Release both button 3 and 4 on the throttle, 
* Mode 2: button 4 on the throttle
* Mode 3 button 3 on the throttle
* Mode 4: both button 3 and 4

This repeats for higher modes. Pushing button 5 - 8 controls the "sticky mode" on the sidewinder. So pushing button 6 on the sidewinder gives mode 5 if button 3 and 4 on the throttle are released, mode 6 if throttle button 4 is pressed and so on, so all in all there are 16 modes, for shift/control modes for each sticky mode.

## Button mapping
All buttons are mapped to joystick buttons different for all modes, making use of 8 vjoy devices. There are a few exceptions:

* The hats have only the first 2 shifted modes for all sticky modes as unique hats, shifted mode 3 and 4 falls back to the first hat, this is true for both the pro throttle and the sidewinder
* Button 1, the fire button on the sidewinder is mapped to the same button in all modes
* Button 1, the ministick on the pro throttle is mapped to mouse buttons and is the same for all sticky modes: 
  - mode 1: left mouse button
  - mode 2: right mouse button
  - mode 3: middle mouse button
  - mode 4: forward mouse button
* Button 3 and 4 on the pro throttle are shift mode buttons
* button 5-8 on the sidewinder are sticky mode buttons

## Pro throttle Ministick
The PT ministick is mapped as mouse
