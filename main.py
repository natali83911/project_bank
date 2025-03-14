# from src.masks import get_mask_card_number, get_mask_account
# card_number = "1234567890123456"
# masked_card = get_mask_card_number(card_number)
# print(f"Masked card number: {masked_card}")
#
# account_number = "12345678901234567890"
# masked_account = get_mask_account(account_number)
# print(f"Masked account number: {masked_account}")


# from src.widget import mask_account_card, get_date
# number = "Visa Classic 6831982476737658"
# masked_number = mask_account_card(number)
# print(masked_number)
#
# date = "2024-03-11T02:26:18.671407"
# correct_date = get_date(date)
# print(correct_date)


from src.processing import filter_by_state, sort_by_date
list1 = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]
result = filter_by_state(list1)
print(result)

result = sort_by_date(list1)
print(result)