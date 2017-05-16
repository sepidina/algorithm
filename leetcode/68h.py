# -*- encoding: utf-8 -*-
'''
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.

click to show corner cases.

Corner Cases:
A line other than the last line might contain only one word. What should you do in this case?
In this case, that line should be left-justified.
'''

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        
        res = []

        i = 0
        while i < len(words):
            k, l = 0, 0
            while i + k < len(words) and l + len(words[i + k]) <= maxWidth - k:
                l += len(words[i + k])
                k += 1

            temp = words[i]
            for j in range(k - 1):
                if i + k >= len(words):
                    temp += ' '
                else:
                    temp += ' ' * ((maxWidth - l) / (k - 1) + (j < ((maxWidth - l) % (k - 1))))

                temp += words[i + j + 1]

            temp += ' ' * (maxWidth - len(temp))
            res.append(temp)

            i += k

        return res
