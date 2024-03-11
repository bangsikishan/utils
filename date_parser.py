import logging
from datetime import datetime

import dateparser


def parse_date(date: str) -> str:
    """
        Parse a given date string and return it in the format "MM/DD/YYYY".

        Args:
            date (str): The date string to parse.

        Returns:
            str: The parsed date string in the format "MM/DD/YYYY". If the date string is invalid, "Invalid Date" is returned.

        Example:
            parse_date("2023-12-25")
    """
    try:
        parsed_date: datetime | None = dateparser.parse(date)

        return parsed_date.strftime("%m/%d/%Y") if parsed_date else "Invalid Date"
    except ValueError:
        logging.error(f"[-] Error while parsing date {date}!")
