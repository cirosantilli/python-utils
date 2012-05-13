PATH_TO_YOUR_AUTOKEY_LIB = "/usr/share/pyshared/autokey"

import sys
sys.path.append(PATH_TO_YOUR_AUTOKEY_LIB)
import model

def create_test_item(engine, folder):
    p = model.Phrase("asdf", 'asdf')
    p.modes.append(model.TriggerMode.ABBREVIATION)
    p.abbreviation = 'abr'
    folder.add_item(p)
    engine.configManager.config_altered()