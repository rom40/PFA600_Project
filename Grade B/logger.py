import csv
from datetime import datetime


LOG_FILE = "C:/Users/rom38/OneDrive - Högskolan Väst/Y1/SP1/PFA600/Project/Grade B/part_log.csv"


def initialize_log():
    with open(LOG_FILE, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "product_id",
            "timestamp",
            "x",
            "y",
            "vacuum"
        ])


def log_location(x, y, product_id, vacuum=1):
    timestamp = datetime.now().isoformat(timespec="seconds")

    with open(LOG_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            product_id,
            timestamp,
            x,
            y,
            vacuum
        ])
        print([
            product_id,
            timestamp,
            x,
            y,
            vacuum
        ])