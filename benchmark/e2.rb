def multiple range, numbers
 (1..(range-1)).select{|n| numbers.any?{|m| (n%m).zero? } }.inject(:+)
end

puts multiple 1000000, [3, 5]
