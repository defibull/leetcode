from collections import Counter
def fractionToDecimal(numerator, denominator):
    num_ans = float(numerator)/float(denominator)
    negative = "-" if num_ans < 0 else ""
    dec_list = []
    dec_non_repeat = ""
    count_remainders = {}
    remainder = numerator % denominator
    repeat = False
    i = 0
    while remainder:
        if remainder not in count_remainders:
            count_remainders[remainder] = i
        else:
            repeat = True
            break
        remainder*=10
        dec_list.append(str(remainder//denominator))
        remainder = remainder%denominator
        i+=1
    if repeat:
        dec_non_repeat = dec_list[:count_remainders[remainder]]
        dec_list = dec_list[count_remainders[remainder]:i+1]
        dec_list.append(")")
        dec_list.insert(0, "(")

    ans = negative + str(int(float(numerator)/denominator))
    if len(dec_list) > 0 or len(dec_non_repeat) > 0:
        ans+= "." +"".join(dec_non_repeat)+"".join(dec_list)
    return ans

print fractionToDecimal(-1, -2147483648)
