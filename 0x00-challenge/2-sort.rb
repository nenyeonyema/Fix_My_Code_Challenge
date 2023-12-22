###
#
#  Sort integer arguments (ascending) 
#
###

result = []

ARGV.each do |arg|
    # Skip if not an integer
    next unless arg =~ /^-?[0-9]+$/

    # Convert to integer
    i_arg = arg.to_i
    
    # Insert result at the right position
    inserted = false
    result.each_with_index do |item, index|
        if i_arg < item
            result.insert(index, i_arg)
            inserted = true
            break
        end
    end

    # If not inserted yet (i_arg is the largest so far)
    result << i_arg unless inserted
end

puts result
