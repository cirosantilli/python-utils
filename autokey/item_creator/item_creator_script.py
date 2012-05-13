# CREATE THE FOLDER gen_itm with the GUI!!! Script Cannot do that yet!!! TODO

#TEST
import sys
if "item_creator" in sys.modules:
    del(sys.modules["item_creator"])
import item_creator
#/TEST

folder_title = 'gen'
f = engine.get_folder(folder_title)

from item_creator import ItemCreator
i = ItemCreator(engine)

#EXAMPLES store
i.store('hapcfd',[
    ['!+a','abr1',1,'cnt1',f,'tit1'],
    ['!+b','abr2',1,'cnt2',f,'tit2'],
    ['^#c', 'abr3',0,"""keyboard.send_keys('cnt3')""",f,'tit3'],
    ['^#d','abr4',0,"""keyboard.send_keys('cnt4')""",f,'tit4'],
])

#EXAMPLES set_is_phrase and set_folder

i.set_folder(f) # from now on save to the given folder by default
i.set_is_phrase(1) # from now on make phrases, not scripts, by default

i.store('ac',[
    ['abr5','cnt5'],
    ['abr6','cnt6'],
])

#EXAMPLES set_hotkey_modifiers

i.set_is_phrase(0)
i.set_hotkey_modifiers('!+') # from now on, if no hotkey modifier char is specified for a hotkey, use Shift + Alt (!+)

i.store('hc',[
    ['e',"""keyboard.send_keys('cnt7')"""],
    ['f',"""keyboard.send_keys('cnt8')"""],
])

#EXAMPLES parse_store

# this makes phrases (because of the 'p') which are expanded by hotkeys (because of the 'h')
i.parse_store("""hp
!a cnt1
^b cnt2
#c cnt3

; this is a comment line, and the above line is blank and thus ignored.
    ; and this is another comment line, even if it starts with whitespaces!
    
; ERROR: you must begin every line with your abbreviation/hotkey, no whitespaces allowed! 
    #c cnt4
""")

# this makes scripts (because of the 's') which are expanded by abbreviation (because of the 'a')
i.parse_store("""as
abr1
    keyboard.send_keys("cnt1")
return

abr2
    keyboard.send_keys("cnt2")
return

; this is a comment line, and the above line is blank and thus ignored.
    ; and this is another comment line, even if it starts with whitespaces!
abr3
    # this is a regular python comment
    keyboard.send_keys("cnt3")
return

; INDENTATION
; you must indent each line of your script with exactly 4 spaces
; or you will get an exception!

; OK, 4 spaces before each line!
abr4
    keyboard.send_keys("cnt4")
    keyboard.send_keys("cnt4 second part")
return

; ERROR: one of the lines (2nd) does not start with exactly 4 spaces (starts with 0)!
; abr5
;     keyboard.send_keys("cnt5")
; keyboard.send_keys("cnt5 second part")
; return

""")

# create all the items that were previously stored.
i.create_stored_items()

# RESTART AUTOKEYS COMPLETELY! Just closing the window will not work. You need to Cntr + Q.