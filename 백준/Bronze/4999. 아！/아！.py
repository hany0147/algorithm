patient = input()
doctor = input()
patient_num = patient.count('a')
doctor_num = doctor.count('a')

if patient_num >= doctor_num:
    print('go')
else:
    print('no')