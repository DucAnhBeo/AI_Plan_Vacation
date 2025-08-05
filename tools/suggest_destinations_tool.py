from langchain.tools import tool
import requests

WEATHER_API_KEY = "62c32d4a03e84ba7a0c13935250508"

@tool
def suggest_destinations_based_on_weather(city: str) -> str:
    """
    Dựa trên thời tiết hiện tại tại thành phố, gợi ý các địa điểm du lịch phù hợp (biển, núi, thành phố, trong nhà).
    """
    try:
        url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}&lang=vi"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        temp = data['current']['temp_c']
        description = data['current']['condition']['text'].lower()

        suggestions = f"Thời tiết hiện tại ở {city}: {description}, {temp}°C.\n"
        suggestions += "Gợi ý địa điểm du lịch:\n"

        if "mưa" in description or "sấm" in description:
            suggestions += "- Thăm bảo tàng, nhà triển lãm, trung tâm mua sắm trong nhà\n"
        elif "nắng" in description or "trời quang" in description:
            if temp > 30:
                suggestions += "- Du lịch biển, nghỉ dưỡng tại hồ, hoặc công viên nước\n"
            elif 20 <= temp <= 30:
                suggestions += "- Khám phá thành phố, du lịch sinh thái, đi bộ đường dài (trekking)\n"
            else:
                suggestions += "- Thăm vùng núi, đồi chè, khu vực khí hậu mát mẻ\n"
        elif temp < 20:
            suggestions += "- Du lịch vùng núi cao, thưởng thức ẩm thực nóng, nghỉ dưỡng\n"
        else:
            suggestions += "- Khám phá điểm đến trong nhà hoặc gần thành phố\n"

        return suggestions
    except Exception as e:
        return f"Lỗi khi gợi ý địa điểm: {str(e)}"
