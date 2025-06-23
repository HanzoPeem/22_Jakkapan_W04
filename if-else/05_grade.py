score = int(input("Enter your score :"))
'''
>90 A เก่งเกิ้นน!!!
>80 B เกงมาก 
>70 C ชื่นชม
>60 D พอใช้
<60 F ตกอิเวง!!!
'''
if score >=90:
    grade = "A"
    comment = "เก่งเกิ้น!!!"
elif score >=80:
    grade = "B"
    comment = "เก่งมาก"
elif score >=70:
    grade = "C"
    comment = "ชื่นชม"
elif score >=60:
    grade = "D"
    comment = "พอใช้"
else:
    grade = "F"
    comment = "ตกอิเวง!!!"
    
print(f"คะแนน : {score}")
print(f"ได้เกรด : {grade}")
print(f"ความเห็น : {comment}")
