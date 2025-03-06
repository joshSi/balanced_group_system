#include "balanced_group_system.hpp"
#include <iostream>
#include <vector>
#include <cassert>
#include <stdexcept>

void test_init() {
    std::vector<std::string> members = {"Alice", "Bob", "Charlie", "David", "Eve"};
    BalancedGroupSystem bgs(members);
    assert(bgs.members == members);
    assert(bgs.familiarity_matrix == std::vector<std::vector<int>>(5, std::vector<int>(5,0)));
}

void test_add_member() {
    std::vector<std::string> members = {"Alice", "Bob", "Charlie", "David", "Eve"};
    BalancedGroupSystem bgs(members);
    bgs.add_member("Frank");
    assert(bgs.members.size() == 6);
    assert(bgs.familiarity_matrix.size() == 6);
    assert(bgs.familiarity_matrix == std::vector<std::vector<int>>(6, std::vector<int>(6,0)));
}

void test_remove_member() {
    std::vector<std::string> members = {"Alice", "Bob", "Charlie", "David", "Eve"};
    BalancedGroupSystem bgs(members);
    bgs.remove_member("Bob");
    assert(bgs.members.size() == 4);
    assert(bgs.familiarity_matrix.size() == 4);
    assert(bgs.familiarity_matrix == std::vector<std::vector<int>>(4, std::vector<int>(4,0)));
}

void test_create_groups() {
    std::vector<std::string> members = {"Alice", "Bob", "Charlie", "David", "Eve"};
    BalancedGroupSystem bgs(members);
    std::vector<std::vector<std::string>> groups = {
        {"Alice", "Bob"},
        {"Charlie", "David", "Eve"}
    };
    bgs.create_groups(groups);
    assert(bgs.familiarity_matrix[0][1] == 1);
    assert(bgs.familiarity_matrix[2][3] == 1);
    assert(bgs.familiarity_matrix[2][4] == 1);
    assert(bgs.familiarity_matrix[3][4] == 1);
}

void test_update_familiarity() {
    std::vector<std::string> members = {"Alice", "Bob", "Charlie", "David", "Eve"};
    BalancedGroupSystem bgs(members);
    std::vector<std::string> group = {"Alice", "Bob", "Charlie"};
    bgs.update_familiarity(group);
    assert(bgs.familiarity_matrix[0][1] == 1);
    assert(bgs.familiarity_matrix[0][2] == 1);
    assert(bgs.familiarity_matrix[1][2] == 1);
}

void test_calculate_balanced_groups() {
    std::vector<std::string> members = {"Alice", "Bob", "Charlie", "David", "Eve"};
    BalancedGroupSystem bgs(members);
    std::vector<std::string> test_members;
    for(std::string member : members) {
      test_members.push_back(member);
    }
    std::vector<std::vector<std::string>> groups = bgs.calculate_balanced_groups(2, test_members);
    assert(groups.size() == 2);
    for(std::vector<std::string> group : groups) {
      assert(group.size() >= 2);
    }
}

void test_create_balanced_groups() {
    std::vector<std::string> members = {"Alice", "Bob", "Charlie", "David", "Eve"};
    BalancedGroupSystem bgs(members);
    std::vector<std::vector<std::string>> groups = bgs.create_balanced_groups(2);
    assert(groups.size() == 2);
    for(std::vector<std::string> group : groups) {
      assert(group.size() >= 2);
    }
}

int main(){
    test_init();
    test_add_member();
    test_remove_member();
    test_create_groups();
    test_update_familiarity();
    test_calculate_balanced_groups();
    test_create_balanced_groups();
}
