"""Load the json from the directory"""

import json
from typing import Dict, List


def load_data(file_path: str) -> Dict[str, List[str]]:
    """Dict loader, from the file_path var"""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
