from hydra_cached.execution.hydra_utils import not_deterministic


def hello(you: str):
	print(f"Hello, {you}!")


@not_deterministic
def load_file(file_name: str) -> str:
	with open(file_name) as f:
		content = f.read()
	return content
