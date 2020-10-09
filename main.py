import unicodedata
from pprint import pprint

from list_of_fonts import list_of_fonts
from unicode_parser import xid_continue
from unicode_parser import xid_start


def char_in_font(unicode_char, font):
    for cmap in font["cmap"].tables:
        if cmap.isUnicode():
            if ord(unicode_char) in cmap.cmap:
                return True
    return False


if __name__ == "__main__":

    xid_start_displayable = {}
    xid_start_non_displayable = {}
    xid_continue_displayable = {}
    xid_continue_non_displayable = {}

    for unicode_range in xid_start:
        print(unicode_range, f"{xid_start.index(unicode_range)+1}/{len(xid_start)+1}")
        unicode_range_list = unicode_range.split("..")
        xid_start_range = int(hex(int(unicode_range_list[0], 16)), 16)
        xid_end_range = int(hex(int(unicode_range_list[-1], 16)), 16)
        for character in range(xid_start_range, xid_end_range + 1):
            for font in list_of_fonts:
                if (
                    str(character) not in xid_start_displayable
                    and str(character) not in xid_start_non_displayable
                    and not char_in_font(chr(character), font)
                ):
                    # Add the character to xid_start_non_displayable
                    try:
                        character_name = unicodedata.name(chr(character))
                    except ValueError:
                        character_name = ""
                    xid_start_non_displayable[character] = [
                        chr(character),
                        chr(character).encode("raw_unicode_escape"),
                        character_name,
                    ]
                elif (
                    str(character) not in xid_start_displayable
                    and str(character) not in xid_start_non_displayable
                    and char_in_font(chr(character), font)
                ):
                    # Add character to xid_start_displayable
                    try:
                        character_name = unicodedata.name(chr(character))
                    except ValueError:
                        character_name = ""
                    xid_start_displayable[character] = [
                        chr(character),
                        chr(character).encode("raw_unicode_escape"),
                        character_name,
                    ]

        # Display all characters that aren't displayable in any font installed
        for key in xid_start_non_displayable:
            if (
                key in range(xid_start_range, xid_end_range + 1)
                and key not in xid_start_displayable
            ):
                print(chr(character), hex(key))

    for unicode_range in xid_continue:
        print(unicode_range, f"{xid_continue.index(unicode_range)+1}/{len(xid_continue)+1}")
        unicode_range_list = unicode_range.split("..")
        xid_start_range = int(hex(int(unicode_range_list[0], 16)), 16)
        xid_end_range = int(hex(int(unicode_range_list[-1], 16)), 16)
        for character in range(xid_start_range, xid_end_range + 1):
            for font in list_of_fonts:
                if (
                    str(character) not in xid_continue_displayable
                    and str(character) not in xid_continue_non_displayable
                    and not char_in_font(chr(character), font)
                ):
                    # Add the character to xid_continue_non_displayable
                    try:
                        character_name = unicodedata.name(chr(character))
                    except ValueError:
                        character_name = ""
                    xid_continue_non_displayable[character] = [
                        chr(character),
                        chr(character).encode("raw_unicode_escape"),
                        character_name,
                    ]
                elif (
                    str(character) not in xid_continue_displayable
                    and str(character) not in xid_continue_non_displayable
                    and char_in_font(chr(character), font)
                ):
                    # Add character to xid_continue_displayable
                    try:
                        character_name = unicodedata.name(chr(character))
                    except ValueError:
                        character_name = ""
                    xid_continue_displayable[character] = [
                        chr(character),
                        chr(character).encode("raw_unicode_escape"),
                        character_name,
                    ]

        # Display all characters that aren't displayable in any font installed
        for key in xid_continue_non_displayable:
            if (
                key in range(xid_start_range, xid_end_range + 1)
                and key not in xid_continue_displayable
            ):
                print(chr(character), hex(key))

    xid_start_non_displayable = {
        key: xid_start_non_displayable[key]
        for key in set(xid_start_non_displayable) - set(xid_start_displayable)
    }
    xid_continue_non_displayable = {
        key: xid_continue_non_displayable[key]
        for key in set(xid_continue_non_displayable) - set(xid_continue_displayable)
    }

    """
    Sublime Text's JSON formatter was pitching a fit, so I just pretty printed and manually copied
    over the completed list of characters to a python file.
    """
    pprint(xid_start_displayable)
    pprint(xid_continue_displayable)
    print(len(xid_start_non_displayable))
    print(len(xid_continue_non_displayable))
