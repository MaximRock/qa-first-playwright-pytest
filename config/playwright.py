import os
from dotenv import load_dotenv

load_dotenv()

class Playwright:
    PAGE_VIEWPORT_SIZE = {'width': 900, 'height': 768}
    BROWSER = os.getenv('BROWSER', 'chrome')
    IS_HEADLESS = os.getenv('HEADLESS', 'false').lower() == 'true'
    SLOW_MO = int(os.getenv('SLOW_MO', '50'))
    LOCALE = 'en-US'

