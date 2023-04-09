#!/bin/python3

import eel
import easygui
import os

ld_flags = []
cxx_flags = []

output_dir = ""

@eel.expose
def register_lib(libname: str):
    if libname == 'ncurses':
        ld_flags.append("-lncurses")
        ld_flags.append("-lmenu")
    elif libname == 'fltk':
        cxx_flags.append("`fltk-config --use-gl --use-images --cxxflags`")
        ld_flags.append("`fltk-config --use-gl --use-images --ldflags`")
    elif libname == 'gtk4':
        cxx_flags.append("`pkg-config --cflags gtk4`")
        ld_flags.append("`pkg-config --libs gtk4`")
    elif libname == 'pthread':
        cxx_flags.append("-pthread")
        ld_flags.append("-lpthread")


@eel.expose
def generate_makefile():
    ld_flags_statement = "LDFLAGS = "
    cxx_flags_statement = "CXXFLAGS = "
    for i in range(ld_flags.__len__()):
        ld_flags_statement += f'{ld_flags[i]} '
    for i in range(cxx_flags.__len__()):
        cxx_flags_statement += f'{cxx_flags[i]} '

    makefile_data = f"""{cxx_flags_statement}
{ld_flags_statement}

dev: *.cpp
\tg++ $(CXXFLAGS) -Wall -o dev *.cpp $(LDFLAGS) && ./dev

cleanup: dev
\trm -f dev
"""
    output_dir = easygui.diropenbox(title="Please select folder.")
    if output_dir == None or output_dir == "" or output_dir == False:
        return None
    with open(os.path.join(output_dir, 'Makefile'), 'w') as makefile:
        makefile.write(makefile_data)
        makefile.close()
    



eel.init("html")
eel.start("index.html", size = (800, 600))
