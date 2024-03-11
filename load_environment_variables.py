import logging
import os

from dotenv import load_dotenv


def load_environment_variables(env_file_path: str) -> dict:
    """
        Loads environment variables from the given .env file and returns them as a dictionary.

        Args:
            env_file_path (str): Path to the .env file that contains the environment variables.

        Returns:
            dict: Dictionary containing all the environment variables read from the .env file.

        Example:
            env_vars = load_environment_variables("/path/to/.env")
            print(env_vars["ECGAINS"])
    """
    try:
        load_dotenv(env_file_path)  # Load environment variables from the .env file
    except FileNotFoundError:
        logging.error(f"The .env file '{env_file_path}' was not found!")

    return {
        "ECGAINS": os.getenv("ECGAINS"),
        "MODULE_NAME": os.getenv("MODULE_NAME"),
        "MAIN_URL": os.getenv("MAIN_URL"),
        "EXECUTABLE_PATH": os.getenv("EXECUTABLE_PATH"),
        "DOWNLOAD_PATH": os.getenv("DOWNLOAD_PATH"),
        "SERVER_PATH": os.getenv("SERVER_PATH"),
        "JSON_PATH": os.getenv("JSON_PATH"),
        "BROWSER_TYPE": os.getenv("BROWSER_TYPE"),
        "SMI_DATA_URL": os.getenv("SMI_DATA_URL"),
        "SMI_RECORD_URL": os.getenv("SMI_RECORD_URL"),
        "REGION_NAME": os.getenv("REGION_NAME"),
        "ENDPOINT_URL": os.getenv("ENDPOINT_URL"),
        "AWS_ACCESS_KEY_ID": os.getenv("AWS_ACCESS_KEY_ID"),
        "AWS_SECRET_ACCESS_KEY": os.getenv("AWS_SECRET_ACCESS_KEY")
    }
