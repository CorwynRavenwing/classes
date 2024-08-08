class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:

        creatorViews = {}
        videoViewsByCreator = {}
        
        for Creator, Id, ViewCount in zip(creators, ids, views):
            # print(f'{Creator=} {Id=} {ViewCount=}')
            creatorViews.setdefault(Creator, 0)
            creatorViews[Creator] += ViewCount
            videoViewsByCreator.setdefault(Creator, {}) # dict key is another dict
            if Id in videoViewsByCreator[Creator]:
                print(f'ERROR: already has one: [{Creator}][{Id}]')
                return [['THROW', 'ERROR']]
            videoViewsByCreator[Creator][Id] = ViewCount
        print(f'{creatorViews=}')
        print(f'{videoViewsByCreator=}')
        highestViews = max(creatorViews.values())
        print(f'{highestViews=}')
        mostPopularCreators = [
            creator
            for creator, viewCount in creatorViews.items()
            if viewCount == highestViews
        ]
        print(f'{mostPopularCreators=}')
        answer = []
        for Creator in mostPopularCreators:
            theirVideos = videoViewsByCreator[Creator]
            sortableVideos = [
                (-score, video)
                for video, score in theirVideos.items()
            ]
            sortableVideos.sort()
            (ignoreScore, bestVideo) = sortableVideos.pop(0)
            answer.append(
                (Creator, bestVideo)
            )

        return answer
# NOTE: Runtime 714 ms Beats 27.10%
# NOTE: Memory 76.70 MB Beats 12.90%
