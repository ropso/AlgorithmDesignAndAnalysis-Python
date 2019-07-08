#PF-Assgn-19

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    if food_type in ["V","N"] and quantity_ordered>1 and distance_in_kms>0:
        # better we make a dictionary to store the vslues
        bill_amount=0
        bill_amount+=150 if food_type=="N" else 120
        bill_amount_home_delivery
        distance_in_kms-=3
        if distance_in_kms>0:
            bill_amount_home_delivery+=3(3 if distance_in_kms-3>=0 else distance_in_kms)
            if distance_in_kms==0:
                pass
            else:
                bill_amount_home_delivery+=6*distance_in_kms
        bill_amount=quantity_ordered*bill_amount
        bill_amount+=bill_amount_home_delivery
    #write your logic here
        return bill_amount
    else:
        -1
#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)