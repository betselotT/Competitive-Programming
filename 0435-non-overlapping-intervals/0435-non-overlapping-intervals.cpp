class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(),intervals.end());
        vector<vector<int>> ans;
        int n=intervals.size();
        int count=0;
        for(int i=0;i<n;i++){
            int start=intervals[i][0];
            int end=intervals[i][1];
            while(i<n-1 && end>intervals[i+1][0]){
                count++;
                end=min(end,intervals[i+1][1]);
                i++;
            }
        }
        return count;
    }
};