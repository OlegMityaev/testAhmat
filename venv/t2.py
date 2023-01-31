import pandas as pd

users = pd.DataFrame({'name': [],
                      'cm': [],
                      'date': []})
users.to_excel('us.xlsx')