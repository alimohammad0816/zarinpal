from enum import Enum
from typing import List
from pydantic import BaseModel


class CurrencyEnum(Enum):
    IRT = "IRT"
    IRR = "IRR"


class MetaData(BaseModel):
    mobile: str = None
    email: str = None
    order_id: str = None
    card_pan: str = None


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


class AuthorityData(BaseModel):
    authority: str
    amount: int
    callback_url: str
    referer: str
    date: str


class UnVerifiedResponseData(BaseModel):
    code: int
    message: str
    authorities: List[AuthorityData] = []


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


class UnVerifiedResponse(BaseModel):
    data: UnVerifiedResponseData
    errors: list = []
