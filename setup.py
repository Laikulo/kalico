import platform

from setuptools import setup, Extension
from glob import glob
from pathlib import Path
from itertools import chain

# Stock klipper compile args: -Wall -g -O2 -shared -fPIC -flto -fwhole-program -fno-use-linker-plugin
# Removed -O2, since -O3 is the default.
# removed -shared, -g, -fPIC, -Wall as they were redundant
chelper_compile_args = ["-flto", "-fwhole-program", "-fno-use-linker-plugin"]

if platform.processor() in ["x86", "x86_64", "amd64"]:
    chelper_compile_args += ["-mfpmath=sse", "-msse2"]

# Gather all the docs and config paths, and transform them into the format that setuptools wants.

klippy_data_files = filter(lambda p: p.is_file(), chain(Path('config').rglob('*'), Path('docs').rglob('*')))
data_file_pairs = {}
for path in klippy_data_files:
    path_dir = str(path.parent)
    if not path_dir in data_file_pairs:
        data_file_pairs[path_dir] = []
    data_file_pairs[path_dir].append(str(path))

setup(
    ext_modules=[
        Extension(
            name="klippy.chelper.precompiled",
            sources=glob("klippy/chelper/*.c"),
            extra_compile_args=chelper_compile_args,
        )
    ],
    data_files=data_file_pairs.items()
)
