from langchain.tools import tool

@tool
def estimate_trip_cost(destination: str, days: int = 3, people: int = 1) -> str:
    """
    Ước lượng chi phí cơ bản cho chuyến du lịch đến một địa điểm cụ thể.
    - Bao gồm: di chuyển, ăn uống, chỗ ở, hoạt động vui chơi.
    - Tham số:
        - destination: địa điểm muốn đến
        - days: số ngày dự định ở lại
        - people: số người
    """
    try:
        # Chi phí cơ bản theo ngày cho 1 người (có thể thay đổi nếu bạn tích hợp dữ liệu thật sau này)
        daily_food = 300_000     # ăn uống mỗi ngày
        daily_stay = 500_000     # khách sạn / homestay
        daily_transport = 200_000
        daily_activities = 300_000

        total_per_day = daily_food + daily_stay + daily_transport + daily_activities
        total = total_per_day * days * people

        return (
            f"Chi phí dự kiến cho {people} người đi {destination} trong {days} ngày là khoảng {total:,} VND "
            f"(~ {total // 24_000} USD). Bao gồm ăn uống, chỗ ở, đi lại và hoạt động giải trí cơ bản."
        )
    except Exception as e:
        return f"Lỗi khi tính chi phí du lịch: {str(e)}"
