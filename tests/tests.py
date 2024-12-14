from src.masks import get_mask_account, get_mask_card_number
from src.widget.widget import mask_account_card

result1 = get_mask_card_number(1234567891234567)
result2 = get_mask_account("12345678901234567890")
print(result1)
print(result2)
print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
