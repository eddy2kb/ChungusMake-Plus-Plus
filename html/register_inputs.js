const reg_libs = () => {
    if(ncurses.checked) {
        eel.register_lib('ncurses');
    }
    if(fltk.checked) {
        eel.register_lib('fltk');
    }
    if(gtk4.checked) {
        eel.register_lib('gtk4');
    }
    if(pthread.checked) {
        eel.register_lib('pthread')
    }
}



