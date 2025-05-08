from pathlib import Path

# 📁 Базалық директория
BASE_DIR = Path(__file__).resolve().parent.parent

# 🚨 Қауіпсіздік
SECRET_KEY = 'django-insecure-v)__f!qfql4sew4^%f2825rdond$v=v4l4hqiu1@b&x4y+xx6k'
DEBUG = True
ALLOWED_HOSTS = []

# 📦 Орнатылған қосымшалар
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 🌐 Үшінші тарап кітапханалар
    'rest_framework',
    'rest_framework.authtoken',

    # 🧩 Сіздің қолданба
    'blog',
]

# 🌐 Middleware (орталық жүйелер)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 🔗 URL конфигурациясы
ROOT_URLCONF = 'miniblog.urls'

# 🖼️ Шаблон жүйесі
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 🚀 WSGI
WSGI_APPLICATION = 'miniblog.wsgi.application'

# 💾 Дерекқор (SQLite — сессия үшін жеткілікті)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 🔐 Құпиясөз валидациясы
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 🌍 Локализация
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Almaty'  # ⏰ өз қалаңызға қарай реттеңіз
USE_I18N = True
USE_TZ = True

# 📁 Статикалық файлдар
STATIC_URL = 'static/'

# 🆔 Әдепкі авто өріс
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 🔐 DRF конфигурациясы (авторизация мен рұқсат)
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
