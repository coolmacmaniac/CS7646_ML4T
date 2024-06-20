import os
import sys

# we can't use the current working directory because it will be the current directoy of the shell
# rather we need to get the directory where this startup module is present i.e., startup_mod_dir
startup_mod_dir = os.path.dirname(os.path.abspath(__file__))

# and then we need to manually see where the source root directory is located
# w.r.t. the startup_mod_dir, this is needed for the imports to work in all scripts
# inside source root and its child folders
source_root = 'src'
source_root_path = None
for root, dirs, files in os.walk(startup_mod_dir):
    if source_root in dirs:
        source_root_path = os.path.join(root, source_root)
        break

if source_root_path:
    sys.path.insert(0, source_root_path)