"""utility modules"""
import os
from modulefinder import packagePathMap
from pathlib import Path

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
package_dir = Path(f"{project_dir}/packages")
build_dir: Path = Path(f"{project_dir}/build")
