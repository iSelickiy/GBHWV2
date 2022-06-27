# Написать скрипт, создающий стартер(заготовку) для проекта

import os

dir_dict = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}

for key, value in dir_dict.items():
    if not os.path.exists(key):
        os.mkdir(key)
    if isinstance(value, list):
        for directory in value:
            if not os.path.exists(os.path.join(key, directory)):
                os.mkdir(os.path.join(key, directory))

