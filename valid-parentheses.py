class Solution:
    def isValid(self, sequence):
        while True:
            if '()' in sequence:
                sequence = sequence.replace('()', '')
            elif '{}' in sequence:
                sequence = sequence.replace('{}', '')
            elif '[]' in sequence:
                sequence = sequence.replace('[]', '')
            else:
                return not sequence


if __name__ == '__main__':
    sequence = '{[()]}'
    print(f'Is {sequence} valid ? : {Solution().isValid(sequence)}')
    sequence1 = '{[()]}{]{}}'
    print(f'Is {sequence1} valid ? : {Solution().isValid (sequence1)}')
    sequence2 = '{[]{()}}'
    print(f'Is {sequence2} valid ? : {Solution().isValid (sequence2)}')

