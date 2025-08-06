class DataForTests:
    def __init__(self):
        self.text_pruduct_menu: list[str] = []
        self.sorting_options: list[tuple[str, list[str]]] = []

        self.text_pruduct_menu = [
            "All Items",
            "About",
            "Logout",
            "Reset App State",
        ]

        self.sorting_options = [
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
