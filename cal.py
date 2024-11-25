def calculate_discount(price, discount_percent):
    
    discount_amount = (discount_percent / 100) * price
    final_price = price - discount_amount
    return final_price
def main():
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    if price < 0 or discount_percent < 0:
        print("Invalid input.")
        return
    
    final_price = calculate_discount(price, discount_percent)
    print(f"The final price is: ${final_price:.2f}")

if __name__ == "__main__":
    main()    