class Solution:
    def reorderSpaces(self, text: str) -> str:
        original_len = len(text)
        print(f"Original   ({original_len}) '{text}'")
        output = text.strip()
        while '  ' in output:
            output = output.replace('  ',' ')
        output_len = len(output)
        # print(f"Output     ({output_len}) '{output}'")
        diff = original_len - output_len
        diff_spaces = ' ' * diff
        # print(f"Difference ({diff}) '{diff_spaces}'")
        no_spaces = output.replace(' ', '')
        nospace_len = len(no_spaces)
        spaces = output_len - nospace_len
        # print(f"Spaces     ({spaces}) '{' ' * spaces}'")
        expand_each_space = (
            diff // spaces
            if spaces != 0
            else 0
        )
        spaces_at_end = diff - (expand_each_space * spaces)
        print(f"{expand_each_space=} {spaces_at_end=}")
        output = (
            output.replace(
                ' ',
                ' ' * (expand_each_space + 1)
            ) + ' ' * spaces_at_end
        )
        print(f"RETURN VAL ({len(output)}) '{output}'")
        return output

