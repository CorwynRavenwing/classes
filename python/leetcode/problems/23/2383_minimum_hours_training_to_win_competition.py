class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:

        def need_training(power: Tuple[int,int], opponents: List[Tuple[int,int]]) -> Tuple[int,int]:
            (E, XP) = power
            for (oppE, oppXP) in opponents:
                print(f'({E},{XP}) vs ({oppE},{oppXP})')
                needE = max(oppE + 1 - E, 0)
                needXP = max(oppXP + 1- XP, 0)
                answer = (needE, needXP)
                if answer != (0,0):
                    return answer
                E -= oppE
                XP += oppXP
            return (0,0)
        
        E = initialEnergy
        XP = initialExperience
        ZIP = tuple(zip(energy, experience))
        print(f'{ZIP}')
        answer = 0
        while True:
            print(f'{answer} ({E},{XP})')
            train = need_training((E,XP), ZIP)
            if train == (0,0):
                break
            (trainE, trainXP) = train
            print(f'need training {train}')
            E += trainE
            XP += trainXP
            answer += trainE + trainXP
        return answer

