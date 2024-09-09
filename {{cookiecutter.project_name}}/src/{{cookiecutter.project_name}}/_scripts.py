import subprocess


def run_all() -> None:
	subprocess.run(['poetry', 'run', 'ruff', 'format'], check=True)
	subprocess.run(['poetry', 'run', 'mypy', '.'], check=True)


if __name__ == '__main__':
	run_all()
