import database as _db


def create_database():
  return _db.Base.metadata.create_all(bind=_db.engine)
