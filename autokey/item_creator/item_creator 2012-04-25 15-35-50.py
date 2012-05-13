PATH_TO_YOUR_AUTOKEY_LIB = "/usr/share/pyshared/autokey"

import sys
sys.path.append(PATH_TO_YOUR_AUTOKEY_LIB)

import iomediator
import model

class ItemCreator:
    '''
    
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
    USAGE
    
        1) Create a new script called "item_creator_script" anywhere using the GUI.
        
        2) copy/paste the content of TEST SCRIPT further down which contains many use examples.
        
        3) Give "generate abbreviations" a hotkey/abbreviation.
        
        4) Create a folder named "gen_itm" using the GUI at top level.
        
        5) Run the "generate abbreviations" using the hotkey.
        
        6) Completely shut down Autokeys and reestart it (right click on taskbar icon > quit, not just closing the window).
        
        7) Your generated scripts should all be in the "generated abreviations" folder and working.
    
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
    
    Those will be used on subsequent calls to store(), unless parameters given in the store method are override them.
    
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
    
    #=======================================================================================================================
    # TEST SCRIPT
    # Use this user script to test the class.
    #=======================================================================================================================
    
    # CREATE THE FOLDER gen_itm with the GUI!!! Script Cannot do that yet!!! TODO
    folder_title = 'gen_itm'
    f = engine.get_folder(folder_title)
    
    from item_creator import ItemCreator
    i = ItemCreator(engine)
    
    #EXAMPLES 1-4
    i.store('hapcfd',[
        ['!+a','abr1',1,'cnt1',f,'tit1'],
        ['!+b',['abr2.1','abr2.2'],1,'cnt2',f,'tit2'],
        ['^#c', 'abr3',0,"""keyboard.send_keys('cnt3')""",f,'tit3'],
        ['^#d',['abr4.1','abr4.4'],0,"""keyboard.send_keys('cnt4')""",f,'tit4'],
    ])
    
    # set cur_default for next 
    
    i.set_folder(f) # from now on save to the given folder by default
    
    #EXAMPLES 5-6
    
    i.set_is_phrase(1) # from now on make phrases, not scripts, by default
    
    i.store('ac',[
        ['abr5','cnt5'],
        ['abr6','cnt6'],
    ])
    
    #EXAMPLES 7-8
    
    i.set_is_phrase(0)
    i.set_hotkey_modifiers('!+') # from now on, if no hotkey modifier char is specified for a hotkey, use Shift + Alt (!+)
    
    i.store('hc',[
        ['e',"""keyboard.send_keys('cnt7')"""],
        ['f',"""keyboard.send_keys('cnt8')"""],
    ])
    
    # creat all the items that were previously stored.
    i.create_stored_items()
    
    # RESTART AUTOKEYS COMPLETELY! Just closing the window will not work. You need to to right click, quit. TODO avoid this.
    '''

    # userland hotkey modifier chars to inner representation keys.
    HOTKEY_MODIFIER_CHAR_TO_KEY = {'^':iomediator.Key.CONTROL,
                                   '!':iomediator.Key.ALT,
                                   '+':iomediator.Key.SHIFT,
                                   '#':iomediator.Key.SUPER,
                                   }
    
    # userland fields.
    # These are fields that the user passes to this class such as a 
    # modifier + Hotkey key string, not necessarily in bijection to the inner representation
    # of an item.
    USER_FIELD_CHAR_TO_ID = {'h':'HOTKEY',
                  'a':'ABBREVIATIONS',
                  'p':'IS_PHRASE',
                  'c':'CONTENT',
                  'd':'DESCRIPTION',
                  'f':'FOLDER',
                  }
    
    # All fields that can be set to current values by the user.
    # These fields hold the same types value as the inner representation. 
    # Note that there are some fields for which current values 
    # make no sense such as an abbreviation, which must be unique.
    INITIAL_CUR_DEFAULT = {'HOTKEY_MODIFIERS':None,
                     'IS_PHRASE':True,
                     'FOLDER':None,
                     }
    
    # correspondence between userland and inner representation of IS_PHRASE
    IS_PHRASE_USER_TO_INNER = {0:False, 1:True}

    
    def __init__(self, engine):
        
        self.engine = engine
        self.items = [] # holds either model.Phrase or model.Script objects
        self.cur_default = self.INITIAL_CUR_DEFAULT.copy()  # holds user modifiable values that are used as defaults unless overwridden directly by store. 
    
    def set_folder(self, folder):
        self.cur_default['FOLDER'] = folder
        
    def set_hotkey_modifiers(self, modifier_chars):
        self.cur_default['HOTKEY_MODIFIERS'] = self._modifier_chars_to_keys(modifier_chars)
        
    def set_is_phrase(self, is_phrase):
        self.cur_default['IS_PHRASE'] = self.IS_PHRASE_USER_TO_INNER[is_phrase]
    
    def store(self, field_chars, items_fields):
        """Stores all the items (scripts or phrases), given in terms of the non default fields present, and a list of field values (see C{ItemCreator} for an an explanation of those terms) in order to create  them all at once with create_stored_and_clear."""
        
        self._check_field_chars(field_chars)      
        for item_fields in items_fields:
            self.items.append(self._make_item(field_chars, item_fields))

    def remake_folder(self, title):
        '''If the folder with title exists, remove it and all of its contents. Endif. Create folder with relative path title.'''
        
        self.engine.monitor.suspend()
        
        folder = self.engine.get_folder(title)
        if folder:
            folder.remove_folder()
        
        folder = model.Folder(title)
        folder.persist()

        self.engine.monitor.unsuspend()
        
        return folder

    def create_stored_items(self):
        '''Creates all the shortcuts that have been previously stored with HotkeysManager.store() in the model.Folder folder, and clears the items to prepare for another call with a different folder.'''
        
        self.engine.monitor.suspend()
        for item in self.items:
            for abr in item.abbreviations:
                if not self.engine.configManager.check_abbreviation_unique(abr, None, None):
                    raise Exception("The specified abbreviation is already in use")
            item.persist()
        self.engine.monitor.unsuspend()
        self.engine.configManager.config_altered(False)

    def _check_field_chars(self, field_chars):
        '''Checks if all the field chars exist, and if they appear at most once in field_chars.'''
    
        chars_present = []
        
        for c in field_chars:
            if not c in self.USER_FIELD_CHAR_TO_ID.keys():
                raise Exception('Character \'' + c + '\' is not a valid field character.' )
            if c in chars_present:
                raise Exception('Character \''+ c + '\' has been repeated more than once at field chars: ' + field_chars )
            chars_present.append(c)

    def _make_item(self, user_field_chars, user_field_vals):
        '''Interprets user land inputs using current state to create an item.'''
        
        # check the number of fields and values given
        n_field_chars = len(user_field_chars)
        n_field_vals = len(user_field_vals)
        if (n_field_chars != n_field_vals):
            raise Exception('The number of field chars in "' + user_field_chars + '" (' + str(n_field_chars) + ' chars) is not the same as the number of given fields (' + str(n_field_vals)  +' fields) ')
        
        # guard the user input in user_field_to_val
        i = 0
        user_field_to_val = {}
        for c in user_field_chars:
            user_field_id = self.USER_FIELD_CHAR_TO_ID[c]
            user_field_to_val[user_field_id] = user_field_vals[i]
            i = i+1
        user_fields_present = user_field_to_val.keys()
               
        #---------------------------------------------
        # calculate inner representation values using the user input and the current default values
        
        # hotkey
        # If the user gives a hotkey char, but there are no modifiers set, throws an exception.
        if 'HOTKEY' in user_fields_present:
            [hotkey_modifiers,hotkey_key] = self._parse_modifiers_key_str(user_field_to_val['HOTKEY'])
            if hotkey_key:   
                if not hotkey_modifiers:
                    default_hotkey_modifiers = self.cur_default['HOTKEY_MODIFIERS']
                    if default_hotkey_modifiers:    # no current value set
                        hotkey_modifiers = default_hotkey_modifiers
                    else:
                        raise Exception('No hotkey modifiers are set, but the hotkey key \''+ hotkey_key +'\' was given')
        else:   # no hotkey given by user.
            hotkey_key = None
        
        if hotkey_key and hotkey_modifiers:
            has_hotkey = True
        else:
            has_hotkey = False
        
        # abbreviations
        if 'ABBREVIATIONS' in user_fields_present:
            abbreviations = user_field_to_val['ABBREVIATIONS']
            if isinstance(abbreviations, str):  # reduce the single string case to the standard list case
                if abbreviations == '':
                    abbreviations = []
                else:
                    abbreviations = [abbreviations]
        else:   # user did not give an abbreviation field
            abbreviations = []

        if abbreviations:
            has_abbreviations = True
        else:
            has_abbreviations = False

        # is_phrase
        if 'IS_PHRASE' in user_fields_present:
            is_phrase = user_field_to_val['IS_PHRASE']
            if is_phrase == 0:
                is_phrase = False
            elif is_phrase == 1:
                is_phrase = True
            else:
                raise Exception('Only \'0\' or \'1\' are accepted in is_phrase field, \''+ str(is_phrase) +'\' found.')
        else:
            is_phrase = self.cur_default['IS_PHRASE']

        # content
        if 'CONTENT' in user_fields_present:
            content = user_field_to_val['CONTENT']
        else:
            content = ''
        
        # description
        if 'DESCRIPTION' in user_fields_present:
            description = user_field_to_val['DESCRIPTION']
        else:
            description = ''
            
        # folder
        if 'FOLDER' in user_fields_present:
            folder = user_field_to_val['FOLDER']
        else:
            folder = self.cur_default['FOLDER']

        #---------------------------------------------
        # build the output using the calculated values.
        if is_phrase:
            output = model.Phrase(description, content)
        else:
            output = model.Script(description, content)
        
        if has_hotkey:
            output.modes.append(model.TriggerMode.HOTKEY)
            output.set_hotkey(hotkey_modifiers, hotkey_key)

        if has_abbreviations: # add abbreviations
            output.modes.append(model.TriggerMode.ABBREVIATION)
            output.abbreviations = abbreviations
        
        output.parent = folder
        
        return output

    def _parse_modifiers_key_str(self, modifiers_key_string):
        '''Returns a [modifiers,  key] pair (both in (IOMediator.Key))  and the corresponding to the modifiers_key_string.
        
            modifiers_key_string = modChar1 [modChar2 [  ] ] keyChar
        
        with modChars1 given by self.hotkey_modifier_chars.
        
        So for example:
        
            "+l" == Shift + l
            "!#c" == Alt + Super + c
            "!+<f1>" == Alt + Super + <f1>
            
        Special chars such as <f1> or <enter> or <<> and <>> are the those defined in IOMediator.
            
        If the string contains only one token (such as 'e' or '<enter>'), it is taken as the key, and modifiers is left empty.
        '''
        
        if modifiers_key_string[-1] == '>':
            raise Exception('Special characters such as <f1> or <enter> are not yet implemented.') #TODO: implement
        else:
            key = modifiers_key_string[-1]
        modifier_chars = modifiers_key_string[0:-1]
        modifiers = self._modifier_chars_to_keys(modifier_chars)
        
        return [modifiers,key]
    
    def _modifier_chars_to_keys(self, modifier_chars):
        modifiers = []
        for c in modifier_chars:
            if c in self.HOTKEY_MODIFIER_CHAR_TO_KEY.keys():
                modifiers.append(self.HOTKEY_MODIFIER_CHAR_TO_KEY[c])
            else:
                raise Exception("The hotkey modifier char " + c + " is not defined.")
        return modifiers
    
    def __str__(self):
        """String representation of the object."""
        output = ''
        for item in self.items:
            output = output + item.__str__() + "\n"
        return output

