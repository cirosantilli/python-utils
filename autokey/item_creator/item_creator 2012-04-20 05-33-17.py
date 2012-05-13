'''
some important constants from the internals of AutoKey:

# trigger modes
TriggerMode.NONE
TriggerMode.ABBREVIATION
TriggerMode.PREDICTIVE
TriggerMode.HOTKEY

# send modes:
SendMode.KEYBOARD 
SendMode.CB_CTRL_V
SendMode.CB_CTRL_SHIFT_V 
SendMode.CB_SHIFT_INSERT

IOMediator.Key
    LEFT = "<left>"
    RIGHT = "<right>"
    UP = "<up>"
    DOWN = "<down>"
    BACKSPACE = "<backspace>"
    TAB = "<tab>"
    ENTER = "<enter>"
    SCROLL_LOCK = "<scroll_lock>"
    PRINT_SCREEN = "<print_screen>"
    PAUSE = "<pause>"
    MENU = "<menu>"
    
    # Modifier keys
    CONTROL = "<ctrl>"
    ALT = "<alt>"
    ALT_GR = "<alt_gr>"
    SHIFT = "<shift>"
    SUPER = "<super>"
    HYPER = "<hyper>"
    CAPSLOCK = "<capslock>"
    NUMLOCK = "<numlock>"
    
    F1 = "<f1>"
    F2 = "<f2>"
    F3 = "<f3>"
    F4 = "<f4>"
    F5 = "<f5>"
    F6 = "<f6>"
    F7 = "<f7>"
    F8 = "<f8>"
    F9 = "<f9>"
    F10 = "<f10>"
    F11 = "<f11>"
    F12 = "<f12>"
    
    # Other
    ESCAPE = "<escape>"
    INSERT = "<insert>"
    DELETE = "<delete>"
    HOME = "<home>"
    END = "<end>"
    PAGE_UP = "<page_up>"
    PAGE_DOWN = "<page_down>"

    # Numpad
    NP_INSERT = "<np_insert>"
    NP_DELETE = "<np_delete>"
    NP_HOME = "<np_home>"
    NP_END = "<np_end>"
    NP_PAGE_UP = "<np_page_up>"
    NP_PAGE_DOWN = "<np_page_down>"
    NP_LEFT = "<np_left>"
    NP_RIGHT = "<np_right>"
    NP_UP = "<np_up>"
    NP_DOWN = "<np_down>"
    NP_DIVIDE = "<np_divide>"
    NP_MULTIPLY = "<np_multiply>"
    NP_ADD = "<np_add>"
    NP_SUBTRACT = "<np_subtract>"
    NP_5 = "<np_5>"

class Phrase init
        self.description = description
        self.phrase = phrase
        self.modes = []
        self.prompt = False
        self.omitTrigger = False
        self.matchCase = False
        self.parent = None
        self.showInTrayMenu = False
        self.sendMode = SendMode.KEYBOARD
        self.path = path
        
class Script
        self.description = description
        self.code = "default script template" #Ciro
        self.store = Store()
        self.modes = []
        self.prompt = False
        self.omitTrigger = True #Ciro
        self.parent = None
        self.showInTrayMenu = False
        self.path = path
'''

PATH_TO_YOUR_AUTOKEY_LIB = "/usr/share/pyshared/autokey"
import sys
sys.path.append(PATH_TO_YOUR_AUTOKEY_LIB)

import iomediator
import model

class Item:
    '''Data representation of an item (an item means either a phrase or a script, 
    so this contains fields common to Phrases and Scripts).'''

    def __init__(self, abstract_hotkey, abbreviations, is_phrase, content , description):
        self.hotkey_string = hotkey_string
        self.abbreviations = abbreviations
        self.is_phrase = is_phrase
        self.content = content
        self.description = description
        
    def str(self):
        """String representation of object"""
        output = ''
        output = output + "hotkey: " + self.hotkey_string + "\n"
        output = output + "abbreviations: " + str(self.abbreviations) + "\n"
        output = output + "is phrase: " + str(self.is_phrase) + "\n"
        output = output + "content" + self.content + "\n"
        output = output + "description" + self.description + "\n"
        return output

