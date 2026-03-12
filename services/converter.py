import json
from fastapi import HTTPException, status
from pathlib import Path

RATE_FILE = Path("data/rates.json")

def load_rates():
    try:
        with open("data/rates.json", "r") as f:
            rates = json.load(f)
        return rates
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to load currency rates"
        )
    
def load_rate():
    if RATE_FILE.exists():
        with open(RATE_FILE, "r") as f:
            return json.load(f)
    return {}    


def save_rates(data):
    with open(RATE_FILE, "w") as f:
        json.dump(data, f, indent=4)




def add_currency(code, rate):
    rates = load_rates()
    code = code.upper()
    if code in rates:
        return False
    rates[code] = rate
    save_rates(rates)
    return True


def convert_currency(from_currency: str, to_currency: str, amount: float) -> float:
    rates = load_rates()

    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    if from_currency not in rates or to_currency not in rates:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Currency not supported: {from_currency} or {to_currency}"
        )


    usd_amount = amount / rates[from_currency]
    result = usd_amount * rates[to_currency]
    return round(result, 2)