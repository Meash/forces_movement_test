from distutils.core import setup

setup(
    name='forces_movement_test',
    version='0.1',
    packages=['ui',
              'copter.util',
              'copter',
              'copter.sensors',
              'copter.behaviour',
              'copter.environment',
              'copter.positioning',
              'geometry'],
    url='',
    license='',
    author='Martin',
    author_email='',
    description='',

    install_requires=['sympy']
)
