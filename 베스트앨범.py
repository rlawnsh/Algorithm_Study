def solution(genres, plays):
    index_plays =[]
    for i in enumerate(plays):
        index_plays.append(i)
    playlist = list(zip(index_plays, genres))
    playlist_dict = {}
    for i in genres:
        playlist_dict[i] = []
    
    for i in playlist:
        playlist_dict[i[1]].append(i[0])
    
    for i in playlist_dict:
        playlist_dict[i].sort(key=lambda x:(-x[1],x[0]))
    
    
    for i in playlist_dict:
        tmp = 0
        for j in playlist_dict[i]:
            tmp += j[1]
        playlist_dict[i].append(tmp)
    
    playlist_dict = sorted(playlist_dict.items(), key=lambda x:x[-1][-1], reverse=True)

    # print(playlist_dict)
    answer = []
    for i in playlist_dict:
        if len(i[1]) >= 3:
            for j in range(2):
                answer.append(i[1][j][0])
        else:
            answer.append(i[1][0][0])
    
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop","jazz"],[500, 600, 150, 800, 2500,10000]))