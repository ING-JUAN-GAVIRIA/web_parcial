# Gestor de Eventos — Flask (datos en memoria)

## Requisitos
- Python 3.10+
- Dependencias: `Flask`, `Flask-WTF`

Instalar:
```bash
python -m venv venv
# Windows PowerShell
venv\Scripts\activate
# Linux/Mac
# source venv/bin/activate

pip install -r requirements.txt
```

## Ejecutar
```bash
set FLASK_APP=app.py   # Windows PowerShell: $env:FLASK_APP="app.py"
flask run --port 5000
```
Abrir: http://127.0.0.1:5000

## Estructura
```
flask_events_app/
  app.py
  data.py
  forms.py
  utils.py
  templates/
    base.html
    index.html
    event_detail.html
    admin_event.html
    register.html
    404.html
  static/
    styles.css
  requirements.txt
```

> Nota: Los datos se mantienen en memoria (se pierden al reiniciar).

## Capturas
1. Inicio: lista y destacados.
2. Detalle de evento: asistentes y botón de registro.
3. Formulario de nuevo evento.
4. Formulario de registro.
```

