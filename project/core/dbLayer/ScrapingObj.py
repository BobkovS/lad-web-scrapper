from project.core import application_db


class ScrapingObj(application_db.Model):
    id = application_db.Column(application_db.Integer, primary_key=True)
    datetime = application_db.Column(application_db.DateTime)

    product_stats = application_db.relationship('ProductStats', back_populates="scraping_obj")

    @staticmethod
    def push(datetime):
        application_db.session.add(ScrapingObj(datetime=datetime))
        application_db.session.commit()

    def fetch(self, datetime):
        return self.query.filter_by(datetime=datetime).first()
