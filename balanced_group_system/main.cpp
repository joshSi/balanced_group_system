#include "balanced_group_system.hpp"
#include "group_system.hpp"
#include <iostream>
#include <vector>

int main() {
    // Create a BalancedGroupSystem object
    std::vector<std::string> members = {"Alice", "Bob", "Charlie", "David", "Eve"};
    BalancedGroupSystem bgs(members);
    //Add members
    bgs.add_member("Frank");
    bgs.add_member("Grace");
    //Remove member
    bgs.remove_member("Alice");
    // Create some groups
    std::vector<std::vector<std::string>> groups = {
        {"Bob", "Charlie"},
        {"David", "Eve", "Frank"},
        {"Grace", "Charlie"}
    };
    bgs.create_groups(groups);
    bgs.print_familiarity();
    
    // Create balanced groups
    std::vector<std::vector<std::string>> balanced_groups = bgs.create_balanced_groups(3);
    std::cout << "Balanced Groups:" << std::endl;
    for (const auto& group : balanced_groups) {
        std::cout << "{ ";
        for (const auto& member : group) {
          std::cout << member << " ";
        }
        std::cout << "}" << std::endl;
    }
    //Evaluate a group
    int group_score = bgs.evaluate_group(groups[0]);
    std::cout << "Group Score:" << group_score << std::endl;

    std::cout << "Testing the group validation function" << std::endl;
    std::vector<std::vector<std::string>> invalid_groups = {
        {"Alice", "Bob", "Charlie", "David", "Eve", "Frank"},
        {"Grace", "Grace"}
    };
    try {
        bgs.create_and_validate_groups(invalid_groups);
    }
    catch(const std::runtime_error& error) {
        std::cout << error.what() << std::endl;
    }

    return 0;
}
