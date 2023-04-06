def apply_migrations():
    from yoyo import read_migrations, get_backend
    # TODO: Сделать получение стринги коннекта из yoyo.ini
    backend = get_backend(
        'postgresql://postgres:321@192.168.220.5:6888/postgres'
    )
    migrations = read_migrations('./migrations')
    backend.apply_migrations(backend.to_apply(migrations))
