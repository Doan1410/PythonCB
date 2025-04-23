import os
import shutil

folder_name="BAI44"
os.makedirs(folder_name,exist_ok=1)
shutil.copy('DATA54.txt',folder_name)
os.rename(os.path.join(folder_name,'DATA54.txt'),os.path.join(folder_name,'Data.dat'))
os.remove(os.path.join(folder_name,'Data.dat'))
os.rmdir(folder_name)