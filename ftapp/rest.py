from flask import Blueprint
from flask import request
from flask_restful import Api
from flask_restful import Resource
from flask_restful import abort
from psycopg2.extras import RealDictCursor

from .db import get_db


class MainResource(Resource):

    def get(self, id):
        db = get_db()
        params = (id,)
        with db.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM hello WHERE id = %s", params)
            res = cur.fetchone()
            if not res:
                abort(404)
        return res

    def post(self):
        data = request.get_json()
        if not data:
            abort(400)

        try:
            params = (data['value'], )
        except KeyError:
            abort(400)

        db = get_db()
        with db.cursor() as cur:
            cur.execute("INSERT INTO hello (value) VALUES (%s) RETURNING id", params)
            id = cur.fetchone()[0]
            db.commit()
        return {'id': id}

    def put(self, id):
        data = request.get_json()
        if not data:
            abort(400)

        try:
            params = (data['value'], id)
        except KeyError:
            abort(400)

        db = get_db()
        with db.cursor() as cur:
            cur.execute("UPDATE hello SET value=%s WHERE id=%s", params)
            db.commit()
            c = cur.rowcount
        return {'success': c}


blueprint = Blueprint('api', __name__)
api = Api(blueprint)
api.add_resource(MainResource,
                 '/hello/',
                 '/hello/<int:id>')
