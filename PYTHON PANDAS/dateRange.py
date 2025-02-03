import pandas as pd
days=pd.date_range(start="2025-01-01",end="2025-01-31")
print(days)

months=pd.date_range(start="2025-01-01",end="2025-12-31",freq="M")
print(months)

business_days=pd.date_range(start="2025-01-01",end="2025-01-31",freq="B")
print(business_days)