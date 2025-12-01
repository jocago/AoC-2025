import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    sample = '''L68
    L30
    R48
    L5
    R60
    L55
    L1
    L99
    R14
    L82'''
    return (sample,)


@app.cell
def _():
    def parse(input:str):
        inst = []
        for line in input.split('\n'):
            direction = line[0]
            distance = line[1:]
            #inst.append((direction,distance))
            if direction == "R":
                inst.append(int(distance))
            else:
                inst.append(0-int(distance))
        return inst
    #print(parse(sample))
    return (parse,)


@app.cell
def _(parse):
    def get_pass_1(input, title):
        val = 50
        targets = 0
        for inp in parse(input):
            val += inp
            while val < 0:
                val += 100
            while val > 99:
                val -= 100
            if val == 0:
                targets += 1
            #print(f'rotated {inp} to {val}')
        print(f'Passcode for {title} is {targets}')
    return (get_pass_1,)


@app.cell
def _(get_pass_1, sample):
    #test
    get_pass_1(sample, "part 1 test")
    return


@app.cell
def _():
    with open('day_01_input.txt','r') as fin:
            dat = fin.read()

    return (dat,)


@app.cell
def _(dat, get_pass_1):
    get_pass_1(dat, "part 1")
    return


@app.cell
def _(parse):
    def get_pass_2(input, title):
        val = 50
        targets = 0
        for inp in parse(input):
            # print('-----')
            incr = 1 if inp >= 0 else -1
            for _ in range(abs(inp)):
                val += incr
                if val > 99:
                    val -= 100
                elif val < 0:
                    val += 100
                if val == 0:
                    targets += 1
                    # print('hit 0')
            # print(f'added {inp} for {val}')
        print(f'Passcode for {title} is {targets}')

    return (get_pass_2,)


@app.cell
def _(get_pass_2, sample):
    #test
    get_pass_2(sample, 'part 2 test')
    return


@app.cell
def _(dat, get_pass_2):
    get_pass_2(dat, "part 2")
    return


if __name__ == "__main__":
    app.run()
