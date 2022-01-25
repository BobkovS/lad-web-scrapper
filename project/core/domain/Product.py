from project.core.dbLayer import product_obj, product_stats, scraping_obj


class Product:
    def __init__(self, title, amount, price):
        self.title = title
        self.amount = amount
        self.price = price

    def save(self, scraping_datetime):
        if product_obj.fetch(self.title) is None:
            product_obj.push(self.title)

        product_id = product_obj.fetch(self.title).id
        scraping_id = scraping_obj.fetch(scraping_datetime).id

        product_stats.push(product_id, scraping_id, self.amount, self.price)
