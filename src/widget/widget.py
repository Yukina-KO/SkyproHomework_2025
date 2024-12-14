from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    if account_card[0:4] == "Счет" or account_card[0:4] == "Счёт":
        mask_card = account_card.replace(account_card[-20:], get_mask_account(account_card[-20:]))
    else:
        mask_card = account_card.replace(account_card[-16:], get_mask_card_number(account_card[-16:]))
    return mask_card
