# Salesforce record csv file generator


This generator creates a csv file with the headers:

`['Name', 'BillingStreet', 'BillingCity', 'BillingPostalCode', 'BillingCountry', 'BillingState', 'MobilePhone']`

How to use:

`pip install -r requirements.txt`

`python src/gen.py --amount 10`

Example results:
```
Name,BillingStreet,BillingCity,BillingPostalCode,BillingCountry,BillingState,MobilePhone
"Pugh, Davis and Gordon",Kelly Squares Cove,Bristol,18296,United States,RI,603-121-7834
```
![csv table example](https://i.imgur.com/Pag0K6i.png "CSV Table Example")
