from fastapi import FastAPI
from fastapi import Path
app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World, this is my first API on FastAPI"}

@app.get("/saludo/{nombre}")
async def saludo(nombre: str):
    return {"mensaje": f"Hola {nombre}"}
@app.get("/usuario/{nombre}/{edad}")
async def usuario(nombre: str, edad: int):
    return {"mensaje": f"Hola {nombre} que tiene {edad} años de edad"}

# parámetros de tipo (?):
@app.get("/buscar")
async def buscar(nombre: str, edad: int):
    return {"nombre": nombre, "edad": edad}

# validar texto
@app.get("/validar/{nombre}")
async def validar(nombre: str = Path(..., min_length=3, max_length=10)):
    return {"mensaje": f"Hola {nombre}"}

# validar números
@app.get("/validar_edad/{edad}")
# ge = greater than or equal to
# le = less than or equal to
async def validar_edad(edad: int = Path(...,ge=1, le=100)):
    return {"mensaje": f"Hola {edad}"}
# ejercicio 
@app.get("/producto/{id}")
async def precio(id: int, precio: float, cantidad: int):
    return {"mensaje": f"El precio del producto es {precio * cantidad}"}
