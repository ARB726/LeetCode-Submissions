class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0;
        int right = s.length()-1;

        while (right > left){
            if (!std::isalnum(static_cast<unsigned char>(s[left]))){
                left ++;
                continue;
            }
            if (!std::isalnum(static_cast<unsigned char>(s[right]))){
                right --;
                continue;
            }
            if (std::tolower(static_cast<unsigned char>(s[left])) != std::tolower(static_cast<unsigned char>(s[right]))){
                return false;
            }
            
                left ++;
                right --;
        
        }
        return true;
    }
};