import argparse
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker

from mypkg.database.model import Base
from mypkg.preprocessing.corpus import import_corpora
from mypkg.util.config import Config


def main() -> None:

    parser = argparse.ArgumentParser()
    parser.add_argument('-d',
                        '--dir-corpus',
                        type=str,
                        required=True,
                        metavar='DIR',
                        help='Directory which contains corpus files')
    parser.add_argument('-c',
                        '--config',
                        type=str,
                        required=False,
                        default='config.toml',
                        metavar='FILE',
                        help='Path to config file (default: `config.toml`)')

    args = parser.parse_args()
    config = Config(args.config)

    engine = create_engine(config.db.uri)
    Base.metadata.create_all(engine)
    SessionMaker = sessionmaker(bind=engine)
    db_session = SessionMaker()

    import_corpora(db_session, Path(args.dir_corpus))
