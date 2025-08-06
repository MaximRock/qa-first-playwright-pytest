class Products:
    PRODUCTS_TITLE: str = '[data-test="title"]'
    PRODUCTS_BURGER_MENU_BTN: str = "#react-burger-menu-btn"
    PRODUCTS_CLOSE_BURGER_MENU_BTN: str = "//div[@class='bm-cross-button']"
    PRODUCTS_MENU: str = ".bm-menu>.bm-item-list>a"
    PROD_ADD_CART_BTN: str = "//button[contains(text(), 'Add to cart')]"
    PROD_ITEMS_LIST: str = "//div[@class='inventory_item_description']/div/a"
    BACK_TO_PRODUCTS_BTN: str = "//button[contains(text(), 'Back to products')]"
    PRODUCTS_CART_BADGE: str = "span.shopping_cart_badge"
    PROD_ITEM_ADD_TO_CART: str = "#add-to-cart"
    PROD_DROPDOWN_SELECT: str = "//select[@class='product_sort_container']"
