import numpy as np
import matplotlib.pyplot as plt
import skyscrapers
list_of_skyscraper = skyscrapers.get_skyscrapers(test=True)
    # initializes the nyc and chicago height lists
NYC = []
CHI = []

    #
for row in list_of_skyscraper:

    if row["location"]["city"] == "Chicago":
        CHI.append(int(row["statistics"]["height"]))
    elif row["location"]["city"] == "New York City":
        NYC.append(int(row["statistics"]["height"]))
    else:
        continue
for i in range(146):
    CHI.append(0)

def avgHeight(city):
    sum = 0
    for i in range(len(city)):
        sum += city[i]
    avg = sum / len(city)
    print("avg height of city ss: ", avg)
    return avg


avgHeight(NYC)
avgHeight(CHI)

nycx_pos = np.arange(len(NYC))
chix_pos = np.arange(len(CHI))
plt.bar(nycx_pos, NYC, align='center', alpha=0.5, color="red", label="New York City")
plt.bar(chix_pos, CHI, align='center', alpha=0.5, color="blue", label="Chicago")
plt.ylabel('Height')
plt.legend(loc='upper right')
plt.title('Comparison of the Heights of Skyscrapers in New York City and Chicago')
plt.show()

# bins = np.linspace(-10, 10, 100)
# plt.hist([NYC, CHI], bins, label=['x', 'y'])
# plt.legend(loc='upper right')
# plt.show()

# work on getting the heights to show up on a matplotlib scatterplot
