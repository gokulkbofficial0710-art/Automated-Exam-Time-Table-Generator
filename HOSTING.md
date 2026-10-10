# Hosting & Deployment Guide

This project can be hosted locally, shared publicly over the internet in seconds, or deployed to cloud platforms 24/7.

---

## 1. Instant Local & LAN Hosting (Currently Active)

The project has been configured so FastAPI directly serves both the React Web UI and the REST API from a single port (`8000`), with full SPA routing.

### To Start the Website:
Simply double-click **`start_website.bat`** (or run in PowerShell/terminal):
```powershell
# 1. Build frontend (already pre-built in dist/)
cd frontend
npm run build
cd ..

# 2. Start unified server
cd backend
py -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Access URLs:
- **Local Browser**: [http://localhost:8000](http://localhost:8000)
- **Local Network (Wi-Fi / Mobile Phones)**: `http://<YOUR_LOCAL_IP>:8000` (e.g. `http://10.1.217.31:8000`)
- **API Documentation (Swagger)**: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 2. Instant Public Tunnel (Share with Anyone Online)

To share the website with external users, evaluators, or across the internet without port-forwarding or paying for hosting:

### Quick Run:
Double-click **`share_online.bat`** (or run in terminal):
```powershell
.\cloudflared.exe tunnel --url http://localhost:8000
```

This generates a free, secure `https://*.trycloudflare.com` URL that exposes the live app directly from your machine with Cloudflare SSL and CDN protection.

---

## 3. Free 24/7 Cloud Hosting on Render.com

Since your repository is on GitHub (`https://github.com/gokulkbofficial0710-art/Clg_Time_Table_Generator.git`):

1. Go to [render.com](https://render.com) and log in.
2. Click **New +** -> **Blueprint**.
3. Connect your GitHub repository.
4. Render will detect `render.yaml` automatically and configure:
   - **Build Command**: `cd frontend && npm install && npm run build && cd ../backend && pip install -r requirements.txt`
   - **Start Command**: `cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. Click **Apply**. Within a few minutes, you get a permanent 24/7 public URL (`https://exam-timetable-generator.onrender.com`).

---

## 4. Docker Compose Hosting (VPS / Cloud Server)

If deploying to an Ubuntu/Debian VPS or AWS EC2:
```bash
docker compose up -d --build
```
- Web UI: `http://<server-ip>:5173`
- Backend API: `http://<server-ip>:8000`
