import os


def rename_file(file_directory: str, file_name: str) -> tuple:
    """
        Rename a file in the specified directory.

        Args:
            file_directory (str): The directory where the file is located.
            file_name (str): The name of the file to be renamed.

        Returns:
            Tuple[str, str]: A tuple containing the original file name and the new renamed file name.

        Example:
            rename_file("path/to/directory", "example file.txt")
    """
    renamed_file_name: str = file_name.replace(" ", "+")

    if not os.path.exists(os.path.join(file_directory, renamed_file_name)):
        os.rename(
            src=os.path.join(file_directory, file_name),
            dst=os.path.join(file_directory, renamed_file_name)
        )

        return file_name, renamed_file_name

    root: str
    ext: str
    root, ext = os.path.splitext(renamed_file_name)

    for file_idx in range(1, len(os.listdir(file_directory)) + 1):
        renamed_file_name: str = f"{root}_{file_idx}{ext}"

        if os.path.exists(os.path.join(file_directory, renamed_file_name)):
            continue

        os.rename(
            src=os.path.join(file_directory, file_name),
            dst=os.path.join(file_directory, renamed_file_name)
        )

        return file_name, renamed_file_name
