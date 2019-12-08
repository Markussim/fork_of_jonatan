rows = []

size = 10
for j in range(0, size):
    rows.append([])
    for i in range(0, size):
        rows[j].append("null_lol")


# rows[9][9] = "x"


def print_board(rows_internal):
    length_of_rows = len(rows_internal)
    for i_internal in range(0, length_of_rows):
        length_of_rows_2 = len(rows_internal[i_internal])
        for j_internal in range(0, length_of_rows_2):
            if rows_internal[i_internal][j_internal] == "null_lol":
                print("| ", end='')
            else:
                print_thing = "|" + rows_internal[i_internal][j_internal]
                print(print_thing, end='')
        print("|")

    for i_internal in range(0, length_of_rows):
        print("", i_internal, end='')  # Mycket fin kod asså
    print()


def add_piece(rows_internal, player_internal, the_row_internal):
    length_of_rows = len(rows_internal)
    for i_internal in range(0, length_of_rows):
        if rows_internal[the_row_internal][i_internal] == "null_lol":
            pass


game = True
player = "x"
while game:
    # print_board(rows)
    the_row = input()
    add_piece(rows, player, the_row)
