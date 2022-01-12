import matplotlib.pyplot as plt
import numpy as np
jezyki=["Python","C","Java","C++","C#","Visual Basic","JavaScript","Assembly language","SQL","Swift"]
ratings=[13.58,12.44,10.66,8.29,5.68,4.74,2.09,1.85,1.80,1.41]
plt.bar(jezyki,ratings,color = "pink",edgecolor = "lightcoral")
plt.annotate("13.58%",(jezyki[0], 13.70))
plt.annotate("12.44%",(jezyki[1], 12.65))
plt.annotate("10.66%",(jezyki[2], 10.80))
plt.annotate("8.29%",(jezyki[3], 8.50))
plt.annotate("5.68%",(jezyki[4], 5.80))
plt.annotate("4.74%",(jezyki[5], 4.95))
plt.annotate("2.09%",(jezyki[6], 2.30))
plt.annotate("1.85%",(jezyki[7], 2.0))
plt.annotate("1.80%",(jezyki[8], 1.95))
plt.annotate("1.41%",(jezyki[9], 1.60))
plt.legend(labels = ["Popularność"])
plt.title("Popularność różnych języków programowania")
plt.xlabel("Języki programów")
plt.ylabel("Procent popularności na wszystkie języki")
plt.show()