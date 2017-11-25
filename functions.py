def color_green(x, y):

    green = "#75ba3b"

    # upper left
    if x < 12:
        if y > 1 and y < 13:
            if y < 8:
                return green
            elif x < 8:
                return green

    # lower left
    if x > 1 and x < 14:
        if y > 15 and x < 8:
            return green
        elif y > 19:
            return green

    # upper right
    if x > 13 and x < 26:
        if y < 8:
            return green
        elif x > 19 and y < 12:
            return green

    # lower right
    if x > 16 and y > 13 and y < 26:
        if x > 19:
            return green
        elif y > 19:
            return green

    if x in [13, 14] and y in [13, 14]:
        return green
