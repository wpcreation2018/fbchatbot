import random

remote_img_urls = {
    'img_cod'       : 'https://i.ibb.co/crCJnNV/cod.png',
    'img_discount'  : 'https://i.ibb.co/jT7wvYf/TPL-12-12-1920x1080.jpg',
    'img_claim'     : 'https://i.ibb.co/bbVQ8Hy/claim.png',
    'img_transfer'  : random.choice([
        'https://i.ibb.co/L5JnvXV/transfer-1.jpg',
        'https://i.ibb.co/dJ5wKF5/transfer-2.jpg',
        'https://i.ibb.co/LC2LKmR/transfer-3.jpg',
        'https://i.ibb.co/Wy9Zxr8/transfer-4.jpg',
        'https://i.ibb.co/rbPzT6g/transfer-5.jpg',
    ]),
    'img_thxq'      : 'https://i.ibb.co/6R9Hs0X/thxq.png'
}

local_img_urls = {
    'img_cod'       : 'imgs/cod.png',
    'img_discount'  : 'imgs/discount.jpg',
    'img_claim'     : 'imgs/claim.png',
    'img_transfer'  : random.choice([
        'imgs/transfer-1.jpg',
        'imgs/transfer-2.jpg',
        'imgs/transfer-3.jpg',
        'imgs/transfer-4.jpg',
        'imgs/transfer-5.jpg',
    ]),
    'img_thxq'      : 'imgs/thxq.png'
}

tpl_urls = {
    'home_page'     : 'https://fashion.theperfectladies.com/',
    'shop_page'     : 'https://fashion.theperfectladies.com/shop/',
    'bigsize_page'  : 'https://fashion.theperfectladies.com/product-category/bigsize/',
}
