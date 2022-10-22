driver_options = [
    "--headless",
    "--no-sandbox",
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    "--window-size=1200x1000",
    "--disable-blink-features=AutomationControlled"
]

mysql_db = {
    'host' : '192.168.98.19',
    'port' : 14102, 
    'user' : 'web',
    'password' : 'web'
}

sites = {
    'mvideo' : {
        'main_page_url' : 'mvideo.ru',
        'catalogue_element_xpath' : "//div[contains(@class, '{}')]",
        'catalogue_list_item_class' : '', 
        'item_element_class_name' : 'product-cards-layout__item',
        'items_screenshots_path' : './images/mvideo/',
        'item_parameters_class' : {
            'item_title_container_class' :  'product-title__text',
            'item_rating_container_class' : 'ng-star-inserted',
            'item_feedback_container_class' : 'product-rating__feedback',
            'item_price_container_class' : 'price__main-value',
            'item_bonus_value_class' : 'mbonus-block__caption'
        },

    },
    'set-tehniki'  : {
        'main_page_url' : 'https://set-tehniki.com/',
        'catalogue_element_xpath' : "//ul[contains(@class, 'nav-catalog')]",
        'catalogue_list_item_xpath' : "//a[contains(@class, 'next-level-menu__link')]",
        'item_element_class_name' : 'product',
        'items_screenshots_path' : './images/set-tehniki/',
        'item_parameters_class' : {
            'item_title_container_class' :  'product-footer__name',
            'item_price_container_class' : 'product-price__current'
        },
    'frontime'  : {
        'main_page_url' : 'https://set-tehniki.com/',
        'catalogue_element_xpath' : "//div[contains(@class,'c-big-catalog__links')]",
        'catalogue_list_item_xpath' : "//div[contains(@class,'c-big-catalog__links')]/span/a",
        'item_element_class_name' : 's-product-wrapper',
        'items_screenshots_path' : './images/frontime/',
        'item_parameters_class' : {
            'item_title_container_class' :  's-product-header',
            'item_price_container_class' : 's-price'
        }
    }
    }
}