#Testing main
if __name__ == '__main__':
    
   
    i = ItemCreator(None)
    f = None
    
    #EXAMPLES 1-4
    i.store('hapcfd',[
        ['!+a','abr1',1,'cnt1',f,'tit1'],
        ['!+b',['abr2.1','abr2.2'],1,'cnt2',f,'tit2'],
        ['^#c', 'abr3',0,"""keyboard.send_keys('cnt3')""",f,'tit3'],
        ['^#d',['abr4.1','abr4.4'],0,"""keyboard.send_keys('cnt4')""",f,'tit4'],
    ])
    
    # set cur_default for next store calls.
    i.set_is_phrase(1) # from now on make phrases, not scripts, by default
    i.set_folder(f) # from now on save to the given folder by default
    i.set_hotkey_modifiers('!+') # from now on, if no hotkey modifier char is specified for a hotkey, use Shift + Alt
    
    #EXAMPLES 5-6
    i.store('ac',[
        ['abr5','cnt5'],
        ['abr6','cnt6'],
    ])
    
    #EXAMPLE 7
    i.store('hpcd',[
        ['e',0,"""keyboard.send_keys('cnt7')""",'tit7'],
        ['f',0,"""keyboard.send_keys('cnt8')""",'tit8'],
    ])
    
    print i.items[0].__str__()
    print i.items[1].__str__()
    
    print i.items[0].parent.path
    
    print i.__str__()
