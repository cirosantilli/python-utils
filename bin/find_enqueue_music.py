#!/usr/bin/env python

if __name__ == '__main__':
    import os
    import sys
    from cirosantilli import files
    import subprocess
    import platform
    
    music_exts = ['flac','mp3','m4a','ogg','wav','wma']
    DEFAULT_PLAYER = 'totem'
    
    # play in totem if no other specified

    if len(sys.argv)>1:
      player = sys.argv[1]
    else:
      player = DEFAULT_PLAYER
    
    # popen will decide where to put output, and there is not 
    # standard form of NUL
    system = platform.system()
    if system == 'Linux':
      nulname = '/dev/null'
    elif system == 'Windows':
      nulname = 'NUL'
    else:
      raise Exception('Unsupported operating system: \'' + system + '\'')
    FNUL = open(nulname, 'w')
    
    exists, the_files = files.list(
      os.getcwd(),
      exts=music_exts,
      files=1,
      dirs=0,
      fulltree=1)
    
    if exists:
      subprocess.Popen([player]+the_files, stdout=FNUL, stderr=FNUL)










