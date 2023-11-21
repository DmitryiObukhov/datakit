import seaborn as sns
# Seaborn Chart Types Cheat Sheet

# 1) Histplot:
# Scope of application: Displaying the distribution of one variable.
# Example:
tips = sns.load_dataset('tips')
sns.histplot(tips['total_bill'], bins=30, kde=True)

# 2) KDE Plot:
# Scope of application: Visualization of the distribution of a single variable using kernel density estimation.
# Example:
tips = sns.load_dataset('tips')
sns.kdeplot(tips['total_bill'])

# 3)ECDF Plot:
# Scope of application: Displaying the empirical cumulative distribution function of a single variable.
# Example:
tips = sns.load_dataset('tips')
sns.ecdfplot(tips['total_bill'])

# 4)Displot:
# Scope of application: Figure-level interface for unitary distribution plots.
# Example:
tips = sns.load_dataset('tips')
sns.displot(tips['total_bill'], bins=30, kde=True)

# 5)Regplot:
# Scope of application: Visualize the relationship between two variables with a scatter plot and a regression line.
# Example:
tips = sns.load_dataset('tips')
sns.regplot(x='total_bill', y='tip', data=tips)

# 6)Catplot:
# Application: Figure-level interface for categorical plots.
# Example:
tips = sns.load_dataset('tips')
sns.catplot(x='day', y='total_bill', data=tips, kind='bar')

# 7)Swarmplot:
# Scope of application: Displaying the distribution of categorical point data.
# Example:
tips = sns.load_dataset('tips')
sns.swarmplot(x='day', y='total_bill', data=tips)
