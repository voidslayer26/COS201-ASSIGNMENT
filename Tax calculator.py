#!/usr/bin/env python3
# Tax computation utility for 2009 IRS brackets

def compute_tax_amount(status_code, earnings):
    """Calculate tax based on 2009 IRS brackets"""
    
    # Tax bracket definitions for 2009
    tax_data = {
        0: [  # Single
            (8350, 0.10), (33950, 0.15), 
            (82250, 0.25), (171550, 0.28),
            (372950, 0.33), (float('inf'), 0.35)
        ],
        1: [  # Married filing jointly
            (16700, 0.10), (67900, 0.15),
            (137050, 0.25), (208850, 0.28),
            (372950, 0.33), (float('inf'), 0.35)
        ],
        2: [  # Married filing separately
            (8350, 0.10), (33950, 0.15),
            (68525, 0.25), (104425, 0.28),
            (186475, 0.33), (float('inf'), 0.35)
        ],
        3: [  # Head of household
            (11950, 0.10), (45500, 0.15),
            (117450, 0.25), (190200, 0.28),
            (372950, 0.33), (float('inf'), 0.35)
        ]
    }
    
    # Status descriptions
    status_names = {
        0: "Single",
        1: "Married Filing Jointly",
        2: "Married Filing Separately", 
        3: "Head of Household"
    }
    
    if status_code not in tax_data:
        print("Invalid status code entered")
        return None
    
    # Initialize tax calculation
    remaining = float(earnings)
    total_tax = 0.0
    previous_limit = 0
    
    # Process each bracket
    for limit, rate in tax_data[status_code]:
        if remaining <= 0:
            break
            
        taxable_in_bracket = min(remaining, limit - previous_limit)
        if taxable_in_bracket > 0:
            total_tax += taxable_in_bracket * rate
            remaining -= taxable_in_bracket
            
        previous_limit = limit
    
    return {
        'status': status_names[status_code],
        'income': earnings,
        'tax': round(total_tax, 2)
    }

def main():
    """Main program loop"""
    print("=" * 50)
    print("2009 U.S. Federal Income Tax Calculator")
    print("=" * 50)
    
    while True:
        try:
            print("\nFiling Status Options:")
            print("  0 → Single")
            print("  1 → Married Filing Jointly")
            print("  2 → Married Filing Separately") 
            print("  3 → Head of Household")
            print("  Q → Quit program")
            
            status_input = input("\nSelect filing status (0-3 or Q): ").strip()
            
            if status_input.upper() == 'Q':
                print("\nProgram terminated.")
                break
                
            try:
                status_value = int(status_input)
                if status_value not in [0, 1, 2, 3]:
                    print("Please enter 0, 1, 2, or 3 only")
                    continue
            except ValueError:
                print("Please enter a valid number (0-3)")
                continue
            
            income_input = input("Enter taxable income ($): ").strip().replace('$', '').replace(',', '')
            
            try:
                income_value = float(income_input)
                if income_value < 0:
                    print("Income cannot be negative")
                    continue
            except ValueError:
                print("Please enter a valid dollar amount")
                continue
            
            # Compute tax
            result = compute_tax_amount(status_value, income_value)
            
            if result:
                print("\n" + "─" * 40)
                print(f"Filing Status: {result['status']}")
                print(f"Taxable Income: ${result['income']:,.2f}")
                print(f"Estimated Tax: ${result['tax']:,.2f}")
                print("─" * 40)
                
                # Offer to calculate again
                again = input("\nCalculate another? (Y/N): ").strip().upper()
                if again != 'Y':
                    print("\nThank you for using the tax calculator.")
                    break
                    
        except KeyboardInterrupt:
            print("\n\nProgram interrupted.")
            break
        except Exception as err:
            print(f"An error occurred: {err}")

if __name__ == "__main__":
    main()