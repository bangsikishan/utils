import hashlib
import logging


def generate_md5_hash(bid_id: str, ecgain: str, file_name: str) -> str:
    """
        Generates an MD5 hash based on the given parameters.

        Args:
            bid_id (str): The bid_id value to include in the hash.
            ecgain (str): The ecgain value to include in the hash.
            file_name (str): The filename value to include in the hash.

        Returns:
            str: The MD5 hash as a hexadecimal string.

        Example:
            generate_md5_hash("12345", "67890", "example.txt")
    """
    try:
        return hashlib.md5(f"{ecgain}{bid_id}{file_name}".encode("utf-8")).hexdigest()
    except ValueError:
        logging.error(f"[-] Invalid input parameters!")
