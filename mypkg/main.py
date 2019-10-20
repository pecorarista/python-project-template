import argparse
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker

from mypkg.preprocessing.corpus import import_documents


def main() -> None:

    parser = argparse.ArgumentParser()
    parser.add_argument('-d',
                        '--dir-corpus',
                        type=str,
                        required=True,
                        metavar='DIR',
                        help='Directory which contains corpus files')

    args = parser.parse_args()

    engine = create_engine(config.db_uri)
    Base.metadata.create_all(engine)
    SessionMaker = sessionmaker(bind=engine)
    db_session = SessionMaker()

    import_documents(session, dir_corpus)
