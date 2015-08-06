========
maxstick
========

Control 3ds Max with a joystick.

This is prototype to use joystick input inside 3ds Max. You can move the
currently selected object with it, e.g. a camera or any scene object.

Sadly the python backend does not yet seem to support proper threading,
so the joystick control will block any other user interaction in Max.


How to use
----------

- Make sure have a joystick connected (with throttle and z-rotation).
- Select an object in 3ds Max, e.g. a camera.
- Launch the joystick control using the supplied start.ms

Button 0::

    Toggle joystick control on/off, the

Button 1::

    Stop joystick loop entirely.

Once stopped, you can restart it using start.ms again.