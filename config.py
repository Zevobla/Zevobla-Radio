import tomllib
from pathlib import Path

class Config:
    def __init__(self, file: Path = "config.toml") -> None:
        with open(file, "rb") as f:
            self.conf = tomllib.load(f)
