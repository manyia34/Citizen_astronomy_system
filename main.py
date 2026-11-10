# main.py
# starting point of the project - shows a menu and runs each milestone

from milestones.milestone_1 import milestone_1
from milestones.milestone_2 import milestone_2
from milestones.milestone_3 import milestone_3
from milestones.milestone_5 import full_session, show_log


def main():
    while True:
        print("\n========== CITIZEN ASTRONOMY SYSTEM ==========")
        print("1. Milestone 1 - Record one observation")
        print("2. Milestone 2 - Full night session")
        print("3. Milestone 3 - Inheritance and polymorphism")
        print("4. Milestone 4 + 5 - Full session, report and log")
        print("5. Milestone 5 - View saved log and metadata")
        print("0. Exit")

        choice = input("Enter your choice : ").strip()

        if choice == "1":
            milestone_1()
        elif choice == "2":
            milestone_2()
        elif choice == "3":
            milestone_3()
        elif choice == "4":
            full_session()
        elif choice == "5":
            show_log()
        elif choice == "0":
            print("Goodbye, clear skies!")
            break
        else:
            print("Invalid choice, please try again")


if __name__ == "__main__":
    main()
