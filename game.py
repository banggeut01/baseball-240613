class Game:
    def guess(self, quessNumber):
        if quessNumber is None:
            raise TypeError()

        if len(quessNumber) != 3:
            raise TypeError()