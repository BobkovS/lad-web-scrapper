from project.core import application_db


class ProductObj(application_db.Model):
    id = application_db.Column(application_db.Integer, primary_key=True)
    title = application_db.Column(application_db.String, unique=True, nullable=False)

    product_stats = application_db.relationship('ProductStats', back_populates="product_obj")

    @staticmethod
    def push(title):
        application_db.session.add(ProductObj(title=title))
        application_db.session.commit()

    def fetch(self, title):
        return self.query.filter_by(title=title).first()