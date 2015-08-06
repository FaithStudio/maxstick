import os
import sys

import MaxPlus


thisfile = os.path.abspath(__file__)
thisdir = os.path.dirname(thisfile)
parentdir = os.path.dirname(thisdir)

def _init_libs():
    libsdir = os.path.join(parentdir, "libs")
    sys.path.append(libsdir)

_init_libs()

import pyglet


mxs_templatefile = os.path.join(thisdir, "mxs_template.ms")
mxs_template = None

stick = None
joystick_control_active = True


def _get_joystick():
    """Returns the first registered joystick."""
    sticks = pyglet.input.get_joysticks()
    stick = sticks[0]
    return stick


def _get_mxs_template():
    """Returns the maxscript template used to drive the object."""
    with open(mxs_templatefile) as f:
        return f.read()


def _update_camera_transform(dt, *args, **kwargs):
    """Fills out the maxscript template and executes it."""
    if joystick_control_active:
        mxs = mxs_template.format(stick=stick, t=1)
        MaxPlus.Core.EvalMAXScript(mxs)
        MaxPlus.ViewportManager.ForceCompleteRedraw()


def _register_handlers(stick):
    """Adds event handlers to joystick buttons.

    Button 0: Toggle joystick control.
    Button 1: Exit event loop.

    """
    def on_joybutton_press(stick, button):
        global joystick_control_active
        if button == 0:
            state = "on hold" if joystick_control_active else "active"
            print("INFO: Joystick control {0}.".format(state))
            if joystick_control_active:
                stop_joystick_control()
            else:
                start_joystick_control()
            joystick_control_active = not joystick_control_active
        elif button == 1:
            exit()

    stick.on_joybutton_press = on_joybutton_press


def initialize():
    """Setup for the joystick object and the maxscript template.

    This can be called repeatedly, e.g. for initial setup and afterwards
    when toggling the joystick control on/off.

    """
    global stick
    try:
        stick = _get_joystick()
    except IndexError:
        print("ERROR: No joystick found.")
        exit()
    _register_handlers(stick)

    global mxs_template
    mxs_template = _get_mxs_template()


def start_joystick_control():
    pyglet.clock.schedule(_update_camera_transform)


def stop_joystick_control():
    pyglet.clock.unschedule(_update_camera_transform)


def exit():
    """Shuts down the main loop."""
    print("INFO: Shutting down joystick control.")
    if stick:
        stick.close()
    pyglet.app.exit()


def main():
    """Launches the main pyglet.app loop."""
    reload(pyglet)
    initialize()
    stick.open()
    start_joystick_control()
    print("INFO: Starting joystick control.")
    pyglet.app.run()


if __name__ == '__main__':
    main()