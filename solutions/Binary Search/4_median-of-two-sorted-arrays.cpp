#include <vector>
#include <climits>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        size_t m = nums1.size();
        size_t n = nums2.size();
        vector<int> res(m + n, 0);

        int i = 0, j = 0, k = 0;
        while (i < m && j < n) {
            if (nums1[i] < nums2[j]) res[k++] = nums1[i++];

            else res[k++] = nums2[j++];
        }
        while (i < m) res[k++] = nums1[i++];
        while (j < n) res[k++] = nums2[j++];

        if ((m + n) % 2) {
            return res[(m + n) / 2];
        } else {
            return (res[(m + n) / 2] + res[(m + n) / 2 - 1]) / 2.0;
        }
    }
};


class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) {
            swap(nums1, nums2);
        }

        int m = nums1.size();
        int n = nums2.size();
        int left = (m + n) / 2;
        bool isOdd = (m + n) % 2;

        int l = 0, r = min(m, left);
        while (l <= r) {
            int mid = (l + r + 1) / 2;

            int i = mid - 1;
            int j = left - mid - 1;

            int t1 = (i < 0)? INT_MIN : nums1[i];
            int t2 = (i + 1 < m)? nums1[i + 1] : INT_MAX;
            int b1 = (j < 0)? INT_MIN : nums2[j];
            int b2 = (j + 1 < n)? nums2[j + 1] : INT_MAX;

            if (t1 <= b2 && b1 <= t2) {
                if (isOdd) {
                    return min(t2, b2);
                } else {
                    return (max(t1, b1) + min(t2, b2)) / 2.0;
                }
            } else if (t1 > b2) r = mid - 1;
            else l = mid + 1;
        }

        return 0;
    }
};