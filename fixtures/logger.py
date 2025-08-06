import logging

from config.project_path import PathManager


def pytest_configure(config):
    # Настройка формата логов
    # log_format = "%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s" #noqa
    log_format = "%(asctime)s | [%(levelname)s] %(name)s: %(message)s"
    formatter = logging.Formatter(log_format)

    # Создание директории для логов
    path_manager = PathManager()
    log_file = path_manager.create_file(
        path_manager.extract_path(path_manager.create_dir("logs")), "tests.log"
    )

    # Файловый обработчик (пишет в файл)
    file_handler = logging.FileHandler(log_file, mode="a")
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    # Консольный обработчик (выводит в терминал)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    # Настройка корневого логгера
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

    # Настройка логгера для Playwright (уменьшаем уровень шума)
    playwright_logger = logging.getLogger("playwright")
    playwright_logger.setLevel(logging.WARNING)
