"""utility modules"""
import os
from pathlib import Path

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
build_dir: Path = Path(f"{project_dir}/build")
