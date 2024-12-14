from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    if account_card[0:4] == "Счет" or account_card[0:4] == "Счёт":
        mask_card: str = account_card.replace(account_card[-20:], get_mask_account(account_card[-20:]))
    else:
        mask_card: str = account_card.replace(account_card[-16:], get_mask_card_number(account_card[-16:]))
    return mask_card


def get_date(date: str) -> str:
    date_split = date[0:10].split("-")
    return f"{date_split[2]}.{date_split[1]}.{date_split[0]}"
