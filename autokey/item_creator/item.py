class Item:
    '''Data representation of an item (an item means either a phrase or a script, 
    so this contains fields common to Phrases and Scripts).'''

    def __init__(self):
        self.abstract_hotkey = Null  # Null if no hotkeys
        self.abstract_abbreviation = Null  # Null if no abbreviations
        self.is_phrase = True  # boolean
        self.content = ''  # string, '' if no content    
        self.parent = Null    # model.Folder, Null if none specified
        self.description = ''  # string, '' if no description 
        
    def __str__(self):
        """String representation of object for debug."""
        output = ''
        output = output + "hotkey: " + self.abstract_hotkey.__str__() + "\n"
        output = output + "abbreviations: " + self.abbreviations.__str__() + "\n"
        output = output + "is phrase: " + str(self.is_phrase) + "\n"
        output = output + "content: " + self.content + "\n"
        output = output + "folder: " + self.folder.__str__() + "\n"
        output = output + "description: " + self.description + "\n"
        return output