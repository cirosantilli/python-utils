# sets/creates all global values to their initial state

gvars =  {
'lang':'python',
}

for key in gvars.keys():
    store.set_global_value(key,gvars[key])