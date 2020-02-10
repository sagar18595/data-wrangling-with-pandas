# --------------
import numpy as np
import pandas as pd

# Read the data. Data is already loaded in the variable `path` use the `delimeter = ';'`.
df = pd.read_csv(path, sep = ';')

# Replace the `unknown` values with the `Nan` and check the value count of missing values and drop the missing rows

df.replace('unknown', np.nan, inplace = True)
print (df.isnull().sum())
df.dropna(axis = 0, inplace=True)
print(df.head())

# Replace the column name from `loan` to `previous_loan_status` and `y` to `loan_status` 
df.rename(columns={"loan": "previous_loan_status", "y": "loan_status"},inplace = True)

# Find out the information of the `job` column.
print (df.job.describe())
print (df.job.unique())

# Check the `loan_status`  approval rate by `job`
y1 = df.groupby('job')['loan_status'].value_counts()
print (y1.groupby(level = 0).apply(lambda y : y/y.sum()))
# Check the percentage of loan approved by `education`
x1 = df.groupby('education')['loan_status'].value_counts()
print (x1.groupby(level = 0).apply(lambda x : x/x.sum()))

# Check the percentage of loan approved by `previous loan status`
z1 = df.groupby('previous_loan_status')['loan_status'].value_counts()
print (z1.groupby(level = 0).apply(lambda z : z/z.sum()))

# Create a pivot table between `loan_status` and `marital ` with values form `age`
print (pd.pivot_table(df,index = 'marital', columns= 'loan_status', values='age'))

# Loan status based on marital status whose status is married
print (df[df.marital == 'married']['loan_status'].value_counts())
#Create a  Dataframes 

# Create a dataframe `df_branch_1` where keys are `'customer_id','first_name','last_name'` you can take any value 
data1 = {'customer_id':[1,2,3,4,5,6,7,8,9,10],'first_name': list ('qwertyuiop'),'last_name': list ('asdfghjklz')}
df_branch_1 = pd.DataFrame(data1)

# Create a dataframe `df_branch_2` where keys are `'customer_id','first_name','last_name'` you can take any value
data2 = {'customer_id':[11,22,33,44,55,66,77,88,99,100],'first_name': list ('sagaronkar'),'last_name': list ('toshniwalg')}
df_branch_2 = pd.DataFrame(data2)

# Create a dataframe `df_credit_score` where keys are `'customer_id','score'` you can take any value

data3 = {'customer_id':[1,2,3,4,5,6,7,8,9,10,11,22,33,44,55,66,77,88,99,100],'credit_score': np.arange(700,780,4)}

df_credit_score = pd.DataFrame(data3)

# Concatenate the dataframe `df_branch_1` and `df_branch_2` along the rows
df_new = pd.concat([df_branch_1,df_branch_2],axis = 0)

# Merge two dataframes `df_new` and `df_credit_score` with both the left and right dataframes using the `customer_id` key
df_merged = pd.merge(df_new,df_credit_score,on = ['customer_id'], how='inner', suffixes=['_left', '_right'])

print (df_merged)


