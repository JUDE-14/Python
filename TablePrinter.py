print('Name: Jude Andrew \nUSN: 1AY24AI049 \nSection: M\n ')

def print_table_with_lines(table):
    col_widths = [max(len(str(item)) for item in col) for col in table]
    num_rows = len(table[0])
    num_cols = len(table)

    def print_border():
        border = '+'
        for width in col_widths:
            border += '-' * (width + 2) + '+'
        print(border)

    for row in range(num_rows):
        print_border()
        row_line = '|'
        for col in range(num_cols):
            item = table[col][row]
            row_line += f' {item.rjust(col_widths[col])} |'
        print(row_line)
    print_border()

table_data = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]

print_table_with_lines(table_data)
