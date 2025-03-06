#include "group_system.hpp"
#include <iostream>
#include <vector>
#include <cassert>
#include <stdexcept>

void test_init() {
    std::vector<std::string> members = {"Alice", "Bob", "Charlie", "David", "Eve"};
    GroupSystem gs(members);
    assert(gs.members == members);
    assert(gs.group_history == std::vector<std::vector<std::vector<std::string>>>(0));
}

void test_add_member() {
    std::vector<std::string> members = {"Alice", "Bob", "Charlie", "David", "Eve"};
    GroupSystem gs(members);
    gs.add_member("Frank");
    assert(gs.members.size() == 6);
}

void test_remove_member() {
    std::vector<std::string> members = {"Alice", "Bob", "Charlie", "David", "Eve"};
    GroupSystem gs(members);
    gs.remove_member("Bob");
    assert(gs.members.size() == 4);
}

void test_create_groups() {
    std::vector<std::string> members = {"Alice", "Bob", "Charlie", "David", "Eve"};
    GroupSystem gs(members);
    std::vector<std::vector<std::string>> group_list1 = {{"Alice", "Bob"}, {"Charlie", "David", "Eve"}};
    std::vector<std::vector<std::string>> group_list2 = {{"Alice", "Bob"}, {"Charlie"}, {"David", "Eve"}};
    gs.create_groups(group_list1);
    gs.create_groups(group_list2);
    assert(gs.group_history == std::vector<std::vector<std::vector<std::string>>>({group_list1, group_list2}));
}

void test_create_validate_groups() {
    std::vector<std::string> members = {"Alice", "Bob", "Charlie", "David", "Eve"};
    GroupSystem gs(members);
    // Test case: Member not in groupSystem.members
    try{
        gs.create_and_validate_groups({{"Alice", "Bob"}, {"Charlie", "David", "Frank"}});
        assert(false);
    } catch(const std::runtime_error& error){
        assert(std::string(error.what()) == "Member not found");
    }
    
    // Test case: Duplicate member within a group
    try {
        gs.create_and_validate_groups({{"Alice", "Bob"}, {"Charlie", "Charlie"}});
    } catch(const std::runtime_error& error){
        assert(std::string(error.what()) == "Duplicate members found");
    }
}

int main() {
    test_init();
    test_add_member();
    test_remove_member();
    test_create_groups();
    test_create_validate_groups();
}
