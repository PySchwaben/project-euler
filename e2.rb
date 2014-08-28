h = Hash.new{|h,k| k < 2 ? k : h[k-1] + h[k-2]}
(1..20).map{|i| h[i] }.to_s
