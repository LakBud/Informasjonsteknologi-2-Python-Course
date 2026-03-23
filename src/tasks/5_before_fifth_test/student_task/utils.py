def to_int(value):
    # Convert a value to int safely; treat None as 0 and remove spaces
    if value is None:
        return 0
    return int(str(value).replace(" ", ""))