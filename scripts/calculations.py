"""By Théo Régi"""
#-------------------------------------------------------------------------------------------------------
#----------------------------Script to implement calculations functions---------------------------------
#-------------------------------------------------------------------------------------------------------

#___________________________________Common functions____________________________________________________
def calculate_returns(prices):
    return prices.pct_change().dropna()

def calculate_tracks(returns):
    tracks = (1 + returns).cumprod()
    tracks.iloc[0] = 1
    return tracks