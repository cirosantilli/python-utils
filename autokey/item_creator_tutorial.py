# CREATE THE FOLDER gen_itm with the GUI!!! Script Cannot do that yet!!! TODO    

#TEST
import sys
if "item_creator" in sys.modules:
    del(sys.modules["item_creator"])
import item_creator
#/TEST

from item_creator import ItemCreator
i = ItemCreator(engine)
f = engine.get_folder('gen')
i.set_folder(f) # from now on save to the given folder by default

#-----------------------------------------------------------
# PARSE STORE
#-----------------------------------------------------------

## PHRASES (because of the 'p') expanded by HOTKEYS (because of the 'h')
i.parse_store("""hp
^+a cnta
^+b cntb
^+c cntc
^!#+d cntd
; this is a comment line. whitespace only lines are also ignored

^e cnte
""")

## SCRIPTS (because of the 's') expanded by ABBREVIATION (because of the 'a')
i.parse_store("""as
abr1
    # YOU MUST ALWAYS INDENT YOUR SCRIPTS WITH FOUR SPACES EXACTLY, OR YOU WILL GET AN ERROR!!!
    keyboard.send_keys("cnt1")
return

abr2
    keyboard.send_keys("cnt2")
return

abr3
    keyboard.send_keys("cnt3")
    keyboard.send_keys(" cnt3 continued")
return

; this is a comment line. whitespace only lines are also ignored

abr4
    # this is a regular Python comment
    keyboard.send_keys("cnt4")
return
""")

#-----------------------------------------------------------
# FACTORING OUT
#-----------------------------------------------------------

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

#-----------------------------------------------------------
# PUNCTUAL STUFF
# 
# You can also create more customized hotkeys using more internal
# functions. This is more verbose, but also more precise.
#-----------------------------------------------------------

i.store('hapcfd',[
    ['!+a','Abr5',1,'Cnt5',f,'tit5'],
    ['!+b','Abr6',1,'Cnt6',f,'tit6'],
    ['!+c', 'Abr7',0,"""keyboard.send_keys('Cnt7')""",f,'tit7'],
    ['!+d','Abr8',0,"""keyboard.send_keys('Cnt8')""",f,'tit8'],
])

i.set_is_phrase(1) # from now on make phrases, not scripts, by default.
# this does does not affect parse_store 

i.store('ac',[
    ['Abr9','Cnt9'],
    ['Abr10','Cnt10'],
])

#EXAMPLES set_hotkey_modifiers

i.set_is_phrase(0)
i.set_hotkey_modifiers('!+') # from now on, if no hotkey modifier char is specified for a hotkey, use Shift + Alt (!+)

i.store('hc',[
    ['e',"""keyboard.send_keys('cnt7')"""],
    ['f',"""keyboard.send_keys('cnt8')"""],
])

# create all the items that were previously stored.
i.create_stored_items()
# RESTART AUTOKEYS COMPLETELY IMMEDIATELY with CONTROL + Q!!!