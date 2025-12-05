import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return


@app.cell
def _():
    sample_input = '''3-5
    10-14
    16-20
    12-18

    1
    5
    8
    11
    17
    32'''
    return (sample_input,)


@app.cell
def _(sample_input):
    def parse(sample=False):
        def parse_ranges(data):
            return [list(map(int,x.strip().split('-'))) for x in data.split('\n')]

        def parse_products(data):
            return [int(x.strip()) for x in data.split('\n')]

        if sample:
            data = sample_input.split('\n\n')
        else:
            with open('day_05_input.txt','r') as fin:
                data = fin.read().split('\n\n')
        return (parse_ranges(data[0]),parse_products(data[1]))
    return (parse,)


@app.function
def solve_part_1(data_list):
    ranges = [range(x[0],x[1]+1) for x in data_list[0]]
    products = data_list[1]

    fresh = []
    for product in products:
        for p_range in ranges:
            if product in p_range:
                fresh.append(product)
                break
    print(fresh)
    print(len(fresh))


@app.cell
def _(parse):
    print("Part 1 solution (test)")
    solve_part_1(parse(sample=True))
    return


@app.cell
def _(parse):
    print("Part 1 solution")
    solve_part_1(parse())
    return


@app.function
def combine_ranges(range_1, range_2):
    # Returns None if the ranges do not overlap
    if not range_1.stop < range_2.start or range_2.stop < range_1.start:
        return range(min(range_1.start,range_2.start),max(range_1.stop, range_2.stop))
    else:
        return None


@app.function
def solve_part_2(data_list):
    input_ranges = sorted([range(x[0],x[1]+1) for x in data_list[0]],key=lambda r: r.start)
    ranges = [input_ranges.pop(0)]
    for _ in range(len(input_ranges)):
        new_range = input_ranges.pop(0)
        overlaped_range = combine_ranges(ranges[-1],new_range)
        if overlaped_range:
            _ = ranges.pop()
            ranges.append(overlaped_range)
        else:
            ranges.append(new_range)
    cnt = 0
    for r in ranges:
        cnt += (r.stop - r.start)
    print(ranges)
    print(cnt)


@app.cell
def _(parse):
    print("Part 2 solution (test)")
    solve_part_2(parse(sample=True))
    return


@app.cell
def _(parse):
    print("Part 2 solution")
    solve_part_2(parse())
    return


if __name__ == "__main__":
    app.run()
