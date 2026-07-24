#include <unordered_map>
#include <vector>
#include <string>

using namespace std;

class TimeMap {
public:
    unordered_map<string, vector<pair<int, string>>> map;

    TimeMap() {}
    
    void set(string key, string value, int timestamp) {
        map[key].push_back({timestamp, value});
    }
    
    string get(string key, int timestamp) {
        const vector<pair<int, string>>& vec = map[key];

        int l = 0, r = vec.size() - 1;
        string res = "";
        while (l <= r) {
            int mid = l + (r - l) / 2;

            if (vec[mid].first <= timestamp) {
                l = mid + 1;
                res = vec[mid].second;
            } else {
                r = mid - 1;
            }
        }

        return res;
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */