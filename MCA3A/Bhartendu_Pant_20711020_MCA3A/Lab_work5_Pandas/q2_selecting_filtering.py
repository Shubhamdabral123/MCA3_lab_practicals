#selection
# importing pandas
import pandas as pd
  
record = {
  
 'Name': ['Ankit', 'Amit', 'Aishwarya', 'Priyanka', 'Priya', 'Shaurya' ],
 'Age': [21, 19, 20, 18, 17, 21],
 'Stream': ['Math', 'Commerce', 'Science', 'Math', 'Math', 'Science'],
 'Percentage': [88, 92, 95, 70, 65, 78] }
  
# create a dataframe
dataframe = pd.DataFrame(record, columns = ['Name', 'Age', 'Stream', 'Percentage'])
  
print("Given Dataframe :\n", dataframe) 
  
# selecting rows based on condition
rslt_df = dataframe[dataframe['Percentage'] > 80]
  
print('\nResult dataframe :\n', rslt_df)





#Filtering
from IPython.display import display
# import module
import pandas as pd

# assign data
dataFrame = pd.DataFrame({'Name': [' RACHEL ', ' MONICA ', 'PHOEBE ',' ROSS ', 'CHANDLER', ' JOEY '],
							
'Age': [30, 35, 37, 33, 34, 30],
							
'Salary': [100000, 93000, 88000, 120000, 94000, 95000],
							
'JOB': ['DESIGNER', 'CHEF', 'MASUS', 'PALENTOLOGY','IT', 'ARTIST']})
# filter dataframe
display(dataFrame.loc[(dataFrame['Salary']>=100000) & (dataFrame['Age']< 40) & (dataFrame['JOB'].str.startswith('D')),['Name','JOB']])
