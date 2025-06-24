num1 = input("ใส่ตัวเลขแรก : ")
num2 = input("ใส่ตัวเลขที่สอง : ")
input3 = input("เลือกวิธีดำเดินการ : ")
num1 = int(num1)
num2 = int(num2)
if input3 == "+":
    result = num1 + num2  
elif input3 == "-":     
    result = num1 - num2
elif input3 == "*":
    result = num1 * num2
elif input3 == "/":      
    if num2 != 0:
        result = num1 / num2
    else:
        result = "ไม่สามารถหารด้วยศูนย์ได้"
print(f"ผลลัพธ์ : {result}")
