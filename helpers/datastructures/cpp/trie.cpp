#include <string>

using namespace std;

struct Trie {
    TrieNode *children[26] = {nullptr};
    char val = 0;
    
    Trie(char c) : val(c) {}
    
    bool find(string s, int p = 0)
    {
        if (p == s.size()) return true;
        else if (this->children[s[p]-'a'] == nullptr) return false;
        return this->children[s[p]-'a']->find(s, p + 1);
    }

    void insert(string s, int p = 0)
    {
        if (p == s.size()) return;
        char c = s[p];
        if (this->children[c-'a'] == nullptr) this->children[c-'a'] = new Trie(c);
        this->children[c-'a']->insert(s, p+1);
    }
};