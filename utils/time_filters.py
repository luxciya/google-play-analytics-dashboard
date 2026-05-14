from datetime import datetime
import pytz


def is_time_between(start_hour, end_hour):

    india = pytz.timezone('Asia/Kolkata')

    current_time = datetime.now(india)

    current_hour = current_time.hour

    return start_hour <= current_hour < end_hour