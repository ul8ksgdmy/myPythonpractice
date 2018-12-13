import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
# x = np.random.normal(size=21)
x = np.arange(0,5,0.1)
y = np.sin(x)
plt.plot(x,y)

len(x)  # 개수
np.mean(x) # 평균
np.var(x) # 분산
np.std(x)  # 표준 편차
np.max(x)  # 최댓값
np.min(x)  # 최솟값
np.median(x)  # 중앙값
np.percentile(x, 25)  # 1사분위 수
np.percentile(x, 75)  # 3사분위 수


