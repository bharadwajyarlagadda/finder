# -*- coding: utf-8 -*-


RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
NO_COLOR = '\033[0m'

FILE_LINE_OUTPUT = '{green}{path}{nc}:{yellow}{line_number}{nc}: {line}'
FILE_ERROR = '{red}{type}{nc}:{green}{path}{nc}:{message} {extra}'


def render_lines(path, line_number, line, colored=True):
    """Render output for the lines in the file which match the given pattern.
    """
    if not colored:
        green = ''
        yellow = ''
        nc = ''
    else:
        green = GREEN
        yellow = YELLOW
        nc = NO_COLOR

    return FILE_LINE_OUTPUT.format(**{'green': green,
                                      'yellow': yellow,
                                      'nc': nc,
                                      'path': path,
                                      'line_number': line_number,
                                      'line': line})


def render_error(type_, path, message, extra, colored=True):
    """Render file error output."""
    if not colored:
        red = ''
        green = ''
        nc = ''
    else:
        red = RED
        green = GREEN
        nc = NO_COLOR

    return FILE_ERROR.format(**{'red': red,
                                'green': green,
                                'nc': nc,
                                'type': type_,
                                'path': path,
                                'message': message,
                                'extra': extra})
