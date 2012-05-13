""" Ciro D. Santilli

*** Multiple Phrase/Script creation script ***

Convenient Autohotkey like user interface for multiple script 
creation from a single script.

#--------------------------------------------------------------------------#
INSTALLATION

    1) Inside item_creator.py, make sure PATH_TO_YOUR_AUTOKEY_LIB, points to your 
    autokey share folder, which contains all non-interface files (common.py, configmanager.py, etc.)
    
    Mine was "/usr/share/pyshared/autokey". 
    
    2) Put the item_creator.py file in your script import path (Edit > Preferences > Script engine) 
    ** DONE **

#--------------------------------------------------------------------------#
BASICS (Examples 1-4)

    - An Item is either a Phrase of a Script.
    
    - First you store, then you create
    
    - Item adder is a STATE MACHINE

#--------------------------------------------------------------------------#
HOTKEY MODIFIERS (Examples 1-4)

    Hotkey modifiers are the same as those used by Autohotkeys:
    
    ^   Control
    +   Shift
    !   Alt
    #   Super

#--------------------------------------------------------------------------#
PARAMETER ORDER

    You decide which parameters you are giving "store", and in what order with a letter. 

    The letters are:

    Letter       meaning
          
    h            Hotkey               
    a            Abbreviations        
    p            Is Phrase           
    c            Contents            
    f            Folder (from engine.get_folder())
    d            Description (will be used to create the title of the hotkey)

The following parameter order is recommended:
    
        h a p c f d

#--------------------------------------------------------------------------#
INNER STATE (Examples 5-...)

An ItemCreator is a state machine. Currently, the following functions set used to set states:

i.set_hotkey_modifiers('!+') # from now on, if no hotkey modifier char is specified for a hotkey, use Shift + Alt
i.set_is_phrase(1)           # from now on make phrases, not scripts, by default
i.set_folder(f)              # from now on save to the given folder by default        

Those will be used on subsequent calls to store(), unless parameters in the store method are used to overide them.

#--------------------------------------------------------------------------#
EXAMPLES

    All examples are created in the folder genabr.
    
    1) a phrase (and not a script, because of the 1)
    hotkey: Alt + Shift + a
    abbreviation:   "abr1" (explained in HOTKEY MODIFIERS)
    expands to: "cnt1"
    title:  "tit1"
    folder: "genabr"
    
    2)  a phrase
    hotkey Alt + Shift + b
    abbreviations: "abr2.1" and "abr2.2"
    expands to: "cnt2"
    title:    "tit2"
    folder: "genabr"
    
    3) a script (because of the 0)
    hotkey: Alt + Shift + c
    abbreviation: "abr3"
    executes:   "keyboard.send_keys("cnt3")" (which happens to sent "cnt3" to the keyboard)
    title:  "tit3"
    folder: "genabr"
    
    4) a phrase (and not a script, because of the 1)
    hotkey: Alt + Shift + d
    abbreviations:   "abr4.1" and  "abr4.2" (explained in HOTKEY MODIFIERS)
    executes:   "keyboard.send_keys("cnt4")" (which happens to sent "cnt4" to the keyboard)
    title:  "tit4"
    folder: "genabr"
    
    5) phrase ( because of the earlier call to set_is_phrase(1) )
    hotkey: NONE (default when not specified)
    abbreviations:   'abr5'
    expands to:   "cnt5"
    title:  ""  (default when not specified)
    folder: "genabr"    ( because of the earlier call to set_folder(f) )

    6) phrase ( because of the earlier call to set_is_phrase(1) )
    hotkey: NONE
    abbreviations:   'abr6'
    expands to:   "cnt6"
    title:  ""
    folder: "genabr"    ( because of the earlier call to set_folder(f) )
    
    7) script
    hotkey: Alt + Shift + e    ( Alt and Shift because of the earlier call to set_hotkey_modifiers('!+') )
    abbreviations:   NONE
    executes:   "keyboard.send_keys("cnt7")"
    title:  "tit7"
    folder: "genabr"
    
    8) script
    hotkey: Alt + Shift + f    ( Alt and Shift because of the earlier call to set_hotkey_modifiers('!+') )
    abbreviations:   NONE
    executes:   "keyboard.send_keys("cnt7")"
    title:  "tit7"
    folder: "genabr"
"""

from item_creator import ItemCreator
i = ItemCreator(engine)

folder_title = 'genabr'
# make sure the folder exists and get it
# f = i.remake_folder('gen_abr')

# CREATE THE FOLDER genabr with the GUI!!!
f = engine.get_folder(folder_title)

#EXAMPLES 1-4
i.store('hapcfd',[
    ['!+a','abr1',1,'cnt1',f,'tit1'],
    ['!+b',['abr2.1','abr2.2'],1,'cnt2',f,'tit2'],
    ['^#c', 'abr3',0,"""keyboard.send_keys('cnt3')""",f,'tit3'],
    ['^#d',['abr4.1','abr4.4'],0,"""keyboard.send_keys('cnt4')""",f,'tit4'],
])

# set cur_default for next 
i.shm('!+') # from now on, if no hotkey modifier char is specified for a hotkey, use Shift + Alt
i.sip(1) # from now on make phrases, not scripts, by default
i.sf(f) # from now on save to the given folder by default


i.set('m !+ p 1 f f ')

i.store(

)

#EXAMPLES 5-6
i.s('ac',[
    ['abr5','cnt5'],
    ['abr6','cnt6'],
])

#EXAMPLES 7-8
i.s('hpcd',[
    ['e',0,"""keyboard.send_keys('cnt7')""",'tit7'],
    ['f',0,"""keyboard.send_keys('cnt8')""",'tit8'],
])

# cursor posisioning
i.ps("""ap
abr1 I want to \n\ngo \t\tto this point \C\n\n \tafter all \n\nis spanded.
""")
# \C == CURSOR POSITION
# \n == enter
# \t == tab

# Parse Store
i.ps("""ap
abr5 cnt5
abr6 cnt6
abr5 cnt5
abr6 cnt6
abr5 cnt5
abr6 cnt6
abr5 cnt5
abr6 cnt6
""")

i.store_parse("""as
abr5
    i = 2
    i = i + 3
return

abr5
    i = 2
    i = i + 3
return

abr5
    i = 2
    i = i + 3     
return
""")

i.ps("""hp
g cntG
h cntH
i cntI
j cntJ
k cntK
""")

i.ps("""Ahp
abr20 abr21 abr22 c cnt20
abr23 abr24 abr25 d cnt23
""")

i.csi()