import logging
from datetime import datetime


def check_date(date: str) -> bool:
    """
        Checks if the given date is in the past.

        Args:
            date (str): The date to be checked in the format "MM/DD/YYYY".

        Returns:
            bool: True if the date is in the past, False otherwise.

        Example:
            check_date("01/01/2023")
    """
    try:
        input_date: datetime = datetime.strptime(date, "%m/%d/%Y")

        current_date: datetime = datetime.now()

        return input_date < current_date
    except ValueError:
        logging.error(f"[-] Invalid input {date} while checking date!")
