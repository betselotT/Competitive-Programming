class Solution {
public:
    vector<int> numberOfLines(vector<int>& widths, string s) {
        int lines = 1, remain = 0;
        for(int i = 0, n = s.length(); i < n; ++i){
            if(remain + widths[s[i] - 'a'] <= 100) remain += widths[s[i] - 'a'];
            else {
                ++lines;
                remain = widths[s[i] - 'a'];
            }
        }
        return {lines , remain};
    }
};