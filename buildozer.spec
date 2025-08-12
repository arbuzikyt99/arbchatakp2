[app]
title = Arbchat
package.name = arbchat
package.domain = org.arbchat

source.dir = .
source.main = main.py
version = 1.0.0
orientation = portrait

icon.filename = %(source.dir)s/data/icon.png

requirements = python3,kivy,sdl2,pyjnius,android

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE

android.minapi = 21
android.api = 31
android.ndk = 23b
android.build_tools_version = 30.0.3

android.accept_sdk_license = True
android.archs = armeabi-v7a, arm64-v8a
android.release_artifact = apk

[buildozer]
log_level = 2
warn_on_root = 1
