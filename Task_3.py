import os
import shutil

dir_project = './my_project'
for root, dirs, files in os.walk(dir_project):
    for dir_name in dirs:
        if dir_name.startswith('templates'):
            root_2 = os.path.join(root, dir_name)
            for _ in os.listdir(os.path.join(root, dir_name)):
                old_way = os.path.join(root_2, _)
                templates_dir = os.path.join(dir_name, _)
                templates_dir_new = os.path.join(dir_project, templates_dir)
                if not os.path.exists(templates_dir_new):
                    shutil.move(old_way, templates_dir_new)
                    os.rmdir(root_2)
