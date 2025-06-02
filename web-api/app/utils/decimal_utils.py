from decimal import Decimal, ROUND_HALF_UP

def get_decimal(value:str) -> Decimal:
    return Decimal(value).quantize(Decimal('.01'))

def get_decimal(value:float) -> Decimal:
    return Decimal(value).quantize(Decimal('.01'))