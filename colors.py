class Colors:
    dark_grey = (26, 31, 40);
    green = (47, 230, 23);
    red = (232, 18, 18);
    orange = (255, 98, 8);
    yellow = (237, 234, 4);
    purple = (166, 0, 247);
    cyan = (21, 204, 209);
    blue = (13, 26, 216);

    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]