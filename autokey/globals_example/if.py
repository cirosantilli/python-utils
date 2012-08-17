lang = store.get_global_value('lang')

if lang == 'python':
    keyboard.send_keys('if :<left>');
elif lang == 'java': 
    keyboard.send_keys('if(){<enter><enter>}<up><up><end><left><left>');
else:
    keyboard.send_keys('if;');