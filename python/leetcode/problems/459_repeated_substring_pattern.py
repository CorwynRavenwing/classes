class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        L = len(s)
        L2 = L // 2
        for ss_len in range(1, L2 + 1):
            ss = s[:ss_len]
            # print(f"{ss_len}/{L2} '{ss}'")
            if L % ss_len != 0:
                # print(f"  fail, {L % ss_len=}")
                continue
            ss_2 = s[ss_len:2 * ss_len]
            if ss != ss_2:
                # print(f"  fail, '{ss}' != '{ss_2}'")
                continue
            copies = L // ss_len 
            check = ss * copies
            if len(check) != L:
                # print(f"  fail, {len(check)=}")
                continue
            if check == s:
                print(f"  SUCCESS! {copies=}")
                # print(f"{ss_len}/{L2} '{ss}'")
                return True
        
        return False

