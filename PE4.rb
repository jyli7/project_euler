#Write a method that tests a number for palindromocity
#Write a script that loops through products of two 3-digit numbers

def palindrome?(number)
  number = number.to_s
  number_middle_pt = ((number.length) / 2).round - 1
  (0..number_middle_pt).each do |index|
    reverse_index = -1*(index+1)
    if number[index] != number[reverse_index]
      puts "false"
      return false
    end
  end
  puts "true"
  return true
end

999.downto(100) do |num1|
  (999).downto(900) do |num2|
    product = num1*num2
    if palindrome?(product)
      puts product
      return product
    end
  end
end