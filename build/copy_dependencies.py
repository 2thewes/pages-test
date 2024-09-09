import shutil
import os

os.makedirs("webpage")

# Leaflet
shutil.copytree("node_modules/leaflet/dist/", "webpage/leaflet/")

# Leaflet-ajax
shutil.copytree("node_modules/leaflet-ajax/dist/", "webpage/leaflet-ajax/")

# Leaflet-extra-markers
shutil.copytree(
    "node_modules/leaflet-extra-markers/dist/", "webpage/leaflet-extra-markers/"
)

# Fontawesome
shutil.copytree(
    "node_modules/@fortawesome/fontawesome-free/css/",
    "webpage/fontawesome/",
)

# Assests
shutil.copy2(
    "build/index.html",
    "webpage/index.html",
)
shutil.copy2(
    "build/campsites.css",
    "webpage/campsites.css",
)
