from dotenv import load_dotenv

load_dotenv()


class Url:
    SHOT: str = "shot"
    PROD: str = "prod"

    def __init__(self):
        self.urls: dict[str, str] = {
            self.SHOT: "https://www.saucedemo.com/",
            self.PROD: "https://google.com/",
        }
