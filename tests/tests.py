from src.masks import get_mask_account, get_mask_card_number
from src.widget.widget import mask_account_card, get_date

print(get_mask_card_number("1234567891234567"))
print(get_mask_account("12345678901234567890"))
print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(get_date("2024-03-11T02:26:18.671407"))
