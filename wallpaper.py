import os
import random
import ctypes
from datetime import datetime

# Path folder wallpaper
WALLPAPER_FOLDER = "C:\\Users\\LENOVO\\OneDrive\\Gambar\\Wallpaper"

hari_mapping = {
    'Monday': 'senin',
    'Tuesday': 'selasa', 
    'Wednesday': 'rabu',
    'Thursday': 'kamis',
    'Friday': 'jumat',
    'Saturday': 'sabtu',
    'Sunday': 'minggu'
}   

# Ambil nama hari hari ini (dalam bahasa Inggris), lalu ubah ke Indonesia
hari_ini_inggris = datetime.now().strftime('%A')
hari_ini = hari_mapping[hari_ini_inggris]

# path gmbar sesuai hari
wallpaper_today = os.path.join(WALLPAPER_FOLDER, f"{hari_ini}.jpg")

# Ganti wallpaper (Windows)
ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_today, 3)

# cek tes
print(f"Wallpaper hari {hari_ini.capitalize()} diganti ke: {wallpaper_today}")


# # Ambil semua file gambar dari folder
# wallpapers = [os.path.join(WALLPAPER_FOLDER, f) for f in os.listdir(WALLPAPER_FOLDER) if f.endswith(('.jpg', '.png', '.bmp'))]

# # Pilih gambar berdasarkan tanggal hari ini
# index = datetime.now().timetuple().tm_yday % len(wallpapers)
# wallpaper_today = wallpapers[index]

# # Ganti wallpaper (untuk Windows)
# ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_today, 3)
