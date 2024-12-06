import csv
import pickle


def load_table(name_table = 'File_1_1.csv', mode = input('Введите один из трёх форматов(csv/txt/pickle): ') ):
    '''
    The function loads files of the csv/txt/pickle format and converts them into a dictionary of the form key - column name, value - column content. Also checks the input values, raising messages if something is wrong
    Arguments:
    name_table - file name, mode - file format

    Return:
    dictionary of the form key - column name, value - column content

    Raises:
    IOError: handles the error "No access to the file"
    UnicodeDecodeError: handles the error "Decoding violation", if the file was damaged.
    '''
    list_table = []
    dist_table = {}
    if mode == 'csv':
        try:
            with open(name_table) as table:
                reader = csv.reader(table, delimiter=';')
                header = next(reader)
                strings = [el for el in reader]
                result_list = []
                for col in range(len(header)):
                    row = []
                    for ln in range(len(strings)):
                        row.append(strings[ln][col])
                    result_list.append(row)
                dict_table = {header[num]:result_list[num] for num in range(len(header))}
        except IOError:
            return 'Нет доступа к файлу'
        except UnicodeDecodeError:
            return 'Файл повреждён'
    if mode == 'txt':
        try:
            with open(name_table, encoding='utf-8') as table:
                header = table.readline().rstrip().split(' ')
                strings = [str_n.rstrip().split(' ') for str_n in table.readlines()]
                result_list = []
                for col in range(len(header)):
                    row = []
                    for ln in range(len(strings)):
                        row.append(strings[ln][col])
                    result_list.append(row)
                dict_table = {header[num]:result_list[num] for num in range(len(header))}
        except IOError:
            return 'Нет доступа к файлу'
        except UnicodeDecodeError:
            return 'Файл повреждён'
    if mode == 'pickle':
        try:
            with open(name_table, 'rb') as file:
                dict_table = pickle.load(file)
        except IOError:
            return 'Нет доступа к файлу'
        except UnicodeDecodeError:
            return 'Файл повреждён'

    return dict_table
print(load_table())

dict_table = load_table()

with open('tablepic.pickle', 'wb') as file:
    pickle.dump(dict_table, file)
def save_table(dict_table):
    '''
    Documentation for the Function:

    The function saves a dictionary as a CSV file where the keys of the dictionary represent column names and the values represent the content of each column.

    Arguments:
    - dict_table: A dictionary where keys are column names and values are the corresponding column contents.

    Return:
    - This function does not return any value. It saves the content to a CSV file named File_1.csv.

    Raises:
    - IOError: Handles the error if there is an issue with file access or saving the file.
    '''
    key = (dict_table.keys())
    val = (dict_table.values()) 
    #print(key,val)
    with open('File_1.csv', 'w+', newline='') as table:
        writer = csv.writer(table, delimiter=';')
        writer.writerows(val)


print(save_table(load_table()))


print('Функция get_rows_by_number')
flag = True
while flag == True:
    start = int(input('Введите индекс строки, с которой вы хотите начать вывод: '))
    stop = int(input('Введите индекс строки, до которой вы хотите вывести (включая): '))
    dict_table = load_table()
    def get_rows_by_number(dict_table, start, stop,copy = bool(input('Введите True, если вы хотите создать копию, False, если не хотите: '))):
        list_result = []
        ''' 
        The function retrieves a specific range of rows from a dictionary-based table, allowing the user to specify the starting and stopping indices. It provides the option to return a deep copy of the results or a direct reference to the original data.

        Arguments:
        - dict_table: A dictionary where keys represent column names and values are lists containing the corresponding column data.
        - start: An integer representing the starting index of the rows to be retrieved (inclusive).
        - stop: An integer representing the ending index of the rows to be retrieved (inclusive).
        - copy: A boolean value indicating whether to create a deep copy of the resulting rows (True) or return a reference to the original data (False). The default value is set based on user input.
        
        Return:
        - A list of rows corresponding to the specified indices. If copy is True, the returned list will be a deep copy; if False, it will reference the original data directly.
        
        Raises:
        - IndexError: Returns a message if the provided column index is invalid or out of range.
        '''
        try:
            for ind in range(start,stop+1):
                for el in dict_table.values():
                    list_result.append([el[ind]])
            if copy:
                import copy
                return copy.deepcopy(list_result)
            else:
                return list_result
        except:
            return 'Неверно введины start/ stop'
    print(get_rows_by_number(dict_table,start,stop))
    flag = False


