"""Создание таблицы компаний."""

from yoyo import step


__depends__ = {}

steps = [
    step(
        """CREATE TABLE IF NOT EXISTS companies (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL UNIQUE,
            stock_name VARCHAR(255) NOT NULL UNIQUE
        );
        """
    ),
    # Заполнение таблицы
    step(
        """INSERT INTO companies
            (name, stock_name)
        VALUES
            ('Apple', 'AAPL'),
            ('International Business Machines Corporation', 'IBM'),
            ('MSFT', 'Microsoft Corporation Common Stock'),
            ('GOOG', 'Alphabet Inc. Class C Capital Stock'),
            ('AMZN', 'Amazon.com, Inc. Common Stock'),
            ('GOOGL', 'Alphabet Inc. Class A Common Stock'),
            ('NVDA', 'NVIDIA Corporation Common Stock'),
            ('TSLA', 'Tesla, Inc. Common Stock'),
            ('V', '	Visa Inc.'),
            ('NVO', 'Novo Nordisk A/S Common Stock')
        ON CONFLICT DO NOTHING;
        """
    )
]
