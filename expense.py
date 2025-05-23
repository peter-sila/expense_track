import json
import os
import datetime



def load_json(filename):
   if not os.path.exists(filename) or os.path.getsize(filename) == 0:
      with open("expense_track/expense.json", "w") as f:
         return json.dump([], f)
   try:
      with open(filename, "r") as f:
         return json.load(f)
   except json.JSONDecodeError:
      return []

def add_expense(expense_id):
   expense = {}

   expense["id"] = str(expense_id)
   expense["description"] = input("Enter your expense: ").lower()
   expense["amount"] = input(f"Enter the amount spend on {expense["description"]}: ")
   expense["created_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   expense["updated_at"] = ""

   return expense

def save_update(filename, data):
   with open(filename, "w") as f:
      json.dump(data, f, indent=4)
   print(f"Updated data saved to '{filename}'.")

def update_expense(filename):
   expenses = load_json(filename)
   if not expenses:
      print("No expenses to update.")
      return
   
   ex_id = input("Enter the id of expense to update: ")
   found = False

   for expense in expenses:
      if expense["id"] == ex_id:
         print(f"\nFound expense: {expense['description']}")
         new_amount = input("Enter new amount: ")
         expense["amount"] = new_amount
         expense["updated_at"] = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
         found = True
         print("Expense updated successfully.")
         break

   if found:
      save_update(filename, expenses)
   else:
      print("Expense not found.")


def delete_expense(filename):
   expenses = load_json(filename)
   expense_id = input("Enter id of expense to delete: ")

   new_list = [expense for expense in expenses if expense["id"] != expense_id]

   if len(new_list) < len(expenses):
      save_update(filename, new_list)
      print("Expense deleted successfully.")
   else:
      print("Expense not found.")


   
def view_all_expense(filename):
   print("Your expenses.")
   expenses = load_json(filename)
   for expense in expenses:
      print(expense)
   
def view_summary_expense(filename):
   print("Choose a summary.")
   print("1. Based on amount.")
   print("2. Based on period.")
   print("3. Based on description")
   print("4. Exit\n")

   summary = input("Choose an option: ")

   if summary == "1":
      print("Enter amount range to filter.")
      low = input("Enter lowest amount: ")
      high = input("Enter the highest amount: ")

      expenses = load_json(filename)
      filter_expense = [expense for expense in expenses if expense["amount"] >= low and expense["amount"] <= high]

      if filter_expense:
         print("Expense summary based on amount.\n")
         for expense in filter_expense:
            print(expense)
      else:
         print("No expense found.\n")
         exit

   elif summary == "2":
      print("Enter date range to filter.")
      start = input("Enter start date (Y-M-D): ")
      end = input("Enter the end date (Y-M-D): ")

      expenses = load_json(filename)
      filter_expense = [expense for expense in expenses if expense["created_at"] >= start and expense["created_at"] <= end]

      if filter_expense:
         print("Expense summary based on date.\n")
         for expense in filter_expense:
            print(expense)
      else:
         print("No expense found.\n")
         exit

   elif summary == "3":
      print("Enter expense description to filter.")
      desc = input("Enter description: ").lower()

      expenses = load_json(filename)
      filter_expense = [expense for expense in expenses if expense["description"] == desc]

      if filter_expense:
         print("Expense summary based on description.\n")
         for expense in filter_expense:
            print(expense)
      else:
         print("No expense found.\n")
         exit

   elif summary == "4":
      print("Exitend successfully.")
      exit
   else:
      print("Enter a valid number.")
      exit

def main():
   filename = "expense_track/expense.json"

   print("Welcome, Choose the activity you want to do.\n")
   print("1. Add Expense.")
   print("2. Update Expense.")
   print("3. Delete Expense.")
   print("4. View All Expenses.")
   print("5. View Specific Expenses.")
   print("6. Exit.\n")
   action = int(input("Choose what to do (1 or 2 or 3 or 4 or 5 or 6): "))

   if action == 1:
      expenses_list = load_json(filename)
      expense_id = len(expenses_list)
      expense_id += 1
      
      while True:
         expense = add_expense(expense_id)
         expenses_list.append(expense)

         more = input("Do you want to add another expense? (yes/no): ").lower()
         if more != "yes":
            break

      save_update(filename, expenses_list)

   elif action == 2:
      update_expense(filename)
   elif action == 3:
      delete_expense(filename)
   elif action == 4:
      view_all_expense(filename)
   elif action == 5:
      view_summary_expense(filename)
   elif action == 6:
      print("Exited the program successfully.")
      exit
   else:
      print("Enter a valid choice.")
      exit
   
if __name__ == "__main__":
   main()
   

