# ImageScanner4Web

**ImageScanner4Web** is a Python Flask microservice that enables scanning documents directly from a web page and retrieving the scanned image as a PDF. It bridges the gap between browser-based user interfaces and local image scanners, making it easy to integrate scanning functionality into any web application.

---

## Features

- **Trigger Scans from the Browser:**  
  Users can initiate a scan from a web page, specifying scan resolution and whether to scan multiple pages.

- **Direct PDF Output:**  
  The scanned image(s) are automatically converted to PDF format and returned to the browser as a base64-encoded file for preview or download.

- **Simple Integration:**  
  Includes a sample HTML client (`client_page.html`) and a jQuery-based AJAX call to demonstrate how to interact with the scanning service.

- **Cross-Origin Support:**  
  CORS is enabled, so you can integrate the scanner service with web pages hosted on different origins.

---

## How It Works

1. **Run the Flask Service:**  
   The backend Flask app (`scanner_service.py`) listens for HTTP POST requests at `/scan`. When a request is received, it uses the [pyinsane2](https://pypi.org/project/pyinsane2/) library to interact with a connected scanner.

2. **Initiate Scan from Web Page:**  
   The provided sample web page (`client_page.html`) lets users set their scan preferences and start the scan process via a button click.

3. **Receive and Display the PDF:**  
   Once scanning is complete, the backend returns the PDF as a base64-encoded string. The client page decodes and displays the PDF for the user.

---

## Requirements

- **Python 3.x**
- [Flask](https://pypi.org/project/Flask/)
- [Flask-CORS](https://pypi.org/project/Flask-Cors/)
- [pyinsane2](https://pypi.org/project/pyinsane2/)
- [img2pdf](https://pypi.org/project/img2pdf/)
- [numpy](https://pypi.org/project/numpy/)
- [Pillow (PIL)](https://pypi.org/project/Pillow/)

A compatible scanner must be connected to the machine running the Flask service.

---

## Usage

### 1. Install Dependencies

```bash
pip install flask flask-cors pyinsane2 img2pdf numpy pillow
```

### 2. Run the Flask Service

```bash
python scanner_service.py
```

The service will listen on `http://127.0.0.1:8000`.

### 3. Open the Sample Web Page

Open `client_page.html` in your browser.  
Make sure the browser can reach the Flask backend (they should run on the same machine for local scanning).

### 4. Scan a Document

- Set the desired resolution.
- Choose whether to scan multiple pages.
- Click "Start scanning".
- The scanned PDF will be displayed on the page.

---

## Example Client Workflow

1. User fills in the resolution and selects options.
2. User clicks "Start scanning".
3. The browser sends a POST request to the Flask backend.
4. The backend performs the scan and returns a PDF.
5. The browser displays the PDF or a download link.

---

## Limitations & Notes

- The service must run on the same machine as the scanner but you can change the address to the machine where the scanner is connected and of course the backend is installed.
- Supported platforms and scanner models depend on `pyinsane2`.
- Security: Exposes a local web service; use with care and do not expose to untrusted networks.
- The sample client uses jQuery (`jq.js`), which must be present in the same directory or replaced with your own implementation.

---

## License

This project is provided AS-IS for personal and educational use.  
Feel free to improve or adapt it for your needs!

---
**Author:** [KHBillel](https://github.com/KHBillel)
