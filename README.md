# URL Shortener

A simple URL shortener web application built with Flask, HTML, and CSS. This application allows users to input a long URL and receive a shortened version that redirects to the original URL.

## Features

- Shorten long URLs
- Redirect to original URLs using the shortened links
- Simple and responsive web interface

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- SQLite3

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/url-shortener.git
    cd url-shortener
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Initialize the database:

    ```bash
    python app.py
    ```

### Running the Application

1. Start the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

## File Structure


- `static/`: Directory for static files (CSS, images, etc.)
- `templates/`: Directory for HTML templates
- `app.py`: Main Flask application
- `requirements.txt`: List of Python dependencies
- `README.md`: Project documentation
- `LICENSE`: License for the project

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - The web framework used
- [SQLite](https://www.sqlite.org/index.html) - The database used

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

If you have any questions or suggestions, feel free to contact us at [info@compcit.com].
