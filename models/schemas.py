from pydantic import BaseModel, Field, PositiveFloat

class ConvertRequest(BaseModel):
    from_currency: str = Field(..., description="Original currency", example="USD")
    to_currency: str = Field(..., description="Request currency", example="YER")
    amount: PositiveFloat = Field(..., description="Amount to transfer", example=100)

class ConvertResponse(BaseModel):
    from_currency: str
    to_currency: str
    amount: float
    result: float

class Currency(BaseModel):
    code: str
    rate_to_usd: float

class CurrencyResponse(BaseModel):
    code: str
    rate_to_usd: float    