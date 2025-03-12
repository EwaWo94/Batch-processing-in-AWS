# About the project

The aim of the work was to design and implement a solution for processing and analyzing data about the Seasoned Advice community from the StackExchange forum. The obtained results allowed us to determine the most popular topics, observe user activity patterns and indicate the usefulness of answers.

The EMR infrastructure and Spark, Pandas, Matplotlib, Wordcloud, NLTK libraries were used to process and analyze the data. I made a number of visualizations presenting metrics and patterns generated based on the acquired data.

## Workflow:

1. API Data Fetching: Data from the StackExchange API is fetched using AWS Cloud9 and saved to S3 in JSON format.

2. Data Cleansing: Data in JSON format is read into a Jupyter Notebook where it is cleaned.

3. Saving Processed Data: Cleaned data is saved back to S3 in Parquet format.

4. Analysis and Visualization: In a Jupyter Notebook environment running on the EMR cluster, data is analyzed and visualized using PySpark, Pandas, nltk, Matplotlib, and WordCloud libraries.



<img width="904" alt="obraz" src="https://github.com/user-attachments/assets/c1c4ed69-b00e-49f5-a198-9c87258effd6" />
