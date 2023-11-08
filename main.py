import requests
from enum import Enum
from pydantic import BaseModel


class CurrencyEnum(Enum):
    IRT = "IRT"
    IRR = "IRR"


class MetaData(BaseModel):
    mobile: str = None
    email: str = None
    order_id: str = None


class RequestResponseData(BaseModel):
    code: int
    message: str
    authority: str
    fee_type: str
    fee: int


class VerifyResponseData(BaseModel):
    code: int
    message: str
    card_hash: str
    card_pan: str
    ref_id: int
    fee_type: str
    fee: int


class RequestInput(BaseModel):
    amount: int
    description: str
    callback_url: str
    currency: CurrencyEnum = None
    metadata: MetaData = None


class VerifyInput(BaseModel):
    authority: str
    amount: int


class RequestResponse(BaseModel):
    data: RequestResponseData
    errors: list = []


class VerifyResponse(BaseModel):
    data: VerifyResponseData
    errors: list = []


class ZarinPal:
    def __init__(self, merchant_id: str) -> None:
        self.merchant_id: str = merchant_id

    def request(self, data: RequestInput) -> RequestResponse:
        result = requests.post(
            "https://api.zarinpal.com/pg/v4/payment/request.json",
            json={"merchant_id": self.merchant_id, **data.model_dump(exclude_none=True)}
        ).json()
        if result["data"] and not result["errors"] == 100:
            return RequestResponse(**result)

        else:
            print(result)

    @staticmethod
    def get_payment_link(authority: str) -> str:
        return f"https://www.zarinpal.com/pg/StartPay/{authority}"

    def verify(self, data: VerifyInput) -> VerifyResponse:
        result = requests.post(
            "https://api.zarinpal.com/pg/v4/payment/verify.json",
            json={"merchant_id": self.merchant_id, **data.model_dump(exclude_none=True)}
        ).json()
        if result["data"] and not result["errors"]:
            return VerifyResponse(**result)

        else:
            print(result)
