import pygame as pg
from view import View
from chess import Chess


class App:
    """
        App - main application
    """

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._view = View()

    def on_init(self):
        pg.init()
        self._display_surf = pg.display.set_mode(self._view.size, pg.HWSURFACE | pg.DOUBLEBUF)
        self._view.on_init()  # must be called after display.set_mode()
        self._running = True

    def on_event(self, event):
        if event.type == pg.QUIT:
            self._running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            # set a piece to be dragged using dragging field in View
            coordinates = pg.mouse.get_pos()
            self._view.setSelectedPiece(coordinates)
        elif event.type == pg.MOUSEMOTION:
            # perform a drag operation
            if self._view.dragging != None:
                coordinates = pg.mouse.get_pos()
                self._view.drag(coordinates)
        elif event.type == pg.MOUSEBUTTONUP:
            # reset dragging field in View
            if self._view.dragging != None:
                coordinates = pg.mouse.get_pos()
                self._view.drop(coordinates)
                self._view.dragging = None

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.blit(self._view._display_surf, (0, 0))
        pg.display.update()

    def on_cleanup(self):
        pg.quit()

    def on_execute(self):
        self.on_init()
        while self._running:
            for event in pg.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
