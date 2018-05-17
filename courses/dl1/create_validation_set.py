import os as os
from os import *
import random
import shutil

def copy_to_valid(path, chosen_files, class_dir):
    for i in range (len(chosen_files)):
        source = "%s/train/%s/%s" % (path, class_dir, chosen_files[i])
        dest = "%s/valid/%s" % (path, class_dir)
        shutil.move(source, dest)


def create_validation_set(path):
    directory = "%s/train/" % path
    classes = [f for f in listdir(directory)]
    for classname in classes:
        os.makedirs('%s/valid/%s' % (path, classname))
        list_of_files = [f for f in listdir("%s/train/%s" % (path, classname))]
        random.shuffle(list_of_files)
        n_files_moved=int(len(list_of_files)*0.2)
        selected_files = [list_of_files[m] for m in range(n_files_moved)]
        copy_to_valid(path, selected_files, classname)