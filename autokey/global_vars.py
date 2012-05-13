import json
from autokey import common

'''
SAMPLE USE CASE:

You want to write equations for both websites and in latex. 

When in websites, you want to use formulas delimiers such as <eq>x^2</eq> 

When in latex, you want \[ x^2\].

Also you will be using the same editor for both (Eclipse for example), so using window class is not an option.

In order to do this, we want a global switch which says if we are in websites mode or not. You could want to type for example

'eq;'

and qet

<eq></eq>

then toogle the switch with something like

'tws/'

for Toogle Web Switch, and the next time you type

'eq;'

you will get 

\[\]

magic! Of course, doing 'tws/' will go back to you web mode.

HOW IT WORKS:

The only problem is that you need to access and modify the switch variable across scripts, which is not currently natively supported as of 0.82.2. 

This is exactly what this class does by saving a json to $/.config/autokey/dateya/global_vars.json , just next to the other data files used by autok.

There is just a catch, initialization. Before you use the switch the first time, you must first use a command to initialize the data, which simply creates/overwrites the json on your disk. 

After the first time you initialize you don't need to do it anymore unless you want to go  back to the initial state. If don't reinitialize, you just return to your last session settings, which might be desirable.

INSTALLATION:

- put this file (global_vars.py) in your modules folder (Edit > Preferences > Script Engine)

USAGE EXAMPLES (3 inner scripts, added in the GUI and set shortcuts to them):

- initialize global variables as in init_global_vars.py script
- send context sensitive expansions as in send_key_switch_sensitive.py script
- toogle the switch as in the toogle_switch script.py

#-------------------------------------------------------------------------------
# init_global.py (inner script)

from global_vars import GlobalVars

gvars =  { 'web_switch':True,  'web_switch_true':'<eq></eq>', 'web_switch_false':r'\[\]',} 

GlobalVars.set_globals(gvars)


#-------------------------------------------------------------------------------
# send_key_switch_sensitive.py (inner script)

from global_vars import GlobalVars

gvars = GlobalVars.get_globals()

if( gvars['web_switch']  ):
    keyboard.send_keys( gvars['web_switch_true'] )
else:
    keyboard.send_keys( gvars['web_switch_false'] )

#-------------------------------------------------------------------------------
# toogle_switch.py (inner script)

from global_vars import GlobalVars

if(  GlobalVars.get_global('web_switch')  ):
    GlobalVars.set_global('web_switch', False)
else:
    GlobalVars.set_global('web_switch',True)
    
'''

class GlobalVars:

	json_path = common.CONFIG_DIR + '/data/global_vars.json'

	@staticmethod
	def set_global(name,value):
		
		data = GlobalVars.get_globals()
		data[name] = value
		GlobalVars.set_globals(data)
	
	@staticmethod		
	def set_globals(gvars):
	   
		json_string = json.dumps(gvars)

		f  = open(GlobalVars.json_path, 'w')
		f.write(json_string)
		f.close()
	
	@staticmethod
	def get_global(name):
		return GlobalVars.get_globals()[name]
	
	@staticmethod
	def get_globals():

		f  = open(GlobalVars.json_path, 'r')
		json_string = f.read()
		f.close()

		return json.loads(json_string)