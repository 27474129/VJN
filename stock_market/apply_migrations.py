from yoyo import read_migrations, get_backend

from backend.config import CONNECTION_STRING


def apply_migrations():
    backend = get_backend(CONNECTION_STRING)
    migrations = read_migrations('./migrations')
    backend.apply_migrations(backend.to_apply(migrations))
