#include "balanced_group_system.hpp"
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <random>

BalancedGroupSystem::BalancedGroupSystem(const std::vector<std::string>& members) : GroupSystem(members), familiarity_matrix(members.size(), std::vector<int>(members.size(), 0)) {
}

void BalancedGroupSystem::add_member(const std::string& member) {
    GroupSystem::add_member(member);
    for (auto& row : familiarity_matrix) {
        row.push_back(0);
    }
    familiarity_matrix.push_back(std::vector<int>(familiarity_matrix.size(), 0));
}

void BalancedGroupSystem::remove_member(const std::string& member) {
    auto it = std::find(members.begin(), members.end(), member);
    if (it == members.end()) {
        throw std::runtime_error("Member not found");
    }
    int index = std::distance(members.begin(),it);
    GroupSystem::remove_member(member);
    for (auto& row : familiarity_matrix) {
        row.erase(row.begin() + index);
    }
    familiarity_matrix.erase(familiarity_matrix.begin()+index);
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
            score += familiarity_matrix[std::distance(members.begin(), std::find(members.begin(), members.end(), group[i]))][std::distance(members.begin(), std::find(members.begin(), members.end(), group[j]))];
        }
    }
    return score;
}

void BalancedGroupSystem::update_familiarity(const std::vector<std::string>& group) {
    for (size_t i = 0; i < group.size(); ++i) {
        for (size_t j = i + 1; j < group.size(); ++j) {
            familiarity_matrix[std::distance(members.begin(), std::find(members.begin(), members.end(), group[i]))][std::distance(members.begin(), std::find(members.begin(), members.end(), group[j]))] += 1;
            familiarity_matrix[std::distance(members.begin(), std::find(members.begin(), members.end(), group[j]))][std::distance(members.begin(), std::find(members.begin(), members.end(), group[i]))] += 1;
        }
    }
}

std::vector<std::vector<std::string>> BalancedGroupSystem::calculate_balanced_groups(int group_count, std::vector<std::string> new_members) {
    std::random_shuffle(new_members.begin(), new_members.end());
    std::vector<std::vector<std::string>> groups(group_count, std::vector<std::string>());
    std::vector<int> scores;
    std::map<std::vector<std::string>, int> memoized_scores;
    
    auto evaluate_member = [&](std::vector<std::string> group, std::string member) {
        std::vector<std::string> group_copy = group;
        std::sort(group_copy.begin(), group_copy.end());
        std::vector<std::string> group_and_member;
        group_and_member.reserve(group_copy.size() + 1);
        group_and_member = group_copy;
        group_and_member.push_back(member);
        std::sort(group_and_member.begin(), group_and_member.end());

        if (memoized_scores.find(group_and_member) != memoized_scores.end()){
            return memoized_scores[group_and_member];
        }
        int score = 0;
        for (std::string i : group) {
             score += familiarity_matrix[std::distance(members.begin(), std::find(members.begin(), members.end(), i))][std::distance(members.begin(), std::find(members.begin(), members.end(), member))];
        }
        memoized_scores[group_and_member] = score + 1;
        return score + 1;
    };

    for (std::string member : new_members) {
        int min_group_index = 0;
        for (int i = 0; i < group_count; i++) {
            if (evaluate_member(groups[min_group_index], member) < evaluate_member(groups[i], member)){
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
