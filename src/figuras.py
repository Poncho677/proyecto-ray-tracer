class Figuras:

    def __init__(self, color, punto):
        self.color = color
        self.punto = punto

    def __iter__(self):
        return iter(self.punto)

    
