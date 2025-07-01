class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        unordered_set<string> bannedSet(banned.begin(), banned.end());
        unordered_map<string, int> freq;

        for (char& ch : paragraph)
            if (ispunct(ch))
                ch = ' ';

        transform(paragraph.begin(), paragraph.end(), paragraph.begin(), ::tolower);
        istringstream iss(paragraph);
        string word, mostCommon;
        int maxFreq = 0;

        while (iss >> word) 
        {
            if (bannedSet.count(word)) continue;
            freq[word]++;
            if (freq[word] > maxFreq) 
            {
                maxFreq = freq[word];
                mostCommon = word;
            }
        }

        return mostCommon;
    }
};