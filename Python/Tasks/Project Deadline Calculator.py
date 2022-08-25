import datetime

deadline = input("Input the deadline for the project (DD/MM/YYYY): ")
deadlineDate = datetime.datetime.strptime(deadline, "%d/%m/%Y").strftime("%d-%m-%Y")

today = input("Input today's date (DD/MM/YYYY): ")
todayDate = datetime.datetime.strptime(today, "%d/%m/%Y").strftime("%d-%m-%Y")

print(deadlineDate - todayDate)
