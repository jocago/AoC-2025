import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return


@app.cell
def _():
    sample= '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'
    return (sample,)


@app.cell
def _():
    def parse(input):
        ranges = []
        arr = input.split(',')
        for block in arr:
            pair = list(map(int, block.split('-')))
            ranges.append(range(pair[0],pair[1]+1))
        return ranges

    def load_input():
        with open('day_02_input.txt','r') as fin:
            dat = fin.read()
        return dat
    return load_input, parse


@app.cell
def _(parse, sample):
    parse(sample)
    return


@app.function
def solve_part_1(parsed_input):
    invalid_ids = []
    for r in parsed_input:
        for val in list(map(str,r)):
            l = len(val)
            if not l %2:
                ld = int(l/2)
                pair = (val[:ld],val[ld:])
                if pair[0] == pair[1]:
                    invalid_ids.append(int(val))
    print(invalid_ids)
    print(sum(invalid_ids))


@app.cell
def _(parse, sample):
    print("Output of Part 1 (test)")
    solve_part_1(parse(sample))
    return


@app.cell
def _(load_input, parse):
    print("Output of Part 1")
    solve_part_1(parse(load_input()))
    return


@app.function
def solve_part_2(parsed_input):
    invalid_ids = []
    for r in parsed_input:
        for val in list(map(str,r)):
            val_match = False
            midway = int(len(val)/2)
            k = 1
            while k <= midway:
                chunks = [val[i:i + k] for i in range(0, len(val), k)]
                if len(set(chunks)) == 1:
                    invalid_ids.append(int(val))
                    break
                k += 1
    print(invalid_ids)
    print(sum(invalid_ids))


@app.cell
def _(parse, sample):
    print("Output of Part 2 (test)")
    solve_part_2(parse(sample))
    return


@app.cell
def _(load_input, parse):
    print("Output of Part 2")
    solve_part_2(parse(load_input()))
    return


if __name__ == "__main__":
    app.run()
