"""Создание таблицы компаний."""

from yoyo import step


__depends__ = {}

steps = [
    step(
        """CREATE TABLE companies (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL UNIQUE,
            stock_name VARCHAR(255) NOT NULL UNIQUE
        );
        """
    )
]
