from dotenv import load_dotenv

load_dotenv()

class Url:

    SHOT = 'shot'
    PROD = 'prod'
    
    urls = {
        SHOT: 'https://www.saucedemo.com/',
        PROD: 'https://google.com/',
    }