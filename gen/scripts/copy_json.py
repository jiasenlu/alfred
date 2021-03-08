import glob
import os
import json
import pdb
import progressbar
from shutil import copyfile
import pathlib

data_path = 'data/new_trajs'
new_path = 'data/trajs_json'
for json_path in progressbar.progressbar(glob.iglob(os.path.join(data_path, "**", "traj_data.json"), recursive=True)):

    folder_path = os.path.join(*json_path.split('/')[2:-1])
    new_folder_path = os.path.join(new_path, folder_path)
    if not os.path.exists(new_folder_path):
        pathlib.Path(new_folder_path).mkdir(parents=True, exist_ok=True)

    copyfile(json_path, os.path.join(new_folder_path, "traj_data.json"))
