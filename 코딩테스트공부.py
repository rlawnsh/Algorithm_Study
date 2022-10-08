from collections import deque

def solution(alp, cop, problems):
    goal_al, goal_co = (max(p[0] for p in problems), max(p[1] for p in problems))
    cur_al, cur_co = min(goal_al, alp), min(goal_co, cop)
    dp=[[1e9 for _ in range(goal_co+1)] for _ in range(goal_al+1)]
    dp[cur_al][cur_co] = 0
    for al in range(cur_al, goal_al+1):
        for co in range(cur_co, goal_co+1):
            if (al<goal_al):
                dp[al+1][co] = min(dp[al][co]+1, dp[al+1][co])
            if (co<goal_co):
                dp[al][co+1] = min(dp[al][co]+1, dp[al][co+1])
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if (alp_req<=al and cop_req<=co):
                    next_al, next_co=min(al+alp_rwd,goal_al), min(co+cop_rwd,goal_co)
                    dp[next_al][next_co] = min(dp[al][co] + cost, dp[next_al][next_co])
    return dp[-1][-1]