(1..1000).select{|n| [3,5].all?{|m| (n%m).zero? } }.inject(:+)
