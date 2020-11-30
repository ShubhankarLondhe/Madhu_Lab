import numpy as np
import seaborn as sns
import matplotlib.pylab as plt

labels = ['2','3','4','2-5','6','7','8','2-9','10','11','12-8-8','2-13','2-14','2-15','2-16','2-2','2-12-8-8','12-2-8-8']

plt.figure(figsize=(10,8))
data = np.array([[45786.0, 440.0, 0.0, 2790.0, 102345.0, 5517.0, 45946.0, 0.0, 0.0, 40704.0, 3687.0, 0.0, 1717.0, 0.0, 1408.0, 3844.0, 28111.0, 0.0], [18006.0, 203.0, 0.0, 1359.0, 49422.0, 2565.0, 21672.0, 0.0, 0.0, 19116.0, 1780.0, 0.0, 781.0, 0.0, 718.0, 1822.0, 13761.0, 0.0], [7706.0, 61.0, 0.0, 621.0, 22008.0, 1161.0, 9469.0, 0.0, 0.0, 8551.0, 794.0, 0.0, 355.0, 0.0, 290.0, 815.0, 6029.0, 0.0], [19068.0, 217.0, 0.0, 1531.0, 53187.0, 2712.0, 23002.0, 1.0, 0.0, 20665.0, 1840.0, 0.0, 877.0, 0.0, 726.0, 1999.0, 14578.0, 0.0], [42185.0, 464.0, 0.0, 3230.0, 120315.0, 6005.0, 51039.0, 1.0, 0.0, 46359.0, 4333.0, 0.0, 1998.0, 0.0, 1595.0, 4361.0, 32654.0, 0.0], [41594.0, 426.0, 0.0, 3042.0, 110698.0, 5930.0, 50744.0, 0.0, 0.0, 44413.0, 4132.0, 0.0, 1840.0, 0.0, 1519.0, 4199.0, 30953.0, 0.0], [48755.0, 500.0, 0.0, 3552.0, 129696.0, 7022.0, 59440.0, 1.0, 0.0, 50630.0, 4572.0, 0.0, 2117.0, 0.0, 1790.0, 4770.0, 35857.0, 0.0], [27997.0, 330.0, 0.0, 2147.0, 78021.0, 4164.0, 34181.0, 0.0, 0.0, 30500.0, 2771.0, 0.0, 1173.0, 0.0, 1014.0, 2941.0, 21490.0, 0.0], [4668.0, 49.0, 0.0, 331.0, 12909.0, 653.0, 5711.0, 0.0, 0.0, 4982.0, 431.0, 0.0, 219.0, 0.0, 153.0, 504.0, 3693.0, 0.0], [15685.0, 182.0, 0.0, 1218.0, 43950.0, 2232.0, 19116.0, 1.0, 0.0, 17454.0, 1588.0, 0.0, 679.0, 0.0, 570.0, 1573.0, 12043.0, 0.0], [24402.0, 254.0, 0.0, 1836.0, 67599.0, 3506.0, 30504.0, 1.0, 0.0, 26725.0, 2676.0, 0.0, 1110.0, 0.0, 892.0, 2608.0, 18922.0, 0.0], [6406.0, 79.0, 0.0, 490.0, 17832.0, 930.0, 7653.0, 0.0, 0.0, 6877.0, 655.0, 0.0, 277.0, 0.0, 249.0, 621.0, 4986.0, 0.0], [14236.0, 157.0, 0.0, 1111.0, 39666.0, 2062.0, 17240.0, 0.0, 0.0, 15535.0, 1407.0, 0.0, 673.0, 0.0, 540.0, 1450.0, 11026.0, 0.0], [4710.0, 44.0, 0.0, 363.0, 13062.0, 674.0, 5829.0, 0.0, 0.0, 5235.0, 487.0, 0.0, 228.0, 0.0, 141.0, 484.0, 3636.0, 0.0], [12187.0, 148.0, 0.0, 984.0, 34431.0, 1789.0, 15234.0, 0.0, 0.0, 13104.0, 1286.0, 0.0, 587.0, 0.0, 467.0, 1237.0, 9502.0, 0.0], [38311.0, 425.0, 0.0, 2915.0, 102904.0, 5674.0, 45375.0, 0.0, 0.0, 40569.0, 3744.0, 0.0, 1775.0, 0.0, 1361.0, 4076.0, 28512.0, 0.0], [33740.0, 353.0, 0.0, 2480.0, 93072.0, 4901.0, 40794.0, 0.0, 0.0, 36243.0, 3437.0, 0.0, 1477.0, 0.0, 1288.0, 3561.0, 26490.0, 0.0], [21165.0, 235.0, 0.0, 1596.0, 56474.0, 3040.0, 25514.0, 1.0, 0.0, 22436.0, 2206.0, 0.0, 917.0, 0.0, 749.0, 2179.0, 16182.0, 0.0]])
ax = sns.heatmap(data, xticklabels=labels, yticklabels=labels, linewidth=0.2)
ax.set(title='Confusion Matrix for NN predictions')
plt.show()

