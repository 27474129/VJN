import logging
import json
from typing import Dict, Any

import tornado.web

from ..constants import *
from .db import CompaniesModel


logger = logging.getLogger(__name__)


class BaseHandler(tornado.web.RequestHandler):
    args_desc: Dict[str, Dict[str, Any]] = {}
    _args: Dict[str, Any] = {}

    def _check_args(self):
        for arg in self.args_desc:
            if self.args_desc[arg]['required'] and arg not in self._args:
                self.response['warnings'].append(
                    WARN_NO_REQUIRED_ARG.format(arg)
                )
            elif (
                arg in self._args and
                type(self._args[arg]) != self.args_desc[arg]['type']
            ):
                self.response['warnings'].append(
                    WARN_INVALID_ARG_TYPE.format(
                        arg, self.args_desc[arg]['type']
                    )
                )

    def _serialize_args(self):
        if self.request.method == 'GET':
            for key in self.request.arguments:
                serialized_value = json.loads(self.request.arguments[key][0])
                self._args[key] = serialized_value
            return

        self._args = json.loads(self.request.body)

    def _begin(self):
        self.response: dict = {
            'rows': {},
            'warnings': [],
            'errors': []
        }
        self._serialize_args()
        self._check_args()

        if self.response['warnings']:
            self.set_status(BAD_REQUEST_STATUS_CODE)

    async def get(self):
        self._begin()

    async def post(self):
        self._begin()

    async def put(self):
        self._begin()

    async def patch(self):
        self._begin()

    async def delete(self):
        self._begin()


class CompaniesHandler(BaseHandler):
    model_class = CompaniesModel

    args_desc: Dict[str, Dict[str, Any]] = {
        'name': {
            'required': True,
            'type': str
        },
        'stock_name': {
            'required': True,
            'type': str
        }
    }

    async def post(self):
        await super().post()
        if self.get_status() == BAD_REQUEST_STATUS_CODE:
            self.write(self.response)
            return

        await self.model_class().insert(self._args)
        self.write(self.response)
