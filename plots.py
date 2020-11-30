import matplotlib.pyplot as plt
    
#arr = [0.0, 0.0, 28.78, 92.41, 0.09, 17.08, 0.23, 35.60, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 28.09]
#arr = [93.25, 72.21, 1.02, 6.71, 0.48, 2.45, 0.56, 1.45, 1.35, 0.21, 1.72, 3.64, 1.17, 47.96, 1.38, 0.20]
arr = [1.20, 0.00, 13.5, 0.45, 7.87, 0.80, 2.71, 15.01, 33.24, 5.73, 0.27, 11.38, 35.09, 23.18, 37.80, 2.32, 0.08, 29.71]
x = list(range(2,20))
plt.plot(x,arr)
plt.xticks(x)
plt.title("Pred acc - Relative Positions - Modified CGs")
plt.xlabel("Chemical Groups")
plt.ylabel("Prediction accuracy")
plt.show()


