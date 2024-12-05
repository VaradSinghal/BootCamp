def convert_number_to_words(n):
  
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    if n == 0:
        return "Zero"
    
    words = []
    
    if n >= 100:
        words.append(ones[n // 100] + " Hundred")
        n %= 100
    
   
    if n >= 20:
        words.append(tens[n // 10])
        n %= 10
        
    if 0 < n < 10:
        words.append(ones[n])
    elif 10 <= n < 20:
        words.append(teens[n - 10])

    return " ".join(words)


number = int(input("Enter a number: "))
print(convert_number_to_words(number))
