import pygame as pg


class View:
    def __init__(self):
        self._running = True
        self.size = self.width, self.height = 800, 800
        self.psize = self.pwidth, self.pheight = 100, 100
        self._display_surf = pg.Surface(self.size)

    def on_init(self):
        # note that placement coords of an image is relative to top left corner
        # set board image
        board = pg.image.load("resources\\board.jpg").convert()
        board = pg.transform.scale(board, self.size)
        self._display_surf.blit(board, (0, 0))

        # set major pieces
        piecePaths = ["r", "n", "b", "q", "k"]
        row = ["r", "n", "b", "q", "k", "b", "n", "r"]
        for piece in piecePaths:
            bpieceImage = pg.image.load("resources\\b{}.png".format(piece)).convert_alpha()
            wpieceImage = pg.image.load("resources\\w{}.png".format(piece)).convert_alpha()
            bpiece = pg.transform.scale(bpieceImage, self.psize)
            wpiece = pg.transform.scale(wpieceImage, self.psize)
            by = 0
            wy = self.height - self.pheight
            for i, square in enumerate(row):
                if square == piece:
                    x = i * self.pwidth
                    self._display_surf.blit(bpiece, (x, by))
                    self._display_surf.blit(wpiece, (x, wy))

        # set pawns
        bpawnImage = pg.image.load("resources\\bp.png").convert_alpha()
        wpawnImage = pg.image.load("resources\\wp.png").convert_alpha()
        bpawn = pg.transform.scale(bpawnImage, self.psize)
        wpawn = pg.transform.scale(wpawnImage, self.psize)
        for x in range(0, self.width, self.pwidth):
            by = self.pheight
            wy = self.height - 2 * self.pheight
            self._display_surf.blit(bpawn, (x, by))
            self._display_surf.blit(wpawn, (x, wy))