print('Функция get_rows_by_index')
flag = True
while flag == True:
    ind_list = []
    ind = ' '
    while ind != '':
        ind = input('Введите индекс строки, которую вы хотите вывести(когда вы введёте все элементы введите, пустую строку : ')
        ind_list.append(ind)
    ind_list = list(map(int,ind_list[:-1]))
    def get_rows_by_index(ind_list,dict_table = load_table(),copy_table = bool(input('Введите True, если вы хотите сделать копию таблицы, False, если не хотите: '))):
        '''
        The function retrieves specific rows from a dictionary-based table based on user-defined indices. It allows the user to decide whether to return a deep copy of the selected rows or a reference to the original list.

        Arguments:
        - ind_list: A list of integers representing the indices of the rows to be retrieved.
        - dict_table: A dictionary loaded from a data source, where keys are column names and values are lists containing corresponding column data. Default is the output from the load_table() function.
        - copy_table: A boolean value indicating whether to create a deep copy of the result (True) or return a reference to the original data (False). It is set based on user input.

        Return:
        - A list containing the selected rows. If copy_table is True, this list will be a deep copy; if False, it will reference the original data directly.

        Raises:
        - IndexError: Returns a message if the provided column index is invalid or out of range.
        '''
        list_table = []
        try:    
            for ind in ind_list:
                for el in dict_table.values():
                    list_table.append(el[ind])
    
            if copy_table:
                import copy
                return copy.deepcopy(list_table)
            else:
                return list_table
        except:
            return 'Неверно введены индексы строки'

    print(get_rows_by_index(ind_list))
    flag = False


print('Функция get_column_types')
flag = True
while flag == True:
    #dict_types = {1: int, 2: bool, 3: float, 4: str}
    def get_column_types(dict_table = load_table(),number = int(input('Введите индекс столбца, тип данных которого вы хотите вывести, если всех столбцов введите 100: '))):
        '''
        The function retrieves the data types of columns in a table based on a dictionary. It allows the user to specify a column index to get the type of that specific column, or to retrieve the types for all columns by entering a specific value.

        Arguments:
        - dict_table: A dictionary loaded from the data source, where the keys are the column names and the values ​​are lists containing the corresponding column data. By default, this is the output of the load_table() function.
        - number: An integer representing the index of the column whose data type you want to retrieve. If you want the types for all columns, enter 100.

        Returns:
        - A dictionary where the keys are the column names and the values ​​are the data types of all the elements in each column's data. If number is 100, the function returns the data types of all columns. If a specific index is specified, it returns the data type of that specific column.

        Raises:
        - IndexError: Returns a message if the provided column index is invalid or out of range.
        '''
        dict_result = {}
        try:
            if number == 100:
                for key in dict_table:
                    dict_result[key] = type(dict_table[key][0])
                return dict_result
            else:
                dict_result[list(dict_table.keys())[number]] = type(dict_table[list(dict_table.keys())[number]][0])
                return dict_result
        except:
            return 'неверно введён индекс столбца'
    print(get_column_types())
    flag = False



print('Функция set_column_types')
flag = True
while flag == True:
    def set_column_types(types,dict_table = load_table(),ind = int(input('Введите индекс столбца: '))):
        '''
        The function sets the data types for a specific column in a dictionary-based table. It allows users to specify the desired type and applies it to the entire column based on the given index.

        Arguments:
        - types: A type or a function representing the desired data type to be applied to the elements of the specified column.
        - dict_table: A dictionary loaded from a data source, where keys are column names and values are lists containing corresponding column data. Default is the output from the load_table() function.
        - ind: An integer representing the index of the column where the data type should be set.

        Return:
        - This function does not return a value. It modifies the original dict_table in place by converting the data type of the specified column.

        Raises:
        - ValueError: Returns a message if the specified type is not suitable for the elements in the column.
        - IndexError: Returns a message if the provided column index is invalid or out of range.``
        '''
        try:
            dict_table[list(dict_table.keys())[ind]] = list(map(types,dict_table[list(dict_table.keys())[ind]]))
        except ValueError:
            return 'Этот тип не подходит этому столбцу '
        except IndexError:
            return 'Неверно введён индекс столбца'

    print(set_column_types(int))
    flag = False


