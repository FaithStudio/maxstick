========
maxstick
========

Control 3ds Max with a joystick.

This is prototype to use joystick input inside 3ds Max. You can move the
currently selected object with it, e.g. a camera or any scene object.

Note: Your joystick should have a throttle control and be able to twist
around its Z axis.

Sadly the python backend does not yet seem to support proper threading,
so the joystick control will block any other user interaction in Max.


Dependencies
------------

The dependencies come bundled with this script to make it easier to run
it inside the 3ds Max python interpreter::

    pyglet : For joystick input and event handling.


Installation
------------

To use the script inside 3ds Max easily you can define a simple
macroscript that you can bind to a toolbar button or hotkey. Edit the
following maxscript as needed, then copy and execute it inside 3ds Max::

    macroscript maxstick_joystick_control
    category:"Buelter"
    buttontext:"Joystick"
    (
        fileIn @"path\to\maxstick\start.ms"
    )


How to use
----------

- Make sure have a joystick connected (with throttle and z-rotation).
- Select an object in 3ds Max, e.g. a camera. Its orientation should be
correct when you have created it in the top viewport, otherwise you must
rotate its pivot.
- Launch the joystick control using the supplied start.ms or the macro.

Button controls::

    Button 0 ('gun' button) : Pause/resume control (blocks 3ds Max interface).

    Button 1 ('rocket' button) : Stop control to free the 3ds Max interface.

Once stopped, you can restart it using start.ms again.