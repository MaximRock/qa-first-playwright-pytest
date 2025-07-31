class DataForTests:

    text_pruduct_menu: list[str] = ["All Items", "About", "Logout", "Reset App State"]

    SORTING_OPTIONS = [
        (
            "az",
            [
                "Sauce Labs Backpack",
                "Sauce Labs Bike Light",
                "Sauce Labs Bolt T-Shirt",
                "Sauce Labs Fleece Jacket",
                "Sauce Labs Onesie",
                "Test.allTheThings() T-Shirt (Red)",
            ],
        ),
        (
            "za",
            [
                "Test.allTheThings() T-Shirt (Red)",
                "Sauce Labs Onesie",
                "Sauce Labs Fleece Jacket",
                "Sauce Labs Bolt T-Shirt",
                "Sauce Labs Bike Light",
                "Sauce Labs Backpack",
            ],
        ),
        (
            "hilo",
            [
                "Sauce Labs Fleece Jacket",
                "Sauce Labs Backpack",
                "Sauce Labs Bolt T-Shirt",
                "Test.allTheThings() T-Shirt (Red)",
                "Sauce Labs Bike Light",
                "Sauce Labs Onesie",
            ],
        ),
        (
            "lohi",
            [
                "Sauce Labs Onesie",
                "Sauce Labs Bike Light",
                "Sauce Labs Bolt T-Shirt",
                "Test.allTheThings() T-Shirt (Red)",
                "Sauce Labs Backpack",
                "Sauce Labs Fleece Jacket",
            ],
        ),
    ]


# ["$7.99", "$9.99", "$15.99", "$15.99", "$29.99", "$49.99"]
# ["$49.99", "$29.99", "$15.99", "$15.99", "$9.99", "$7.99"]
