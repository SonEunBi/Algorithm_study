def solution(players, callings):
    play_dict={}
    play_dict = {string:i for i, string in enumerate(players)}

    for c in callings:        
        players[play_dict[c]], players[play_dict[c]-1] = players[play_dict[c]-1], players[play_dict[c]]
        play_dict[players[play_dict[c]]], play_dict[players[play_dict[c]-1]] = play_dict[players[play_dict[c]-1]], play_dict[players[play_dict[c]]]

    return players