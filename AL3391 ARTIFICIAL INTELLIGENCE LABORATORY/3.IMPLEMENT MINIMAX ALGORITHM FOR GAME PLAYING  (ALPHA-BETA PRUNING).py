import math

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth, alpha, beta):
    if curDepth == targetDepth:
        return scores[nodeIndex]

    if maxTurn:
        best = float('-inf')
        for i in range(2):
            val = minimax(curDepth + 1, nodeIndex * 2 + i, False, scores, targetDepth, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = minimax(curDepth + 1, nodeIndex * 2 + i, True, scores, targetDepth, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

# Driver code
scores = [3, 5, 2, 9, 12, 5, 23, 23]
treeDepth = math.log(len(scores), 2)
print("The optimal value is: ", end="")
print(minimax(0, 0, True, scores, treeDepth, float('-inf'), float('inf')))
