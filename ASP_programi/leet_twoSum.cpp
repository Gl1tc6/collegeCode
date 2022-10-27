#include <iostream>
#include <vector>
using namespace std;

/* class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> solution = {0,0};
        for(int i = 0;i< nums.size(); i++){
            if(i+1 < nums.size()){
                for(int j = i+1; j < nums.size(); j++)
                     if(nums[i] + nums[j] == target){
                         solution = {i, j};
                         return solution;}
                }
        }
        return {0,0};
    }
}; */



int main(){
    vector<int> vec = {0,4,3,0};
    int target = 0;
    Solution vect;
    vec = vect.twoSum(vec, target);
    cout << vec.at(0) << " " << vec.at(1) << endl;


    return 0;
}