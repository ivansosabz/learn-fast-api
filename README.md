# 🚀 FastAPI - Guía Completa de Inicio

Guía paso a paso para crear, configurar y ejecutar un proyecto con FastAPI desde cero.

---

## 📦 Requisitos

- Python 3.8 o superior
- pip instalado
- Terminal (PowerShell, CMD, Bash)

---

## 📁 1. Crear carpeta del proyecto

```bash
mkdir mi_proyecto_fastapi
cd mi_proyecto_fastapi
```

---

## 🧪 2. Crear entorno virtual

```bash
python -m venv venv
```

---

## ⚡ 3. Activar entorno virtual

**Windows (PowerShell)**

```bash
venv\Scripts\activate
```

**Windows (CMD)**

```bash
venv\Scripts\activate.bat
```

**Linux / Mac**

```bash
source venv/bin/activate
```

---

## 📥 4. Instalar dependencias

```bash
pip install fastapi uvicorn
```

---

## 📝 5. Crear archivo principal

Crear archivo: `main.py`

---

## 🧠 6. Código inicial

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"mensaje": "Hola mundo con FastAPI 🚀"}
```

---

## ▶️ 7. Ejecutar el servidor

```bash
uvicorn main:app --reload
```

---

## 🌐 8. Acceder a la aplicación

| Recurso | URL |
|---|---|
| API | http://127.0.0.1:8000 |
| Swagger Docs | http://127.0.0.1:8000/docs |
| Redoc | http://127.0.0.1:8000/redoc |

---

## 🔍 9. Estructura recomendada

```
mi_proyecto_fastapi/
│
├── venv/
├── main.py
├── app/
│   ├── routes/
│   ├── models/
│   ├── schemas/
│   └── database/
└── requirements.txt
```

---

## 📌 10. Guardar dependencias

```bash
pip freeze > requirements.txt
```

Instalar después:

```bash
pip install -r requirements.txt
```

---

## 🧪 11. Ejemplo Path Parameter

```python
@app.get("/saludo/{nombre}")
async def saludo(nombre: str):
    return {"mensaje": f"Hola {nombre}"}
```

---

## 🧪 12. Ejemplo Query Parameter

```python
@app.get("/producto")
async def producto(nombre: str, precio: float):
    return {
        "nombre": nombre,
        "precio": precio
    }
```

Ejemplo de uso:

```
http://127.0.0.1:8000/producto?nombre=Teclado&precio=50
```

---

## 🔄 13. Ejemplo combinado

```python
@app.get("/usuario/{nombre}")
async def usuario(nombre: str, edad: int):
    return {"nombre": nombre, "edad": edad}
```

Uso:

```
http://127.0.0.1:8000/usuario/Ivan?edad=25
```

---

## 🔐 14. Validaciones básicas

```python
from fastapi import Path, Query

@app.get("/validar/{nombre}")
async def validar_nombre(
    nombre: str = Path(..., min_length=3, max_length=10)
):
    return {"nombre": nombre}
```

```python
@app.get("/edad")
async def validar_edad(
    edad: int = Query(..., ge=1, le=100)
):
    return {"edad": edad}
```

---

## 🧠 Conceptos clave

| Concepto | Descripción |
|---|---|
| **FastAPI** | Framework para APIs rápidas |
| **Uvicorn** | Servidor ASGI |
| **Path Parameters** | `/usuario/Ivan` |
| **Query Parameters** | `?edad=25` |
| **Validación** | Automática con tipos de Python |
| **Documentación** | Automática con Swagger |

---

## 🛑 15. Detener servidor

```
CTRL + C
```

---

## ✅ Checklist

- [ ] Crear carpeta
- [ ] Crear entorno virtual
- [ ] Activar entorno
- [ ] Instalar dependencias
- [ ] Crear `main.py`
- [ ] Ejecutar servidor
- [ ] Probar en navegador
- [ ] Usar `/docs`

---

## 🚀 Siguiente paso

- Pydantic (modelos)
- Request Body (POST)
- CRUD completo

---

## 👨‍💻 Autor

Guía de aprendizaje de FastAPI