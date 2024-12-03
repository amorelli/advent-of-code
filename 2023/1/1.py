file = open('input.txt', 'r')
lines = file.readlines()

def get_total():
    total = 0
    for line in lines:
        print('line:', line)
        left = 0
        right = len(line) - 1
        tens = ""
        ones = ""
        while (left < right):
            print("left:", left, line[left])
            print("tens", tens)
            print("right:", right, line[right])
            print("ones", ones)
            if len(tens) == 0:
                if line[left].isnumeric():
                    tens = line[left]
                else:
                    left += 1
            
            if len(ones) == 0:
                if line[right].isnumeric():
                    ones = line[right]
                else:
                    right -= 1
            if (len(tens) > 0 and len(ones) > 0):
                break
        
        if len(tens) > 0 and len(ones) > 0:
            current = tens + ones
            print(line, tens, ones, current, total)
            total += int(current)
            
    print(total)
    return total

get_total()