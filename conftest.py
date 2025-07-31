from dotenv import load_dotenv

load_dotenv()


pytest_plugins: list[str] = [
    'fixtures.page',
    'fixtures.auth_page',
    'fixtures.logger'
]