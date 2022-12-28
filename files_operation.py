doing = 'открыт существующий файл'
try:
    file = open('my_file.txt')
except FileNotFoundError:
#except:
    file = open('my_file.txt', encoding='cp1251', mode='w')
    doing = 'создан новый файл'
finally:
    print(f'Успешно {doing}!!!')
    file.close()
