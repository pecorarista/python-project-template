from pathlib import Path
from typing import Dict

import toml


class DBConfig:
    def __init__(self, d: Dict[str, str]) -> 'DBConfig':
        self.uri = d['uri']
        self.uri_test = d['uri_test']


class Config:
    def __init__(self, dest_config: Path) -> 'Config':
        config = toml.load(dest_config)
        db = config['database']
        self.db = DBConfig(db)
