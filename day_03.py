import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.function
def get_data(sample=False):
    if sample:
        return ['987654321111111','811111111111119','234234234234278','818181911112111']
    else:
        with open('day_03_input.txt', 'r') as fin:
            return fin.readlines()


@app.function
def solve_part_1(data):
    jolts = []
    for bank in data:
        bank = list(map(int, bank.strip()))
        max_val = max(bank[:-1]) # don't use last val because need 2 digits
        idx_max_val = bank.index(max_val)
        next_max_val = max(bank[idx_max_val+1:])
        jolts.append(max_val * 10 + next_max_val)
    print(jolts)
    print(sum(jolts))


@app.cell
def _():
    print('Part 1 solution (test)')
    solve_part_1(get_data(sample=True))
    return


@app.cell
def _():
    print('Part 1 solution')
    solve_part_1(get_data())
    return


@app.function
def solve_part_2(data):
    jolts = []
    for bank in data:
        bank = list(map(int, bank.strip()))
        power = 0
        for spacer in range(11): # walk through a closing window
            max_val = max(bank[:spacer - 11])
            power = power * 10 + max_val
            bank = bank[bank.index(max_val) + 1:]
        jolts.append(power * 10 + max(bank))
    print(jolts)
    print(sum(jolts))


@app.cell
def _():
    print('Part 2 solution (test)')
    solve_part_2(get_data(sample=True))
    return


@app.cell
def _():
    print('Part 2 solution')
    solve_part_2(get_data())
    return


if __name__ == "__main__":
    app.run()
