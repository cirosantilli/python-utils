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