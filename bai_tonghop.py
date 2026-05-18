import random

patient_name = input("Nhập tên bệnh nhân")
patient_gender = input("Nhập giới tính")
patient_bỉthyear = int(input("Nhập năm sinh bệnh nhân"))
patient_phonenumb = int(input("Nhập sdt"))
patient_email = input("Nhập email bệnh nhân")
patient_symptoms = input("Nhập triệu chứng ban đầu")
patient_medbill = float(input("Nhập chi phí khám của bệnh nhân"))






random_number = random.randint(100,999)
print("--------------------------------------")
print(f"Mã BN : BN{patient_bỉthyear}{random_number}")
print(f"Tên : {patient_name}", type(patient_name))
print(f"Giới tính : {patient_gender}", type(patient_gender))
print(f"Năm sinh : {patient_bỉthyear}", type(patient_bỉthyear))
print(f"Điện thoại : {patient_phonenumb}",type(patient_phonenumb))
print(f"Email : {patient_email}",type(patient_email))
print(f"Triệu chứng : {patient_symptoms}",type(patient_symptoms))
print(f"Chi phí {patient_medbill}",type(patient_medbill))