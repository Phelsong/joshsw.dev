from utils import project_dir
import os


def build():
    os.system(f"docker compose -f {project_dir}/docker/docker-compose.yaml build --no-cache")

def compose_up():
    os.system(f"docker compose -f {project_dir}/docker/docker-compose.yaml up -d")