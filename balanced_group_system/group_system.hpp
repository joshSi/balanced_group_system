#ifndef GROUPSYSTEM_HPP
#define GROUPSYSTEM_HPP

#include <vector>
#include <string>
#include <iostream>

class GroupSystem {
public:
    // Constructor
    GroupSystem(const std::vector<std::string>& members);

    // Methods
    void add_member(const std::string& member);
    void remove_member(const std::string& member);
    void create_groups(const std::vector<std::vector<std::string>>& group_list);
    void create_and_validate_groups(const std::vector<std::vector<std::string>>& group_list);
    void print_history();
private:
    std::vector<std::string> members;
    std::vector<std::vector<std::vector<std::string>>> group_history;
};

#endif // GROUPSYSTEM_HPP
