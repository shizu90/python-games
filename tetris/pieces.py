import shapes

class Piece(object):
    rows = 20  # y
    columns = 10  # x
 
    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shapes.shape_colors[shapes.shapes.index(shape)]
        self.rotation = 0  # number from 0-3