import platform

from setuptools import setup, Extension
from glob import glob

# Stock klipper compile args: -Wall -g -O2 -shared -fPIC -flto -fwhole-program -fno-use-linker-plugin
# Removed -O2, since -O3 is the default.
# removed -shared, -g, -fPIC, -Wall as they were redundant
chelper_compile_args=['-flto', '-fwhole-program', '-fno-use-linker-plugin']

if platform.processor() in ['x86', 'x86_64', 'amd64']:
    chelper_compile_args+=['-mfpmath=sse', '-msse2']

setup(
    ext_modules=[
        Extension(
            name='klippy.chelper.precompiled',
            sources=glob('klippy/chelper/*.c'),
            extra_compile_args=chelper_compile_args
        )
    ]
)