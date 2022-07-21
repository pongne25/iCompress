def encode(input):
    if len(input)==0:
        return ""

        count =1
        prev_char =input(0)
        output =[]
        for char in input[1:]:
            if char !=prev_char:
                output.append(f"{count}{prev_char}")
                count =1
                prev_char =char
            else:
                count+=1
        else:
             output.append(f"{count}{prev_char}")



        return "".join(output)


def decode(inpu):
    ouput= ""
    amount= ""
    for char in input:
        if char.isdigit():
            amount_str =char
        else:
            amount =int(amount_str)
            output +=char *amount
            amount_str
    return output


text="wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"
compressed_text =encode(text)
print(f":compressed_text   {compressed_text}")
#assert compressed_text== "12W1B123B24WW1B14W", f"EXPECTED: 12W1B123B24WW1B14W   OBTAINED: {compressed_text}"
decompressed_text = decode (compressed_text)
print(f"compressed_text ={decompressed_text}")
assert decompressed_text == text