""" Ciro D. Santilli

*** Multiple Phrase/Script creation script ***

A script to create a bunch of scripts and phrases effectively!

#--------------------------------------------------------------------------#
I N S T A L L A T I O N

    1) Inside item_creator.py, make sure PATH_TO_YOUR_AUTOKEY_LIB, points to your 
    autokey share folder, which contains all non-interface files (common.py, configmanager.py, etc.)
    
    Mine was "/usr/share/pyshared/autokey", and yours is probably the same.

    2) Put the item_creator.py file in your script import path (Edit > Preferences > Script engine)
    
    ** DONE **

#--------------------------------------------------------------------------#
B A S I C S

    An Item is either a Pharse of a Script.

#--------------------------------------------------------------------------#
H O T K E Y   M O D I F I E R S

    Hotkey modifiers are the same as those used by Autohotkeys:
    
    ^   Control
    +   Shift
    !   Alt
    #   Super

#--------------------------------------------------------------------------#
P A R A M E T E R   O R D E R

    You may specify which parameters you are giving and in what order with a letter. 

    If a letter is missing, the field gets a default value.

    The letters are:

    Letter          meaning         default_value
    h           Hotkey                       None
    a           Abbreviations        None
    p           Is Phrase                   1
    c           Contents                   None
    t           Title                              None

The following parameter order is recommended:
    
        h a p c t

#--------------------------------------------------------------------------#
I N T E R N A L   S T A T E

    ItemCreator is a state machine! 
    
    You can set switches which it applies to the following all the following items
    
    This way you don't have to specify some switches several times.
    
    Currently available states are:
    
        is_phrase:   determines if following items are phrases or scripts
        hotkey_modifiers:   determines the modifiers of following hotkeys
        
    If one property is set as a state, but is also set in a store call, the store call gets priority, see TODO.

#--------------------------------------------------------------------------#
E X A M P L E S
    
    1) a phrase (and not a script, because of the 1)
    hotkey: Alt + Shift + a
    abbreviation:   "abr1" (explained in HOTKEY MODIFIERS)
    expands to: "cnt1"
    title:  "tit1"
    
    2)  a phrase
    hotkey Alt + Shift + b
    abbreviations: "abr2.1" and "abr2.2"
    expands to "cnt2"
    
    3) a script (because of the 0)
    hotkey: Alt + Shift + c
    abbreviation: "abr3"
    executes:   "keyboard.send_keys("cnt3")" (which happens to sent "cnt3" to the keyboard)
    title:  "tit3"
    
    4) a phrase (and not a script, because of the 1)
    hotkey: Alt + Shift + a
    abbreviations:   "abr4.1" and  "abr4.2" (explained in HOTKEY MODIFIERS)
    executes:   "keyboard.send_keys("cnt4")" (which happens to sent "cnt4" to the keyboard)
    title:  "tit4"
    
    5) phrase (default when not specified)
    hotkey: NONE (default when not specified)
    abbreviations:   'abr5'
    expands to:   "cnt5"
    title:  ""  (default when not specified)

    6) phrase (default when not specified)
    hotkey: NONE (default when not specified)
    abbreviations:   'abr5'
    expands to:   "cnt5"
    title:  ""  (default when not specified)
    
"""

from item_creator import ItemCreator
i = ItemCreator(engine)

#EXAMPLES 1-4
i.store('hapct',[
    ['!+a',"abr1",1,'cnt1','tit1'],
    ['!+b',["abr2.1","abr2.2"],1,'cnt2','tit2'],
    ['^#c', "abr3",0,"""keyboard.send_keys("cnt3")""",'tit3'],
    ['^#d',["abr4.1","abr4.4"],0,"""keyboard.send_keys("cnt4")""",'tit4'],
])

#EXAMPLES 5-6
i.store("ac",[
    ['abr5', 'cnt5'],
    ['abr6', 'cnt6'],
])

#EXAMPLE 7
i.store("hpc",[
    ["!+e", 0, """keyboard.send_keys("cnt7")"""],
 ])
 


#creates a script, and not a phrase
h.is_phrase(0)
i.store("ac",[
    ["abr11","""keyboard.send_keys("cnt11")"""]
    ["abr11","""keyboard.send_keys("cnt11")"""]
])

h.is_phrase(1)

# will also create a script, and not a phrase.
h.store("hc",[
    ["abr12","""keyboard.send_keys("cnt12")"""]
])

# make all the items in the specified folder.
folder_relpath = "genabr"
folder = h.remake_folder(folder_relpath) 
engine.create_abbreviation(folder, "abr2", "abr2", "cnt2")
#h.create_stored_items_in(folder)