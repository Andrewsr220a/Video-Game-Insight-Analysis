#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[3]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data_df = pd.read_csv(file_to_load)
purchase_data_df.head()


# ## Player Count

# * Display the total number of players
# 

# In[4]:


total_players= purchase_data_df["SN"].value_counts()
purchase_data_df


# In[5]:


clean_Players_data_df = purchase_data_df.loc[:,["SN","Age","Gender"]].drop_duplicates()
clean_Players_data_df


# In[6]:


total_players = clean_Players_data_df.count()[0]
total_players


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[7]:


unique_items = purchase_data_df["Item ID"].nunique()
unique_items


# In[8]:


Prices = purchase_data_df["Price"].mean()
Prices


# In[9]:


revenue = purchase_data_df ["Price"].sum()
revenue


# In[10]:


total_purchases = purchase_data_df ["Purchase ID"].count()
total_purchases


# In[11]:


raw_data = {
   'Number of Unique': [unique_items],
'Average Price' : [Prices], 'Number of Purchases': [total_purchases], 'Total Revenue': [revenue]} 
df = pd.DataFrame(raw_data)
df


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[12]:


player_gender_df = clean_Players_data_df["Gender"].value_counts()
player_gender_df 


# In[13]:


total_percentage = player_gender_df / total_players * 100
total_percentage


# In[14]:


Gender_Demo = {
    'Total Count': player_gender_df,
'Total Percentage' : total_percentage} 
df = pd.DataFrame(Gender_Demo)
df


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[15]:


purchase_group_by_gender = purchase_data_df.groupby(["Gender"])
purchase_group_by_gender.count()['Item ID']


# In[16]:


purchase_group_by_price = purchase_data_df.groupby(["Gender"])
purchase_group_by_price.sum()['Price']


# In[17]:


purchase_group_by_price.mean()['Price']


# In[18]:


Avg_Total_Purchase = purchase_group_by_price.mean()['Price']/ purchase_group_by_gender.count()['Item ID']
Avg_Total_Purchase


# In[19]:


Purchasing_Analysis = {
    'Purchase Count': purchase_group_by_gender.count()['Item ID'],
    'Purchase Average': purchase_group_by_price.mean()['Price'],
'Total Purchase Value' : purchase_group_by_price.sum()['Price'],
    'vg Total Purchase per Person': Avg_Total_Purchase} 
df = pd.DataFrame(Purchasing_Analysis)
df


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[20]:


player_ages= purchase_data_df["Age"]

bins= [0,9,14,19,24,29,34,39,45]

group_labels= ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39","40+"]


# In[21]:


clean_Players_data_df["Age_Group"] = pd.cut(clean_Players_data_df["Age"], bins, labels=group_labels, include_lowest=True)
clean_Players_data_df


# In[22]:


Age_group= clean_Players_data_df["Age_Group"].value_counts()
Age_group


# In[23]:


Age_percentage = Age_group / total_players * 100
Age_percentage


# In[24]:


Age_Demographics = {
    'Total Count': Age_group,
    'Percentage of Players': Age_percentage} 
df = pd.DataFrame(Age_Demographics)
df


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[25]:


purchase_data_df["Age_Group"] = pd.cut(purchase_data_df["Age"], bins, labels=group_labels, include_lowest=True)
purchase_data_df


# In[26]:


Age_type_data_df = purchase_data_df.groupby(["Age_Group"])
Age_type_data_df.head()


# In[27]:


Purchase_count_by_age = Age_type_data_df["Purchase ID"].count()
Purchase_count_by_age


# In[28]:


avg_purchase_price = Age_type_data_df["Price"].mean()
avg_purchase_price


# In[29]:


purchase_total_value = Purchase_count_by_age * avg_purchase_price
purchase_total_value


# In[30]:


total_price_age = Age_type_data_df["Price"].sum()

average_total_per_person = total_price_age / total_players

average_total_per_person


# In[31]:


Purchasing_Age_Analysis = {
    'Age Ranges': Age_group,
    'Purchase Count': Purchase_count_by_age,
    'Average Purchase Price': avg_purchase_price,
    'Total Purchase Value': purchase_total_value,
    'Avg Total Purchase per Person': average_total_per_person} 
df = pd.DataFrame(Purchasing_Age_Analysis)
df


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[160]:


purchases_by_person_df = purchase_data_df.groupby(["SN"])

purchases_by_person_df.head()


# In[168]:


purchase_count = purchase_data_df.groupby(["SN"]).count()['Purchase ID']
purchase_count


# In[169]:


average_purchase_price = purchase_data_df.groupby(["SN"]).mean()['Price']
average_purchase_price


# In[171]:


total_purchase = purchase_data_df.groupby(["SN"]).sum()['Price']
total_purchase


# In[173]:


top_Sellers = {
    'Purchase Count': purchase_count,
    'Average Purchase Price': average_purchase_price,
    'Total Purchase Value':total_purchase}
df = pd.DataFrame(top_Sellers)
df


# In[177]:


df.sort_values("Total Purchase Value", axis=0, ascending=False).head(5)


# In[ ]:


1. purchase_order get total purchase count
    1.1 groupby "SN"
    1.2 find count of purchases 
2. create dataframe fron series
3. df.sort("total purchase value") in a descending order
4. display a sample of the data frame


# In[ ]:





# In[ ]:





# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, average item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[178]:


Item_info_df = purchase_data_df.loc[:,["Item Name","Item ID","Price"]]
Item_info_df


# In[183]:


purchase_count = Item_info_df.groupby(["Item ID","Item Name"]).count()["Price"]


# In[184]:


avg_price = Item_info_df.groupby(["Item ID","Item Name"]).mean()["Price"]


# In[185]:


total_purchase = Item_info_df.groupby(["Item ID","Item Name"]).sum()["Price"]


# In[188]:


popular_items = {
    'Purchase Count': purchase_count,
    'Item Price': avg_price,
    'Total Purchase Value':total_purchase}
df = pd.DataFrame(popular_items)
df


# In[192]:


df.sort_values("Purchase Count", axis=0, ascending=False).head(5).round({"Item Price": 2})


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[193]:


df.sort_values("Total Purchase Value", axis=0, ascending=False).head(5).round({"Item Price": 2})


# In[ ]:





# In[ ]:





# In[ ]:




