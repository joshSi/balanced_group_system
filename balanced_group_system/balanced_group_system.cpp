#include "balanced_group_system.hpp"
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <random>

BalancedGroupSystem::BalancedGroupSystem(const std::vector<std> &members) : GroupSystem(members), familiarity_matrix(members.size(), std::vector<int>(members.size(), 0)) {
    for (size_t i = 0; i < members.size(); ++i) {
        member_indices[members[i]] = i;
    }
}

void BalancedGroupSystem::add_member(const std::string &member) {
    GroupSystem::add_member(member);
    member_indices[member] = members.size() - 1;
    int index = members.size() - 1;
    for (auto &row : familiarity_matrix) {
        row.resize(members.size());
    }
    familiarity_matrix.resize(members.size(), std::vector<int>(members.size(), 0));
    for (int i = 0; i < familiarity_matrix.size(); ++i) {
        familiarity_matrix[i].resize(members.size());
        for (int j = 0; j < familiarity_matrix.size(); ++j) {
            if (i == index) {
                familiarity_matrix[i][j] = 0;
            }
        }
    }
}

void BalancedGroupSystem::remove_member(const std::string &member) {
    auto it = member_indices.find(member);
    if (it == member_indices.end()) {
        throw std::runtime_error("Member not found");
    }
    int index = it->second;
    GroupSystem::remove_member(member);
    member_indices.erase(member);
    for (auto &row : familiarity_matrix) {
        row.erase(row.begin() + index);
    }
    familiarity_matrix.erase(familiarity_matrix.begin() + index);
    for (int i = 0; i < familiarity_matrix.size(); ++i) {
        familiarity_matrix[i].resize(members.size());
        for (int j = 0; j < familiarity_matrix.size(); ++j) {
           familiarity_matrix[i][j] = 0;
        }
    }
    for (int i = 0; i < members.size(); ++i) {
        member_indices[members[i]] = i;
    }
}

void BalancedGroupSystem::create_groups(const std::vector<std::vector<std::string>>& group_list) {
    GroupSystem::create_groups(group_list);
    for (const auto& group : group_list) {
        update_familiarity(group);
    }
}

void BalancedGroupSystem::print_familiarity() {
    std::cout << "  ";
    for(std::string member : members) {
        std::cout << member << ", ";
    }
    std::cout << std::endl;
    for (const auto& row : familiarity_matrix) {
        for (auto const& element : row) {
            std::cout << element << " ";
        }
        std::cout << std::endl;
    }
}

int BalancedGroupSystem::evaluate_group(const std::vector<std::string>& group) {
    int score = 0;
    for (size_t i = 0; i < group.size(); ++i) {
        for (size_t j = i + 1; j < group.size(); ++j) {
            score += familiarity_matrix[member_indices[group[i]]][member_indices[group[j]]];
        }
    }
    return score;
}

void BalancedGroupSystem::update_familiarity(const std::vector<std::string>& group) {
    for (size_t i = 0; i < group.size(); ++i) {
        for (size_t j = i + 1; j < group.size(); ++j) {
            familiarity_matrix[member_indices[group[i]]][member_indices[group[j]]] += 1;
            familiarity_matrix[member_indices[group[j]]][member_indices[group[i]]] += 1;
        }
    }
}

std::vector<std::vector<std::string>> BalancedGroupSystem::calculate_balanced_groups(int group_count, std::vector<std::string> new_members) {
    std::random_shuffle(new_members.begin(), new_members.end());
    std::vector<std::vector<std::string>> groups(group_count, std::vector<std::string>());
    std::vector<int> scores;
    std::map<std::vector<std::string>, int> memoized_scores;
    
    auto evaluate_member = [&](std::vector<std::string> group, std::string member) {
        std::vector<std::string> group_and_member;
        group_and_member.reserve(group.size() + 1);
        group_and_member = group;
        group_and_member.push_back(member);
        std::sort(group_and_member.begin(), group_and_member.end());
        auto it = memoized_scores.find(group_and_member);
        if (it != memoized_scores.end()) {
            return memoized_scores[group_and_member];
        }
        int score = 0;
        for (const std::string& i : group) {
             score += familiarity_matrix[member_indices[i]][member_indices[member]];
        }
        memoized_scores[group_and_member] = score + 1;
        return score + 1;
    };

    for (const std::string& member : new_members) {
        int min_group_index = 0;
        for (int i = 0; i < group_count; ++i) {
            if (evaluate_member(groups[min_group_index], member) < evaluate_member(groups[i], member)) {
                min_group_index = i;
            }
        }
        groups[min_group_index].push_back(member);
    }
    return groups;
}

std::vector<std::vector<std::string>> BalancedGroupSystem::create_balanced_groups(int group_count) {
    std::vector<std::string> copy_members = members;
    return calculate_balanced_groups(group_count, copy_members);
}
