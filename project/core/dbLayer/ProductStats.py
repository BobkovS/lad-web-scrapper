from project.core import application_db


class ProductStats(application_db.Model):
    id = application_db.Column(application_db.Integer, primary_key=True)
    product_id = application_db.Column(application_db.Integer, application_db.ForeignKey('product_obj.id'))
    scraping_id = application_db.Column(application_db.Integer, application_db.ForeignKey('scraping_obj.id'))
    amount = application_db.Column(application_db.Integer)
    price = application_db.Column(application_db.Float)

    product_obj = application_db.relationship('ProductObj', back_populates="product_stats")
    scraping_obj = application_db.relationship('ScrapingObj', back_populates="product_stats")

    @staticmethod
    def push(product_id, scraping_id, amount, price):
        application_db.session.add(ProductStats(
            product_id=product_id, scraping_id=scraping_id, amount=amount, price=price))
        application_db.session.commit()
