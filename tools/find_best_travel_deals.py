from langchain.tools import tool
import requests


@tool
def get_best_travel_days(city: str) -> str:
    """
    Tìm những ngày thời tiết tốt nhất để đi du lịch trong 3 ngày tới tại thành phố.
    Tiêu chí: Không mưa, nhiệt độ trung bình từ 22°C - 30°C.
    """
    try:
        # Gọi API từ weatherapi.com
        url = f"http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q={city}&days=3&aqi=no&alerts=no"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        forecast_days = data['forecast']['forecastday']
        result = f"Những ngày đẹp trời ở {city} phù hợp để du lịch:\n"
        count = 0

        for day in forecast_days:
            date = day['date']
            avg_temp = day['day']['avgtemp_c']
            condition = day['day']['condition']['text'].lower()

            if "rain" not in condition and 22 <= avg_temp <= 30:
                result += f"- {date}: {condition}, {avg_temp}°C\n"
                count += 1

        if count == 0:
            return f"Không có ngày nào lý tưởng trong 3 ngày tới tại {city}."
        return result

    except Exception as e:
        return f"Lỗi khi phân tích thời tiết: {str(e)}"
