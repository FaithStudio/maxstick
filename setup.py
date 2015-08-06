import setuptools


setuptools.setup(name="maxstick",
                 version="0.2.3",
                 description="Control 3ds Max with a joystick.",
                 long_description=open("README.rst").read(),
                 author="Christoph Buelter",
                 packages=setuptools.find_packages(),
                 install_requires=[]  # maxstick/libs/pyglet
                 )