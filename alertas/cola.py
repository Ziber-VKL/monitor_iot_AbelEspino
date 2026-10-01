"""Cola FIFO de alertas sonoras."""
from collections import deque
import config

# LABORATORIO: deque evita bloquear el ciclo mientras esperan sonidos.
_cola = deque(maxlen=config.MAX_COLA_ALERTAS)

def encolar(evento):
    # LABORATORIO
    if evento in config.SONIDOS:
        _cola.append(evento)
        return True
    return False

def siguiente():
    # LABORATORIO
    return _cola.popleft() if _cola else None

def pendientes():
    # LABORATORIO
    return len(_cola)

def limpiar():
    # LABORATORIO
    _cola.clear()
