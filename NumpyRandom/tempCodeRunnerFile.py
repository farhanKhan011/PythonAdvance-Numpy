 random
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(random.normal(size=(20,30)), kind="kde")
plt.show()