A Python Script to simulate user browsing sessions to add to Recommendation System Training Datasets. 

**Input**:

Recommendation System Training Dataset:

['ISBN', 'Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher', 'Image-URL-S', 'Image-URL-M', 'Image-URL-L']

**Output**:

User Browsing Session Dataset:

['ISBN', 'Book-Author', 'Year-Of-Publication', 'Publisher', 'Final_Item', 'Considered_Before', 'Considered_After', 'Time_to_Transaction', 'Time_Considered']


**NOTE**:

The dataset generated is completely random, which means that there are no semantic patterns or any sort of logic to the preferences of each user. This may cause problems in modelling preferences down the line. Use only for testing purposes. 
