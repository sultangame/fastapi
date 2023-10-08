from sqlalchemy.orm import (
    DeclarativeBase, mapped_column, Mapped, declared_attr
)


class Base(DeclarativeBase):
    __abstarct__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}"

    id: Mapped[int] = mapped_column(primary_key=True)
