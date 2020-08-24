#include<stdio.h>
#include<stdlib.h>
struct node
{
  int data;
  struct node * next;
}*temp,*start=NULL,*t,*prev=NULL,*end=NULL;

void create_node(int d)
{
  temp = (struct node *) malloc(sizeof(struct node));
  temp -> data = d;
  temp -> next = NULL;
  if (start == NULL)
  {
    start = temp;
  }
  else
  {
    t = start;
    while (t -> next != NULL)
    {
      t = t -> next;
    }
    t->next = temp;
  }
}
void insert_in_middle(int d)
{
  t = start;
  temp = malloc(sizeof(struct node));
  temp -> data = d;
  while (t->data < d)
  {
    prev = t;
    t = t->next;
  }
  
  t = prev;
  if (t->next != NULL)
  {
    temp->next = t->next;
    t->next = temp;
  }
}
void insert_at_end(int d)
{
  temp = malloc(sizeof(struct node));
  temp -> data = d;
  end = start;
  while (end->next != NULL)
  {
    end = end->next;
  }
  end -> next = temp;
  temp -> next = NULL;
  end = temp;
}
  
void traverse()
{
  t = start;
  while ( t != NULL)
  {
    printf("%d ",t->data);
    t = t -> next;
  }
}
int main() {
  
  create_node(9);
  create_node(10);
  create_node(12);
  insert_in_middle(11);
  insert_at_end(19);
  insert_in_middle(15);
  traverse();
  return 0;
}
