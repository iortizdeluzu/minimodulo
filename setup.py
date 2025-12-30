# Fichero instalador

from setuptools import setup, find_packages

setup(
    name="minimodulo",           # Nombre del paquete
    version="0.1",              # Versión inicial
    packages=find_packages(),   # Encuentra automáticamente las carpetas con __init__.py
    install_requires=[],        # Dependencias externas si las hay
    author="Iker Ortiz de Luzuriaga",
    author_email="iker.ortiz@dipc.org",
    description="Un módulo de ejemplo que solicita datos",
    url="https://github.com/iortizdeluzu/minimodulo",
)
