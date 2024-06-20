###############################################################################
# code for sitecustomize.py
# ~/.pyenv/versions/<env_name>/lib/python<x>.<y>/site-packages/sitecustomize.py
# loads startup module to perform initial configurations if that is found
# folder until maximum depth starting the current one are searched for that
###############################################################################

import importlib
import os

# a non-negative value
# 0 for current directory,
# 1 for parent of current directory up the hierarchy and so on
max_depth = 2

# current directory to search by default for startup module
dir_path = ['.']

# parent to create the relative paths of all parents recursively
parent = '..'

# python module startup.py is expected to be present in the hierarchy
py_module = 'startup'

# based on the depth add directory paths to search for the module
# if depth is zero, only the current directory will be searched
for depth in range(max_depth):
    dir_path.append(parent)
    parent = os.path.join(parent, '..')

try:
    # if module is found, it returns ModuleSpec(name, loader, origin)
    # otherwise None is returned
    mod_spec = importlib.machinery.PathFinder().find_spec(py_module, dir_path)
    if mod_spec:
        _ = mod_spec.loader.load_module()
    else:
        raise ModuleNotFoundError(
			py_module + ' module not found at ' + str(dir_path)
		)
except Exception as e:
    # broad exception handling since sitecustomize exceptions are ignored
    # we can opt not to print the error message
	# because the customization is optional
    # print(e)
    pass

###############################################################################

