from uppercase_to_underline_lowercase_pathnames import uppercase_to_underline_lowercase_pathnames
from put_all_files_in_dir_into_folders import put_all_files_in_dir_into_folders

exts = ["avi", "mkv", "ogm", "rmvb", "srt"]

#BE CAREFULL, IF YOU PUT path = C:\, this will modify your whole disk!!!!!
path = r"C:\Users\Thiago\Videos\Animations"
assert(len(path)>10) #non intelligent disk destruction prevention

put_all_files_in_dir_into_folders(path,exts)
