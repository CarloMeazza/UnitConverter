from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField
from wtforms.validators import DataRequired
import numpy as np
import os

udm = [
    ("mm", "Millimeter"),
    ("cm", "Centimeter"),
    ("m", "Meter"),
    ("km", "Kilometer"),
    ("in", "Inch"),
    ("ft", "Foot"),
    ("yd", "Yard"),
    ("mi", "Mile"),
]

unit_weight = [
    ("mg", "Milligram"),
    ("g", "Gram"),
    ("kg", "Kilogram"),
    ("oz", "Ounce"),
    ("lb", "Pound"),
]

temperature = [("C", "Celsius"), ("F", "Fahrenheit"), ("K", "Kelvin")]


class LengthForm(FlaskForm):
    from_number = FloatField(
        "from_number",
        validators=[DataRequired()],
        default=0,
        render_kw={"pattern": r"^-?\d+(\.\d+)?$", "class": "number_field"},
    )
    from_unit = SelectField(
        "from_unit", choices=udm, default="m", render_kw={"class": "select_unit"}
    )
    to_number = FloatField(
        "to_number",
        validators=[DataRequired()],
        default=0,
        render_kw={"pattern": r"^-?\d+(\.\d+)?$", "class": "number_field"},
    )
    to_unit = SelectField(
        "to_unit", choices=udm, default="in", render_kw={"class": "select_unit"}
    )


class WeightForm(FlaskForm):
    from_number = FloatField(
        "from_number",
        validators=[DataRequired()],
        default=0,
        render_kw={"pattern": r"^-?\d+(\.\d+)?$", "class": "number_field"},
    )
    from_unit = SelectField(
        "from_unit",
        choices=unit_weight,
        default="mg",
        render_kw={"class": "select_unit"},
    )
    to_number = FloatField(
        "to_number",
        validators=[DataRequired()],
        default=0,
        render_kw={"pattern": r"^-?\d+(\.\d+)?$", "class": "number_field"},
    )
    to_unit = SelectField(
        "to_unit", choices=unit_weight, default="kg", render_kw={"class": "select_unit"}
    )


class TempForm(FlaskForm):
    from_number = FloatField(
        "from_number",
        validators=[DataRequired()],
        default=0,
        render_kw={"pattern": r"^-?\d+(\.\d+)?$", "class": "number_field"},
    )
    from_unit = SelectField(
        "from_unit",
        choices=temperature,
        default="C",
        render_kw={"class": "select_unit"},
    )
    to_number = FloatField(
        "to_number",
        validators=[DataRequired()],
        default=0,
        render_kw={"pattern": r"^-?\d+(\.\d+)?$", "class": "number_field"},
    )
    to_unit = SelectField(
        "to_unit", choices=temperature, default="F", render_kw={"class": "select_unit"}
    )


app = Flask(__name__)
# SECRET_KEY = os.urandom(32)
app.config["SECRET_KEY"] = "secretsafesafesecret"


@app.route("/", methods=["GET", "POST"])
def index():
    lengthForm = LengthForm()
    weightForm = WeightForm()
    tempForm = TempForm()
    menu = ["Length", "Weight", "Temperature"]

    return render_template(
        "index.html",
        menu=menu,
        lengthForm=lengthForm,
        weightForm=weightForm,
        tempForm=tempForm,
    )


@app.route("/length_conversion", methods=["POST"])
def length_conversion():
    data = request.get_json()

    response = {}

    value = float(data["value"])
    from_unit = data["from_unit"]
    to_unit = data["to_unit"]

    converted_value = convert_length_numpy(value, from_unit, to_unit)

    response["converted_value"] = converted_value

    return jsonify(response)


@app.route("/weight_conversion", methods=["POST"])
def weight_conversion():
    data = request.get_json()

    response = {}

    value = float(data["value"])
    from_unit = data["from_unit"]
    to_unit = data["to_unit"]

    converted_value = convert_weight_numpy(value, from_unit, to_unit)

    response["converted_value"] = converted_value

    return jsonify(response)


@app.route("/temp_conversion", methods=["POST"])
def temp_conversion():
    data = request.get_json()

    response = {}

    value = float(data["value"])
    from_unit = data["from_unit"]
    to_unit = data["to_unit"]

    converted_value = convert_temperature(value, from_unit, to_unit)

    response["converted_value"] = converted_value

    return jsonify(response)


def convert_length_numpy(value, initial_unit, final_unit):
    """Convert a length value from one unit to another using NumPy.

    Args:
        value (float): The numerical value to convert.
        initial_unit (str): The initial unit of measurement (mm, cm, m, km, in, ft, yd, mi).
        final_unit (str): The final unit of measurement (mm, cm, m, km, in, ft, yd, mi).

    Returns:
        float: The converted value.

    Raises:
        ValueError: If the units of measurement are not valid.
    """
    conversion_factors = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1.0,
        "km": 1000.0,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.34,
    }
    if initial_unit not in conversion_factors or final_unit not in conversion_factors:
        raise ValueError(f"Invalid units: {initial_unit} and {final_unit}")

    return round(
        value * conversion_factors[initial_unit] / conversion_factors[final_unit], 3
    )


def convert_weight_numpy(value, initial_unit, final_unit):
    """Convert a weight value from one unit to another using NumPy.

    Args:
        value (float): The numerical value to convert.
        initial_unit (str): The initial unit of measurement (mg, g, kg, oz, lb).
        final_unit (str): The final unit of measurement (mg, g, kg, oz, lb).

    Returns:
        float: The converted value.

    Raises:
        ValueError: If the units of measurement are not valid.
    """
    conversion_factors = {
        "mg": 0.001,
        "g": 1.0,
        "kg": 1000.0,
        "oz": 28.3495,
        "lb": 453.592,
    }
    if initial_unit not in conversion_factors or final_unit not in conversion_factors:
        raise ValueError(f"Invalid units: {initial_unit} and {final_unit}")

    return round(
        value * conversion_factors[initial_unit] / conversion_factors[final_unit], 4
    )


def convert_temperature(value, initial_unit, final_unit):
    """Convert a temperature value from one unit to another.

    Args:
        value (float): The numerical value to convert.
        initial_unit (str): The initial unit of measurement (C, F, K).
        final_unit (str): The final unit of measurement (C, F, K).

    Returns:
        float: The converted value.

    Raises:
        ValueError: If the units of measurement are not valid.
    """
    if initial_unit == final_unit:
        return value

    if initial_unit not in ["C", "F", "K"] or final_unit not in ["C", "F", "K"]:
        raise ValueError(f"Invalid units: {initial_unit} and {final_unit}")

    # Convert initial temperature to Celsius
    if initial_unit == "F":
        value = (value - 32) * 5.0 / 9.0
    elif initial_unit == "K":
        value = value - 273.15

    # Convert Celsius to final unit
    if final_unit == "F":
        return value * 9.0 / 5.0 + 32
    elif final_unit == "K":
        return value + 273.15
    else:
        return value


if __name__ == "__main__":
    app.run(debug=True)
