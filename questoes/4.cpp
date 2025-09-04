#include <vector>
#include <stdexcept>
#include <climits>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n1 = nums1.size();
        int n2 = nums2.size();

        if (n1 > n2)
            return findMedianSortedArrays(nums2, nums1);

        int low = 0, high = n1;

        while (low <= high) {
            int part1 = (low + high) / 2;              
            int part2 = (n1 + n2 + 1) / 2 - part1;     

            int maxLeft1 = (part1 == 0) ? INT_MIN : nums1[part1 - 1];
            int minRight1 = (part1 == n1) ? INT_MAX : nums1[part1];

            int maxLeft2 = (part2 == 0) ? INT_MIN : nums2[part2 - 1];
            int minRight2 = (part2 == n2) ? INT_MAX : nums2[part2];

            if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
             
                if ((n1 + n2) % 2 == 0) {
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0;
                } 
                
                else {
                    return double(max(maxLeft1, maxLeft2));
                }
            }

            else if (maxLeft1 > minRight2) {
                high = part1 - 1;  
            } else {
                low = part1 + 1;   
            }
        }

        throw runtime_error("Entrada inválida"); 
    }
};
