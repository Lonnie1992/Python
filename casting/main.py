# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

#  Add your code after this line
leek_price = 2
leek = 'Leek is ' + str(leek_price) + ' ' + 'euro per kilo.'
print(leek)
leek_ordered = 'leek 4'
leek4 = leek_ordered.find('4')
# finding the index of '4' because it can be anywhere in the string and i dont want to make a counting mistake
leek_index = leek_ordered.index('4')
# creating a variable with the amount ordered as integer, to use in calculation
order_quantity = int(leek_ordered[leek_index])
sum_total = leek_price * order_quantity
print(sum_total)

broccoli = 2.34
broccoli_ordered = 1.6
sum_broccoli = str(round(broccoli * broccoli_ordered, 2))
print(str(broccoli_ordered) + 'kg broccoli costs ' + sum_broccoli + 'e')
