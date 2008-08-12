#!/usr/bin/python
# setup.py
from distutils.core import setup
import py2exe
import glob

opts = {
    "py2exe": {
        "includes": "pango,atk,gobject",
        "dll_excludes": [
        "iconv.dll","intl.dll","libatk-1.0-0.dll",
        "libgdk_pixbuf-2.0-0.dll","libgdk-win32-2.0-0.dll",
        "libglib-2.0-0.dll","libgmodule-2.0-0.dll",
        "libgobject-2.0-0.dll","libgthread-2.0-0.dll",
        "libgtk-win32-2.0-0.dll","libpango-1.0-0.dll",
        "libpangowin32-1.0-0.dll"],
        }
    }

setup(
    name = "Luigi Pantano",
    description = "A nice GUI interface from geometry",
    version = "2.0",
    windows = [
        {"script": "go.py",
        }
    ],
    options=opts,
    data_files=[("zhfsj.glade"),
                ("zhfsj.gladep", glob.glob("pixmaps/*.png")),
                ("glade", glob.glob("glade/gui.glade"))
    ],
)
