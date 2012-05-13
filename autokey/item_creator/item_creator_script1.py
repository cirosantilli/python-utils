# CREATE THE FOLDER gen_itm with the GUI!!! Script Cannot do that yet!!! TODO
from item_creator import ItemCreator
i = ItemCreator(engine)

folder_title = 'gen_itm'
f = engine.get_folder(folder_title)
i.set_folder(f)

i.store('hpc',[
    ['!+a',0,"""keyboard.send_keys('cnt7')"""],
])

i.create_stored_items()

# RESTART AUTOKEYS COMPLETELY! Just closing the window will not work. You need to to right click, quit. TODO avoid this.