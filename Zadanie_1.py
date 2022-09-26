if __name__ == '__main__':
        letters = {'а', 'у', 'е', 'о', 'э', 'я', 'и', 'ю', 'ё', 'ы'}
        string = list(input('Введите строку: ').lower())
        count = 0
        for i, slovo in enumerate(string):
            if slovo in letters:
                count += 1
        print(count)