"""Example __init__py file."""

from . import common, linear, squared

"""If file is blank, the loader won't do anything.
`__all__` specifies what is public and the recommended way.
`from . import blah` is specific.
Each have their advantages and disadvantages
"""

print('Loaded nick')
