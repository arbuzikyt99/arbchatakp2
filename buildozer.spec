[app]
title = Arbchat
package.name = arbchat
package.domain = org.arbchat

source.dir = .
source.main = main.py
version = 1.0.0
orientation = portrait

icon.filename = %(source.dir)s/data/icon.png

requirements = python3,kivy
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE

# Минимальная и целевая версия API
android.minapi = 21
android.api = 31

# Версия NDK
android.ndk = 23b

# Версия build-tools
android.build_tools_version = 30.0.3

# Лицензии
android.accept_sdk_license = True

# Архитектуры
android.archs = armeabi-v7a, arm64-v8a

# Формат
android.release_artifact = apk

[buildozer]
log_level = 2
warn_on_root = 1
