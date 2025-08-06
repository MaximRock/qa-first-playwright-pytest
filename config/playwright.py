import os

from dotenv import load_dotenv

load_dotenv()


class Playwright:
    def __init__(self) -> None:
        self.PAGE_VIEWPORT_SIZE = {"width": 900, "height": 768}
        self.BROWSER = os.getenv("BROWSER", "chrome")
        self.IS_HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
        self.SLOW_MO = int(os.getenv("SLOW_MO", "50"))
        self.LOCALE = "en-US"
