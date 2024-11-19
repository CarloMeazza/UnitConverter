# Unit Converter

A simple web application to convert units of length, weight, and temperature.
[https://roadmap.sh/projects/unit-converter](https://roadmap.sh/projects/unit-converter)

## Project Overview

This project provides a user-friendly interface for converting different units of measurement. 
It's built using Flask for the backend and HTML/CSS/JavaScript for the frontend.

## Installation

1. **Clone the repository**: 
   ```bash
   git clone https://github.com/yourusername/unit-converter.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd unit-converter
   ```
3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```
4. **Activate the virtual environment**:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
5. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application**:
   ```bash
   flask run
   ```
2. **Open your browser** and go to `http://localhost:5000` to start converting units.

## Requirements

- Python 3.9 or higher
- Flask
- Flask-WTF
- NumPy

## Features

- Convert lengths between millimeters, centimeters, meters, kilometers, inches, feet, yards, and miles.
- Convert weights between milligrams, grams, kilograms, ounces, and pounds.
- Convert temperatures between Celsius, Fahrenheit, and Kelvin.

## License

This project is licensed under the MIT License.
