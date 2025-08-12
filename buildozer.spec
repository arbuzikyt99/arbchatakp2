[app]
title = ArbChat
package.name = arbchat
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
android.accept_sdk_license = True
android.api = 31
android.minapi = 21
android.sdk_path = $ANDROIDSDK
android.ndk_path = $ANDROIDNDK
android.ndk_version = 23b
android.accept_sdk_license = True

[android]
# если нужны дополнительные permissions:
# android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE
