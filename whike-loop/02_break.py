numbers = [12,13,14,15,16,17]
divisor = 6

print(f"ตัวที่หาร {divisor} ลงตัว :")

for i in numbers:
    if i % divisor == 0:
        print(f"{i} หาร {divisor} ลงตัว(={i // divisor})")
        found += 1
        
        if found == 3:
            break