# Modules are python files that we can import in our current python file

import useful_tools

print(useful_tools.roll_dice(5))

# If you want to install 3rd party packages, you need to use pip which is the package manager(You can install, manage, uninstall etc using this module)

# For example, there is a 3rd party module called python-docx, you can install it by saying "pip install python-docx". Unlike inbuilt modules, it will not be stored as a single folder in the lib direcotry, but under lib there will be a folder created named SITE-PACKAGES