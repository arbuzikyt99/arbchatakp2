[app]
# Название приложения
title = Arbchat

# Имя пакета (латиницей, без пробелов и спецсимволов)
package.name = arbchat

# Домен приложения (обратно записанный)
package.domain = org.arbchat

# Главный исполняемый файл
source.dir = .
source.main = main.py

# Иконка
icon.filename = %(source.dir)s/data/icon.png

# Версия
version = 1.0.0

# Ориентация
orientation = portrait

# Разрешения
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE

# Минимальная и целевая версия Android
android.minapi = 21
android.sdk = 30
android.ndk = 23b
android.accept_sdk_license = True
android.build_tools_version = 36.0.0

# Зависимости Python
requirements = python3,kivy

# Архитектуры
android.archs = arm64-v8a, armeabi-v7a

# Формат билда
android.release_artifact = apk

[buildozer]
log_level = 2
warn_on_root = 1
