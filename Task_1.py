import os

dir_name = './my_project'
dir_child_name = ['settings', 'mainapp', 'adminapp', 'authapp']
for name in dir_child_name:
    if not os.path.exists(os.path.join(dir_name, name)):
        os.makedirs(os.path.join(dir_name, name))
