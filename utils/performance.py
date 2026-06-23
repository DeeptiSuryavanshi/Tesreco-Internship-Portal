from utils.decorators import log_performance

@log_performance
def calculate_score(score):
    return score * 10