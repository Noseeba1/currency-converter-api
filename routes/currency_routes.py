from fastapi import APIRouter, status ,HTTPException
from models.schemas import ConvertRequest, ConvertResponse ,Currency, CurrencyResponse
from services.converter import convert_currency ,add_currency,load_rate

router = APIRouter(
    prefix="/currency",
    tags=["Currency"]
)

# GET endpoint
@router.get("/convert", response_model=ConvertResponse, status_code=status.HTTP_200_OK)
def convert_get(from_currency: str, to_currency: str, amount: float):
    result = convert_currency(from_currency, to_currency, amount)
    return ConvertResponse(
        from_currency=from_currency.upper(),
        to_currency=to_currency.upper(),
        amount=amount,
        result=result
    )

# POST endpoint
@router.post("/", response_model=CurrencyResponse)
def add_currency_route(currency: Currency):
    code = currency.code.upper()
    success = add_currency(currency.code, currency.rate_to_usd)
    if not success:
        raise HTTPException(status_code=400, detail="Currency already exists")
    rates = load_rate()
    return {"code": currency.code, "rate_to_usd": currency.rate_to_usd}



