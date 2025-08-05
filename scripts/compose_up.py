from utils import project_dir
import os


def compose_up():
    os.system(f"docker compose -f {project_dir}/docker/docker-compose.yaml up -d")


if __name__ == "__main__":
    compose_up()
