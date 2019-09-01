RIGHT, DOWN, LEFT, UP = range(4)

directions = [RIGHT, DOWN, LEFT, UP]


class Ant:

    def __init__(self, k):
        self.x, self.y = 0, 0
        self.black = set()
        self.direction = RIGHT
        for i in range(k):
            self.move_once()

    def __str__(self):
        min_x = max_x = min_y = max_y = 0
        for x, y in self.black:
            min_x = min(min_y, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)
        return '\n'.join(
            ''.join(
                ' █'[(x, y) in self.black]
                for x in range(min_x, max_x + 1)
            )
            for y in range(min_y, max_y + 1)
        )

    def move_once(self):
        if (self.x, self.y) in self.black:
            self.black.remove((self.x, self.y))
            self.turn_left()
            self.step_forward()
        else:
            self.black.add((self.x, self.y))
            self.turn_right()
            self.step_forward()

    def turn_left(self):
        self.direction = (self.direction - 1) % 4

    def turn_right(self):
        self.direction = (self.direction + 1) % 4

    def step_forward(self):
        self.x, self.y = {
            RIGHT: (self.x + 1, self.y),
            DOWN: (self.x, self.y - 1),
            LEFT: (self.x - 1, self.y),
            UP: (self.x, self.y + 1)
        }[self.direction]


def print_k_moves(k):
    print(Ant(k))


print_k_moves(10000)
