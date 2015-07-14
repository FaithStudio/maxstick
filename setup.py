import setuptools

setuptools.setup(name="maxstick",
                 version="0.1.0",
                 description="Control 3ds Max with a joystick.",
                 long_description=open("README.rst").read(),
                 author="Christoph Buelter",
                 packages=["libs", "maxstick"],
                 install_requires=[]  # libs/pyglet.
                 )