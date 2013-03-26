lang = store.get_global_value('lang')

if lang == 'python':
    keyboard.send_keys('for  in :<left><left><left><left><left>');
elif lang == 'java': 
    keyboard.send_keys('for(i=0; i<n; i++){<enter><enter>}<up><tab>');
else:
    keyboard.send_keys('for;');