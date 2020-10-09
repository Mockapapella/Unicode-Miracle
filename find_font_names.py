from pprint import pprint

import matplotlib.font_manager

# Fonts that have file paths with spaces in them will only display part of the directory.
fonts = matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext="ttf")
pprint(fonts)
