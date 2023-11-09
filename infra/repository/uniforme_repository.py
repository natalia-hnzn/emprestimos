from infra.config.connection import DBConnectionHandler
from infra.entities.uniforme import Uniforme


class UniformeRepository:

    @staticmethod
    def select_uniforme_by_id(id_uniforme):
        with DBConnectionHandler() as db:
            data = db.session.query(Uniforme).filter(Uniforme.id == id_uniforme).first()
            return data

    @staticmethod
    def select_uniforme_by_name(name_uniforme):
        with DBConnectionHandler() as db:
            uniforme = db.session.query(Uniforme).filter(Uniforme.nome == name_uniforme).first()
            return uniforme

    @staticmethod
    def select_all_uniformes():
        with DBConnectionHandler() as db:
            uniforme = db.session.query(Uniforme).all()
            return uniforme



    @staticmethod
    def select_first_uniforme():
        with DBConnectionHandler() as db:
            data = db.session.query(Uniforme).first()
            return data

    @staticmethod
    def insert_many_uniformes(uniformes):
        with DBConnectionHandler() as db:
            db.session.add_all(uniformes)
            db.session.commit()


    @staticmethod
    def insert_one_uniforme(uniforme):
        with DBConnectionHandler() as db:
            db.session.add(uniforme)
            db.session.commit()

    @staticmethod
    def update_uniforme(uniforme):
        with DBConnectionHandler() as db:
            db.session.query(Uniforme).filter(Uniforme.id == uniforme.id).update({'nome': uniforme.nome})
            db.session.commit()

    @staticmethod
    def delete_uniforme(uniforme):
        with DBConnectionHandler() as db:
            db.session.query(Uniforme).filter(Uniforme.id == uniforme.id).update({'ativo': False})
            db.session.commit()

