import setuptools


setuptools.setup(name="maxstick",
                 version="0.2.0",
                 description="Control 3ds Max with a joystick.",
                 long_description=open("README.rst").read(),
                 author="Christoph Buelter",
                 packages=setuptools.find_packages(),
                 install_requires=[]  # maxstick/libs/pyglet
                 )