class Solution {
public:
    string toGoatLatin(string sentence) {
        istringstream ss(sentence);
        string word, result, suffix = "ma";
        string vowels = "AEIOUaeiou";
        int count = 1;
        while (ss >> word) {
            if (vowels.find(word[0]) == string::npos) word = word.substr(1) + word[0];
            result += word + suffix + string(count, 'a') + ' ';
            ++count;
        }
        result.pop_back();
        return result;
    }
};