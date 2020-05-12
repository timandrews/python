#!/usr/bin/python3
import pandas

reviews = pandas.read_csv("ign.csv")

#remove the first column
reviews = reviews.iloc[:,1:]
print("The first 2 rows are:")
print(reviews.head())


print("The last 2 rows are")
print(reviews.tail(2))

print("The shape, ie the number of rows and columns, is:")
print(reviews.shape)

print("With indexing dataframes and iloc:")
print(reviews.iloc[0:2,3:5])

print("1st 5 rows with loc")
print(reviews.loc[0:5,:])

print("")