
#include <iostream>
#include <stack>
using namespace std;

struct Node
{
    int data;
    Node *left;
    Node *right;

    Node(int val)
    {
        data = val;
        left = nullptr;
        right = nullptr;
    }
};

Node *addNode(Node *root, int val)
{
    if (root == nullptr)
        return new Node(val);

    if (val < root->data)
        root->left = addNode(root->left, val);
    else if (val > root->data)
        root->right = addNode(root->right, val);
    else
        cout << "Value already exists, so it was skipped." << endl;

    return root;
}

void displayInorder(Node *root)
{
    stack<Node *> nodes;
    Node *temp = root;

    while (temp != nullptr || !nodes.empty())
    {
        while (temp != nullptr)
        {
            nodes.push(temp);
            temp = temp->left;
        }

        temp = nodes.top();
        nodes.pop();

        cout << temp->data << " ";
        temp = temp->right;
    }
}

void displayPreorder(Node *root)
{
    if (root == nullptr)
        return;

    stack<Node *> nodes;
    nodes.push(root);

    while (!nodes.empty())
    {
        Node *temp = nodes.top();
        nodes.pop();

        cout << temp->data << " ";

        if (temp->right != nullptr)
            nodes.push(temp->right);

        if (temp->left != nullptr)
            nodes.push(temp->left);
    }
}

void displayPostorder(Node *root)
{
    if (root == nullptr)
        return;

    stack<Node *> first, second;
    first.push(root);

    while (!first.empty())
    {
        Node *temp = first.top();
        first.pop();

        second.push(temp);

        if (temp->left != nullptr)
            first.push(temp->left);

        if (temp->right != nullptr)
            first.push(temp->right);
    }

    while (!second.empty())
    {
        cout << second.top()->data << " ";
        second.pop();
    }
}

int main()
{
    Node *root = nullptr;
    int count, value;

    cout << "Enter the number of nodes: ";
    cin >> count;

    cout << "Enter " << count << " values:" << endl;

    for (int i = 0; i < count; i++)
    {
        cin >> value;
        root = addNode(root, value);
    }

    cout << "\nInorder: ";
    displayInorder(root);

    cout << "\nPreorder: ";
    displayPreorder(root);

    cout << "\nPostorder: ";
    displayPostorder(root);

    return 0;
}