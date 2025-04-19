# ISS Overhead Notifier

This Python script checks whether the International Space Station (ISS) is currently flying over your location and if it’s dark outside by using public APIs. If both conditions are met—meaning the ISS is nearby and it's nighttime—it sends you an email alert so you can step outside and try to see it in the sky.

## How It Works

- Retrieves the current position of the ISS using the [Open Notify API](http://api.open-notify.org/iss-now.json).
- Checks if the ISS is within ±5° latitude and longitude of your location.
- Gets sunrise and sunset times from the [Sunrise-Sunset API](https://sunrise-sunset.org/api) to determine if it's currently dark.
- Sends an email notification if the ISS is close and visible.

## Setup

1. Clone the repository or download the script.
2. Replace the following values in the script:
   - `MY_LAT` and `MY_LONG` with your actual latitude and longitude.
   - `EMAIL_ID` and `PASSWORD` with your Gmail address and app password.
3. To run the script continuously, wrap it in a loop and use `time.sleep(60)` to check every 60 seconds.

## Requirements

- Python 3.x
- `requests` library (install with `pip install requests`)
- A Gmail account with [App Passwords](https://support.google.com/accounts/answer/185833?hl=en) enabled.

## Note

- Google may block sign-ins from this script unless you use App Passwords and enable "less secure apps" (or set up OAuth).
- You can schedule the script to run automatically using cron (Linux/macOS) or Task Scheduler (Windows).

