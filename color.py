

class Colors:

    def __init__(self, hex_code):
        self.hex_code = hex_code

    def three_hex_to_rgb(self):
        if self.hex_code is True:
            color = color.lstrip('#')
            lv = len(color)
            if lv = 3:
                color = color[self.hex_code[0:2]], color[hex_code[2:4]], color[hex_code[4:6]]
                return tuple(int(six_hex[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
            elif lv = 6:
                return tuple(int(six_hex[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
            else:
                pass
        else:
            pass
