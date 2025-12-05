import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from enum import Enum
    return (Enum,)


@app.cell
def _():
    sample_input = '''..@@.@@@@.
    @@@.@.@.@@
    @@@@@.@.@@
    @.@@@@..@.
    @@.@@@@.@@
    .@@@@@@@.@
    .@.@.@.@@@
    @.@@@.@@@@
    .@@@@@@@@.
    @.@.@@@.@.'''
    return (sample_input,)


@app.cell
def _(sample_input):
    def parse(sample=False):
        if sample:
            return sample_input.splitlines()
        else:
            with open('day_4_input.txt','r') as fin:
                return fin.readlines()
    
    return (parse,)


@app.cell
def _(Enum):
    class State(Enum):
        EMPTY = '.'
        ROLL = '@'
    return (State,)


@app.class_definition
class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


@app.cell
def _(State):
    class Grid:
        def __init__(self,data):
            self.grid = [list(line.strip()) for line in data]
            self.x_size = len(self.grid[0])
            self.y_size = len(self.grid)

        def get_val(self, coord: Vec2):
            if coord.x < 0 or coord.x >= self.x_size or coord.y < 0 or coord.y >= self.y_size:
                raise(Exception("coord outside of bounds"))
            return State(self.grid[coord.y][coord.x])

        def get_offset_val(self, coord: Vec2, offset: Vec2):
            if coord.x < 0 or coord.x >= self.x_size or coord.y < 0 or coord.y >= self.y_size:
                raise(Exception("coord outside of bounds"))
            if coord.x + offset.x < 0:
                return None
            if coord.x + offset.x >= self.x_size:
                return None
            if coord.y + offset.y < 0:
                return None
            if coord.y + offset.y >= self.y_size:
                return None
            return State(self.grid[coord.y + offset.y][coord.x + offset.x])

        def set_state(self, coord: Vec2, state: State):
            if coord.x < 0 or coord.x >= self.x_size or coord.y < 0 or coord.y >= self.y_size:
                raise(Exception("coord outside of bounds"))
            self.grid[coord.y][coord.x] = state.value
    return (Grid,)


@app.cell
def _():
    satelite_coords = [
        Vec2(-1,-1),
        Vec2(-1,0),
        Vec2(-1,1),
        Vec2(0,-1),
        Vec2(0,1),
        Vec2(1,-1),
        Vec2(1,0),
        Vec2(1,1),
    ]
    return (satelite_coords,)


@app.cell
def _(Grid, State, satelite_coords):
    def solve_part_1(data):
        match_threshold = 4 # match less than
        matches = []
        g = Grid(data)
        for y in range(g.y_size):
            for x in range(g.x_size):
                coords = Vec2(x,y)
                if g.get_val(coords) == State.ROLL:
                    # print(f'{x}:{y} = {match_val}')
                    cnt = 0
                    for offset in satelite_coords:
                        if g.get_offset_val(coords,offset) == State.ROLL:
                            cnt += 1
                    if cnt < 4:
                        matches.append(coords)
        print([(m.x,m.y) for m in matches])
        print(len(matches))
    return (solve_part_1,)


@app.cell
def _(parse, solve_part_1):
    print("Part 1 Solution (test)")
    solve_part_1(parse(sample=True))
    return


@app.cell
def _(parse, solve_part_1):
    print("Part 1 Solution")
    solve_part_1(parse())
    return


@app.cell
def _(Grid, State, satelite_coords):
    def solve_part_2(data):
        match_threshold = 4 # match less than
        g = Grid(data)
        removed = 0
        matches = []
        while True:
            for match in matches:
                g.set_state(coord=match,state=State.EMPTY)
                removed += 1
            matches.clear()
            for y in range(g.y_size):
                for x in range(g.x_size):
                    coords = Vec2(x,y)
                    if g.get_val(coords) == State.ROLL:
                        cnt = 0
                        for offset in satelite_coords:
                            if g.get_offset_val(coords,offset) == State.ROLL:
                                cnt += 1
                        if cnt < 4:
                            matches.append(coords)
            if len(matches) == 0:
                break
        print(removed)
    return (solve_part_2,)


@app.cell
def _(parse, solve_part_2):
    print("Part 2 Solution (test)")
    solve_part_2(parse(sample=True))
    return


@app.cell
def _(parse, solve_part_2):
    print("Part 2 Solution")
    solve_part_2(parse())
    return


if __name__ == "__main__":
    app.run()
