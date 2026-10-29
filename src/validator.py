def dimension_check(data_frame):
    rows, columns = data_frame.shape
    total_values = data_frame.size

    return {
        "rows": rows,
        "columns": columns,
        "total_values": total_values
    }


def missing_values_check(data_frame):
    total_missing_values = data_frame.isna().sum().sum()
    return int(total_missing_values)

def format_validation(data_frame):
    non_numeric_columns = data_frame.select_dtypes(exclude="number").columns.tolist()

    if len(non_numeric_columns) == 0:
        return ("All columns have numeric data types.")
    else:
        return f"Non numeric columns: {non_numeric_columns}"
    

def range_validation(data_frame, min_value, max_value):
    numeric_data = data_frame.select_dtypes(include="number")

    out_of_range = (
        (numeric_data > max_value) |
        (numeric_data < min_value)
    )

    if out_of_range.any().any():
        return "Values outside of the allowed range were found."
    else:
        return "All values are within the allowed range."

def generate_validation_report(data_frame,min_value,max_value):
    dimensions = dimension_check(data_frame)
    missing_values = missing_values_check(data_frame)
    formating = format_validation(data_frame)
    range_values = range_validation(data_frame,min_value,max_value)
    
    return {
        "dimensions":dimensions,
        "missing_values":missing_values,
        "format_validation":formating,
        "range_validation":range_values
    }