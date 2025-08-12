[app]
title = MyApp
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

# Android
android.sdk = 33
android.ndk = 25b
android.api = 33
android.minapi = 21
android.arch = armeabi-v7a
android.accept_sdk_license = True
android.build_tools = 33.0.2

# Чтобы исправить твою ошибку:
android.sdk_path = $HOME/.buildozer/android/platform/android-sdk
android.ndk_path = $HOME/.buildozer/android/platform/android-ndk-r25b

# Автоустановка нужных пакетов SDK (aidl и build-tools)
android.extra_packages = build-tools;33.0.2,platform-tools,platforms;android-33

# GitHub Actions: отключить интерактивные вопросы
android.accept_sdk_license = True

# (опционально) убираем поддержку старых версий
p4a.local_recipes =
