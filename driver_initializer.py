import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.remote.webdriver import WebDriver


def initialize_webdriver(
        browser_type: str,
        executable_path: str,
        download_path: str = None,
        is_headless: bool = True,
        proxy_address: str = None
) -> WebDriver:
    """
        Initialize a WebDriver instance based on the specified browser type.

        Args:
            browser_type (str): The type of browser to use (e.g., 'chrome', 'edge').
            executable_path (str): The path to the browser driver executable.
            download_path (str, optional): The directory path for downloads. Defaults to None.
            is_headless (bool, optional): Whether to run the browser in headless mode. Defaults to True.
            proxy_address (str, optional): The proxy address to use. Defaults to None.

        Returns:
            WebDriver: A WebDriver instance based on the specified browser type.

        Example:
            initialize_webdriver(browser_type='chrome', executable_path='/path/to/chromedriver.exe')
    """
    try:
        if browser_type.lower() == "edge":
            options = EdgeOptions()
            service = EdgeService(executable_path=executable_path)
        else:
            options = ChromeOptions()
            service = ChromeService(executable_path=executable_path)

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--log-level=3")
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/113.0.5666.197 Safari/537.36")

        if download_path:
            download_prefs = {
                "download.default_directory": download_path,
                "download.prompt_for_download": False
            }
            options.add_experimental_option("prefs", download_prefs)

        if is_headless:
            options.add_argument("--headless")

        if proxy_address:
            proxy = Proxy()
            proxy.proxy_type = ProxyType.MANUAL
            proxy.http_proxy = proxy_address
            options.add_argument(f"--proxy-server={proxy_address}")

        if browser_type.lower() == "edge":
            return webdriver.Edge(options=options, service=service)
        else:
            return webdriver.Chrome(options=options, service=service)
    except Exception as e:
        logging.error(f"An error occurred while initializing web driver: {e}")
