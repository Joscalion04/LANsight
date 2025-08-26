# LANsight

**LANsight** es un dashboard de monitoreo para redes locales (LAN), diseñado para brindar
visibilidad sobre los dispositivos conectados, su actividad y posibles riesgos.
Está orientado a entornos educativos, domésticos o pequeñas empresas que buscan
tener control básico de su red interna.

---

## 🚀 Funcionalidades
- Escaneo de red local usando `nmap`/`scapy`.
- Inventario de dispositivos (IP, MAC, hostname, puertos abiertos).
- Dashboard en React con gráficas y tablas interactivas.
- Autenticación JWT (roles: admin / user).
- Registro histórico de dispositivos y eventos.
- Alertas de:
  - Nuevos dispositivos conectados.
  - Puertos sospechosos abiertos.
- Despliegue con **Docker** y orquestación con **Kubernetes**.

---

## 🛠️ Stack Tecnológico
- **Backend**: [FastAPI](https://fastapi.tiangolo.com/) + Postgress
- **Frontend**: React + Recharts (gráficas) + shadcn/ui o Material UI
- **Base de Datos**: PostgreSQL
- **CI/CD**: Docker + Jenkins + Trivy + SonarQube + Kubernetes (minikube/k3s)
- **Seguridad**: JWT, HTTPS con Nginx/Traefik


## ⚙️ Instalación y Uso

### Requisitos previos
- Docker y Docker Compose instalados
- Acceso a la red local en modo bridge (si se usa VM)

### Paso 1: Clonar el repositorio
```bash
git clone https://github.com/tuusuario/lansight.git
cd lansight
```

### Paso 2: Levantar el entorno con Docker

````bash
docker-compose up --build
````

### Paso 3: Acceder a la aplicación
- Frontend (React) → http://localhost:3000
- Backend (FastAPI docs) → http://localhost:8000/docs


### Seguridad
Autenticación vía JWT para proteger los endpoints.
Escaneo de imágenes con Trivy antes de despliegues.
Uso de HTTPS en despliegues productivos.

### Roadmap
 WebSockets para monitoreo en tiempo real.
 Exportación de reportes (PDF/CSV).
 Integración con LDAP/AD.
 Notificaciones por correo/Telegram.
