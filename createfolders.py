import os
import sys
from datetime import datetime, timedelta

def create_folders_for_year(year, base_path):
    year_path = os.path.join(base_path, str(year))
    os.makedirs(year_path, exist_ok=True)

    for month_index in range(1, 13):
        month_str = f"{year}-{month_index:02d}"
        month_path = os.path.join(year_path, month_str)
        os.makedirs(month_path, exist_ok=True)

        # Create the Investigation folder
        investigation_folder = os.path.join(month_path, f"{month_str}-Investigation")
        os.makedirs(investigation_folder, exist_ok=True)

        current_day = datetime(year, month_index, 1)
        while current_day.month == month_index:
            if current_day.weekday() in [1, 3]:  # Tuesday or Thursday
                day_folder = current_day.strftime("%Y-%m-%d")
                os.makedirs(os.path.join(month_path, day_folder), exist_ok=True)
            current_day += timedelta(days=1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python create_folders.py <year> <base_path>")
        sys.exit(1)

    year = int(sys.argv[1])
    base_path = sys.argv[2]
    create_folders_for_year(year, base_path)
