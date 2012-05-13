# CREATE THE FOLDER gen with the GUI!!! Script Cannot do that yet!!!

from item_creator import ItemCreator
i = ItemCreator(engine)
i.set_folder(engine.get_folder('gen')) # from now on save to the given folder by default

# PHRASES (because of the 'p') expanded by HOTKEYS (because of the 'h')
i.parse_store("""hp
^+a cnta
^+b cntb
^+c cntc
^!#+d cntd
; this is a comment line. whitespace only lines are also ignored

^e cnte
""")

# SCRIPTS (because of the 's') expanded by ABBREVIATION (because of the 'a')
i.parse_store("""as
abr1
    keyboard.send_keys("cnt1")
return

abr2
    keyboard.send_keys("cnt2")
return

abr3
    keyboard.send_keys("cnt3")
    keyboard.send_keys("\ncnt3 continued")
return

; this is a comment line. whitespace only lines are also ignored

abr4
    # this is a regular Python comment
    keyboard.send_keys("cnt4")
return
""")

# FACTORING OUT

i.set_hotkey_modifiers('!+^#') # make hotkeys with alt shift  control super modifiers

i.parse_store("""hp
f cntf
g cntg
h cnth
""")

# from now on, '/' will be put before abbreviation trigger sequences, and ';' after them
i.set_abbreviation_prefix('/')
i.set_abbreviation_prefix(self, ';')

i.parse_store("""ap
abr5 cnt5
abr6 cnt6
abr7 cnt7
""")

# create all the items that were previously stored.
i.create_stored_items()

# RESTART AUTOKEYS COMPLETELY IMMEDIATELY with CONTROL + Q!!!