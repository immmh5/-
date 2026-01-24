xdef get_grade_description(score):
    if score >= 90:
        return "Excellent"
    elif score >= 80:
        return "Very Good"
    elif score >= 70:
        return "Good"
    else:
        return "Needs Improvement"

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def format_currency(amount, currency_symbol="$"):
    return f"{currency_symbol}{amount:,.2f}"

def is_even(number):
    return number % 2 == 0

def find_max_value(numbers_list):
    if not numbers_list:
        return None
    return max(numbers_list)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def generate_user_email(first_name, last_name):
    email = f"{first_name.lower()}.{last_name.lower()}@company.com"
    return email

def get_list_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

# --- الأمثلة لتجربة الدوال ---
print(get_grade_description(85))
print(calculate_bmi(70, 1.75))
print(format_currency(1250.5))
print(is_even(10))
print(find_max_value([10, 55, 2, 90]))
print(celsius_to_fahrenheit(30))
print(generate_user_email("Sami", "Ali"))
print(get_list_average([10, 20, 30]))