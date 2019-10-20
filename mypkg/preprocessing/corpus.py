from itertools import chain
from pathlib import Path

from sqlalchemy.orm.session import Session

from mypkg.database.model import Document


def import_corpora(db_session: Session, dir_corpus: Path) -> None:

    mappings = []
    for dest_corpus in dir_corpus.glob('**/*'):
        with dest_corpus.open(mode='r') as f:
            mapping = {
                'name': str(dest_corpus),
                'content': ' '.join(chain.from_iterable((line.split(' ') for line in f.read().splitlines())))
            }
            mappings.append(mapping)

    db_session.execute(Document.__table__.insert(), mappings)
    db_session.commit()
