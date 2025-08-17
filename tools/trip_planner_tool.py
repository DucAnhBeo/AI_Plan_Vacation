from langchain.tools import tool
import requests



@tool
def plan_trip(destination: str, days: int = 3) -> str:
    """
    Dùng Gemini API để lập kế hoạch du lịch chi tiết cho từng ngày đến một địa điểm cụ thể.
    """
    try:
        prompt = (
            f"Hãy lập kế hoạch du lịch trong {days} ngày tại {destination}. "
            "Cho mỗi ngày, hãy gợi ý chi tiết buổi sáng, buổi trưa, buổi chiều và buổi tối. "
            "Nêu rõ hoạt động, ẩm thực, điểm tham quan phù hợp. "
            "Lưu ý đưa ra các gợi ý phong phú, hấp dẫn và phù hợp cho du lịch tự túc."
        )

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
        response = requests.post(
            url,
            json={
                "contents": [{"parts": [{"text": prompt}]}]
            },
            headers={"Content-Type": "application/json"}
        )

        response.raise_for_status()
        result = response.json()
        text = result["candidates"][0]["content"]["parts"][0]["text"]

        return text.strip()

    except Exception as e:
        return f"Lỗi khi lập kế hoạch du lịch bằng Gemini: {str(e)}"
