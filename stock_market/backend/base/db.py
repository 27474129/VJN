from typing import List, Dict, Any

from ..postgres.postgres_conn import PostgresConn


class BaseModel:
    table_name = ''

    fields = ''

    registry_query = f"""SELECT * FROM {table_name};"""

    async def get_registry(self) -> List[Dict[str, Any]]:
        async with PostgresConn() as conn:
            registry = conn.fetch(self.registry_query)

            parsed_registry = []
            for row in registry:
                parsed_registry.append(dict(row))

            return parsed_registry

    async def insert(self, data: Dict[str, Any]):
        fields = ''
        values = ''
        for field in data:
            if field in self.fields:
                fields += f'{field}, '
                values += f"'{data[field]}', "

        query = f"""
        INSERT INTO {self.table_name} 
            ({fields[:-2]})
        VALUES 
            ({values[:-2]});
        """

        async with PostgresConn() as conn:
            await conn.fetch(query)


class CompaniesModel(BaseModel):
    table_name = 'companies'

    fields = 'id, name, stock_name'
