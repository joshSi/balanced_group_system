#include "group_system.hpp"
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

GroupSystem::GroupSystem(const std::vector<std::string>& members) : members(members) {
}

void GroupSystem::add_member(const std::string& member) {
    members.push_back(member);
}

void GroupSystem::remove_member(const std::string& member) {
    auto it = std::find(members.begin(), members.end(), member);
    if(it == members.end()) {
        throw std::runtime_error("Member not found");
    }
    members.erase(it);
}

void GroupSystem::create_groups(const std::vector<std::vector<std::string>>& group_list) {
    group_history.push_back(group_list);
}

void GroupSystem::create_and_validate_groups(const std::vector<std::vector<std::string>>& group_list) {
    std::vector<std::string> all_members;
    std::unordered_set<std::string> members_set;
    for (const auto& group : group_list) {
        for (const auto& member : group) {
            if (members_set.find(member) != members_set.end()){
              throw std::runtime_error("Duplicate members found");
            }
            all_members.push_push_back(member);
        }
    }
    std::sort(all_members.begin(), all_members.end());
    std::vector<std::string> unique_members;
    std::unique_copy(all_members.begin(), all_members.end(), std::back_inserter(unique_members));
    std::unordered_set<std::string> members_set_temp(members.begin(), members.end());
    for(std::string member : all_members) {
        if (members_set_temp.find(member) == members_set_temp.end()){
          throw std::runtime_error("Element not found in members list");
        }
    }
    group_history.push_back(group_list);
}

void GroupSystem::print_history() {
    for (const auto& group : group_history) {
        for (const auto& member_list : group) {
            for(std::string member : member_list) {
                std::cout << member << " ";
            }
            std::cout << std::endl;
        }
        std::cout << std::endl;
    }
}
