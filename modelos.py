from typing import List
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Sala(Base):
    __tablename__ = 'sala'
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    capacidad: Mapped[int] = mapped_column(nullable=False)
    disponible: Mapped[bool] = mapped_column(default=True)
    reservas: Mapped[List["Reserva"]] = relationship(back_populates="sala")

class Reserva(Base):
    __tablename__ = 'reserva'
    id: Mapped[int] = mapped_column(primary_key=True)
    estudiante: Mapped[str] = mapped_column(String(100), nullable=False)
    sala_id: Mapped[int] = mapped_column(ForeignKey('sala.id'), nullable=False)
    fecha: Mapped[str] = mapped_column(String(10), nullable=False)
    sala: Mapped["Sala"] = relationship(back_populates="reservas")