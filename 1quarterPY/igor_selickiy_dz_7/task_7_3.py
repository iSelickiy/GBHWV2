# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или
# «руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку
# templates,

import os
import shutil


for root, d, files in os.walk(os.path.join('my_project')):
    if 'templates' in root and not dir:
        print(root, d, files)
        print(os.path.split(root)[1])
        for file in files:
            print(os.path.join(root, file))
            if not os.path.exists(os.path.join('templates', os.path.split(root)[1])):
                os.makedirs(os.path.join('templates', os.path.split(root)[1]))
            shutil.copy(os.path.join(root, file), os.path.join('templates', os.path.split(root)[1]))





