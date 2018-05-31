typedef unsigned int uint;

class Node {
public:
    struct Node *left = nullptr;
    struct Node *right = nullptr;
    struct Node *parent = nullptr;
    int value;
    uint size;
    
    Node(int value) : value(value) {}
    
    void insert(int v) 
    {
        Node *x = this, *y = nullptr;
        while (x != nullptr) {
            y = x;
            if (x->value > v) x = x->left;
            else x = x->right;
            y->size++;
        }
        Node *n = new Node(v);
        n->parent = y;
        if (y->value > v) y->left = n;
        else y->right = n;
    }

    Node *find(int v)
    {
        Node *x = this;
        while (x != nullptr && x->value != v) {
            if (x->value > v) x = x->left;
            else x = x->right;
        }
        return x;
    }
};
