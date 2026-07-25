"""
#271. Encode and Decode Strings
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

String encode(List<String> strs) {
    // ... your code
    return encoded_string;
}
Machine 2 (receiver) has the function:

List<String> decode(String encoded_string) {
    // ... your code
    return decoded_strs;
}
So Machine 1 does:

String encoded_string = encode(strs);
and Machine 2 does:

List<String> decoded_strs = decode(encoded_string);
decoded_strs in Machine 2 should be the same as the input strs in Machine 1.

Implement the encode and decode methods.

Example 1:

Input: strs = ["Hello","World"]

Output: ["Hello","World"]
Explanation:

Solution solution = new Solution();
String encoded_string = solution.encode(strs);

// Machine 1 ---encoded_string---> Machine 2

List<String> decoded_strs = solution.decode(encoded_string);

Example 2:

Input: strs = [""]

Output: [""]

Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains any possible characters out of 256 valid ASCII characters.

Follow up: Could you write a generalized algorithm to work on any possible set of characters?

"""

# Solution:
class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            # for each word, store in format "length#(delimiter)word"
            # e.g. ["Hello","World"] --> 5#Hello5#World
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        result,i = [],0 # create result array and a pointer
        while i < len(s): # go over every letter in the string and separate each word
            j = i # second pointer to find out the length
            while s[j] != "#":
                j += 1 # while not reach delimiter, it's the integer -> length of the word
            length = int(s[i:j]) # e.g. 5#Hello, j = 1, length = s[0:1] = 5
            result.append(s[j + 1:j + length + 1]) # append the word, s[3:7] = Hello
            i = j + length + 1 # Start from the next index, which is the integer
        return result



"""
Here, time complexity O(n), where n is the length of the strs & s
Space complexity is O(n). 
"""
        