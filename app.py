"""Texto a Voz: servidor local que convierte texto en audio con voces neurales de Microsoft.

Abre http://localhost:5050 en el navegador.
"""
import asyncio
import subprocess
import tempfile
import time
import uuid
from pathlib import Path

import edge_tts
import imageio_ffmpeg
from flask import Flask, abort, jsonify, request, send_file

PUERTO = 5050
CARPETA = Path(__file__).parent
SALIDA = Path(tempfile.gettempdir()) / "texto_a_voz"
SALIDA.mkdir(exist_ok=True)

VOCES = {
    "es-MX-DaliaNeural": "Dalia (mujer)",
    "es-MX-JorgeNeural": "Jorge (hombre)",
}
MAX_CARACTERES = 20000
HORAS_A_CONSERVAR = 6

app = Flask(__name__)


def limpiar_antiguos():
    limite = time.time() - HORAS_A_CONSERVAR * 3600
    for f in SALIDA.glob("*"):
        if f.stat().st_mtime < limite:
            f.unlink(missing_ok=True)


@app.get("/")
def inicio():
    return send_file(CARPETA / "index.html")


@app.get("/voces")
def voces():
    return jsonify([{"id": k, "nombre": v} for k, v in VOCES.items()])


@app.post("/generar")
def generar():
    datos = request.get_json(force=True)
    texto = (datos.get("texto") or "").strip()
    voz = datos.get("voz", "es-MX-DaliaNeural")
    volumen = int(datos.get("volumen", 0))

    if not texto:
        return jsonify(error="Escribe algún texto primero."), 400
    if len(texto) > MAX_CARACTERES:
        return jsonify(error=f"Máximo {MAX_CARACTERES} caracteres."), 400
    if voz not in VOCES:
        return jsonify(error="Voz no válida."), 400
    volumen = max(-50, min(50, volumen))

    limpiar_antiguos()
    ident = uuid.uuid4().hex
    mp3 = SALIDA / f"{ident}.mp3"
    comunicar = edge_tts.Communicate(texto, voz, volume=f"{volumen:+d}%")
    try:
        asyncio.run(comunicar.save(str(mp3)))
    except Exception as e:  # sin internet, etc.
        return jsonify(error=f"No se pudo generar el audio: {e}"), 502
    return jsonify(id=ident)


@app.get("/audio/<ident>")
def audio(ident):
    mp3 = SALIDA / f"{ident}.mp3"
    if not ident.isalnum() or not mp3.exists():
        abort(404)
    return send_file(mp3, mimetype="audio/mpeg")


@app.get("/descargar/<ident>")
def descargar(ident):
    formato = request.args.get("formato", "mp4")
    mp3 = SALIDA / f"{ident}.mp3"
    if not ident.isalnum() or not mp3.exists():
        abort(404)
    nombre = f"texto-a-voz-{time.strftime('%Y%m%d-%H%M%S')}"

    if formato == "mp3":
        return send_file(mp3, as_attachment=True, download_name=f"{nombre}.mp3")

    mp4 = SALIDA / f"{ident}.mp4"
    if not mp4.exists():
        ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
        subprocess.run(
            [ffmpeg, "-y", "-i", str(mp3), "-c:a", "aac", "-b:a", "192k", str(mp4)],
            check=True, capture_output=True,
            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
        )
    return send_file(mp4, as_attachment=True, download_name=f"{nombre}.mp4",
                     mimetype="audio/mp4")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=PUERTO)
