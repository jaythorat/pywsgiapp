# pyWSGIapp

`pywsgiapp`  is a lightweight WSGI application framework aimed at simplifying the development of WSGI-based web applications. It offers an intuitive interface for managing HTTP requests and responses, enabling easy creation and deployment of web applications.

---

## Features

- Lightweight and easy-to-use WSGI framework.
- Customizable request handler for processing HTTP requests.
- Compatible with WSGI servers like `gunicorn`.

---

## Installation

To install the package, use the following command:

```bash
pip install pywsgiapp
```


---

## Usage

### Example: Basic WSGI Application

Here’s an example of how to use `pywsgiapp` to create a simple WSGI application:

```python
from pywsgiapp.WSGIApp import createWSGIApp

# Define a request handler function
def requestHandler(url: str, requestHeaders: dict, postData: dict) -> dict:
    response_body = f"Received URL: {url}, Headers: {requestHeaders}, Post Data: {postData}"
    return {
        "responseCode": 200,
        "responseHeaders": {"Content-Type": "text/plain"},
        "responseBody": response_body
    }

# Create the WSGI application
app = createWSGIApp(requestHandler)
```

Save this code in a file (e.g., `basic.py`) and run it with a WSGI server like `gunicorn`:

```bash
gunicorn basic:app
```

For more examples, see the [Examples Documentation](./pywsgiapp/examples/examples.md).

---

- **`pywsgiapp/`**: The main package containing the framework code.
- **`examples/`**: Example scripts demonstrating how to use the framework.
- **`setup.py`**: Metadata and installation configuration.
- **`requirements.txt`**: List of dependencies for development and deployment.

---


## Development

If you want to contribute or modify the framework, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/jaythorat/pywsgiapp.git
   cd pywsgiapp
   ```

2. Install the package in editable mode:
   ```bash
   pip install -e .
   ```

---

## Dependencies

The framework requires the following dependencies:
- `gunicorn>=20.1.0`

Install them using:
```bash
pip install -r requirements.txt
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! If you’d like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push the branch.
4. Open a pull request.

---

## Contact

For any questions or issues, feel free to contact the author:

- **Author**: Jay Thorat
- **Email**: dev.jaythorat@gmail.com
- **GitHub**: [jaythorat](https://github.com/jaythorat)
- **Portfolio**: [portfolio.jaythorat.in](portfolio.jaythorat.in)