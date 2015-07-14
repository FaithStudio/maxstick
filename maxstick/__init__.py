import os
import sys

def _init_libs():
    thisfile = os.path.abspath(__file__)
    parentdir = os.path.dirname(os.path.dirname(thisfile))
    libsdir = os.path.join(parentdir, "libs")
    sys.path.append(libsdir)

_init_libs()

import pyglet

import MaxPlus


def loop():
    sticks = pyglet.input.get_joysticks()
    if not sticks:
        print("ERROR: No joystick found.")
        return

    stick = sticks[0]

    def update_camera_transform(dt, *args, **kwargs):
        mxs = (
               "tm = $Camera001.transform\n"

               # Joystick accelerate/deaccelerate.
               "preTranslate tm [0, 0, {stick.z}]\n"

               # Joystick up and down.
               "preRotate tm (eulerToQuat (eulerAngles {stick.y} 0 0))\n"

               # Joystick left to right.
               "preRotate tm (eulerToQuat (eulerAngles 0 0 ({stick.x} * -1) ))\n"

               # Joystick rotate around itself.
               "preRotate tm (eulerToQuat (eulerAngles 0 ({stick.rz} * -1) 0))\n"

               "$Camera001.transform = tm\n"

               "slidertime += 1\n"

               # "windows.processPostedMessages()\n"
              ).format(stick=stick)
        # print(mxs)
        MaxPlus.Core.EvalMAXScript(mxs)
        MaxPlus.ViewportManager.ForceCompleteRedraw()

    pyglet.clock.schedule(update_camera_transform)

    # Display a window so we can close the event loop.
    # By default it will stop when all open windows are closed.
    caption = "maxstick: Close me to stop the joystick."
    dialogstyle = pyglet.window.Window.WINDOW_STYLE_DIALOG
    window = pyglet.window.Window(300, 10, caption=caption, style=dialogstyle)

    # @window.event
    # def on_draw():
    #     # s = stick
    #     # print s.x, s.y, s.z, s.hat_x, s.hat_y

    # def on_joybutton_press(joystick, button):
    #     # on_draw()
    #     # print("Pressed button: {button}".format(**locals()))

    # def on_joybutton_release(joystick, button):
    #     # on_draw()
    #     # print("Released button: {button}".format(**locals()))

    # def on_joyaxis_motion(joystick, axis, value):
    #     # on_draw()
    #     # print("Motion on axis: {axis} with value: {value}".format(**locals()))

    # def on_joyhat_motion(joystick, hat_x, hat_y):
    #     # on_draw()
    #     # print("Joyhat motion x: {hat_x}, y: {hat_y}".format(**locals()))

    # stick.on_joybutton_press    = on_joybutton_press
    # stick.on_joybutton_release  = on_joybutton_release
    # stick.on_joyaxis_motion     = on_joyaxis_motion
    # stick.on_joyhat_motion      = on_joyhat_motion
    stick.open()

    print("Starting app...")
    pyglet.app.run()

loop()

# """
# python.executeFile @"C:\Users\Buelter\Google Drive\dev\maxstick\maxstick\__init__.py"
# """
