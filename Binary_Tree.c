#include<stdio.h>
#include<stdlib.h>
struct node
{
  int data;
  struct node * left;
  struct node * right;
}*root=NULL,*temp,*t,*sroot;

int search(int d)
{
  t = root;
  if (root ->data == d)
  {
    printf("%d ",d);
    return (0);
  }
  
  else
  {
    if (d < t -> data)
    {
      if (t-> left != NULL)
      {
        root=t->left;
        search(d);
        root = t;
      }
    }
    else
    {
      if (t->right != NULL)
      {
        root=t->right;
        search(d);
        root = sroot;
      }
    }
  }
}
  
void insert(int d)
{
  t=root;
  
  if (d < t->data)
  {
    if (t->left == NULL)
    {
      temp = malloc (sizeof(struct node));
      temp ->data = d;
      temp ->left = NULL;
      temp ->right = NULL;
  
      t->left = temp;
      return (0);
    }
    root=t->left;
    insert(d);
    root = sroot;
  }
  else
  {
    if (t->right == NULL)
    {
      temp = malloc (sizeof(struct node ));
      temp ->data = d;
      temp ->left = NULL;
      temp ->right = NULL;
      
      t->right = temp;
      return (0);
    }
    root = t->right;
    insert(d);
    root = sroot;
  }
}

void create_node(int d)
{
  temp = (struct node *) malloc(sizeof(struct node));
  temp -> data = d;
  temp -> left = NULL;
  temp -> right = NULL;

  if (root == NULL) //Check if root is null
  {
    root = temp;   //Make temp as root
    sroot = root;
  }
  else      
  {
    t = root;    //Take a pointer pointing to root
    if (d < t->data)
    {
      if (t->left != NULL)
      {
        root = t->left ;
        create_node(d); 
        root = sroot;
      }
      else if (t-> left == NULL)
      {
        t->left = temp;
      }
    }
    else
    {
      if (t->right != NULL)
      {
        root = t->right;
        create_node(d);              
        root = sroot;
      }
      else if (t->right == NULL)
      {
        t->right = temp;
      }
    }
  }
}
    
    

int main() {
  sroot = root;
  create_node(12);
  create_node(8);
  insert(9);
  insert(15);
  insert(13);
  insert(6);
  insert(14);
  create_node(5);

  return 0;
}