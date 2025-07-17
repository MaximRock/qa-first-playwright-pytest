import os
import config

from dotenv import load_dotenv

load_dotenv()

class Environment:

    def __init__(self) -> None:
        self.env = os.getenv('ENV', config.url.SHOT)


    def get_base_url(self) -> str:
        if self.env in config.url.urls:
            return config.url.urls[self.env]
        raise Exception(f'Invalid environment {self.env}')