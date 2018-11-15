import csv
import numpy as np
import matplotlib.pyplot as plt

# figure out what data we want to use
categories = [] # these are the column headers in the CSV file
installs =[] # this is the installs row
ratings =[]	# this is the ratings row

with open('data/googeplaystore.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		# move the page column headers out of the actual data to get a clean dataset
		if line_count is 0: # this will be text, not data
			print('pushing categories into a seperate array')
			categories.append(row) # push the text into this array
			line_count +=1 # increment the line count for the next top
		else:
			# grab the ratings and push them into the ratings array
			ratingsData = row[2]
			ratingsData = ratingsData.replace("NaN", "0")
			ratings.append(float(ratingsData)) # int turn a string (piece of text) into a number
			# print('pushing ratings data into the ratings array')
			installData = row[5]
			installData = installData.replace(",", "") # get rid of the commas

			# get rid of the trailing."+"
			installs.append(np.char.strip(installData, "+")) 
			line_count += 1

# get some values we can work with
# how many ratings are 4+?
# how many are below 2?
# how many are int he middle?
np_ratings = np.array(ratings) # turn a plain Python list into a Numpy array	
popular_apps = np_ratings > 4
print("popular_apps:", len(np_ratings[popular_apps]))

percent_popular = int(len(np_ratings[popular_apps]) / len(np_ratings) * 100)
print(percent_popular)

unpopular_apps = np_ratings < 4
print("unpopular_apps:", len(np_ratings[unpopular_apps]))

percent_unpopular = int(len(np_ratings[unpopular_apps]) / len(np_ratings) * 100)
print(percent_unpopular)

kinda_popular = int(100 - (percent_popular + percent_unpopular))
print(kinda_popular)

# do a visualization with our shiny new data
labels = "Sucks", "Meh", "Love it!"
sizes = [percent_unpopular, kinda_popular, percent_popular]
colors = ['yellowgreen', 'lightgreen', 'lightskyblue']
explode = (0.1, 0.1, 0.15)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("DO we love us some apps?")
plt.xlabel("User Ratings = App Installs (10,000+ apps")
plt.show()