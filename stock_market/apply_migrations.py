from yoyo import read_migrations, get_backend

from postgres_conn import PostgresConn


def apply_migrations():
    backend = get_backend(PostgresConn.connection_string)
    migrations = read_migrations('./migrations')
    backend.apply_migrations(backend.to_apply(migrations))