print('Функция get_values')
flag = True
while flag == True:
    def get_values(ind = int(input('Введите индекс столбца: ')),dict_table = load_table()):
        '''
        The function retrieves the values of a specific column from a dictionary-based table based on the provided column index.

        Arguments:
        - ind: An integer representing the index of the column whose values you want to retrieve. The function prompts the user for this value.
        - dict_table: A dictionary loaded from a data source, where keys are column names and values are lists containing the corresponding column data. The default is the output from the load_table() function.

        Return:
        - A list containing the values of the specified column. If the provided index is valid, it returns the corresponding column values.

        Raises:
        - IndexError: Returns a message if the provided column index is invalid or out of range, indicating that the input was incorrect.
        '''
        try:
            return dict_table[list(dict_table.keys())[ind]]
        except IndexError:
            return 'Неверно ввелён нидекс столбца'
    print(get_values())
    flag = False


print('Функция get_value')
flag = True
while flag == True:
    def get_value(string = int(input('Введите индекс строки: ')), column= int(input('Введите индекс столба: ')),dict_table = load_table()):
        '''
        The function retrieves a specific value from a dictionary-based table by specifying the row and column indices.

        Arguments:
        - string: An integer representing the index of the row from which to retrieve the value. The function prompts the user for this value.
        - column: An integer representing the index of the column from which to retrieve the value. The function prompts the user for this value.
        - dict_table: A dictionary loaded from a data source, where keys are column names and values are lists containing the corresponding column data. The default is the output from the load_table() function.

        Return:
        - The function returns the value located at the specified row (string) and column (column) indices. If the provided indices are valid, it returns the corresponding value from the table.

        Raises:
        - IndexError: Returns a message if the provided row or column indices are invalid or out of range, indicating that the input was incorrect.
        '''
        try:
            return dict_table[list(dict_table.keys())[column]][string]
        except IndexError:
            return 'Неверно введён индекс'
    print(get_value())
    flag = False


print('Функция set_values')
flag = True
while flag == True:
    def set_values(values = [input('Введите значение столбца: ') for n in range(4)],ind = int(input('Введите индекс столбца: ')), dict_table = load_table()):
        '''
        The function updates the values of a specific column in a dictionary-based table. It allows users to input new values for the specified column index.

        Arguments:
        - values: A list of values to set for the specified column. The default value is generated by prompting the user to enter values for four entries.
        - ind: An integer representing the index of the column to be updated. The function prompts the user for this value.
        - dict_table: A dictionary loaded from a data source, where keys are column names and values are lists containing the corresponding column data. The default is the output from the load_table() function.

        Return:
        - The function returns the updated dict_table, with the specified column values replaced by the new values.

        Raises:
        - IndexError: Returns a message if the provided column index is invalid or out of range, indicating that the input was incorrect.
        '''
        try:
            dict_table[list(dict_table.keys())[ind]] = values
            return dict_table
        except IndexError:
            return 'Неверно введён индекс'
            
    print(set_values())
    flag = False


print('Функция set_value')
flag = True
while flag == True:
    def set_value(value = input('Введите значение, которое вы хотите ввести: '), string = int(input('Введите индекс строки: ')), column= int(input('Введите индекс столба: ')),dict_table = load_table()):
        '''
        The function updates a specific value in a dictionary-based table by specifying the row and column indices. It allows the user to input a new value for that specific cell in the table.

        Arguments:
        - value: The value to be set in the specified cell. The default value is obtained by prompting the user for input.
        - string: An integer representing the index of the row where the value will be placed. The function prompts the user for this value.
        - column: An integer representing the index of the column where the value will be placed. The function prompts the user for this value.
        - dict_table: A dictionary loaded from a data source, where keys are column names and values are lists containing the corresponding column data. The default is the output from the load_table() function.

        Return:
        - The function returns the updated dict_table with the specified value inserted at the given cell (row, column).

        Raises:
        - IndexError: Returns a message if the provided row or column indices are invalid or out of range, indicating that the input was incorrect.
        '''
        try:
            dict_table[list(dict_table.keys())[column]][string] = value
            return dict_table
        except IndexError:
            return 'Неверно введён индекс'
        
    print(set_value())
    flag = False


print('Функция print_table')
flag = True
while flag == True:
    def print_table(dict_table = load_table()):
        '''
        Documentation for the Function:

        The function prints the contents of a dictionary-based table to the console. It displays the column names followed by the corresponding values for each row.

        Arguments:
        - dict_table: A dictionary loaded from a data source, where keys are column names and values are lists containing the corresponding column data. The default is the output from the load_table() function.

        Return:
        - The function does not return any value. It prints the column names and their corresponding values directly to the console.

        Raises:
        - The function does not explicitly raise exceptions but will print an error message if there is an issue with the table loaded from load_table().
        '''
        try:
            print(*dict_table.keys())
            for string in dict_table.values():
                print(*string)
            return ''
        except:
            'Ошибка с таблицей в функции load_table'
    print(print_table())
    flag = False






