def init_url_dict():
    url_dict = {
        'product_url': None,
        'n_reviews': None,
        'product_name': None,
        'product_price': None,
        'mean_rating': None
    }
    return url_dict


def init_product_dict():
    product_dict = {
        'product_name': None,
        'product_information': None,
        'product_availability': None,  # div[class="stock-level h-display-ib u-nudge-top h-third-l"]
        'product_price': None,
        'n_reviews': None
    }
    return product_dict


def init_reviews_dict():
    reviews_dict = {
        'review_rating': None,
        'review_title': None,
        'review_author': None,
        'review_date': None,
        'review_text': None,
    }
    return reviews_dict