class ItemCreator:
    '''This class is meant to be used directly by the user scripts to create several items (an item either a phrase or a scripts) at once, so as to factor out their script creation as much as possible.
    
    Example 1)
    
        h = ItemAdder()

        h.store([
        ["asa", "asdf", 1, 'asdfasdfasdf'],
        
        ["sc", ["sdfg","gfds"], 0, """
        keyboard.send_keys("sdfgsdfgsdfg")
        """],
        
        ])
        
        h.create_stored_and_clean("Generated Abbreviations")
 
    Example 2) Using custom abbreviation terminators
    
        Suppose that you want to end  all of your 
            - coding expansion abbreviations (c, html, python even) with the character with ';' (strategically placed under the small finger in US keyboard)
            - command abbreviations (open firefox, open a folder, etc) with the character '\\'
        You want that for example , and separate them from , so that you can use the same abbreviations for commands and for  commands and expansions (ff\ opens firefox, ff; expands to /usr/bin/Firefox)        
        
        You could hardcode ';' in each of your abbreviations, but if you ever decide to change that character, it would be messy.
        With ItemCreator, you could just

    creates two items:

        1) A Phrase (because of the 1) which expands to 'asdfasdfasdf', and has a hotkey "Alt + Shift + a" (see split_modifiers_key) and an abbreviation "asdf"
	2) A Script (because of the 0) with code """keyboard.send_keys("sdfgsdfgsdfg")""", and has a hotkey "Shift + c" (see split_modifiers_key) and two abbreviations "sdfg" and "gfds".

    Example 3) Creating several switch sensitive abbreviations

    Rationale
    
        There are two advantages of using this class instead of the GUI:
        
        1) lots of items can be kept in the same text file. This is advantageous because it:
        
            - avoids lots of mouse clicks to create new items and toogle between them
            - allows to see all the items together
            - makes it practical to use your favorite text editor to create your scripts
            - allows you to easily factor out items (as shown in the above real live examples)              
                
     Comparisons to Autohotkeys as of today.
    
        A similar style of item creation is present in the Autohotkeys program (Windows mainly, with an alpha version called IronAHK for linux). While Autohotkeys ha
        Autohotkeys has the advantage of using a script language, which make notation lighter.
        However, this is also a disadvantage of Autohotkeys, since it also makes factoring code out harder (you could in principle create a python script that generates you Autohotkeys code, but this is much nicer when done natively in Python)  
    '''

    HOTKEY_MODIFIER_CHAR_TO_KEY = {'^':iomediator.Key.CONTROL, '!':iomediator.Key.ALT, '+':iomediator.Key.SHIFT, '#':iomediator.Key.SUPER}
    
    CHAR_TO_ID = { 'h':'HOTKEY', 'a':'ABBREVIATIONS', 'p':'IS_PHRASE', 'c':'CONTENT', 'd':'DESCRIPTION'}
    ID_TO_DEFAULT = { 'HOTKEY':'', 'ABBREVIATIONS':'', 'IS_PHRASE':'', 'CONTENT':'', 'DESCRIPTION':'' }
    
    def __init__(self, engine):
        
        self.engine = engine
        self.items = [] # phrases or scripts
        
        self.cur_folder = Null
        self.cur_is_phrase = True
        
    def store(self, field_chars, items_fields):
        """Stores all the items (scripts or phrases), given in terms of the non default fields present, and a list of field values (see C{ItemCreator} for an an explanation of those terms) in order to create  them all at once with create_stored_and_clear."""
        
        self.check_field_chars(field_chars)      
        for item_fields in items_fields:
            self.items.append(self.get_item(field_chars, item_fields))
    
    
    def to_autokey_item(self,item):
        '''Converts an Item see c{Item} to a standard Autokey Model.Phrase or Model.Script.'''
        
        if item.is_phrase == 1:
            p = model.Phrase(item.description, item.content)    
        else:
            p = model.Script(item.description, item.content)
    
        if item.hotkey_string != "":
            p.modes.append(model.TriggerMode.HOTKEY)
            [modifiers,key] = self.split_modifiers_key(item.hotkey_string)
            p.set_hotkey(modifiers, key)
        
        if isinstance(item.abbreviations, str):  # reduce the single string case to the standard list case
            if item.abbreviations == "":
                autokey_abbreviations = None
            else:
                autokey_abbreviations = [item.abbreviations]
        else:
            autokey_abbreviations = item.abbreviations
                
        if item.abbreviations: # add abbreviations
            p.modes.append(model.TriggerMode.ABBREVIATION)
            p.abbreviations = autokey_abbreviations
         
        return p
    
    def check_field_chars(self, field_chars):
        '''Checks if all the field chars exist, and if they appear at most once in field_chars.'''
    
        chars_present = []
        
        for c in field_chars:
            if not c in self.CHAR_TO_ID.keys():
                raise Exception('Character \'' + c + '\' is not a valid field character.' )
            if c in chars_present:
                raise Exception('Character \''+ c + '\' has been repeated more than once at field chars: ' + field_chars )
            chars_present.append(c)

    def get_item(self, field_chars, field_vals):
        '''Given the user given string field_chars their values in a list field_vals,
        returns the Item object that is represented by the input, taking into consideration
        the internal state of ItemCreator.'''
        
        ids_present = []
        id_to_val = {}
        
        n_field_chars = len(field_chars)
        n_field_vals = len(field_vals)
        if (n_field_chars != n_field_vals):
            raise Exception('The number of field chars in "' + field_chars + '" (' + str(n_field_chars) + ' chars) is not the same as the number of given fields (' + str(n_field_vals)  +' fields) ')
        
        i = 0
        for c in field_chars:
            id = self.CHAR_TO_ID[c]
            id_to_val[id] = field_vals[i]
            ids_present.append(id)
            i = i+1
        
        for id in self.ID_TO_DEFAULT.keys():
           if not id in ids_present:
               id_to_val[id] = self.ID_TO_DEFAULT[id]
        
        hotkey = model.AbstractHotkey()
        
        return Item(id_to_val['HOTKEY'], id_to_val['ABBREVIATIONS'], id_to_val['IS_PHRASE'], id_to_val['CONTENT'], id_to_val['DESCRIPTION']) 
    
    def split_modifiers_key(self, modifiers_key_string):
        '''Returns modifiers (IOMediator.Key) and the key corresponding to the modifiers_key_string. The syntax is as follows
        
            modifiers_key_string = modChar1 [modChar2 [  ] ] keyChar
        
        with modChars1 given by self.hotkey_modifier_chars.
        
        So for example:
        
            "sl" == Shift + l
            "auc" == Alt + Super + c
        '''
        
        key =  modifiers_key_string[-1]
        modifier_chars = modifiers_key_string[0:-1]
        modifiers = []
        for c in modifier_chars:
            if c in self.HOTKEY_MODIFIER_CHAR_TO_KEY.keys():
                modifiers.append(self.HOTKEY_MODIFIER_CHAR_TO_KEY[c])
            else:
                raise Exception("The hotkey modifier char " + c + " is not defined.")
        return [modifiers,key]
    
    def create_stored_items_in(self, folder):
        '''Creates all the shortcuts that have been previously stored with HotkeysManager.store() in the model.Folder folder, and clears the items to prepare for another call with a different folder.'''
        
        self.engine.monitor.suspend()
        for item in self.items:
            for abr in item.abbreviations:
                if not self.engine.configManager.check_abbreviation_unique(abr, None, None):
                    raise Exception("The specified abbreviation is already in use")
            autokey_item = self.to_autokey_item(item)
            folder.add_item(autokey_item)
            autokey_item.persist()
        self.engine.monitor.unsuspend()
        self.engine.configManager.config_altered(False)
        
    def create_stored_items_in_relpath(self, folder_relpath):
        '''Creates all the shortcuts that have been previously stored with HotkeysManager.store() in the folder folder_name, and clears the items to prepare for another call with a different folder.'''
        self.create_stored_items_in( self.engine.get_folder(folder_relpath) )

    def clear_store(self):
        """Removes all the items that have been stored for instance with the store method."""
        self.items = []
        
    def remake_folder(self, folder_relpath):
        '''If the folder with folder_relpath exists, remove it and all of its contents. Endif. Create folder with relative path folder_relpath.'''
        
        self.engine.monitor.suspend()
        
        folder = self.engine.get_folder(folder_relpath)
        if folder != None:
            folder.remove_data()
        else:
            folder = model.Folder(folder_relpath)
            folder.persist()
        
        self.engine.monitor.unsuspend()
        
        return folder
    
    def str(self):
        """String representation of the object."""
        output = ''
        for item in self.items:
            output = output + item.str() + "\n"
        return output

#Testing main
if __name__ == '__main__':
    
    i = ItemCreator(None)
    i.store('hapct',[
        ['!+a','abr1',1,'cnt1','tit1'],
        ['!+b',['abr2.1','abr2.2'],1,'cnt2','tit2'],
    ])
    #print i.str()
    
    print i.items[0].str()
    i.to_autokey_item(i.items[0])
    
    print i.items[1].str()
    i.to_autokey_item(i.items[1])
