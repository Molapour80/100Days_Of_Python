import folium
from geopy.geocoders import Nominatim

# 1. پیدا کردن مختصات تهران به صورت خودکار
geolocator = Nominatim(user_agent="my_app")
location = geolocator.geocode("تهران")

if location:
    # 2. ساخت نقشه با موقعیت تهران
    tehran_map = folium.Map(
        location=[location.latitude, location.longitude],
        zoom_start=12,
        tiles="cartodbpositron"
    )
    
    # 3. اضافه کردن مارکر
    folium.Marker(
        [location.latitude, location.longitude],
        popup=f"<b>تهران</b><br>مختصات: {location.latitude}, {location.longitude}",
        tooltip="اینجا تهران است!",
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(tehran_map)
    
    # 4. ذخیره نقشه
    tehran_map.save("tehran_map.html")
    print(f"نقشه تهران در مختصات {location.latitude}, {location.longitude} ذخیره شد.")
else:
    print("موقعیت تهران پیدا نشد!")