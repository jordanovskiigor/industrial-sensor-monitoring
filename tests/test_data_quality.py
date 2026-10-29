import pandas as pd

from src.validator import (
    dimension_check,
    missing_values_check,
    format_validation,
    range_validation,
    generate_validation_report
)

def test_dimension_check():
    data = pd.DataFrame({
        "PS1":[10,20,30],
        "PS2":[40,50,60]
    })
    result = dimension_check(data)
    assert result['rows'] == 3
    assert result['columns'] == 2
    assert result['total_values'] == 6

def test_missing_values_check():
    data = pd.DataFrame({
        "PS1":[150.2,None,148.7],
        "PS2":[200.1,199.8,None]
    })

    result = missing_values_check(data)
    assert result == 2.

def test_range_validation_bellow_minimum():
    data = pd.DataFrame({
        "PS1": [150.0,90.0,200.0]
    })

    result = range_validation(data,100,250)
    assert result == "Values outside of the allowed range were found."

def test_range_validation_above_maximum():
    data = pd.DataFrame({
        "PS1": [150.0,180.0,260.0]
    })

    result = range_validation(data,100,250)
    assert result == "Values outside of the allowed range were found."

def test_format_validation_numeric_data():
    data = pd.DataFrame({
        "PS1":[150.2,148.7,151.1],
        "PS2":[200.1,199.8,201.3]
    })

    result = format_validation(data)
    assert result == 'All columns have numeric data types.'

def test_format_validation_non_numeric_data():
    data = pd.DataFrame({
        "PS1": [150.2, 148.7, 151.1],
        "status": ["normal", "normal", "warning"]
    })

    result = format_validation(data)

    assert result == "Non numeric columns: ['status']"

def test_generate_validation_report():
    data = pd.DataFrame({
        "PS1": [150.0, 180.0, 200.0],
        "PS2": [160.0, 190.0, 210.0]
    })

    result = generate_validation_report(data, 100, 250)

    assert result["dimensions"]["rows"] == 3
    assert result["dimensions"]["columns"] == 2
    assert result["dimensions"]["total_values"] == 6

    assert result["missing_values"] == 0

    assert result["format_validation"] == (
        "All columns have numeric data types."
    )

    assert result["range_validation"] == (
        "All values are within the allowed range."
    )

def test_generate_validation_report_with_missing_values():
    data = pd.DataFrame({
        "PS1": [150.0, None, 200.0],
        "PS2": [160.0, 190.0, 210.0]
    })

    result = generate_validation_report(data, 100, 250)

    assert result["missing_values"] == 1

def test_generate_validation_report_with_non_numeric_data():
    data = pd.DataFrame({
        "PS1": [150.0, 180.0, 200.0],
        "status": ["normal", "normal", "warning"]
    })

    result = generate_validation_report(data, 100, 250)

    assert result["format_validation"] == (
        "Non numeric columns: ['status']"
    )