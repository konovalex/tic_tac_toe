class FieldIndexError(IndexError):
    """Если вышли за границу игрового поля - выбрасывает исключение"""

    def __str__(self):
        return 'Введено значение за границами игрового поля'


class CellOccupiedError(ValueError):
    """Если выбранная ячейка занята - выбрасывает исключение"""

    def __str__(self):
        return 'Попытка изменить занятую ячейку'
