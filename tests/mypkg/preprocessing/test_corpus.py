from pathlib import Path

from sqlalchemy.orm.session import Session

from mypkg.database.model import Document
from mypkg.preprocessing.corpus import import_corpora


def test_import_corpora(db_session: Session) -> None:

    dir_corpora = Path('resources/corpora/lyrics')
    import_corpora(db_session, dir_corpora)
    result = db_session \
        .query(Document) \
        .first()
    assert result.content.startswith('Alas')
