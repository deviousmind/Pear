from distutils.core import setup
import py2exe

setup(
    console=[
        {
            'script': 'pear.py',
            'icon_resources': [(0, "pear.ico")]
        }
    ]
)