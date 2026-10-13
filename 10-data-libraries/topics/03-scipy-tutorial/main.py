"""SciPy tutorial: independent learner project. See README.md for purpose and use."""

from scipy import stats

result = stats.ttest_1samp([10, 11, 12, 13, 14], popmean=8)
print("statistic:", round(result.statistic, 3))
print("p-value:", round(result.pvalue, 4))
