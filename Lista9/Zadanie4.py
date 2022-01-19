import matplotlib.pyplot as plt
import numpy as np
jezyki=["Python","C","Java","C++","C#","Visual Basic","JavaScript","Assembly language","SQL","Swift"]
ratings=[13.58,12.44,10.66,8.29,5.68,4.74,2.09,1.85,1.80,1.41]
plt.bar(jezyki,ratings,color = "pink",edgecolor = "lightcoral")
for i in range(len(jezyki)):
    plt.annotate(f"{ratings[i]}%",(jezyki[i], ratings[i]))
plt.legend(labels = ["Popularność"])
plt.title("Popularność różnych języków programowania")
plt.xlabel("Języki programów")
plt.ylabel("Procent popularności na wszystkie języki")
plt.show()