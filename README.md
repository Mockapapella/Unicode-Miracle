# What is this?

This repo started off as an attempt to find every character in unicode that can be used as a starting character in python. For the full story check out my blog post on it here.

# Setup

1. `pip install -r requirements.txt`
2. Run `find_font_names.py`
3. Copy the output of that to `list_of_fonts.py` and correct for any mistakes in path finding and parameters
4. Run `main.py` to obtain a list of characters that are both supported and not supported by the fonts on your system

# Info

Dictionaries for `xid_start` and `xid_continue` are in `xid.py` as `xid_start_dict` and `xid_continue_dict` respectively.
