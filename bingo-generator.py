from PIL import Image, ImageDraw, ImageFont
from os.path import exists
from os import mkdir
from import_db import import_bingo


def generate_bingo(filename, width, height, bg_color, line_color, text_color, board_values, font_path):
    bingo_board = Image.new('RGBA', (width, height), color=bg_color)

    draw = ImageDraw.Draw(bingo_board)
    for l in range(1, 5):
        draw.line(xy=[(0, int(height/5)*l), (width, int(height/5)*l)],
                  fill=line_color, width=5, joint=None)
        draw.line(xy=[(int(width/5)*l, 0), (int(width/5)*l, height)],
                  fill=line_color, width=5, joint=None)

    font = ImageFont.truetype(font_path, 16)
    for i in range(len(board_values)):
        text_size = draw.textsize(board_values[i], font)
        text_x = int(width/10 - text_size[0]/2) + (i % 5)*int(width/5)
        text_y = int(height/10 - text_size[1]/2) + int(i/5)*int(height/5)
        draw.text(
            xy=(text_x, text_y),
            text=board_values[i],
            fill=text_color,
            font=font,
            align='center'
        )

    bingo_board.save('output/{0}.png'.format(filename))


if(__name__ == "__main__"):
    if(not exists('output')):
        mkdir('output')
    db = import_bingo()
    params = {
        'filename': 'test',
        'width': 640,
        'height': 480,
        'bg_color': (13, 89, 221),
        'line_color': (24, 24, 24),
        'text_color': (204, 216, 255),
        'board_values': ['test'],
        'font_path': '/usr/share/fonts/truetype/msttcorefonts/arial.ttf'
    }
    generate_bingo(
        params['filename'],
        params['width'],
        params['height'],
        params['bg_color'],
        params['line_color'],
        params['text_color'],
        params['board_values'],
        params['font_path']
    )
