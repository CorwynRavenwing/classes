class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:

        friends_at_level = {id}     # level 0 == just myself
        seen = set()
        print(f'L=0: F={friends_at_level}')
        for L in range(1, level + 1):
            new_FAL = set()
            for friend in sorted(friends_at_level):
                seen.add(friend)
                print(f'  {friend=}')
                his_friends = sorted(friends[friend])
                print(f'    {his_friends=}')
                for F in his_friends:
                    if F in seen:
                        continue
                    else:
                        print(f'      {F=}')
                        new_FAL.add(F)
                        seen.add(F)
            friends_at_level = new_FAL
            print(f'{L=}: F={friends_at_level}')
        # do this inside out, for clarity
        videos = Counter()
        for (I, videoList) in enumerate(watchedVideos):
            if I in friends_at_level:
                videoList.sort()
                print(f'{I=} V={videoList}')
                for V in videoList:
                    videos[V] += 1
                    # print(f'    +"{V}"')
        # print(f'{videos=}')
        videos_with_counts = [
            (count, V)
            for V, count in videos.items()
        ]
        # print(f'sort by video: {videos_with_counts=}')
        videos_with_counts.sort()
        sorted_to_print = "\n".join(map(str, videos_with_counts))
        print(f'sort videos_with_counts:\n{sorted_to_print}')
        videos_by_count = [
            V
            for C, V in videos_with_counts
        ]
        # print(f'{videos_by_count=}')
        return videos_by_count



