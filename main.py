import requests
from pydantic import validate_call

from errors import ERROR_DICT
from models import RequestInput, RequestResponse, VerifyInput, VerifyResponse, UnVerifiedResponse


class ZarinPal:
    def __init__(self, merchant_id: str) -> None:
        self.merchant_id: str = merchant_id

    @validate_call
    def request(self, data: RequestInput) -> RequestResponse:
        result = requests.post(
            "https://api.zarinpal.com/pg/v4/payment/request.json",
            json={"merchant_id": self.merchant_id, **data.model_dump(exclude_none=True)}
        ).json()
        if result["data"] and result["data"]["code"] == "100":
            return RequestResponse(**result)

        else:
            raise ERROR_DICT.get(
                result["errors"]["code"],
                Exception(f'Code: {result["errors"]["code"]}, Message: {result["errors"]["message"]}')
            )

    @staticmethod
    def get_payment_link(authority: str) -> str:
        return f"https://www.zarinpal.com/pg/StartPay/{authority}"

    @validate_call
    def verify(self, data: VerifyInput) -> VerifyResponse:
        result = requests.post(
            "https://api.zarinpal.com/pg/v4/payment/verify.json",
            json={"merchant_id": self.merchant_id, **data.model_dump(exclude_none=True)}
        ).json()
        if result["data"] and result["data"]["code"] == "100":
            return VerifyResponse(**result)

        else:
            raise ERROR_DICT.get(
                result["errors"]["code"],
                Exception(f'Code: {result["errors"]["code"]}, Message: {result["errors"]["message"]}')
            )

    def un_verified(self) -> UnVerifiedResponse:
        """
        متد unverified در مواردی استفاد می‌شود که نیازمند اطلاعات پرداخت‌هایی هستید
        که توسط وب‌سرویس به درستی انجام شده است، اما متد verifyروی آنها اعمال نشده است.
        به عبارت دیگر این متد لیست پرداخت‌های موفق اعتبارسنجی نشده را نشان می‌دهد.
        نكته : حداکثر تعداد تراکنشی که در این روش بازگردانی می‌شوند،
        محدود به ۱۰۰ تراکنش آخری است که اعتبارسنجی نشده اند.
        :return: UnVerifiedResponse
        """
        result = requests.post(
            "https://api.zarinpal.com/pg/v4/payment/unVerified.json",
            json={"merchant_id": self.merchant_id}
        ).json()
        if result["data"] and result["data"]["code"] == "100":
            return UnVerifiedResponse(**result)

        else:
            raise ERROR_DICT.get(
                result["errors"]["code"],
                Exception(f'Code: {result["errors"]["code"]}, Message: {result["errors"]["message"]}')
            )
