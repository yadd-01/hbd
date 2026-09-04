# Deployment Guide
## Web Ulang Tahun - PythonAnywhere Deployment

---

## Prerequisites

| Item | Requirement |
|------|-------------|
| PythonAnywhere Account | Free tier (https://www.pythonanywhere.com) |
| Python Version | 3.10+ |
| Django Version | 5.x |
| Git | Optional (for version control) |

---

## Step-by-Step Deployment

### Step 1: Create PythonAnywhere Account

1. Go to https://www.pythonanywhere.com
2. Click **"Pricing & Contribute"** → **"Create a Beginner account"**
3. Fill in registration form
4. Verify email address
5. Log in to dashboard

---

### Step 2: Upload Project Files

#### Option A: Using File Upload (Recommended for beginners)

1. Go to **Dashboard** → **Files**
2. Navigate to `/home/yourusername/`
3. Click **"Upload a file"**
4. Upload all project files one by one:
   - `manage.py`
   - `requirements.txt`
   - `hbd_project/` folder
   - `birthday/` folder
   - `static/` folder
   - `templates/` folder (if exists)

#### Option B: Using Git

1. Go to **Dashboard** → **Consoles**
2. Open **Bash console**
3. Run:
```bash
cd ~
git clone https://github.com/yourusername/hbd_project.git
```

---

### Step 3: Set Up Virtual Environment

1. Go to **Dashboard** → **Consoles**
2. Open **Bash console**
3. Run:
```bash
# Create virtual environment
python3.10 -m venv ~/hbd_venv

# Activate virtual environment
source ~/hbd_venv/bin/activate

# Navigate to project
cd ~/hbd_project

# Install dependencies
pip install -r requirements.txt

# Install additional packages if needed
pip install django Pillow
```

---

### Step 4: Configure Django Settings

1. Edit `hbd_project/settings.py`:
```python
# Add your PythonAnywhere username
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']

# Security settings
DEBUG = False
SECRET_KEY = 'your-secret-key-here'  # Generate new key

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = '/home/yourusername/hbd_project/staticfiles'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/yourusername/hbd_project/media'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]
```

---

### Step 5: Run Migrations

1. In Bash console:
```bash
cd ~/hbd_project
source ~/hbd_venv/bin/activate

# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput
```

---

### Step 6: Configure Web App

1. Go to **Dashboard** → **Web**
2. Click **"Add a new web app"**
3. Choose **"Manual configuration"**
4. Select **Python 3.10**
5. Click **"Next"**

#### Configure WSGI File:

1. Click **"WSGI configuration file"** link
2. Replace contents with:
```python
import os
import sys

# Add your project directory to sys.path
project_home = '/home/yourusername/hbd_project'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'hbd_project.settings'

# Activate virtual environment
activate_this = '/home/yourusername/hbd_venv/bin/activate_this.py'
exec(open(activate_this).read(), dict(__file__=activate_this))

# Import Django WSGI handler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

#### Configure Static Files:

1. In **Web** page, scroll to **"Static files"**
2. Click **"Add new static files mapping"**
3. Add:
   - URL: `/static/`
   - Directory: `/home/yourusername/hbd_project/staticfiles`

4. Add another mapping for media:
   - URL: `/media/`
   - Directory: `/home/yourusername/hbd_project/media`

---

### Step 7: Set Environment Variables

1. In **Web** page, scroll to **"Environment variables"**
2. Add:
   - `DJANGO_SETTINGS_MODULE` = `hbd_project.settings`
   - `SECRET_KEY` = `your-production-secret-key`

---

### Step 8: Reload Web App

1. Click **"Reload"** button (yellow button at top)
2. Wait for reload to complete
3. Your app is now live at: `https://yourusername.pythonanywhere.com`

---

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| **500 Internal Server Error** | Check error log: Web → Logs → Error log |
| **Static files not loading** | Verify static files mapping in Web page |
| **Database errors** | Run migrations again: `python manage.py migrate` |
| **Import errors** | Check virtual environment path in WSGI |
| **Media files not uploading** | Check MEDIA_ROOT path and permissions |

### Viewing Logs

1. Go to **Dashboard** → **Web**
2. Click **"Error log"** or **"Server log"**
3. Check for error messages

### Debug Mode (Development only)

```python
# In settings.py (TEMPORARY only!)
DEBUG = True
```

> **WARNING:** Never leave DEBUG = True in production!

---

## Post-Deployment Checklist

- [ ] Website loads at public URL
- [ ] Countdown timer works correctly
- [ ] Static files (CSS, JS, images) load
- [ ] Gallery navigation works
- [ ] Love letter animation works
- [ ] Music player works
- [ ] Timeline displays correctly
- [ ] Mobile responsive design works
- [ ] No error logs

---

## Updating the App

1. Upload new files via Files
2. Go to Web → Click "Reload"
3. Test changes

---

## Backup Strategy

### Database Backup
```bash
cd ~/hbd_project
python manage.py dumpdata > backup.json
```

### Restore Database
```bash
cd ~/hbd_project
python manage.py loaddata backup.json
```

---

## Free Tier Limitations

| Feature | Limit |
|---------|-------|
| CPU seconds | 512/day |
| Memory | 512 MB |
| Disk Space | 512 MB |
| Web Apps | 1 |
| MySQL Databases | 1 |

> This is sufficient for a birthday website!

---

## Alternative Deployment Options

| Platform | Pros | Cons |
|----------|------|------|
| **PythonAnywhere** | Easy Django setup | Limited free tier |
| **Railway** | Modern, easy | Limited free tier |
| **Render** | Good free tier | Less Python focus |
| **Heroku** | Popular | No free tier anymore |

---

*Document created: September 4, 2026*
*Author: Opencode Assistant*
