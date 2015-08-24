# Running

Linux: Run `python3 -m pygibank` in the project directory.

Windows: Compile the program with pynsist and install it (For the files that need to be packaged see the pynsist documentation).

This command will build the installer:

```
python3 -m nsist installer.cfg
```

# Translations

## Create the pot file from the source code

```
xgettext --from-code=UTF-8 --keyword=translatable --keyword=_ --sort-output pygibank/*.{py,glade} -o pygibank/po/pygibank.pot
```

## To start a new localization:

Use this command or use poedit.

For Italian as spoken in Italy for example:
```
msginit --locale=it_IT --input=pygibank.pot
```

## Compile the po files into mo files:

For Italian for example:
```
msgfmt -o po/it.mo po/it.po
```

## Where does the mo-file go?

For Linux the translations can go into the directory defined in the source code:

For example for German:
```
pygibank/mo/de/LC_MESSAGES/pygibank.mo
```

For Windows, the *.mo files currently need to go into the bundled packages:

For example for French:
```
gnome/share/locale/fr/LC_MESSAGES/pygibank.mo
```
