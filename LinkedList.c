#include<stdio.h>
#include<stdlib.h>
struct node
{
  int data;
  struct node * next;
}*temp,*start=NULL,*t;

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
  
  create_node(10);
  traverse();
  create_node(11);
  create_node(12);
  traverse();
  return 0;
}