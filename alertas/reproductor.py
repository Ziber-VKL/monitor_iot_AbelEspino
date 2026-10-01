"""Reproductor no bloqueante basado en cola y marcas de tiempo."""
import os
import time
import config
from .cola import siguiente

# LABORATORIO
_ultima_reproduccion = 0.0

def _ruta(nombre):
    # LABORATORIO
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, config.CARPETA_SONIDOS, config.SONIDOS[nombre])

def _reproducir(evento):
    # LABORATORIO: winsound con SND_ASYNC retorna inmediatamente.
    if config.MODO_SILENCIOSO:
        return
    try:
        if os.name == "nt":
            import winsound
            winsound.PlaySound(_ruta(evento), winsound.SND_FILENAME | winsound.SND_ASYNC)
        else:
            print("\a", end="", flush=True)
    except Exception:
        pass

def actualizar(ahora=None):
    """Reproduce como maximo una alerta cuando corresponde; nunca espera."""
    # LABORATORIO
    global _ultima_reproduccion
    ahora = time.time() if ahora is None else ahora
    if ahora - _ultima_reproduccion < config.INTERVALO_ALERTAS:
        return None
    evento = siguiente()
    if evento is None:
        return None
    _reproducir(evento)
    _ultima_reproduccion = ahora
    return evento
