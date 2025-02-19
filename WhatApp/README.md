# WhatsApp Session Stealer

## Description

This program is a proof of concept demonstrating how easily one can steal WhatsApp data from a victim's machine. The victim's payload will create a zip of all the WhatsApp data located at `LOCALAPPDATA\Packages\5319275A.WhatsAppDesktop_cv1g1gvanyjgm`, upload it to a local server at `127.0.0.1/upload.php`.

## How it works

1. The victim's payload will create a zip of the WhatsApp data.
2. The zip file will be uploaded to a local server at `127.0.0.1/upload.php`.

## Setup

1. Clone the repository.
2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Run the `main.py` script:
    ```sh
    python main.py
    ```

## Disclaimer

This project is for educational purposes only. Do not use it for malicious purposes.