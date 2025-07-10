# 🍽️ Gestión de Menú Semanal

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)

Aplicación web para gestión de menús semanales desarrollada con Django que permite organizar platillos por día de la semana.

## 🌐 Demo en Vivo
🔗 [https://platillos-zr21.onrender.com/](https://platillos-zr21.onrender.com/)  

## ✨ Características

- ✅ CRUD completo de platillos
- 📅 Organización por días de la semana
- 🛡️ Validaciones de backend

## 🛠️ Tecnologías

### Backend
- Python 3.10+
- Django 4.2
- Django ORM
- SQLite 

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- Django Templates

### Deployment
- Render

## 🏗️ Arquitectura del Sistema

```mermaid
graph TD
    A[Cliente] --> B[Vistas Django]
    B --> C[Formularios]
    C --> D[Modelos]
    D --> E[(PostgreSQL)]
    B --> F[Templates HTML]
    F --> A
