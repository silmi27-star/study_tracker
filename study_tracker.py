records = []
while True:
    print("===== STUDY TRACKER =====")
    print()
    print("1. Add Study Session")
    print("2. View Study Records")
    print("3. View Total Study Time")
    print("4. Exit")
    choose = input("choose an option: ")
    if choose == '1':
        print("1. Which subject did you study?")
        choose_1 = input("subject: ")
        print("2. How many minutes did you study?")
        choose_2 = input("minutes: ")
        choose_2 = int(choose_2)
        print(f"{choose_1} studied for {choose_2} minutes.")
        choose_3 = [choose_1, choose_2]
        records.append(choose_3)
    elif choose == '2':
        for i in records:
            print(f"{i[0]} - {i[1]} minutes")
    elif choose == '3':
        choose_4 = 0
        for i in records:
            choose_4 = choose_4 + i[1]
        print(f"Total study time : {choose_4} minutes")
    elif choose == '4':
        print("Goodbye!")
        break
