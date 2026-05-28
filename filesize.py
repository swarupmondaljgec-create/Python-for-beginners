
import os

def display_txt_file_sizes(directory):
	"""Print the size in bytes for all .txt files in the given directory."""
	try:
		for name in sorted(os.listdir(directory)):
			if name.lower().endswith('.txt'):
				path = os.path.join(directory, name)
				if os.path.isfile(path):
					try:
						size = os.path.getsize(path)
						print(f"{path}: {size} bytes")
					except OSError as e:
						print(f"Could not get size for {path}: {e}")
	except FileNotFoundError:
		print(f"Directory not found: {directory}")
	except PermissionError:
		print(f"Permission denied: {directory}")


if __name__ == '__main__':
	target_dir = r"C:\Users\smondal\VSCODE\python"
	display_txt_file_sizes(target_dir)
