"""
config.py
Parametros de configuracion del nodo de telemetria.
Todo lo que puede cambiar entre una instalacion y otra vive aqui.
Ningun otro archivo del proyecto debe contener un numero literal.

Unidad 2 - Programacion en Python para sistemas IoT
Facultad de Ingenieria de Sistemas Computacionales - UTP
"""

import os

# --------------------------------------------------------------------------
# Identificacion del nodo
# --------------------------------------------------------------------------

NODO = "laptop-lab3"
UBICACION = "Laboratorio 3 - FISC"

# --------------------------------------------------------------------------
# Periodos de muestreo, en segundos.
# Cada metrica tiene el suyo: leer los procesos es caro, leer la CPU no.
# --------------------------------------------------------------------------

PERIODO_RAPIDO = 1.0
PERIODO_LENTO = 5.0
PERIODO_REPORTE = 30.0
REFRESCO_MS = 200

# --------------------------------------------------------------------------
# Umbrales. Dos valores por metrica: uno para entrar en alarma y otro,
# mas bajo, para salir de ella. Esa diferencia es la HISTERESIS y evita
# que una lectura oscilando en el limite genere decenas de eventos falsos.
# --------------------------------------------------------------------------

CPU_ALTO = 70.0
CPU_BAJO = 50.0
CPU_NUCLEO_SATURADO = 90.0

RAM_ALTA = 85.0
RAM_BAJA = 75.0

DISCO_LLENO = 90.0
DISCO_ALIVIADO = 85.0

RED_PICO_KBS = 500.0
RED_CALMA_KBS = 200.0

BATERIA_BAJA = 20.0
BATERIA_RECUPERADA = 30.0

PROCESO_PESADO = 50.0

# Variacion brusca entre dos muestras consecutivas: evento de anomalia.
SALTO_ANOMALO = 40.0

# --------------------------------------------------------------------------
# Ventana movil y almacenamiento
# --------------------------------------------------------------------------

VENTANA = 10
MAX_EVENTOS_LOG = 200
ARCHIVO_BITACORA = "bitacora.json"

# --------------------------------------------------------------------------
# Unidad de disco a vigilar. Se detecta sola segun el sistema operativo.
# --------------------------------------------------------------------------

UNIDAD_DISCO = "C:\\" if os.name == "nt" else "/"

# Cantidad de procesos que se muestran en el ranking.
TOP_PROCESOS = 8

# Procesos del sistema que no vale la pena reportar.
PROCESOS_IGNORADOS = (
    "kworker", "kthread", "ksoftirqd", "migration",
    "rcu_", "irq/", "svchost"
)

# --------------------------------------------------------------------------
# LABORATORIO - Alertas sonoras y supervision de conexion
# --------------------------------------------------------------------------

# LABORATORIO: modo silencioso para trabajar en el salon.
MODO_SILENCIOSO = False

# LABORATORIO: control del reproductor no bloqueante.
INTERVALO_ALERTAS = 1.0
MAX_COLA_ALERTAS = 20

# LABORATORIO: comprobacion y recordatorio de conexion.
PERIODO_CONEXION = 3.0
RECORDATORIO_RED = 30.0
HOST_PRUEBA_RED = "8.8.8.8"
PUERTO_PRUEBA_RED = 53
TIMEOUT_RED = 0.35

# LABORATORIO: sonidos centralizados.
CARPETA_SONIDOS = "sonidos"
SONIDOS = {
    "cpu_alta": "cpu_alta.wav",
    "ram_alta": "ram_alta.wav",
    "red_pico": "red_pico.wav",
    "red_desconectada": "red_desconectada.wav",
    "red_conectada": "red_conectada.wav",
    "red_sigue_desconectada": "red_sigue_desconectada.wav",
}
