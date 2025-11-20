from decimal import Decimal
from datetime import datetime


def serialize_value(value):
    if isinstance(value, Decimal):
        return float(value)   # or str(value) if you want exact precision
    if isinstance(value, datetime):
        return value.isoformat()  # '2025-03-21T19:21:12'
    if isinstance(value, (bytes, bytearray)):
        return int.from_bytes(value, byteorder='little')  # e.g. 0/1 for BIT
    return value