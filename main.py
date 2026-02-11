import json
from datetime import datetime


def parse_data_1(data):
    return {
        "device_id": data["device_id"],
        "timestamp": data["timestamp"],
        "temperature": data["temperature"],
        "humidity": data["humidity"]
    }


def parse_data_2(data):
    iso_time = data["time"]
    timestamp_ms = int(datetime.fromisoformat(iso_time.replace("Z", "")).timestamp() * 1000)

    return {
        "device_id": data["device"],
        "timestamp": timestamp_ms,
        "temperature": data["temp"],
        "humidity": data["hum"]
    }


def main():
    with open("data-1.json", "r") as f:
        data1 = json.load(f)

    with open("data-2.json", "r") as f:
        data2 = json.load(f)

    result = []
    result.append(parse_data_1(data1))
    result.append(parse_data_2(data2))

    with open("data-result.json", "w") as f:
        json.dump(result, f, indent=2)


if __name__ == "__main__":
    main()


