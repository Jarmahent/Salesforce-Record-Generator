import csv
from faker import Faker
import random
from g_abr import us_state_abbrev
from g_cities import city_to_state_dict
import click

def phone():
    n = '0000000000'
    while '9' in n[3:6] or n[3:6]=='000' or n[6]==n[7]==n[8]==n[9]:
        n = str(random.randint(10**9, 10**10-1))
    return n[:3] + '-' + n[3:6] + '-' + n[6:]

@click.command()
@click.option('--amount', default=10, help='Number of records to generate.')
def generate_data(amount):
  with open('generated_account_data.csv', mode='w') as account_data:
    print("Creating "+ str(amount) + ' records')
    fake = Faker()
    account_data = csv.writer(account_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    # Create initial headers
    account_data.writerow(
      ['Name', 'BillingStreet', 'BillingCity', 'BillingPostalCode', 'BillingCountry', 'BillingState', 'MobilePhone']
    )

    for index in range(amount):
      
      # Generate address and company name
      non_abr_state = fake.state()
      state = us_state_abbrev.get(non_abr_state)
      city_state = city_to_state_dict.get(non_abr_state)
      city = random.choice(city_state)
      street_name = fake.street_name() + ' ' + fake.street_suffix()

      # Append generated values to csv row
      row = [fake.company(), street_name, city, fake.zipcode(), 'United States', state.upper(), phone()]

      # Write values to csv object
      account_data.writerow(row)

if __name__ == "__main__":
  generate_data()
