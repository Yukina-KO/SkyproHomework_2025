from src.masks import get_mask_account, get_mask_card_number

result1 = get_mask_card_number(1234567891234567)
result2 = get_mask_account("12345678901234567890")
print(result1)
print(result2)
