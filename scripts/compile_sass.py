from utils import project_dir
import os


def compile_sass():
    os.system(f"sass {project_dir}/sass/index.scss {project_dir}/public/index.css")
