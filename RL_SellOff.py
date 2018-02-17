# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 15:39:28 2018

@author: GK



Basic Reinforcement Learning environment for simple but useful scenario of
selling off objects to maximize profit, subject to some time constraint.



Objective:
Sell of N bricks by time T, maximizing profit.
Each discrete time step t is an opportunity to list up to N_t bricks,
where N_t is number of bricks remaining at time t. 
Each of the bricks can be listed for one of a few prices, but the probability 
of actually being sold is not uniform over all prices (if you undersell market
price it will be easier to fill vs. if you overprice you are less likely to sell.)
Say you list L_t bricks, with 0 <= L_t <= N_t, i.e. you can list for sale anything in
{0,1,2,...,N_t} bricks at time t.

So at time t, the amount actually sold is S_t, where 0 <= S_t <= L_t <= N_t
since the amoutn sold is subset of the amount listed, which is subset of all your bricks.

The market price at time t is P_t. But you can sell at market price, or a little above or a little below
{P_t - delta, P_t, P_t + delta}

If you have remaining bricks at final time T, there is large penalty fine FT.


"""


import numpy as np
import matplotlib.pyplot as plt


# =============================================================================
# PARAMETERS
# =============================================================================
T = 100 #Number time steps
Nbricks = 20 #Number starting bricks.
delta = 1. #Up and down offset of price. Allowed to sell at {P_t - delta, P_t, P_t + delta}

Nepisodes = 10000
#...







def Price(t):
    """
    Example function defining how price changes as a function of time.
    
    For now just make deterministic but could imagine adding random noise, etc.
    
    For now just use a simple sine curve offset to always be positive (so 
    price is always positive)
    
    
    input:
        t - np array of timesteps
        
        **could eventually make more sophisticated if other vars influence
        price too, and take in other input vectors or params.
        
    return:
        P_t 
    """
    A = 100.
    return .5*A*np.sine(t) + A





def SaleProbability(P_t):
    """
    Define some probability distribution for probability of sale as function of 
    distance from current market price.
    For now just simple discrete 3-5 price case.
    
    
    input:
        P_t - float. Current market price at time t
        
    return:
        
    """
    pass






def GetPossibleActions(state):
    """
    Given the state vector,
    return the potential actions.
    
    
    input:
        state - np array. State vector
        
    return:
        actions = list of available actions
        
    """
    pass
    
    
    
    
    
    
def SelectAction_Agent(state):
    """
    The action chosen by the agent
    
    input:
        state - np array. State vector
        
    return:
        action = the action chosen by agent
    """
    pass    
    
    
    
    

def SelectAction_Environment(state,action,probabilities):
    """
    The action chosen stochastically by the environment.
    
    input:
        state - np array. State vector
        action - the action chosen by agent
        probabilities - the probabilities of following states given agents state-action
        
    return:
        next_state
        
    """
    pass




def Train_Agent_Single_Episode():
    pass



def Simulation(Nepisodes):
    aaaa = []
    for i in xrange(Nepisodes):
        Train_Agent_Single_Episode(aaaaaaaa)
    





def VisualizeEpisode():
    plt.figure()
    plt.plot()
    plt.show()
    pass






if __name__ == "__main__":
    
    #Run simulations of the agent in the environment for the given parameters
    #Simulation(Nepisodes)
    #...
    
    #Visualize the agent in the environment as the simulations happen
    #...
    
    #Save figs, decisions, actions, final policy
    #...