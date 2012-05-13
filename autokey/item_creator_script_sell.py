# CREATE THE FOLDER gen with the GUI!!! Script Cannot do that yet!!!

from item_creator import ItemCreator
i = ItemCreator(engine)
i.set_folder(engine.get_folder('gen')) # from now on save to the given folder by default

# PHRASES (because of the 'p') expanded by HOTKEYS (because of the 'h')
i.parse_store("""hp
^+a cnta
^+b cntb
^+c cntc
^+d cntd
^#!+e cnte
""")

i.set_trigger_immediately(True)
i.parse_store("""as
abr1
    keyboard.send_keys("cnt1")
return

abr2
    keyboard.send_keys("cnt2")
keyboard.send_keys(" cnt3 continued")
return
""")

# FACTORING OUT
i.set_hotkey_modifiers('!+^#') # make hotkeys with alt shift  control super modifiers

i.parse_store("""hp
f cntf
g cntg
h cnth
""")

i.set_hotkey_modifiers('') # reset default hotkey modifiers

i.set_trigger_immediately(True)
#i.set_ommit_trigger_char(True) # could also be used
i.set_abbreviation_prefix('/')
i.set_abbreviation_sufix(';')
# from now on, '/' will be put before abbreviation trigger sequences, and ';' after them

i.parse_store("""ap
abr5 cnt5
abr6 cnt6
abr7 cnt7
""")

i.set_trigger_immediately(False)
i.set_abbreviation_prefix('')   # remove the prefix
i.set_abbreviation_sufix('')    # remove the suffix

# create all the items that were previously stored.
i.create_stored_items()

# RESTART AUTOKEYS COMPLETELY IMMEDIATELY with CONTROL + Q!!!