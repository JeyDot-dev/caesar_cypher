alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
retry = "yes"
while retry == "yes" :
  c_or_d  = int(input("Would you like to 1.cypher or 2.decypher ? type number : "))
  string  = list(input("Input which string you want to treat :\n").lower())
  ceasar             = int(input("Enter the number : "))
  
  def rot(string, ceasar, c_or_d, alpha) :
    if c_or_d == 2 :
      ceasar *= -1
    for c in range(0, len(string)) :
      if not string[c].isalpha() :
        continue
      total = alpha.index(string[c]) + ceasar
      while total > 25 or total < 0 :
        total %= 26
      string[c] = alphabet[total]
    return string
  print(f"Here you go :\n{''.join(rot(string, ceasar, c_or_d, alphabet))}")
  retry = input("Would you like to continue ? yes or no :")
print("Ok see ya.")
