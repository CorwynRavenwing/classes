class Solution:
    def removeComments(self, source: List[str]) -> List[str]:

        COMMENT_LINE = '//'
        COMMENT_BLOCK = '/*'
        COMMENT_BLOCK_END = '*/'

        def any_comments(S):
            return (COMMENT_LINE in S) or (COMMENT_BLOCK in S)
        
        def first_comment(S):
            answers = []
            if COMMENT_LINE in S:
                answers.append(
                    (S.index(COMMENT_LINE), COMMENT_LINE)
                )                
            if COMMENT_BLOCK in S:
                answers.append(
                    (S.index(COMMENT_BLOCK), COMMENT_BLOCK)
                )
            return min(answers)
        
        D = []
        commentMode = False
        splice_in = ""
        for S in source:
            print(f':{S}')
            working = True
            while working:
                working = False
                if not commentMode:
                    # re-check commentMode b/c it can be changed inside the loop
                    while not commentMode and any_comments(S):
                        working = True
                        (index, comment_type) = first_comment(S)
                        if comment_type == COMMENT_LINE:
                            # print(f'FOUND LINE COMMENT AT {index=}')
                            S = S[:index]
                            # print(f'={S}')
                        if comment_type == COMMENT_BLOCK:
                            # print(f'FOUND BLOCK COMMENT AT {index=}')
                            check_index = index + len(COMMENT_BLOCK)
                            if COMMENT_BLOCK_END in S[check_index:]:
                                index_block_end = S.index(COMMENT_BLOCK_END, check_index)
                                index_end = index_block_end + len(COMMENT_BLOCK_END)
                                # print(f'  .. ENDING AT {index_end}')
                                # print(f'DELETING "{S[index:index_end]}" COMMENT')
                                S = S[:index] + S[index_end:]
                                # print(f'={S}')
                            else:
                                # print(f'BLOCK COMMENT CONTINUES:')
                                S = S[:index]
                                # print(f'={S}<SPLICE>')
                                splice_in = S
                                S = ""
                                commentMode = True
                                working = False
                else:
                    # in comment mode
                    if COMMENT_BLOCK_END in S:
                        working = True
                        index_block_end = S.index(COMMENT_BLOCK_END)
                        index_end = index_block_end + len(COMMENT_BLOCK_END)
                        # print(f'  .. BLOCK COMMENT ENDS AT {index_end}')
                        # print(f'#{splice_in}<SPLICE>{S[index_end:]}')
                        S = splice_in + S[index_end:]
                        # print(f'={S}')
                        splice_in = ""
                        commentMode = False
                    else:
                        # comment-mode not ending: delete entire line
                        S = ""
                        # print(f'={S}')
            if S == "":
                # print(f'|BLANK')
                pass
            else:
                print(f'|{S}')
                D.append(S)
        return D

