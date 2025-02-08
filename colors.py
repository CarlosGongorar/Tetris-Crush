class Colors:
    dark_grey = (26, 31, 40);
    green = (47, 230, 23);
    red = (232, 18, 18);
    orange = (255, 98, 8);
    yellow = (237, 234, 4);
    purple = (166, 0, 247);
    cyan = (21, 204, 209);
    blue = (13, 26, 216);
    white = (255, 255, 255);
    background_color = (44, 44, 127);
    details = (59, 85, 162);

    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]