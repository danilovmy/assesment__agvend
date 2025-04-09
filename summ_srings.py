# python ==================
# У нас есть текстовый файл input.txt. В нем через запятую записаны числа. Надо написать скрипт который
# - создаст output.txt

# - запишет в файл суммы чисел сгруппированныe по две строки. т.е. сложить все числа по паре строк
# - первая строчка = сумма всех чисел из 1 и 2 строки
# - вторая строчка = сумма всех чисел из 3 и 4 строки
# - файл можно считать чистым, только целые числа и запятые
# - в файле произвольное кол-во строк.
# - сумма всех чисел input.txt = сумма всех чисел output.txt

# input.txt
# 5,5,0
# 5
# 1,1
# 1,1
# 3
# 4

# output.txt
# 15
# 4

# 7
from pathlib import Path

source = Path('input.txt')
output = Path('output.txt')

def pairs_reader(source):
    with source.open() as data:
        while True:
            first, second = data.readline(), data.readline()
            if not first:
                return
            yield first or '', second or ''


if __name__ == '__main__':
    with output.open('w') as output_file:
        generator = pairs_reader(source)

        for first, second in generator:
            first_num = sum(int(bit or 0) for bit in first.split(','))
            second_num =  sum(int(bit or 0) for bit in second.split(','))
            output_file.writelines(f'{first_num + second_num}\n')
            third, fourth = next(generator, (None, None))
            if third is not None:
                first_num = sum(int(bit or 0) for bit in third.split(','))
                second_num =  sum(int(bit or 0) for bit in fourth.split(','))
                output_file.writelines(f'{first_num + second_num}\n')

            output_file.writelines('\n')
