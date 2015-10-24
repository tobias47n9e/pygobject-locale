# encoding: utf-8
from __future__ import print_function, unicode_literals

from gi.repository import Gtk
import gettext
import locale
import sys
import os

from os.path import join, abspath, dirname


APP = "pygibank"
WHERE_AM_I = abspath(dirname(__file__))
LOCALE_DIR = join(WHERE_AM_I, 'mo')

if sys.platform.startswith('win'):
    # Set $LANG on MS Windows for gettext
    if os.getenv('LANG') is None:
        lang, enc = locale.getdefaultlocale() #lang is POSIX e.g. de_DE
        print(lang, enc)
        os.environ['LANG'] = lang

    # Set LOCALE_DIR for MS Windows
    import ctypes
    LIB_INTL = abspath(join(WHERE_AM_I, "../gnome/libintl-8.dll"))
    libintl = ctypes.cdll.LoadLibrary(LIB_INTL)
    lc = locale.setlocale(locale.LC_ALL, "")
    print(lc) # Returns local. On W e.g. German_Germany.1252
    btd = libintl.bindtextdomain(APP, LOCALE_DIR)
    print(btd) # Returns a random number e.g. 52047488 (?)
    libintl.bind_textdomain_codeset(APP, "UTF-8")
else:
    #POSIX locale settings
    locale.setlocale(locale.LC_ALL, locale.getlocale())
    locale.bindtextdomain(APP, LOCALE_DIR)

gettext.bindtextdomain(APP, LOCALE_DIR)
gettext.textdomain(APP)
_ = gettext.gettext


class MyApp(object):
    def __init__(self):
        self.builder = Gtk.Builder()
        self.glade_file = join(WHERE_AM_I, 'ui.glade')
        ret = self.builder.set_translation_domain("pygibank")
        print(ret) # = None. Not useful.
        self.builder.add_from_file(self.glade_file)

        print(_('PyGiBank - The window title'))
        print(_('Hellö User'))
        print(_('Press the Button'))
        print(_('On or off?'))

        go = self.builder.get_object
        self.window = go('window')
        self.builder.connect_signals(self)
        self.translate_gui() # This call is only needed for Windows tranlation.
        self.window.show()

    def translate_gui(self):
        """
        For Windows, cycle over objects and set label and title again.

        This function only executes on Windows. For each object in
        the Glade-file, the label and title is retrieved and if it is
        None it sets the label and title again. The '_()' ensures that
        the strings are translated.
        """
        if sys.platform == "win32":
            for obj in self.builder.get_objects():
                if (not isinstance(obj, Gtk.SeparatorMenuItem)) and hasattr(obj, "get_label"):
                    label = obj.get_label()
                    if label is not None:
                        obj.set_label(_(label))
                elif hasattr(obj, "get_title"):
                    title = obj.get_title()
                    if title is not None:
                        obj.set_title(_(title))

    def main_quit(self, widget):
        Gtk.main_quit()


if __name__ == '__main__':
    gui = MyApp()
    Gtk.main()

def start():
    gui = MyApp()
    Gtk.main()
