"""Detector de conexion agregado para el Laboratorio 1."""
import socket
import time
import config

# LABORATORIO
_estado_anterior = None
_desde_desconexion = None
_ultimo_recordatorio = None

def hay_conexion():
    # LABORATORIO: no altera sensores/red.py; solo prueba alcance de red.
    try:
        with socket.create_connection(
            (config.HOST_PRUEBA_RED, config.PUERTO_PRUEBA_RED),
            timeout=config.TIMEOUT_RED
        ):
            return True
    except OSError:
        return False

def detectar(ahora=None, conectado=None):
    """Genera eventos por flanco y recordatorio temporal."""
    # LABORATORIO
    global _estado_anterior, _desde_desconexion, _ultimo_recordatorio
    ahora = time.time() if ahora is None else ahora
    conectado = hay_conexion() if conectado is None else conectado
    eventos = []

    if _estado_anterior is None:
        _estado_anterior = conectado
        if not conectado:
            _desde_desconexion = ahora
            _ultimo_recordatorio = ahora
            eventos.append(("red_desconectada", {"segundos": 0}))
        return eventos

    if conectado != _estado_anterior:
        _estado_anterior = conectado
        if conectado:
            duracion = 0 if _desde_desconexion is None else ahora - _desde_desconexion
            eventos.append(("red_conectada", {"segundos": round(duracion, 1)}))
            _desde_desconexion = None
            _ultimo_recordatorio = None
        else:
            _desde_desconexion = ahora
            _ultimo_recordatorio = ahora
            eventos.append(("red_desconectada", {"segundos": 0}))
        return eventos

    if not conectado and _ultimo_recordatorio is not None:
        if ahora - _ultimo_recordatorio >= config.RECORDATORIO_RED:
            _ultimo_recordatorio = ahora
            duracion = ahora - (_desde_desconexion or ahora)
            eventos.append(("red_sigue_desconectada", {"segundos": round(duracion, 1)}))

    return eventos

def reiniciar():
    # LABORATORIO: apoyo para pruebas unitarias.
    global _estado_anterior, _desde_desconexion, _ultimo_recordatorio
    _estado_anterior = None
    _desde_desconexion = None
    _ultimo_recordatorio = None
