from .tools import GoTestStrategy
from .goalsearch import GoalSearch

expe = GoalSearch(strategy = GoTestStrategy(), params={'strength': [0.1, 1]})
expe.start()
print(expe.get_res())
print(expe.get_best())