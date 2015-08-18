# Running

Linux: Run `python3 -m pygibank` in the project directory.

Windows: Compile the program with pynsist and install it (For the files that need to be packaged see the pynsist documentation).

This command will build the installer:

```
python3 -m nsist installer.cfg
```

# Translations

## create the pot file from the source code

```
xgettext --from-code=UTF-8 --keyword=translatable --keyword=_ --sort-output pygibank/*.{py,glade} -o pygibank/po/pygibank.pot
```

## to start a new localization

Use this command or use poedit.

```
msginit --locale=$LANG --input=pygibank.pot
```

## to compile the po thus build mo

```
msgfmt -o po/it_IT.UTF-8.mo po/it_IT.UTF-8.po
```

## place the mo-file into

For example for German:

```
pygibank/mo/de/LC_MESSAGES/pygibank.mo
```
