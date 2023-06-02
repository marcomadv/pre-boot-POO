from settings import BOARD_LENGTH

class LinearBoard():
    """
    Clase que represnta un tablero de una sola columna
    x - un jugador
    o - otro jugador
    None - espacio vacio
    """
    def __init__(self):
        """
        Una lista de None 
        """
        self._column = [None for i in range(BOARD_LENGTH)]
    
    def add(self, char):
        """
        Juega en la primera posicion disponible
        """
        # siempre y cuando no este lleno...
        if not self.is_full():
            # buscamos la primera posicion libre (None)
            i = self._column.index(None)
            # lo sustituimos por char
            self._column[i] = char

    def is_full(self):
        return self._column[-1] != None

    def is_victory(self, char):
        return False
    
    def is_tie(self, char1, char2):
        """
        no hay victoria ni de char1 ni de char2
        """
        return (self.is_victory('x') == False) and (self.is_vicrory('o') == False)