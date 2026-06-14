import random
import string

coupon = ''.join(
    random.choices(
        string.ascii_uppercase + string.digits,
        k=8
    )
)

print("Coupon Code : ",coupon)
