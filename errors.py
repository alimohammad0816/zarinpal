# error code 101
class AlreadyPaidError(Exception):
    def __str__(self):
        return "تراکنش موفق بوده و یک‌بار قبلا عملیات verifyبر روی آن انجام شده است."


# error code -54
class InvalidAuthorityError(Exception):
    def __str__(self):
        return "اتوریتی نامعتبر است."


# error code -53
class InvalidMerchantSessionError(Exception):
    def __str__(self):
        return "پرداخت متعلق به این مرچنت کد نیست."


# error code -52
class ZarinPalError(Exception):
    def __str__(self):
        return "خطای غیر منتظره‌ای رخ داده است. پذیرنده مشکل خود را به امور مشتریان زرین‌پال ارجاع دهد."


# error code -51
class FailedPaymentError(Exception):
    def __str__(self):
        return "پرداخت ناموفق"


# error code -50
class InvalidPaymentAmountError(Exception):
    def __str__(self):
        return "مبلغ پرداخت شده با مقدار مبلغ ارسالی در متد وریفای متفاوت است."


# error code -10
class InvalidIpOrMerchantError(Exception):
    def __str__(self):
        return "ای پی یا مرچنت كد پذیرنده صحیح نیست."


# error code -11
class MerchantIsNotActiveError(Exception):
    def __str__(self):
        return "مرچنت کد فعال نیست، پذیرنده مشکل خود را به امور مشتریان زرین‌پال ارجاع دهد."


# error code -12
class TooManyAttemptsError(Exception):
    def __str__(self):
        return "تلاش بیش از دفعات مجاز در یک بازه زمانی کوتاه به امور مشتریان زرین پال اطلاع دهید"


# error code -15
class TerminalIsSuspendError(Exception):
    def __str__(self):
        return "درگاه پرداخت به حالت تعلیق در آمده است، پذیرنده مشکل خود را به امور مشتریان زرین‌پال ارجاع دهد."


# error code -16
class SilverAccessError(Exception):
    def __str__(self):
        return "سطح تایید پذیرنده پایین تر از سطح نقره ای است."


# error code -17
class BlueAccessError(Exception):
    def __str__(self):
        return "محدودیت پذیرنده در سطح آبی"


# error code -30
class FloatingWagesError(Exception):
    def __str__(self):
        return "پذیرنده اجازه دسترسی به سرویس تسویه اشتراکی شناور را ندارد."


# error code -31
class TerminalNotAllowAcceptWagesError(Exception):
    def __str__(self):
        return ("حساب بانکی تسویه را به پنل اضافه کنید. مقادیر وارد شده برای تسهیم درست نیست."
                "پذیرنده جهت استفاده از خدمات سرویس تسویه اشتراکی شناور،"
                "باید حساب بانکی معتبری به پنل کاربری خود اضافه نماید.")


# error code -32
class OverLoadMaxAmountError(Exception):
    def __str__(self):
        return "مبلغ وارد شده از مبلغ کل تراکنش بیشتر است."


# error code -33
class InvalidWagesFloatingError(Exception):
    def __str__(self):
        return "درصدهای وارد شده صحیح نیست."


# error code -35
class WagesMaxLimitPartsError(Exception):
    def __str__(self):
        return "تعداد افراد دریافت کننده تسهیم بیش از حد مجاز است."


# error code -36
class MinimumWagesAmountError(Exception):
    def __str__(self):
        return "حداقل مبلغ جهت تسهیم باید ۱۰۰۰۰ ریال باشد"


# error code -37
class InActiveIbanError(Exception):
    def __str__(self):
        return "یک یا چند شماره شبای وارد شده برای تسهیم از سمت بانک غیر فعال است."


# error code -38
class IbanNotSetError(Exception):
    def __str__(self):
        return "خطا٬عدم تعریف صحیح شبا٬لطفا دقایقی دیگر تلاش کنید."


# error code -39
class WagesError(Exception):
    def __str__(self):
        return "خطایی رخ داده است به امور مشتریان زرین پال اطلاع دهید"
