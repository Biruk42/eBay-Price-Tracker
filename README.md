# eBay Price Tracker

## Overview
This is a Python script that tracks the price of a specific item on eBay. It sends an email notification when the price drops below a certain threshold.

## Requirements
- Python 3.x
- `requests` library
- `BeautifulSoup` library
- `smtplib` library

## Installation
1. Clone this repository to your local machine.
2. Install the required libraries by running:
    ```shell
    pip install requests
    pip install beautifulsoup4
    ```
3. Configure the script by replacing placeholders with your own details:
    - `URL`: The URL of the item to be tracked on eBay.
    - `user`: Your Gmail email address.
    - `password`: Your Gmail password.
    - `to_addrs`: The email address where you want to receive notifications.

## Usage
1. Run the script by executing `python ebay_price_tracker.py`.
2. The script will continuously check the price of the item.
3. When the price drops below the specified threshold, an email notification will be sent to the specified email address.

## Configuration
- You can adjust the price threshold for notification by modifying the `price` variable in the script.
- Ensure that your Gmail account has less secure app access enabled. You can enable this in your Google account settings.

## Disclaimer
This script is for educational purposes only. Use it responsibly and ensure compliance with eBay's terms of service.

## Contributions
Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or create a pull request.
