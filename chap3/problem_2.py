from datetime import datetime
from string import Template

letter = Template('''Dear $name,
You are selected.
Date: $date''')

user_name = input("enter candidate name: ").strip().title()
current_date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

output = letter.substitute(name = user_name, date = current_date)

print(output)