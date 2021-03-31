MOVES_MAX = 9


def analyze_field(f):
    max_col = len(f[0])
    max_row = len(f)
    cols = [[] for _ in range(max_col)]
    rows = [[] for _ in range(max_row)]
    fdiag = [[] for _ in range(max_row + max_col - 1)]
    bdiag = [[] for _ in range(len(fdiag))]
    min_bdiag = -max_row + 1

    for x in range(max_col):
        for y in range(max_row):
            cols[x].append(f[y][x])
            rows[y].append(f[y][x])
            fdiag[x + y].append(f[y][x])
            bdiag[x - y - min_bdiag].append(f[y][x])

    return {
        'columns': cols,
        'rows': rows,
        'fdiag': fdiag,
        'bdiag': bdiag
    }


def someone_won(data):
    for key, value in data.items():
        if check_sequence(value):
            return True


def check_sequence(input_sequence):
    for sequence in input_sequence:
        if len(sequence) == 3 and sequence.count(sequence[0]) == len(sequence) and sequence[0] != 0:
            return True


def move(x, y, value, f):
    if f[y][x] == 0:
        f[y][x] = value
        return True
    return False


def print_field(data):
    print("  0 1 2")
    string_field = [
        ["0", "0", "0"],
        ["0", "0", "0"],
        ["0", "0", "0"]
    ]

    for ix in range(0, 3):
        for jx, cell in enumerate(data['rows'][ix]):
            if cell == 0:
                string_field[ix][jx] = "-"
            elif cell == 1:
                string_field[ix][jx] = "x"
            elif cell == 2:
                string_field[ix][jx] = "o"

        values = " ".join(val for val in string_field[ix])
        print(f"{ix} {values}")


def main():
    field = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    move_x = True
    current_move = 1

    while current_move <= MOVES_MAX:
        if move_x:
            value = 1
            print('Ход игрока 1 (x)')
        else:
            value = 2
            print('Ход игрока 2 (o)')

        input_y = int(input("Введите ряд: "))
        input_x = int(input("Введите столбец: "))

        if move(input_x, input_y, value, field):
            current_move += 1
            move_x = not move_x
        else:
            print("Это поле уже занято, выберете другое")
            pass

        data = analyze_field(field)
        print_field(data)

        if someone_won(data):
            if move_x:
                print('Игрок 2(o) побеждает')
            else:
                print('Игрок 1(x) побеждает')
            break
        elif current_move > MOVES_MAX:
            print('Ничья')


if __name__ == '__main__':
    main()
