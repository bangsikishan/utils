import logging
import os


def setup_logger(log_save_directory: str, log_file_name: str) -> None:
    """
        Set up logging configuration with the specified log save directory and file name.

        Args:
            log_save_directory (str): The directory where the log file will be saved.
            log_file_name (str): The name of the log file.

        Returns:
            None

        Example:
            setup_logger(log_save_directory='/path/to/logs', log_file_name='example.log')
    """
    try:
        logging.basicConfig(
            filename=os.path.join(log_save_directory, log_file_name),
            level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    except OSError as e:
        logging.error(f"An error occurred creating the log file: {e}")
