# from src.masks import get_mask_card_number, get_mask_account
# card_number = "1234567890123456"
# masked_card = get_mask_card_number(card_number)
# print(f"Masked card number: {masked_card}")
#
# account_number = "12345678901234567890"
# masked_account = get_mask_account(account_number)
# print(f"Masked account number: {masked_account}")


from src.widget import mask_account_card, get_date
number = "Visa Classic 6831982476737658"
masked_number = mask_account_card(number)
print(masked_number)

date = "2024-03-11T02:26:18.671407"
correct_date = get_date(date)
print(correct_date)
