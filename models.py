import db
from sqlalchemy import Column, Integer, String, DateTime


class GestorTareas(db.Base):
    __tablename__ = "tarea"
    id = Column(Integer, primary_key=True)
    tarea = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    fechalimite = Column(DateTime, nullable=False)
    estado = Column(String, default="En Proceso")

    def __init__(self, tarea, categoria, fechalimite, estado):
        self.tarea = tarea
        self.categoria = categoria
        self.fechalimite = fechalimite
        self.estado = estado

    def __str__(self):
        return "Tarea(ID: {}, Tarea:{}, Categoria:{}, Fecha Limite:{}, Estado:{})".format(self.id, self.tarea,
                                                                                          self.categoria,
                                                                                          self.fechalimite, self.estado)
