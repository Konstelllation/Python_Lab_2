if __name__ == '__main__':
        string1 = set(input('Введите первую строку: ').lower())
        string2 = set(input('Введите вторую строку: ').lower())
        print(string2.intersection(string1))