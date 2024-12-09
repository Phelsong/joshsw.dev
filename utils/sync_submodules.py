from utils import project_dir
import os


def sync_submodules():
    try:
        os.chdir(project_dir)
        print(project_dir)
        assert os.getcwd() == project_dir
        os.system(f"git submodule update --init --recursive")
    except AssertionError:
        print(f"You must be in {project_dir} to sync submodules")
