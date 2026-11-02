# 🔊 Texto a Voz

Aplicación local que convierte texto en audio con **voces neurales de Microsoft** en español de México, y permite descargarlo en **MP3** o **MP4**.

---

## 🎯 Propósito

- Generar narraciones de buena calidad de forma **gratuita y sencilla**, sin instalar programas pesados.
- Usarlo para crear audio de **contenido** (por ejemplo, narraciones para videos o el podcast).
- Practicar un proyecto completo con **Python + Flask**: servidor, interfaz web y automatización en Windows, como **proyecto de portafolio**.

## ✨ Qué hace

- Escribes o pegas un texto (hasta 20 000 caracteres)
- Eliges la voz y el volumen
- Escuchas el resultado en el navegador
- Lo descargas en MP3 o MP4
- Los audios temporales se borran solos después de 6 horas

**Voces disponibles:**

| Voz | Tipo |
|---|---|
| Dalia | Mujer (predeterminada) |
| Jorge | Hombre |

## 🛠️ Tecnologías

| Herramienta | Uso |
|---|---|
| Python 3 | Lenguaje del servidor |
| [Flask](https://flask.palletsprojects.com/) | Servidor web local |
| [edge-tts](https://github.com/rany2/edge-tts) | Voces neurales de Microsoft |
| imageio-ffmpeg | Conversión de MP3 a MP4 |
| HTML, CSS y JavaScript | Interfaz |

## 🚀 Cómo ejecutarlo

Requisitos: Python 3 e internet (las voces se generan en línea).

```powershell
python -m pip install -r requirements.txt
python app.py
```

Luego abre <http://localhost:5050> en el navegador.

### Arranque automático en Windows

- **Una vez:** doble clic en `iniciar.vbs` (corre en segundo plano, sin ventana).
- **Siempre al encender la PC:** ejecuta `activar-inicio-automatico.ps1`. También crea un acceso directo en el escritorio.
- **Para desactivarlo:** borra `Texto a Voz.lnk` de la carpeta `shell:startup`.

## 📁 Estructura

| Archivo | Contenido |
|---|---|
| `app.py` | Servidor (Flask + edge-tts; usa ffmpeg para el MP4) |
| `index.html` | Interfaz |
| `iniciar.vbs` | Arranca el servidor sin ventana |
| `activar-inicio-automatico.ps1` | Arranque automático al iniciar sesión y acceso directo |
| `requirements.txt` | Dependencias de Python |

## 👤 Autor

**Fernando Sánchez Mejía** — proyecto personal de aprendizaje y portafolio, desarrollado con apoyo de Claude Code.

> Las voces pertenecen al servicio de Microsoft al que se conecta edge-tts. Este proyecto no está afiliado a Microsoft.
