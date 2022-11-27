#1
card = input('Введите номер карты: ')
def card_hide(card123):
    return '*' * (len(card123)-4) + card123[-4:]
a = card_hide(card)
print(a)

#2
def isPalindrome(string):
	left_pos = 0
	right_pos = len(string) - 1
	
	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
	return True
print(isPalindrome('rttttr')) 