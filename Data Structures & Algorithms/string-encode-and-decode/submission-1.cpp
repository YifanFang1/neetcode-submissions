class Solution {
public:

    string encode(vector<string>& strs) {
        string output = "";
        for(int i = 0; i < strs.size(); i++) {
            output += strs[i] + '/';
        }
        return output;
    }

    vector<string> decode(string s) {
        vector<string> output;
        string word = "";
        for(int i = 0; i < s.length(); i++) {
            if(s[i] == '/') {
                output.push_back(word);
                word = "";
            }
            else {
                word += s[i];
            }
        }
        return output;
    }
};
