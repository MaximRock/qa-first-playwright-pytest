class Auth:
    USERNAME_INPUT: str = "#user-name"
    PASSWORD_INPUT: str = "#password"  # noqa
    LOGIN_BTN: str = "#login-button"
    LOGIN_ERROR_TEXT: str = "//h3[text()='Epic sadface: Username is required']"
    LOGIN_ERROR: str = "//form/div[@class='error-message-container error']"
