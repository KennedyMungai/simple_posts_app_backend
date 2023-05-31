"""The main file for the application"""
from fastapi import FastAPI


app = FastAPI(title='Posts App', description='A simple posts app')


@app.get('/', name='Root', description='A test endpoint for the application')
async def root() -> dict[str, str]:
    """The root endpoint for the application"""
    return {"Message": "FastAPI works"}
