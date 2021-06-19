import thingsboard_api as tb
import pandas as pd

df = pd.read_csv (r'devices_names.csv')
df.head()

for i in range(len(df)):
    dev_name = str(df.iloc[i][0])
    tb.create_dev(dev_name=dev_name, 
                  dev_profile="Device-Name",
                  token_name=dev_name, 
                  url = "http://ip_address:port", 
                  username = "tenant@thingsboard.org", 
                  password = "tenant")
    print("Created "+dev_name)

for i in range(len(df)):
    dev_name = str(df.iloc[i][0])
    token_fromDev = tb.get_tokenByDevName(dev_name=dev_name, 
                                          url = "http://ip_address:port", 
                                          username = "tenant@thingsboard.org", 
                                          password = "tenant")
    print("Token returned "+token_fromDev)

for i in range(len(df)):
    dev_name = str(df.iloc[i][0])
    tb.delete_dev(dev_name=dev_name,
                  url = "http://ip_address:port", 
                  username = "tenant@thingsboard.org", 
                  password = "tenant")
    print("Deleted "+dev_name)