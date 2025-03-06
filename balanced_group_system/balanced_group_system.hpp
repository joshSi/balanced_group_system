#ifndef BALANCEDGROUPSYSTEM_HPP
#define BALANCEDGROUPSYSTEM_HPP

#include "group_system.hpp"
#include <vector>
#include <string>
#include <iostream>

class BalancedGroupSystem : public GroupSystem {
public:
    // Constructor
    BalancedGroupSystem(const std::vector<std::string>& members);

    // Methods
    void add_member(const std::string& member) override;
    void remove_member(const std::string& member) override;
    void create_groups(const std::vector<std::vector<std::string>>& group_list) override;
    void print_familiarity();
    int evaluate_group(const std::vector<std::string>& group);
    void update_familiarity(const std::vector<std::string>& group);
    std::vector<std::vector<std::string>> calculate_balanced_groups(int group_count, std::vector<std::string> members = std::vector<std::string>());
    std::vector<std::vector<std::string>> create_balanced_groups(int group_count);

private:
    std::vector<std::vector<int>> familiarity_matrix;
    std::unordered_map<std::string, int> member_indices;
};

#endif // BALANCEDGROUPSYSTEM_HPP
