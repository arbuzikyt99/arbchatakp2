[app]
title = Arbchat
package.name = arbchat
package.domain = org.example
source.dir = .
version = 0.1
requirements = python3,kivy
orientation = portrait
android.permissions = INTERNET
android.api = 33
android.minapi = 21
# Force known working NDK/SKD versions for Colab environments
android.ndk = 23b
android.sdk = 24

[buildozer]
log_level = 2