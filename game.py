class Game:
    def guess(self, quessNumber):
        if quessNumber is None:
            raise TypeError()