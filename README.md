# ms-sidewinder-ch-pro-throttle-ch-pro-pedals
A joystick gremlin map for vjoy, microsoft-sidewinder2 joystick, ch-pro throttle and ch pro pedals

## vJoy
configure vjoy 1 and 2 with at least the 4 first axises, 2 POVs and 32 buttons. The number of axises or buttons must differ for joystick gremlin to work, so I use 33 buttons for vjoy 2 otherwise as the default.

## HiHide
I use hidHide:
https://github.com/nefarius/HidHide/releases
To hide the physical inputs from the elite, it simplifies the key/axis mapping  a lot.

Make sure joystick gremlin is whitelisted before hiding your devices. I also whitelist the CH control manager to be able to calibrate the throttle and pedals.

## joystick gremlin
I use joustick gremlin Release 13.3

http://whitemagic.github.io/JoystickGremlin 

Make sure to install vjoy devices as described above before loading the map into joystick gremlin.


## Toe breaks are strafe up down axis
The toe breaks are combined into one axis in this map and are mapped as strafe the up/down axis in elite.

## Sticky fire button
On mode 2 the fire button is sticky. That is nice for mining. Map your collector limpets to the same fire group as the mining lasers, push the fire button in mode 2 and sit back and relax until the asteroid is depleted.

## Modes
There are way too many modes for elite on this map, buttons 5-8 on the sidewinder probably could find a better use. Button 3 and 4 controls mode 1-4 in a non sticky way, just like a shift/control key combination would. 

* Mode 1: Release both button 3 and 4 on the throttle, 
* Mode 2: button 4 on the throttle
* Mode 3 button 3 on the throttle
* Mode 4: both button 3 and 4

This repeats for higher modes. Pushing button 5 - 8 controls the "sticky mode" on the sidewinder. So pushing button 6 on the sidewinder gives mode 5 if button 3 and 4 on the throttle are released, mode 6 if throttle button 4 is pressed and so on. However they all are unmapped so all higher modes behave as its parent mode which currently translates to mode 1.

To get back to "normal" again, push button 5 on the sidewinder.

## elite dangerous binds
To use the binds in this repo you must first make sure that vJoy is configured. Then just copy it over to %userprofile%\AppData\Local\Frontier Developments\Elite Dangerous\Options\Bindings