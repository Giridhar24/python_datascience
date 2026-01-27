# Concept of the Day: The Curse of Dimensionality
#
# Explanation: Why did we use PCA earlier? Because of the Curse of Dimensionality. As you add more features (columns) to your data, the "space" becomes incredibly sparse.
#
# Analogy: Finding a penny on a 10-meter string is easy. Finding a penny on a 10x10m floor is harder. Finding a penny in a 10x10x10m room is very hard.
#
# With too many dimensions, distance calculations (like in KNN) become meaningless because everything is far away from everything else.