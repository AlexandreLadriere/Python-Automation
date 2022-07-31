FILE_IN = 'test.txt'
FILE_OUT = 'out.txt'

def getColumn(*args):
    '''
    Return a list of tuples which corresponds to columns in a file

    *args : (filename, col1_start, col1_end, col2_start, col2_end, ...)
    '''
    columns = []
    col_number = int((len(args) - 1) / 2)
    with open(args[0], 'r', encoding='UTF-8') as file:
        while (line := file.readline().rstrip()):
            j = 0
            col_by_line_list = []
            for i in range(0, col_number):
                col_tmp = line[args[j + 1] - 1:args[j + 2] - 1]
                j+=2
                col_by_line_list.append(col_tmp)
            columns.append(tuple(col_by_line_list))
    return columns

def removeDuplicates(duplicates_list):
    return list(dict.fromkeys(duplicates_list))

def saveFile(filename, values):
    with open(filename, 'w') as f:
        for line in values:
            for element in line:
                f.write(element + ";")
            f.write("\n")

if __name__ == '__main__':
    columns = getColumn(FILE_IN, 1, 13)
    columns_without_duplicates = removeDuplicates(columns)
    saveFile(FILE_OUT, columns_without_duplicates)