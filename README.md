# 💬 Chatterhub

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Made with Django](https://img.shields.io/badge/Made%20with-Django-blue)
![Hosted on Render](https://img.shields.io/badge/Hosted%20on-Render-orange)

Chatterhub is a real-time group chat application built using Django and Django Channels. It supports dynamic group-based chatting, real-time WebSocket communication, user authentication, profile management, and cloud-based media storage. With a Tailwind CSS frontend and Redis caching backend, Chatterhub is optimized for scalability and responsiveness. The app is fully deployed on Render.

---

## 🚀 Features

- 🔐 Authentication with Django Allauth
- 💬 Dynamic group chat rooms
- 👤 View your own and others' profiles
- ⚡ Real-time messaging via Django Channels & WebSockets
- 🧠 Redis as a caching layer
- ☁️ Cloudinary integration for media (profile images, etc.)
- 🎨 Tailwind CSS for modern, responsive UI
- 📦 Whitenoise for static file handling in production
- 🌐 Deployed on Render

---
🔗 [Live Demo](https://chatterhub.onrender.com)

---
## 🛠️ Tech Stack
- Django, Django Channels
- HTML, Tailwind CSS, JavaScript
- Redis, WebSockets
- Cloudinary, Whitenoise
- Render (for deployment)

---

## 🛠 Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/chatterhub.git
cd chatterhub

# 2. Create and activate a virtual environment

# Create virtual environment
python -m venv .venv

# Activate it:
# On macOS/Linux:
source .venv/bin/activate

# On Windows (CMD):
.venv\Scripts\activate

# On Windows (PowerShell):
.venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create a .env file in the root directory (DO NOT commit this file)

# Example .env content:
# ----------------------
# SECRET_KEY=your_secret_key
# DEBUG=True
# ALLOWED_HOSTS=127.0.0.1,localhost
# REDIS_URL=redis://localhost:6379
# CLOUDINARY_URL=cloudinary://your_key:your_secret@your_cloud_name

# 5. Run database migrations
python manage.py migrate

# 6. Create a superuser
python manage.py createsuperuser

# 7. Run the development server
python manage.py runserver

# 8. Start the ASGI server (for WebSockets)
daphne chatterhub.asgi:application
# or
uvicorn chatterhub.asgi:application
```
