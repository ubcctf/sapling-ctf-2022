#include<bits/stdc++.h>
using namespace std;

struct node{
  char key;
  node* ch[2]; // don't keep parent pointers
  node(char c) : key(c) {
    ch[0] = ch[1] = NULL;
  }
};

node* rotate(node* e, bool r) {
  node * c = e->ch[r];
  e->ch[r] = c->ch[r^1];
  c->ch[r^1] = e;
  e = c;
  return e;
}

node* find(char c, node* u) { // returns found node as root, rotate as we gooooo
  if (u == NULL) {
    u = new node(c);
  }
  if (c == u->key) return u;
  if (c < u->key) { // definitely not equal
    u->ch[0] = find(c, u->ch[0]);
    return rotate(u, 0);
  } else {
    u->ch[1] = find(c, u->ch[1]);
    return rotate(u, 1);
  }
}

string print_tree(node* u) {
  if (u==NULL) return "";
  string s = "(";
  s += print_tree(u->ch[0]);
  s += ")";

//  s += u->key;

  s += "(";
  s += print_tree(u->ch[1]);
  s += ")";
  return s;
}

int main(){
  cin.tie(0); ios_base::sync_with_stdio(0);
  string s;
  cin >> s;
  node* tree = NULL;
  for(char c: s) {
    tree = find(c, tree);
    cout << tree->key << " " << print_tree(tree) << endl;
  }
  for(char c:"1234567890qwertyuiopasdfghjklzxcvbnm{}_+!@#$%^&*()") {
    tree = find(c, tree);
    print_tree(tree);
    cout << tree->key << " " << print_tree(tree) << endl;
  }

}
