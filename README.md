# ===========================================
# 🧩 SYSFLOW — FULL DJANGO + REACT SETUP GUIDE
# ===========================================

# -------------------------------
# 1️⃣  Clone or create the project
# -------------------------------
cd ~/Documents
git clone https://github.com/masc4424/SysFlow.git
cd SysFlow

# If you already had the project locally, skip cloning and just:
# cd ~/Documents/SysFlow

# -------------------------------
# 2️⃣  Create and activate virtual environment
# -------------------------------
python3 -m venv venv
source venv/bin/activate

# On Windows (PowerShell):
# python -m venv venv
# .\venv\Scripts\Activate.ps1

# Upgrade pip
pip install --upgrade pip

# -------------------------------
# 3️⃣  Install Django dependencies
# -------------------------------
pip install django djangorestframework django-cors-headers whitenoise python-dotenv
pip freeze > requirements.txt

# -------------------------------
# 4️⃣  Basic Django setup checklist
# -------------------------------
# (These are manual edits — open backend/settings.py in VS Code or editor)
# 
# Ensure these lines exist:

# INSTALLED_APPS += [
#     'rest_framework',
#     'corsheaders',
#     'api',
# ]
#
# MIDDLEWARE = [
#     'corsheaders.middleware.CorsMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     # ... other middleware ...
#     'whitenoise.middleware.WhiteNoiseMiddleware',
# ]
#
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",
#     "http://127.0.0.1:3000",
# ]
#
# import os
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_DIRS = [os.path.join(BASE_DIR, '..', 'frontend', 'build', 'static')]

# -------------------------------
# 5️⃣  Migrate database and create superuser
# -------------------------------
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  # optional
python manage.py runserver

# Visit: http://127.0.0.1:8000 to confirm backend works

# -------------------------------
# 6️⃣  Setup React frontend
# -------------------------------
cd frontend
npm install
npm install axios

# If you get file watcher errors (ENOSPC), fix with:
# sudo sysctl fs.inotify.max_user_watches=524288
# echo "fs.inotify.max_user_watches=524288" | sudo tee -a /etc/sysctl.conf
# sudo sysctl -p

npm start

# Visit: http://localhost:3000

# -------------------------------
# 7️⃣  Fix common React-Django connection error
# -------------------------------
# Make sure your API base URL in frontend (e.g., axios config) points to:
# http://127.0.0.1:8000/api/
#
# Example React axios config:
# const api = axios.create({ baseURL: "http://127.0.0.1:8000/api" });

# -------------------------------
# 8️⃣  Create a .gitignore file
# -------------------------------
cat << 'EOF' > .gitignore
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
*.db
*.sqlite3
*.log

# Virtualenv
venv/
.env

# Django
staticfiles/
media/

# React
frontend/node_modules/
frontend/build/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
EOF

# -------------------------------
# 9️⃣  Initialize Git and push to GitHub
# -------------------------------
git init
git add .
git commit -m "Initial commit: SysFlow Django + React"
git branch -M main
git remote add origin https://github.com/masc4424/SysFlow.git

# If remote branch already exists, pull before pushing
git pull origin main --allow-unrelated-histories
git add .
git commit -m "Merge remote and local"
git push -u origin main

# If still rejected and you want to overwrite remote (⚠️ be careful):
# git push origin main --force

# -------------------------------
# 🔟  Build frontend for production (optional)
# -------------------------------
cd frontend
npm run build
cd ..

# Serve React build via Django static files:
python manage.py collectstatic

# -------------------------------
# 1️⃣1️⃣  Run both servers
# -------------------------------
# Django:
source venv/bin/activate
python manage.py runserver

# React (new terminal):
cd frontend
npm start

# -------------------------------
# 1️⃣2️⃣  Optional: Setup SSH for Git (no password prompts)
# -------------------------------
# Generate SSH key (only once per machine):
ssh-keygen -t ed25519 -C "your_email@example.com"
cat ~/.ssh/id_ed25519.pub
# Copy that key → GitHub → Settings → SSH and GPG keys → New SSH key
# Then:
git remote set-url origin git@github.com:masc4424/SysFlow.git

# -------------------------------
# ✅  Summary of useful commands
# -------------------------------
# Django commands
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

# React commands
cd frontend
npm start
npm run build

# Git commands
git add .
git commit -m "update"
git push origin main
