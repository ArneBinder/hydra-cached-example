import time
from typing import Any

from hydra_cached.execution.hydra_utils import not_deterministic


def hello(name: str):
	print(f"Hello, {name}!")


def delay(seconds: int, data: Any) -> Any:
	time.sleep(seconds)
	return data


@not_deterministic
def load_file(file_name: str) -> str:
	with open(file_name) as f:
		content = f.read()
	return content
