"""
TODO:
        
    - cannot parse a script a "\n", even if it is inside quotes (this sees it as a line break)
    
    - understand better the Abstract Abbreviation model and allow to manipulate its properties (only some of them are not yet implemented )

    - implement special chars <f1>, <space>, etc.
"""

PATH_TO_YOUR_AUTOKEY_LIB = "/usr/share/pyshared/autokey"

import sys
sys.path.append(PATH_TO_YOUR_AUTOKEY_LIB)

import iomediator
import model

import re

all_whitespace_or_empty_re = re.compile(r'^\s*$')

def is_all_whitespace_or_empty(s):
    """
    True iff the string is composed entirely of whitespace.
    """
    if all_whitespace_or_empty_re.match(s):
        return True
    else:
        return False

class ItemCreator:
    """
    
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
    
        1) Create a new script called "generate abbreviations" anywhere using the GUI.
        
        2) copy/paste the contents of the accompagning file item_creator_tutorial.py there 
        
        3) Give "generate abbreviation" a hotkey/abbreviation.
        
        4) Create a folder named "gen" using the GUI at top level.
        
        5) Run the "generate abbreviation" using the hotkey you assigned it.
        
        6) Completely shut down Autokeys (Control Q) and reestart it (right click on taskbar icon > quit, not just closing the window).
        
        7) Your generated scripts should all be in the "generated abbreviations" folder and working.
    
    """

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
                  'a':'ABBREVIATION',
                  'p':'IS_PHRASE',
                  'c':'CONTENT',
                  'd':'DESCRIPTION',
                  'f':'FOLDER',
                  }
    
    USER_FIELD_ID_TO_CHAR = dict((v,k) for k, v in USER_FIELD_CHAR_TO_ID.iteritems())

    # All fields that can be set to current values by the user.
    # These fields hold the same types value as the inner representation. 
    # Note that there are some fields for which current values 
    # make no sense such as an abbreviation, which must be unique.
    #
    # I chose to make this a map because it groups things better, and
    # allows for operations such as copy. Might consider into turning it
    # into variables later
    INITIAL_CUR_DEFAULT = {'FOLDER':None,
                     'IS_PHRASE':True,
                     'HOTKEY_MODIFIERS':None,
                     'REMOVE_TYPED_ABBREVIATION':True,
                     'OMMIT_TRIGGER_CHAR':False,
                     'MATCH_CASE':False,
                     'IGNORE_CASE':False,
                     'TRIGGER_WHEN_PART_OF_WORD':False,
                     'TRIGGER_IMMEDIATELY':False,
                     'ABBREVIATION_PREFIX':'',
                     'ABBREVIATION_SUFIX':'',
                     }
    
    
    
    # correspondence between userland and inner representation of IS_PHRASE
    IS_PHRASE_USER_TO_INNER = {0:False, 1:True}
    
    # parsing parameters
    USER_IS_HOTKEY_CHAR_TO_IS_HOTKEY = {'h':True, 'a':False}
    USER_IS_PHRASE_CHAR_TO_IS_PHRASE = {'p':True, 's':False}
    INITIAL_DEFAULT_PARSE_STORE_IS_HOTKEY = False
    INITIAL_DEFAULT_PARSE_STORE_IS_PHRASE = True
    SCRIPT_END_LINE = 'return'
    IS_COMMENT_LINE_RE = re.compile(r'^\s*;')
    TRAILING_WHITESPACE_RE = re.compile(r'^\s')
    
    def __init__(self, engine):
        self.engine = engine
        self.items = [] # holds either model.Phrase or model.Script objects
        self.cur_default = self.INITIAL_CUR_DEFAULT.copy()  # holds user modifiable values that are used as defaults unless overwridden directly by store.
        self.noname_item_count = 1  # number of items that have not been given a name by the user. will be named automatically for convenience
        
    def set_folder(self, folder):
        self.cur_default['FOLDER'] = folder
        
    def set_is_phrase(self, is_phrase):
        self.cur_default['IS_PHRASE'] = self.IS_PHRASE_USER_TO_INNER[is_phrase]
    
    def set_hotkey_modifiers(self, modifier_chars):
        self.cur_default['HOTKEY_MODIFIERS'] = self._modifier_chars_to_keys(modifier_chars)
        
    def set_remove_typed_abbreviation(self, is_phrase):
        self.cur_default['REMOVE_TYPED_ABBREVIATION'] = self.IS_PHRASE_USER_TO_INNER[is_phrase]
          
    def set_ommit_trigger_char(self, val):
        self.cur_default['OMMIT_TRIGGER_CHAR'] = val
    
    def set_match_case(self, val):
        self.cur_default['MATCH_CASE'] = val
    
    def set_ignore_case(self, val):
        self.cur_default['IGNORE_CASE'] = val
        
    def set_trigger_when_part_of_word(self, val):
        self.cur_default['TRIGGER_WHEN_PART_OF_WORD'] = val
    
    def set_trigger_immediately(self, val):
        self.cur_default['TRIGGER_IMMEDIATELY'] = val
    
    def set_abbreviation_prefix(self, prefix):
        """
        The given prefix will be added before all the following abbreviations
        """
        self.cur_default['ABBREVIATION_PREFIX'] = prefix
        
    def set_abbreviation_sufix(self, sufix):
        """
        The given prefix will be added before all the following abbreviations
        """
        self.cur_default['ABBREVIATION_SUFIX'] = sufix

    def store(self, field_chars, items_fields):
        """
        Stores all the items (scripts or phrases), given in terms of the non default fields present, 
        and a list of field values (see below) in order to create 
        them all at once with create_stored_and_clear.
    
        You decide which parameters you are giving "store", and in what order with a letter. 
    
        The letters are:
    
        Letter       meaning        default behaviour if not specified
              
        h            Hotkey
        a            Abbreviation
        p            Is Phrase           
        c            Contents            
        f            Folder (from engine.get_folder())
        d            Description (will be used to create the title of the hotkey which you see on the GUI)
    
    The following parameter order is recommended:
        
            h a p c f d
        """
        
        self._check_field_chars(field_chars)      
        for item_fields in items_fields:
            new_item = self._make_item(field_chars, item_fields)
            self._add_item(new_item)

    def parse_store(self, s):
        '''
        Parses a string containing several items and store those items.
        
        The following examples should clarify the syntax:
        
        parse_store("""hp
        !a cnt1
        ^b cnt2
        #c cnt3
        """)
        
        Creates 3 phrases (second char char 'p') expanded by hotkeys (first char 'h'),  :
        Alt + a expands to 'cnt1'
        Control + b expands to 'cnt2'
        etc...
        (see _{store} for why !a expands to Alt + a and so on)
        
        parse_store("""as
        abr1
            print "This is script 1"
        return
        abr2
            print "This is script 2"
        return
        
        # this is a comment line, and the above line is blank and thus igonred.
            # and this is another comment line, even if it starts with whitespaces!
        abr3
            print "This is script 3"
        return
        """)
        
        Creates 3 scripts (second char 's') expanded by abbreviations (first char 'a'):
        abr1 executes 'print "This is script 1"'
        abr2 executes 'print "This is script 2"'
        etc.
        
        Glossary:
        
        ignored line: a line that is either blank or a comment (starts with '#')
        trigger sequence: the sequence that the user has to type in order to see his item expanded/executed
        
        '''
        
        lines = s.split('\n') # s split
        
        # decide the type of string that will be parsed
        line0 = lines[0]
        if line0:
            if len(line0) != 2:
                raise Exception("Initial string must be either empty or contain exactly two mode characters.")
            else:
                is_hotkey_char = line0[0]
                is_phrase_char = line0[1]
                if is_hotkey_char in self.USER_IS_HOTKEY_CHAR_TO_IS_HOTKEY:
                    is_hotkey = self.USER_IS_HOTKEY_CHAR_TO_IS_HOTKEY[is_hotkey_char]
                else:
                    raise Exception("Only the values 'h' (hotkey) or 'a' (abbreviation) are accepted for the first char. \'"+is_hotkey_char+"\' found instead.")
                if is_phrase_char in self.USER_IS_PHRASE_CHAR_TO_IS_PHRASE:
                    is_phrase = self.USER_IS_PHRASE_CHAR_TO_IS_PHRASE[is_phrase_char]
                else:
                    raise Exception("Only the values 'p' (phrase) or 's' (script) are accepted for the second char. \'"+is_phrase_char+"\' found instead.")
        else: # empty first string, take defaults
            is_hotkey = self.INITIAL_DEFAULT_PARSE_STORE_IS_HOTKEY
            is_phrase = self.INITIAL_DEFAULT_PARSE_STORE_IS_PHRASE

        if is_hotkey:
            user_expand_seq_type_char = self.USER_FIELD_ID_TO_CHAR['HOTKEY']
        else:
            user_expand_seq_type_char = self.USER_FIELD_ID_TO_CHAR['ABBREVIATION']
        
        # do the actual parsing
        if is_phrase:
            for line in lines[1:]:
                if not self._should_ignore_line(line): # ignore empty and comment lines
                    self._check_phrase_line_indent(line) # check that there are no spaces
                    if ' ' in line:
                        i = line.index(' ')
                        trigger_seq = line[:i] # the sequence the user has to input in order to trigger
                        content = line[i+1:]
                        self.store('p'+user_expand_seq_type_char+'c',[[1,trigger_seq,content]])
                    else:
                        raise Exception("There must be at least one space character for each non-ignored line ' ' separating your trigger sequence from the content:\n\t" + line)
        
        else:   # is a script
            i = self._index_of_first_non_ignored_line(lines,1)
            while i < len(lines):
                
                # the trigger sequence is the whole first non ignored line
                trigger_seq = lines[i]
                i = i+1
                
                content = ''
                # read the current script until the self.SCRIPT_END_LINE sequence is found
                while lines[i] != self.SCRIPT_END_LINE:
                    self._check_script_line_indent(lines[i]) # check that there are exactly 4 spaces
                    content = content + lines[i][4:] + '\n'
                    i = i+1
                    if i==len(lines): # if we reached the end of the file here, there is problem
                        raise Exception("Parsing of script ended before expected 'return' statement was found at line: " + str(i))
                i = i+1
                content = content[:-1] # remove the last extra '\n'
                
                # store the script
                self.store('p'+user_expand_seq_type_char+'c',[[0,trigger_seq,content]])
                
                i = self._index_of_first_non_ignored_line(lines,i)
                
    def remake_folder(self, title):
        """
        If the folder with title exists, remove it and 
        all of its contents. Endif. Create folder with relative path title.
        """
        
        self.engine.monitor.suspend()
        
        folder = self.engine.get_folder(title)
        if folder:
            folder.remove_folder()
        
        folder = model.Folder(title)
        folder.persist()

        self.engine.monitor.unsuspend()
        
        return folder

    def create_stored_items(self):
        """
        Creates all the shortcuts that have been previously stored with 
        HotkeysManager.store() in the model.Folder folder, and clears the items to 
        prepare for another call with a different folder.
        """
        
        for item in self.items:
            if not self.engine.configManager.check_abbreviation_unique(item.abbreviation, None):
                raise Exception("The specified abbreviation \'"+item.abbreviation+"\' is already in use")
            item.parent.add_item(item)
        self.engine.configManager.config_altered()

    def _check_phrase_line_indent(self,line):
        """
        Checks that the given phrase line has no trailing whitespaces, and throws an exception otherwise.
        """
        if self.TRAILING_WHITESPACE_RE.match(line):
            raise Exception("Phrase lines in parse_store must begin directly with the trigger sequence, no whitespace or indentation is allowed. Found instead:\n\t'"+line+"'")

    def _check_script_line_indent(self,line):
        """
        Checks that the given script line starts with exactly 4 whitespaces, and throws an exception otherwise.
        """
        for i in range(3):
            if line[i] != ' ':
                raise Exception("Script lines in parse_store must begin with exactly 4 spaces. Found instead:\n\t'"+line+"'")

    def _should_ignore_line(self, line):
        if is_all_whitespace_or_empty(line) or self._is_comment_line(line):
            return True
        else:
            return False
    
    def _is_comment_line(self,line):
        """
        Decides if the given line is a comment for a parsed abbreviations set.
        
        Comments contain first whitespace only, followed by a '#' and then the actual comment.
        
        Examples:
        
        '# nice hotkey' is a comment
        '   # nice hotkey' is a comment
        'nice hotkey' is not a comment
        '   nice hotkey' is not a comment
        '   nice # hotkey' is not a comment line
        """
        if self.IS_COMMENT_LINE_RE.match(line):
            return True
        else:
            return False
    
    def _index_of_first_non_ignored_line(self,lines,starting_i):
        """
        Returns the index of the first line that should not be ignored starting from (and including) first_i.
        
        If the end is reached before a non ignored line is found, returns len(lines).
        """
        i = starting_i
        while self._should_ignore_line(lines[i]): # skip empty lines and comments
            i = i+1
            if i == len(lines):
                break
        return i
            
    def _add_item(self, new_item):
        self.items.append(new_item)
        
    def _check_field_chars(self, field_chars):
        """
        Checks if all the field chars exist, and if they appear at most once in field_chars.
        """
    
        chars_present = []
        
        for c in field_chars:
            if not c in self.USER_FIELD_CHAR_TO_ID.keys():
                raise Exception('Character \'' + c + '\' is not a valid field character.' )
            if c in chars_present:
                raise Exception('Character \''+ c + '\' has been repeated more than once at field chars: ' + field_chars )
            chars_present.append(c)

    def _make_item(self, user_field_chars, user_field_vals):
        """
        Interprets user land inputs using current state to create an item.
        """
        
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
        if 'ABBREVIATION' in user_fields_present:
            abbreviation = user_field_to_val['ABBREVIATION']
        else:
            abbreviation = ''

        if abbreviation:
            has_abbreviation = True
            abbreviation = self.cur_default['ABBREVIATION_PREFIX'] + abbreviation + self.cur_default['ABBREVIATION_SUFIX']
        else:
            has_abbreviation = False

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
            description = str(self.noname_item_count)
            self.noname_item_count = self.noname_item_count+1
        
        # folder
        if 'FOLDER' in user_fields_present:
            folder = user_field_to_val['FOLDER']
        else:
            folder = self.cur_default['FOLDER']
        
        # fields that can only be set by playing with the defaults
        remove_typed_abbreviation = self.cur_default['REMOVE_TYPED_ABBREVIATION']
        ommit_trigger_char = self.cur_default['OMMIT_TRIGGER_CHAR']
        match_case = self.cur_default['MATCH_CASE']

        #---------------------------------------------
        # build the output using the calculated values.
        if is_phrase:
            output = model.Phrase(description, content)
        else:
            output = model.Script(description, content)
        
        if has_hotkey:
            output.modes.append(model.TriggerMode.HOTKEY)
            output.set_hotkey(hotkey_modifiers, hotkey_key)

        if has_abbreviation: # add abbreviations
            output.modes.append(model.TriggerMode.ABBREVIATION)
            output.abbreviation = abbreviation
        
        output.parent = folder
        
        output.ignoreCase = self.cur_default['IGNORE_CASE']
        output.immediate = self.cur_default['TRIGGER_IMMEDIATELY']
        output.triggerInside = self.cur_default['TRIGGER_WHEN_PART_OF_WORD']
        
        return output

    def _parse_modifiers_key_str(self, modifiers_key_string):
        """Returns a [modifiers,  key] pair (both in (IOMediator.Key))  and the corresponding to the modifiers_key_string.
        
            modifiers_key_string = modChar1 [modChar2 [  ] ] keyChar
        
        with modChars1 given by self.hotkey_modifier_chars.
        
        So for example:
        
            "+l" == Shift + l
            "!#c" == Alt + Super + c
            "!+<f1>" == Alt + Super + <f1>
            
        Special chars such as <f1> or <enter> or <<> and <>> are the those defined in IOMediator.
            
        If the string contains only one token (such as 'e' or '<enter>'), it is taken as the key, and modifiers is left empty.
        """
        
        if modifiers_key_string[-1] == '>':
            raise Exception('Special characters such as <f1> or <enter> are not yet implemented.')
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
    
    print "TESTING 'item_creator'"
    
    i = ItemCreator(None)
    f = None
    
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

; this is a comment line, and the above line is blank and thus ignored.
    ; and this is another comment line, even if it starts with whitespaces!
#c cnt3
""")
    
    # this makes scripts (because of the 's') which are expanded by abbreviation (because of the 'a')
    i.parse_store("""as
abr1
    keyboard.send_keys("cnt1")
return
abr2
    keyboard.send_keys("cnt2")
return

; this is a comment line, and the above line is blank and thus igonred.
    ; and this is another comment line, even if it starts with whitespaces!
abr3
    keyboard.send_keys("cnt3")
return
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
    keyboard.send_keys(" cnt3")
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
    i.set_abbreviation_prefix(';')

    i.parse_store("""ap
abr5 cnt5
abr6 cnt6
abr7 cnt7
""")

    print i.items[0].__str__()
    print i.items[1].__str__()
    
    print i.__str__()
    
    print "END TESTING 'item_creator'"
