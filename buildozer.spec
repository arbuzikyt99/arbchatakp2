[app]
title = Arbchat
package.name = arbchat
package.domain = org.arbchat
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,android,urllib3,certifi,chardet,idna
orientation = portrait
fullscreen = 0
android.archs = armeabi-v7a, arm64-v8a
android.api = 31
android.minapi = 21
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r23b
android.ndk_api = 21
android.gradle_dependencies = androidx.appcompat:appcompat:1.4.2,androidx.swiperefreshlayout:swiperefreshlayout:1.1.0
log_level = 2

[buildozer]
log_level = 2
warn_on_root = 0
