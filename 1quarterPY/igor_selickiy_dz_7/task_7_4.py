# Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором
# ключи — верхняя граница размера файла (пусть будет кратна 10), а значения — общее
# количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
# но больше предыдущей (начинаем с 0)

# *(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи те же, а значения — кортежи вида (<files_quantity>,
# [<files_extensions_list>])

import os
import json
from pathlib import Path


folder_name = 'some_data'
files = max([os.stat(os.path.join(r, file)).st_size for r, d, f in os.walk(folder_name) for file in f])
nums = []
counter = 1
for _ in range(len(str(files))):
    counter *= 10
    nums.append(counter)

dict_for_calc = {num: (sum(1 for r, d, f in os.walk(folder_name)
                           for file in f if
                           os.stat(os.path.join(r, file)).st_size in range(nums.index(num) - 1, num + 1)),
                       list({Path(file).suffix for r, d, f in os.walk(folder_name)
                             for file in f if
                             os.stat(os.path.join(r, file)).st_size in range(nums.index(num) - 1, num + 1)}))
                 for num in nums if num != 0}

with open(folder_name + '_summary.json', 'w') as f_json:
    json.dump(dict_for_calc, f_json)
