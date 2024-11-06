from sqlalchemy.types import UserDefinedType

class Direccion(UserDefinedType):
    def get_col_spec(self):
        return "direccion"

    def bind_processor(self, dialect):
        def process(value):
            if value is not None:
                # Usar formateo manual para asegurarse de que no hay comillas adicionales
                calle = value['calle']
                ciudad = value['ciudad']
                estado = value['estado']
                codigo_postal = value['codigo_postal']
                
                # Evita las comillas escapadas
                return f'({calle}, {ciudad}, {estado}, {codigo_postal})'
            return None
        return process

    def result_processor(self, dialect, coltype):
        def process(value):
            if value is not None:
                # Eliminar los paréntesis inicial y final y dividir por comas
                calle, ciudad, estado, codigo_postal = value[1:-1].split(",")
                return {
                    "calle": calle.strip().strip('"'),
                    "ciudad": ciudad.strip().strip('"'),
                    "estado": estado.strip().strip('"'),
                    "codigo_postal": codigo_postal.strip().strip('"')
                }
            return None
        return process
