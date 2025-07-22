import folium

# ساخت نقشه با موقعیت تهران
tehran_map = folium.Map(location=[35.6892, 51.3890], zoom_start=12)

# اضافه کردن یک مارکر
folium.Marker(
    location=[35.6892, 51.3890],
    popup="<b>تهران</b>",  # متن قابل کلیک
    tooltip="اینجا تهران است!",  # متن هنگام هاور
    icon=folium.Icon(color="red", icon="info-sign")
).add_to(tehran_map)

# ذخیره نقشه در فایل HTML
tehran_map.save("tehran_map.html")