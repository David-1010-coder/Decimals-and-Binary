decimal_numbers = 25, 21, 69
for num in decimal_numbers:
    original_num = num
    binary_string = ""
while num > 0:
        remainder = num % 2           
        binary_string = str(remainder) + binary_string  
        num = num // 2        
if original_num == 0:
        binary_string = "0"
print("Decimal" {original_num} "in Binary is:"  {binary_string})   