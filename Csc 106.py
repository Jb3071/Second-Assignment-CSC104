print("UBA BANK USSD CODE:")
USSD = input("please type in your bank USSD code:")
option = int(input("1.Airtime_self \n 2.Airtime_others \n 3.Transfer_UBA \n 4.Transfer_otherBanks \n 5. Transfer_UBA_prepaid \n 6. Check_Balance \n 7.Pay_Bills \n 8. Next"))
if (option == 1):
	print("Please Enter In Your Pin")
	pin = input("Enter Four Digit Pin:")
	assured = pin
if (assured == pin):
   print("Please Enter Amount:")
   Amount = input("50 - 10000:")
   assured = Amount
if (assured == Amount):
   print("Your Transaction Is Successfully")
   main = int(input("Enter \n 1. ENTER 1 TO RETURN TO MENU \n 2. ENTER 2 TO END"))

	
	
	