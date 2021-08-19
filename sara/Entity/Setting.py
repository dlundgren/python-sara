from sara.Entity import db


class Setting(db.Model):
    """
    This operates on the main database.
    """
    __tablename__ = 'config_settings'

    namespace = db.Column(db.String(64), primary_key=True)
    group = db.Column(db.String(64), primary_key=True)
    key = db.Column(db.String(255), primary_key=True)
    type = db.Column(db.String(24), nullable=False)
    value = db.Column(db.LargeBinary, nullable=False)
