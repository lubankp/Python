import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "includes": ["tkinter"],
    "include_files": ["icon.ico"]
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup( 
    options = {"build_exe": build_exe_options},
    executables = [Executable("question1.py", base=base, icon="icon.ico")]
)
